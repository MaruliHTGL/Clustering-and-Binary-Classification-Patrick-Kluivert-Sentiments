import streamlit as st
import numpy as np
import pandas as pd
import re
import nltk
nltk.download('punkt_tab')
nltk.download('stopwords')
nltk.download('wordnet')
nltk.download('omw-1.4')
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

# import ml package
import joblib
import os   

from Sastrawi.Stemmer.StemmerFactory import StemmerFactory

factory = StemmerFactory()
stemmer = factory.create_stemmer()

# Defining a function to clean up the text
def clean(Text):
    text = re.sub('[^a-zA-Z]', ' ', Text) #Replacing all non-alphabetic characters with a space
    text = text.lower() #converting to lowecase
    text = word_tokenize(text)
    text = [stemmer.stem(word) for word in text if not word in stopwords.words("indonesian")]
    text = ' '.join(text)
    return text
        
def load_model(model_file):
    loaded_model = joblib.load(open(os.path.join(model_file), 'rb'))
    return loaded_model

def load_vectorization(vectorization_file):
    loaded_vectorization = joblib.load(open(os.path.join(vectorization_file), 'rb'))
    return loaded_vectorization

def run_ml_app():
    st.markdown("<h2 style = 'text-align: center;'> Input the Post </h2>", unsafe_allow_html=True)
    post = st.text_area('Enter the X Post:', 'Patrick Kluivert')

    with st.expander("Your Selected Options"):
        result = {
            'Post': post,
        }

    # dataframe
    df = pd.DataFrame({'Post': [post]})

    # clean text
    df["clean_text"] = df["Post"].apply(clean)

    st.markdown("<h2 style = 'text-align: center;'> Your Post </h2>", unsafe_allow_html=True)

    vectorization = load_vectorization("vectorization.pkl")
    vectorization_array = vectorization.transform(df["clean_text"])

    st.write(post)

    # prediction section
    st.markdown("<h2 style = 'text-align: center;'> Analysis Result </h2>", unsafe_allow_html=True)

    model = load_model("model.pkl")  
    prediction = model.predict(vectorization_array)

    if prediction == 'Negative':
        st.warning("Negative Post")
        st.write('Ini adalah sentimen negatif, mohon berhati-hati dalam memposting sesuatu di media sosial.')
    else:
        st.success('Positive Post')
        st.write('Ini adalah sentimen positif, mohon berhati-hati dalam memposting sesuatu di media sosial.')

    st.markdown('''<p style='text-align: justify;'> <br> <strong>Disclaimer:</strong> This tool is only to help analyze and may analyze sentiments incorrectly. Perform further analysis to reduce analysis errors.</p>''', unsafe_allow_html=True)