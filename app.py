import streamlit as st
from model import recommend, movies

st.title("Movie Recommendation System")

movie = st.selectbox(
    "Select a movie",
    movies["title"].values
)

if st.button("Recommend"):
    results = recommend(movie)

    if results:
        for m in results:
            st.write(m)
    else:
        st.write("Movie not found")
