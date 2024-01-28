# 🎬 Movie Recommender System 🍿

Welcome to the Movie Recommender System! This Streamlit web application suggests movies to users based on their plot descriptions. It utilizes advanced techniques like TF-IDF and cosine similarity to provide accurate recommendations.

link to the website : https://movie-recommendation-system-m.streamlit.app/

## Demo 📸
![ezgif-7-d679b2ced0](https://github.com/pankil-soni/movie-recommendation-system/assets/116267467/a07d7bd1-1b1c-430a-913a-7af94568f844)
![Streamlit - Google Chrome 28-01-2024 12_23_00](https://github.com/pankil-soni/movie-recommendation-system/assets/116267467/0a07a433-70f2-4edc-8e07-f35b4052b399)
![Streamlit - Google Chrome 28-01-2024 12_22_41](https://github.com/pankil-soni/movie-recommendation-system/assets/116267467/7918af68-7cab-4528-9570-6250eb1c74b0)
![Streamlit - Google Chrome 28-01-2024 12_23_19](https://github.com/pankil-soni/movie-recommendation-system/assets/116267467/6789e1e9-c5ad-4e86-be89-92e570f98094)


## Overview 📋

This recommendation system assists users in discovering new movies similar to those they have enjoyed. By analyzing the plot descriptions of movies, the system identifies similarities and suggests relevant recommendations.

## How It Works 🤔

### TF-IDF (Term Frequency-Inverse Document Frequency) 📊

TF-IDF is a numerical statistic that reflects the importance of a word in a document relative to a collection of documents. In the context of our recommendation system:
- **Term Frequency (TF)** measures how frequently a term (word) occurs in a movie's plot description.
- **Inverse Document Frequency (IDF)** measures how important a term is across all movie plot descriptions.
- **TF-IDF** is the product of TF and IDF, combining the local importance of a term in a movie's plot description with its global importance across all movies.

![TF-IDF](https://i.postimg.cc/0yMPpYzh/tfidf.jpg "TF-IDF")

### Cosine Similarity 📐

Cosine similarity calculates the cosine of the angle between two vectors, giving a measure of similarity between them. In our recommendation system:
- We represent each movie's plot description as a TF-IDF vector.
- We calculate the cosine similarity between the TF-IDF vectors of different movies.
- Higher cosine similarity values indicate greater similarity between movies.

![Cosine](https://i.postimg.cc/jdkRwgSz/Cosine.jpg)

## Streamlit App 🚀

The Streamlit app provides an intuitive interface for users to interact with the recommendation system:
- **Select Movie**: Users can choose a movie from the dropdown menu to view details about that movie.
- **Recommended Movies**: The app displays five recommended movies based on cosine similarity to the selected movie.
- **Interactive Interface**: Users can easily navigate through the app's interface and explore movie recommendations.

## Dataset 📊

The recommendation system is built upon a dataset containing information about thousands of movies, including their titles, genres, cast, crew, tags, and plot descriptions. The dataset used in this app can be found [here](https://www.kaggle.com/datasets/gazu468/tmdb-10000-movies-dataset).

## Technologies Used 🛠️

- **Streamlit**: For creating the interactive web application.
- **Pandas**: For data manipulation and preprocessing.
- **NumPy**: For numerical computations.
- **Pillow (PIL)**: For loading and displaying movie posters.
- **Python**: For backend logic and calculations.

## How to Run ▶️

To run the app locally, follow these steps:

1. Clone this repository:

```bash
git clone https://github.com/yourusername/movierecommender.git
```
2. Navigate to the project directory:
```bash
cd movierecommender
```
3. Run the Streamlit app:
```bash
streamlit run app.py
```
## About the Author 📝
This project was developed by **Pankil Soni**. Feel free to reach out with any questions or suggestions.
- gmail - pmsoni2016@gmail.com
- kaggle - https://www.kaggle.com/pankilsoni
- LinkedIn - https://www.linkedin.com/in/pankil-soni-5a0541170/
