Movie Recommendation System

A content-based movie recommendation system built using NLP techniques.
Movies are recommended based on similarity between genres and overviews.

Tech Stack
- Python
- Pandas
- Scikit-learn
- Streamlit

How it Works
- Combine genre and overview into a single text feature
- Convert text into vectors using CountVectorizer
- Compute cosine similarity between movies
- Recommend top similar movies

Run Locally
pip install -r requirements.txt
streamlit run app.py
