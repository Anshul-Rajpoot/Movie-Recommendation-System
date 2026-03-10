import pandas as pd
import streamlit as st
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

@st.cache_resource
def load_data():

    movies = pd.read_csv("dataset.csv")

    movies["tags"] = (movies["genre"] + " " + movies["overview"]).astype(str)

    movies = movies[["id", "title", "tags"]]

    movies["title"] = movies["title"].str.strip()
    movies["title_lower"] = movies["title"].str.lower()

    vectorizer = CountVectorizer(
        max_features=3000,   # reduced to avoid memory crash
        stop_words="english"
    )

    vectors = vectorizer.fit_transform(movies["tags"]).toarray()

    similarity = cosine_similarity(vectors)

    return movies, similarity


movies, similarity = load_data()


def recommend(movie_name, top_n=5):

    name = movie_name.strip().lower()

    if name not in movies["title_lower"].values:
        return []

    idx = movies[movies["title_lower"] == name].index[0]

    scores = sorted(
        enumerate(similarity[idx]),
        key=lambda x: x[1],
        reverse=True
    )

    return [movies.iloc[i[0]].title for i in scores[1:top_n+1]]
