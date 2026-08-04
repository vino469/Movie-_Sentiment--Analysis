import streamlit as st
import joblib
import re


# Load saved model and vectorizer
model = joblib.load("sentiment_model.pkl")
tfidf = joblib.load("tfidf_vectorizer.pkl")


# Text cleaning function
def clean_text(text):
    text = text.lower()
    text = re.sub("[^a-zA-Z]", " ", text)
    text = re.sub("\s+", " ", text)
    return text


# Streamlit App

st.set_page_config(
    page_title="Movie Sentiment Analysis",
    page_icon="🎬"
)


st.title("🎬 Movie Sentiment Analysis")
st.write("Enter a movie review to predict sentiment")


review = st.text_area(
    "Movie Review",
    placeholder="Example: This movie was amazing and I loved it..."
)


if st.button("Predict Sentiment"):

    if review.strip() != "":

        # Cleaning
        cleaned_review = clean_text(review)

        # TF-IDF transformation
        vector = tfidf.transform([cleaned_review])

        # Prediction
        prediction = model.predict(vector)


        if prediction[0] == 1:
            st.success("😊 Positive Review")
        else:
            st.error("😞 Negative Review")


    else:
        st.warning("Please enter a movie review")