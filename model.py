import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

movies = pd.read_csv("dataset.csv")

movies["tags"] = (movies["genre"] + " " + movies["overview"]).astype(str)
movies = movies[["id", "title", "tags"]]

movies["title"] = movies["title"].str.strip()
movies["title_lower"] = movies["title"].str.lower()

vectorizer = CountVectorizer(max_features=10000, stop_words="english")
vectors = vectorizer.fit_transform(movies["tags"]).toarray()

similarity = cosine_similarity(vectors)

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

    recommendations = []

    for i in scores[1:top_n+1]:
        recommendations.append(movies.iloc[i[0]].title)

    return recommendations