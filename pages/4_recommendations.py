import streamlit as st
from connection import TmdbConnection

# st.set_page_config(page_title="Plotting Demo", page_icon="📈")
connection = st.experimental_connection("tmdb", type=TmdbConnection,key=st.secrets.api.key)

st.title('Top Rated TV / Movies')
option = st.selectbox(
    'What do you want to search?',
    ('Movie', 'TV'))
if option == 'Movie':
    print('Movie')
    st.session_state['option'] = option
    title=st.text_input('Enter a movie name to get recommendations',key='movie_name',placeholder='Matrix')
    df=connection.query_recommendations(title)
elif option == 'TV':
    print('TV')
    st.session_state['option'] = option
    title=st.text_input('Enter a TV show to get recommendations',key='movie_name',placeholder='Game of Thrones')
    df=connection.query_recommendations(title)


# st.data_editor(df)
st.data_editor(df,column_config={
        "poster_path": st.column_config.ImageColumn(width="100px",help="Double click to enlarge",label="Poster"),
        "overview": st.column_config.TextColumn(width="300px",help=""),
        "genre_names": st.column_config.TextColumn(label="Genres",),
        "vote_average": st.column_config.NumberColumn(label="Rating"),
},hide_index=True)

