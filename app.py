import streamlit as st
from model import recommend, movies

st.set_page_config(page_title="Movie Recommendation System", page_icon="🎬")

st.title("🎬 Movie Recommendation System")

movie = st.selectbox(
    "Select a movie",
    movies["title"].values
)

if st.button("Recommend"):
    results = recommend(movie)

    if results:
        st.subheader("Recommended Movies")
        for m in results:
            st.success(m)
    else:
        st.error("Movie not found")