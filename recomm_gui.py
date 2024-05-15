import streamlit as st
import pickle
import pandas as pd
import numpy as np


books_dict = pickle.load(open('books_dict.pkl', 'rb'))
book_df= pd.DataFrame(books_dict)
#b = pickle.load(open('books_dict_1.pkl', 'rb'))

predict = pickle.load(open('predict.pkl', 'rb'))

# Convert titles to series
indices = pd.Series(book_df.index, index= book_df["Book-Title"])

# Importing cosine similarity calculated from the main code file
cosine_similar = pickle.load(open('cosine_similar.pkl', 'rb'))

Books = book_df['Book-Title']


# Convert titles to series
indices = pd.Series(book_df.index, index= Books)

# Function to get book suggestion based on cosine similarity
def Book_recomender(title, n = 5):
    index = indices[title]
    Similar_scores = list(enumerate(cosine_similar[index]))
    Similar_scores = sorted(Similar_scores, key = lambda X:X[1], reverse = True) 

    Similar_scores = Similar_scores[1:n+1]
    book_index = [i[0] for i in Similar_scores]
    #book_index = Similar_scores
    book = []   

    for i in book_index:
        book.append(book_df.iloc[book_index])

    return book


st.title(" Books recommender system ... ")

Book_selected = st.selectbox(
 'Select book : ',
book_df['Book-Title'].values
)

if st.button('Recommend'):
    book_recom = Book_recomender(Book_selected)
    for i in book_recom:
        st.write(i['Book-Title'])
        break


if st.button('Popular books based on ratings ..'):
    dict = {}
    #rows = predict.collect()

    
    df = predict.sample(n = 5)
    
    st.write(df)