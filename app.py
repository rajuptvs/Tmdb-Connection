import streamlit as st
# from connection import TmdbConnection

from st_tmdb_connection import TmdbConnection

st.set_page_config(
    page_title="Hello",
    page_icon="👋",
)
st.title('Tmdb Connection Demo')

conn = st.experimental_connection("tmdb", type=TmdbConnection,key=st.secrets.api.key)

option = st.selectbox(
    'What do you want to search?',
    ('Movie', 'TV','Top Rated Movies','Top Rated TV Shows'))
    

if option == 'Movie':
    st.session_state['option'] = option
    moviename=st.text_input('Movie Name',placeholder="Enter Movie Name")
elif option == 'TV':
    st.session_state['option'] = option
    moviename=st.text_input('TV Show Name',placeholder="Enter TV Show Name")    
movies = conn.query(moviename)


st.data_editor(movies,column_config={
        "poster_path": st.column_config.ImageColumn(width="100px",help="Double click to enlarge",label="Poster"),
        "overview": st.column_config.TextColumn(width="300px",help=""),
        "genre_names": st.column_config.TextColumn(label="Genres",),
        "vote_average": st.column_config.NumberColumn(label="Rating"),
},hide_index=True)
               
    #            column_config={
    #     "poster_path": st.column_config.ImageColumn(
    #          help="Streamlit app preview screenshots"
    #     )
    # },
    # hide_index=True)
# print(movies)
# conn.query("movies")
