import streamlit as st
from connection import TmdbConnection

# st.set_page_config(page_title="Plotting Demo", page_icon="📈")
connection = st.experimental_connection("tmdb", type=TmdbConnection,key=st.secrets.api.key)

st.title('Popular TV / Movies')
popular_option = st.selectbox(
    'What do you want to search?',
    ('Movie', 'TV'))
if popular_option == 'Movie':
    print('Movie')
    st.session_state['popular_option'] = popular_option
    df=connection.query_popular()
elif popular_option == 'TV':
    print('TV')
    st.session_state['popular_option'] = popular_option
    df=connection.query_popular()

st.data_editor(df)