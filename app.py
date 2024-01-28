import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image
import pickle as pkl

# expanded layout
st.set_page_config(layout="wide")

# Title
st.title('Movie Recommender System')
st.divider()

df = pkl.load(open('dataframe.pkl', 'rb'))
similarities = pkl.load(open('similarities.pkl', 'rb'))

titles = df['title'].values
titles = np.sort(titles)

selected_movie = st.selectbox('Select a movie', titles, index=titles.tolist(
).index(st.session_state.get("selected_movie", titles[0])))

st.session_state["selected_movie"] = selected_movie

outercol = st.columns(2, gap="medium")
with outercol[0]:

    cols = st.columns(2)
    poster_prefix = "https://image.tmdb.org/t/p/w1280"

    score_list = []
    input_index = df[df['title'] == selected_movie].index[0]

    for index, score in enumerate(similarities[input_index]):
        score_list.append((score, index))

    sortedlist = sorted(score_list, reverse=True, key=lambda x: x[0])[1:6]

    with cols[0]:
        st.image(poster_prefix + df[df['title'] == st.session_state["selected_movie"]]
                 ['poster_path'].values[0], width=200)

    with cols[1]:
        selected_row = df[df['title'] == st.session_state["selected_movie"]]
        st.header(selected_row['title'].values[0])
        st.write('Description:', selected_row['overview'].values[0])
        st.markdown(
            f'''<strong>Cast: </strong><code>{", ".join(selected_row['Cast'].values[0])}</code>''', unsafe_allow_html=True)
        st.markdown(
            f'''<strong>Genre: </strong><code>{", ".join(selected_row['Genres'].values[0])}</code>''', unsafe_allow_html=True)


st.header("Recommended Movies")
poster_cols = st.columns(5)


def trimtitle(x): return x[:30] if len(x) > 30 else x


for i in range(5):
    with poster_cols[i]:
        curr_row = df.iloc[sortedlist[i][1]]
        st.image(poster_prefix + curr_row['poster_path'], width=200)
        if st.button(trimtitle(curr_row['title'])):
            st.session_state["selected_movie"] = curr_row['title']
            st.experimental_rerun()


# about
st.divider()

st.markdown("# About This Project: ")

