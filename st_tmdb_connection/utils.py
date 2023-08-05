import pandas as pd
import streamlit as st
   
   
def prep(movie):
        df=pd.DataFrame(movie)

        def map_genres(genre_ids):
            return [genredf[genredf['id'] == genre_id]['genres'].iloc[0] for genre_id in genre_ids]

        def process_genre_names(genre_list):
            if not genre_list:
                return "N/A"
            return ', '.join(genre_list)

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


        df['genre_names'] = df['genre_ids'].apply(map_genres)
        df['genre_names'] = df['genre_names'].apply(lambda x: process_genre_names(x))
        df['poster_path'] = df['poster_path'].apply(lambda x: full_url(x))
        return df
