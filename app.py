import numpy as np
import streamlit as st
import pickle

st.header("Book Recommender system")
model = pickle.load(open("artifacts/model.pkl",'rb'))
book_pivot = pickle.load(open("artifacts/book_pivot.pkl",'rb'))
books_name = pickle.load(open("artifacts/books_name.pkl",'rb'))
final_rating = pickle.load(open("artifacts/final_rating.pkl",'rb'))


select_books = st.selectbox(
    "Type or select a book",
    books_name
)

def fetch_poster(suggestion):
    book_name = []
    ids_idx = []
    poster_url = []

    for book_id in suggestion:
        book_name.append(book_pivot.index[book_id])
    for name in book_name[0]:
        ids = np.where(final_rating['title']==name)[0][0]
        ids_idx.append(ids)
    for ids in ids_idx:
        url = final_rating.iloc[ids]['image_url']
        poster_url.append(url)
    return poster_url

def recommend_books(book_name):
    book_list = []
    book_id = np.where(book_pivot.index==book_name)[0][0]
    distance,suggestion = model.kneighbors(book_pivot.iloc[book_id,:].values.reshape(1,-1),n_neighbors=6)
    poster_url = fetch_poster(suggestion)
    for i in range(len(suggestion)):
        books  = book_pivot.index[suggestion[i]]
        for j in books[1:]:
            book_list.append(j)
    return book_list,poster_url


if st.button('Show Recommendation'):
    recommendation_books, poster_url = recommend_books(select_books)
    c1,c2,c3,c4,c5 = st.columns(5)
    with c1:
        st.text(recommendation_books[0])
        st.image(poster_url[0])
    with c2:
        st.text(recommendation_books[1])
        st.image(poster_url[1])
    with c3:
        st.text(recommendation_books[2])
        st.image(poster_url[2])
    with c4:
        st.text(recommendation_books[3])
        st.image(poster_url[3])
    with c5:
        st.text(recommendation_books[4])
        st.image(poster_url[4])

print("DONE")