st.markdown('''

## **Content-Based Movie Recommendation System**

Dataset link - https://www.kaggle.com/datasets/gazu468/tmdb-10000-movies-dataset

## Introduction

In this notebook, we'll implement a content-based movie recommendation system using **TF-IDF** (Term Frequency-Inverse Document Frequency) and **cosine similarity**. Content-based recommendation systems recommend items which are similar in item desctiption. In our case, we'll recommend movies based on their plot descriptions.

## Dataset

We'll be using a dataset containing information about movies, including their **Titles, Genres, Cast , Crew, Tags and Plot Descriptions**.

Here's a sample of the dataset:

| Title | Genre | Plot Description |
| ----- | ----- | ----------------- |
| The Shawshank Redemption | Drama | Two imprisoned men bond over a number of years, finding solace and eventual redemption through acts of common decency. |
| The Godfather| Crime, Drama | The aging patriarch of an organized crime dynasty transfers control of his clandestine empire to his reluctant son. |
| The Dark Knight | Action, Crime, Drama |When the menace known as The Joker emerges from his mysterious past, he wreaks havoc and chaos on the people of Gotham.|
| Pulp Fiction | Crime, Drama | The lives of two mob hitmen, a boxer, a gangster's wife, and a pair of diner bandits intertwine in four tales of violence and redemption. |
| Inception | Action, Adventure, Sci-Fi | A thief who steals corporate secrets through the use of dream-sharing technology is given the inverse task of planting an idea into the mind of a C.E.O. |

## **Explanation of TF-IDF and Cosine Similarity**

### TF-IDF (Term Frequency-Inverse Document Frequency)

![img](tfidf.jpg "TF-IDF")

TF-IDF is a numerical statistic that reflects the importance of a word in a document(row) relative to a collection of documents(whole corpus). It is calculated in two parts: Term Frequency (TF) and Inverse Document Frequency (IDF). 

- **Term Frequency (TF)** measures how frequently a term occurs in a document(row). It is calculated as the ratio of the number of times a term appears in a document(row) to the total number of words in the document(row).
- **Inverse Document Frequency (IDF)** measures how important a term is across the entire corpus. It is calculated as the logarithm of the ratio of the total number of rows to the number of rows containing the term.
- **TF-IDF** is the product of TF and IDF, combining the local importance of a term in a document (TF) with its global importance across the document corpus (IDF).

We'll convert the plot descriptions into numerical vectors using TF-IDF. TF-IDF is a numerical statistic that reflects the importance of a word in a row relative to a all rows(corpus).

Here's an example TF-IDF representation for the plot descriptions:

| Word       | Doc 1: The Shawshank Redemption | Doc 2: The Godfather | Doc 3: The Dark Knight | Doc 4: Pulp Fiction | Doc 5: Inception |
|------------|----------------------------------|----------------------|------------------------|----------------------|------------------|
| imprisoned |               0.34               |         0.00         |          0.00          |         0.00         |        0.00      |
| men        |               0.34               |         0.00         |          0.00          |         0.00         |        0.00      |
| bond       |               0.34               |         0.00         |          0.00          |         0.00         |        0.00      |
| years      |               0.34               |         0.00         |          0.00          |         0.00         |        0.00      |
| solace     |               0.34               |         0.00         |          0.00          |         0.00         |        0.00      |
| redemption |               0.34               |         0.00         |          0.00          |         0.00         |        0.00      |
| acts       |               0.34               |         0.00         |          0.00          |         0.00         |        0.00      |
| common     |               0.34               |         0.00         |          0.00          |         0.00         |        0.00      |
| decency    |               0.34               |         0.00         |          0.00          |         0.00         |        0.00      |
| aging      |               0.00               |         0.29         |          0.00          |         0.00         |        0.00      |
| patriarch  |               0.00               |         0.29         |          0.00          |         0.00         |        0.00      |
| organized  |               0.00               |         0.29         |          0.00          |         0.00         |        0.00      |
| crime      |               0.00               |         0.29         |          0.00          |         0.33         |        0.00      |
| dynasty    |               0.00               |         0.29         |          0.00          |         0.00         |        0.00      |
| transfers  |               0.00               |         0.29         |          0.00          |         0.00         |        0.00      |
| control    |               0.00               |         0.29         |          0.00          |         0.00         |        0.00      |
| empire     |               0.00               |         0.29         |          0.00          |         0.00         |        0.00      |
| reluctant  |               0.00               |         0.29         |          0.00          |         0.00         |        0.00      |
| son        |               0.00               |         0.29         |          0.00          |         0.00         |        0.00      |

### Cosine Similarity

Cosine similarity calculates the cosine of the angle between two vectors. If the vectors are similar, the angle between them will be small, and the cosine similarity value will be closer to 1. If the vectors are dissimilar, the angle will be large, and the cosine similarity value will be closer to 0. 

- Cosine similarity is often used in text analysis to measure the similarity between document vectors, such as TF-IDF vectors.
- It is calculated as the dot product of the two vectors divided by the product of their magnitudes.

![img](cosine.jpg "Cosine Similarity")

Once we have the TF-IDF representation for each movie, we'll calculate the cosine similarity between movies' TF-IDF vectors. Cosine similarity measures the cosine of the angle between two vectors, giving a measure of similarity between them.

Here's an example cosine similarity matrix for the movies:

|                             | The Shawshank Redemption | The Godfather | The Dark Knight | Pulp Fiction | Inception |
| --------------------------- | ------------------------ | ------------- | --------------- | ------------ | --------- |
| The Shawshank Redemption    |           1.00           |     0.02      |       0.01      |     0.03     |   0.00    |
| The Godfather               |           0.02           |     1.00      |       0.00      |     0.14     |   0.00    |
| The Dark Knight             |           0.01           |     0.00      |       1.00      |     0.00     |   0.33    |
| Pulp Fiction                |           0.03           |     0.14      |       0.00      |     1.00     |   0.05    |
| Inception                   |           0.00           |     0.00      |       0.33      |     0.05     |   1.00    |

Recommendation
--------------

To recommend movies to a user, we'll select movies with the highest cosine similarity.


''')

st.write('''
This app was built using [Streamlit](https://streamlit.io/).
''')

st.divider()

st.write('''
The source code can be found here : [Github](
         "https://github.com")
''')

colli = st.columns(3)
innercol = colli[0].columns(3)

with colli[0]:
    with innercol[0]:
        st.write("")
        st.write("")
        st.write("My Github Profile: ")
    with innercol[1]:
        st.markdown(f'''<a href="https://github.com/pankil-soni/"><img src="https://avatars.githubusercontent.com/u/116267467?v=4" width="100px"><br><a href = "https://github.com/pankil-soni/" style="margin: 12px;">Pankil Soni</a>''', unsafe_allow_html=True)
