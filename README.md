# 🎬 Movie Recommendation System

A **content-based movie recommendation system** built using **Python, Scikit-Learn, and Streamlit**.
The system recommends similar movies based on **genres and movie overviews** using **cosine similarity**.

---

## 🚀 Live Demo

🔗 **Try the App:**
https://movie-recommendation-system-a6hiye3ozmgmzzxwrunwtz.streamlit.app

---

## 📸 Screenshot

<img width="1164" height="657" alt="Movie Recommendation System Screenshot" src="https://github.com/user-attachments/assets/c13f4a6f-7883-4841-9b53-505ca9c186a9" />

---

## 🚀 Project Overview

This project suggests movies similar to a selected movie by analyzing textual metadata such as:

* Movie **genre**
* Movie **overview**

It converts text into numerical vectors using **CountVectorizer** and computes similarity using **cosine similarity** to identify movies with similar content.

The system is deployed as an **interactive web application using Streamlit**, allowing users to select a movie and instantly receive recommendations.

---

## 🧠 How It Works

1. Load movie data from `dataset.csv`
2. Combine **genre** and **overview** into a single `tags` column
3. Convert textual data into numerical vectors using **Bag of Words (CountVectorizer)**
4. Compute **cosine similarity** between movie vectors
5. Recommend the **top N most similar movies**

---

## 📂 Project Structure

```
Movie-Recommendation-System/
│
├── dataset.csv        # Movie dataset
├── model.py           # Recommendation logic
├── app.py             # Streamlit web application
├── requirements.txt   # Python dependencies
├── runtime.txt        # Python version for deployment
└── README.md
```

---

## 🛠 Technologies Used

* **Python**
* **Pandas**
* **NumPy**
* **Scikit-Learn**
* **Streamlit**
* **Natural Language Processing (NLP)**

---

## 📌 Core Algorithm

### ✔ Content-Based Filtering

This system uses **content-based filtering**, which recommends movies based on their similarity to a selected movie.

Key steps:

* Convert movie text data into vectors using **CountVectorizer**
* Represent movies using **Bag of Words**
* Compute similarity using **cosine similarity**
* Recommend movies with the **highest similarity scores**

---

## 👨‍💻 Author

**Anshul Rajpoot**
ECE Undergraduate | Data Science & Machine Learning Enthusiast

🔗 GitHub:
https://github.com/Anshul-Rajpoot

---

⭐ If you like this project, consider **starring the repository**!
