import streamlit as st
import pickle
import pandas as pd

def recommend(movie, movies, similarity):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommended_movies = []
    for i in movies_list:
        recommended_movies.append(movies.iloc[i[0]].title)
    return recommended_movies

# Load movies data
movies_list = pickle.load(open('movies.pkl', 'rb'))

# Create DataFrame from the loaded movies_list
movies = pd.DataFrame(movies_list)

# Load similarity matrix
similarity = pickle.load(open('similarity.pkl', 'rb'))

st.title('Movie Recommendation System')

selected_movie_name = st.selectbox(
    'Choose your favourite movie?',
    movies['title'].values)

if st.button('Recommend'):
    # Check if the selected movie is in the DataFrame
    if selected_movie_name in movies['title'].values:
        recommendations = recommend(selected_movie_name, movies, similarity)
        for i in recommendations:
            st.write(i)
    else:
        st.write("Movie not found. Please select a valid movie.")
