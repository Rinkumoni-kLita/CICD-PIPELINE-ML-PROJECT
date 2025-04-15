import streamlit as  st
import pickle
import pandas as pd
import requests

#function for fetching poster from json viewer

def fetch_poster(movie_id):
    response = requests.get('https://api.themoviedb.org/3/movie/{}?api_key=561a2067c77481e74242d3599f9298d6&language=en-US'.format(movie_id))
    data = response.json()
    return "https://image.tmdb.org/t/p/w500" + data['poster_path']

#API KEY : 561a2067c77481e74242d3599f9298d6
#URL FOR API IMAGE = https://api.themoviedb.org/3/movie/65?api_key=561a2067c77481e74242d3599f9298d6&language=en-US

#recommend function

def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommended_movies = []
    recommended_movies_poster = []

    for i in movies_list:
        #fetch movies based on id
        movie_id = movies.iloc[i[0]].id

        #fetch poster form API

        recommended_movies.append(movies.iloc[i[0]].title)
        # fetch poster form API

        recommended_movies_poster.append(fetch_poster(movie_id))
    return recommended_movies,recommended_movies_poster

#to use the streamlit i have installed in the terminal
#by using pip install streamlit


#under movies_list the movies.pkl and movie_dict.pkl are added

movies_dict = pickle.load(open('movie_dict.pkl','rb'))
movies = pd.DataFrame(movies_dict) #this is the dataframe

#similartiy
similarity = pickle.load(open('similarity.pkl','rb'))

st.title('Movie Recommender System')

#select box
#from streamlit API reference
selected_movie_name= st.selectbox(
    "How would you like to be contacted?",
    movies['title'].values)


#botton
#to add the predefined botton
if st.button("Recommend"):
    names,posters = recommend(selected_movie_name)

    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        st.text(names[0])
        st.image(posters[0])

    with col2:
        st.text(names[1])
        st.image(posters[1])

    with col3:
        st.text(names[2])
        st.image(posters[2])

    with col4:
        st.text(names[3])
        st.image(posters[3])

    with col5:
        st.text(names[4])
        st.image(posters[4])


