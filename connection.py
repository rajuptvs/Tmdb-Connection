import streamlit as st
from streamlit.connections import ExperimentalBaseConnection

from themoviedb import TMDb
import pandas as pd

class TmdbConnection(ExperimentalBaseConnection):
    def _connect(self, **kwargs):
        if 'key' in kwargs:
            key = kwargs.pop('key')
            # print(key)
        else:
            key = self._secrets['key']
        tmdb = TMDb(key=key)
        return tmdb
    
    def cursor(self) -> TMDb:
        return self._instance
    
    # preparing the data with preprocessing
    def prep(movie):
        # df=pd.DataFrame(movie)
    
        def map_genres(genre_ids):
            return [genredf[genredf['id'] == genre_id]['genres'].iloc[0] for genre_id in genre_ids]

        def process_genre_names(genre_list):
            if not genre_list:
                return "N/A"
            return ', '.join(genre_list)
        
        #Url for poster
        def full_url(poster_path):
            if poster_path:
                return "https://image.tmdb.org/t/p/w185" + poster_path
            else:
                return "https://upload.wikimedia.org/wikipedia/commons/a/a7/Blank_image.jpg"
        
        #Movie genre info
        moviedata = {'id': [28,12,16,35,80,99,18,10751,14,36,27,10402,9648,10749,878,10770,53,10752,37],
        'genres': ["Action","Adventure","Animation","Comedy","Crime","Documentary","Drama","Family","Fantasy","History","Horror","Music","Mystery","Romance","Science Fiction","TV Movie","Thriller","War","Western"]}

        #TV genre info
        tvdata={'id': [10759, 16, 35, 80, 99, 18, 10751, 10762, 9648, 10763, 10764, 10765, 10766, 10767, 10768, 37],
        'genres': ['Action & Adventure','Animation','Comedy','Crime','Documentary','Drama','Family','Kids','Mystery','News','Reality','Sci-Fi & Fantasy','Soap','Talk','War & Politics','Western']}
        
        #convert to dataframe
        if st.session_state['option'] == 'Movie':
            genredf=pd.DataFrame(moviedata)
        elif st.session_state['option'] == 'TV':
            genredf=pd.DataFrame(tvdata)

        if not movie.empty:
            movie['genre_names'] = movie['genre_ids'].apply(map_genres)
            movie['genre_names'] = movie['genre_names'].apply(lambda x: process_genre_names(x))
            movie['poster_path'] = movie['poster_path'].apply(lambda x: full_url(x))
        # print(movie)
        return movie
        


    def query(self, title: str, ttl: int = 2):
        @st.cache_data(ttl=ttl)
        def _query(title: str):
            cursor = self.cursor()
            if st.session_state['option'] == 'Movie':
                #only process below if title is not empty
                if title:
                    df=TmdbConnection.prep(pd.DataFrame(cursor.search().movies(title)))
                    return df[['poster_path','title','vote_average','genre_names', 'overview', 'release_date','original_language']]
            elif st.session_state['option'] == 'TV':
                if title:
                    df=TmdbConnection.prep(pd.DataFrame(cursor.search().tv(title)))
                    return df[['poster_path','name','vote_average', 'genre_names','overview','first_air_date', 'original_language']]
        
        return _query(title)
    
    def query_popular(self, ttl: int = 1):
        @st.cache_data(ttl=ttl)
        def _query_popular():
            cursor = self.cursor()
            if st.session_state['option'] == 'Movie':
                df=TmdbConnection.prep(pd.concat([pd.DataFrame(cursor.movies().popular(page=i)) for i in range(1, 6)]))
                return df[['poster_path','title','vote_average','genre_names', 'overview', 'release_date','original_language']]
            elif st.session_state['option'] == 'TV':
                
                df=TmdbConnection.prep(pd.concat([pd.DataFrame(cursor.tvs().popular(page=i)) for i in range(1, 6)]))
                return df[['poster_path','name','vote_average', 'genre_names','overview','first_air_date', 'original_language']]
                
        return _query_popular()

    def query_toprated(self, ttl: int = 1):
        @st.cache_data(ttl=ttl)
        def _query_toprated():
            cursor = self.cursor()
            if st.session_state['option'] == 'Movie':
                df=TmdbConnection.prep(pd.concat([pd.DataFrame(cursor.movies().top_rated(page=i)) for i in range(1, 6)]))
                return df[['poster_path','title','vote_average','genre_names', 'overview', 'release_date','original_language']]
            elif st.session_state['option'] == 'TV':
                
                df=TmdbConnection.prep(pd.concat([pd.DataFrame(cursor.tvs().top_rated(page=i)) for i in range(1, 6)]))
                return df[['poster_path','name','vote_average', 'genre_names','overview','first_air_date', 'original_language']]
                
        return _query_toprated() 

    def query_nowplaying(self, ttl: int = 1):
        @st.cache_data(ttl=ttl)
        def _query_nowplaying():               
            cursor = self.cursor()
            if st.session_state['option'] == 'Movie':
                df=TmdbConnection.prep(pd.concat([pd.DataFrame(cursor.movies().now_playing(page=i)) for i in range(1, 6)]))
                return df[['poster_path','title','vote_average','genre_names', 'overview', 'release_date','original_language']]
            elif st.session_state['option'] == 'TV':
                
                df=TmdbConnection.prep(pd.concat([pd.DataFrame(cursor.tvs().on_the_air(page=i)) for i in range(1, 6)]))
                return df[['poster_path','name','vote_average', 'genre_names','overview','first_air_date', 'original_language']]
                
        return _query_nowplaying() 
    
    def query_recommendations(self, title:str, ttl: int = 1):
        @st.cache_data(ttl=ttl)
        def _query_recommendations(title:str):
            cursor = self.cursor()
            if st.session_state['option'] == 'Movie':
                if title:
                    df=TmdbConnection.prep(pd.DataFrame(cursor.movie(cursor.search().movies(title)[0].id).recommendations()))
                    # print(df)
                    if df.empty:
                        st.write('No recommendations found')
                    else:
                         return df[['poster_path','title','vote_average','genre_names', 'overview', 'release_date','original_language']]
            elif st.session_state['option'] == 'TV':
                if title:
                    # df=TmdbConnection.prep(pd.DataFrame(cursor.movie(cursor.search().movies(title)[0].id).recommendations()))
                    df=TmdbConnection.prep(pd.DataFrame(cursor.tv(cursor.search().tv(title)[0].id).recommendations()))
                    # print(df)
                    if df.empty:
                        st.write('No recommendations found')
                    else:
                        return df[['poster_path','name','vote_average', 'genre_names','overview','first_air_date', 'original_language']]
                
        return _query_recommendations(title)