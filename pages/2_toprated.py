import streamlit as st


from connection import TmdbConnection
# st.set_page_config(page_title="Plotting Demo", page_icon="📈")
connection = st.experimental_connection("tmdb", type=TmdbConnection,key=st.secrets.api.key)
N = 15

st.title('Top Rated TV / Movies')



option = st.selectbox(
    'What do you want to search?',
    ('Movie', 'TV'))
if option == 'Movie':
    print('Movie')
    st.session_state['option'] = option
    df=connection.query_toprated()
elif option == 'TV':
    print('TV')
    st.session_state['option'] = option
    df=connection.query_toprated()

# st.data_editor(df)
st.data_editor(df,column_config={
        "poster_path": st.column_config.ImageColumn(width="100px",help="Double click to enlarge",label="Poster"),
        "overview": st.column_config.TextColumn(width="300px",help=""),
        "genre_names": st.column_config.TextColumn(label="Genres",),
        "vote_average": st.column_config.NumberColumn(label="Rating"),
},hide_index=True)

