import streamlit as st
# from connection import TmdbConnection

from connection import TmdbConnection

st.set_page_config(
    page_title="Hello",
    page_icon="👋",
)
st.title('Tmdb Connection Demo')

conn = st.experimental_connection("tmdb", type=TmdbConnection,key=st.secrets.api.key)

option = st.selectbox(
    'What do you want to search?',
    ('Movie', 'TV'))
    
# To choose between searching of movies or tvs
if option == 'Movie':
    st.session_state['option'] = option
    moviename=st.text_input('Movie Name',placeholder="Enter Movie Name")
    
elif option == 'TV':
    st.session_state['option'] = option
    moviename=st.text_input('TV Show Name',placeholder="Enter TV Show Name")    
df = conn.query(moviename)


st.data_editor(df,column_config={
        "poster_path": st.column_config.ImageColumn(width="100px",help="Double click to enlarge",label="Poster"),
        "overview": st.column_config.TextColumn(width="300px",help=""),
        "genre_names": st.column_config.TextColumn(label="Genres",),
        "vote_average": st.column_config.NumberColumn(label="Rating"),
},hide_index=True)

