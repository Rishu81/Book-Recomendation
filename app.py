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