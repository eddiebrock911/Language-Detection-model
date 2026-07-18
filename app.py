import streamlit as st
import pandas as pd
import numpy as np
import pickle

# streamlit run app.py

# Load the trained model and vectorizer
with open('language_detection_model.pkl', 'rb') as f:
    model = pickle.load(f)

with open('vectorizer.pkl', 'rb') as f:
    vectorizer = pickle.load(f)

st.set_page_config(page_title="Language Detection", page_icon=":globe_with_meridians:", layout="wide")

st.title("Language Detection")
st.write("Enter text to detect its language:")

def clear_text():
    st.session_state.input_text = ""

text = st.text_area("Text", height=200, key="input_text").lower()
col1, col2 = st.columns(2)

with col1:
    if st.button("Detect Language"):
        if text:
            # Preprocess the input text
            text_vectorized = vectorizer.transform([text])
            # Make prediction
            prediction = model.predict(text_vectorized)
            st.success(f"The detected language is: {prediction[0]}")
        else:
            st.warning("Please enter some text to detect its language.")

with col2:
    st.button("Clear", on_click=clear_text)