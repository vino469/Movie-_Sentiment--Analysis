# Movie Sentiment Analysis Using NLP and Machine Learning

## Project Overview

Movie Sentiment Analysis is a Natural Language Processing (NLP) and Machine Learning based project that classifies movie reviews into two sentiment categories: Positive and Negative.

This project uses text preprocessing techniques to clean and prepare movie review data. TF-IDF Vectorization is applied to convert text data into numerical features, and Logistic Regression is used as the classification algorithm to predict sentiment.

The trained machine learning model is deployed using Streamlit, allowing users to enter movie reviews and get real-time sentiment predictions.

---

## Objectives

- Analyze movie reviews using Natural Language Processing techniques
- Clean and preprocess text data for machine learning
- Convert text data into numerical features using TF-IDF Vectorization
- Build and train a Machine Learning classification model
- Predict sentiment of new movie reviews
- Deploy the trained model using Streamlit

---

## Technologies Used

- Python
- Pandas
- NumPy
- Scikit-learn
- Natural Language Processing (NLP)
- TF-IDF Vectorizer
- Logistic Regression
- Streamlit
- Joblib

---

## Project Structure


Movie-Sentiment-Analysis/

│
├── dataset/
│ └── movie_reviews.csv
│
├── model/
│ ├── sentiment_model.pkl
│ └── tfidf_vectorizer.pkl
│
├── app.py
├── train_model.py
├── requirements.txt
└── README.md


---

## Project Workflow

### 1. Data Collection

- Load the movie review dataset using Pandas.
- Dataset contains movie reviews with sentiment labels.

### 2. Text Preprocessing

The review text is cleaned using preprocessing techniques:

- Convert text into lowercase
- Remove special characters
- Remove unnecessary spaces
- Prepare clean text data for model training

### 3. Feature Extraction

TF-IDF (Term Frequency-Inverse Document Frequency) Vectorization is used to convert text reviews into numerical feature vectors.

It helps the machine learning model understand important words and patterns from the movie reviews.

### 4. Model Training

- Split the dataset into training and testing data
- Train the Logistic Regression model using TF-IDF features
- Learn patterns from positive and negative reviews

### 5. Model Evaluation

The model performance is evaluated using:

- Accuracy Score
- Classification Report

### 6. Model Deployment

- Save the trained model and TF-IDF vectorizer using Joblib
- Deploy the application using Streamlit
- Provide real-time sentiment prediction

---

## Machine Learning Algorithm

### Logistic Regression

Logistic Regression is a supervised machine learning algorithm used for binary classification problems.

In this project:

Input:
- Movie review text

Output:
- Positive sentiment
- Negative sentiment

The model learns from labeled movie reviews and predicts the sentiment of new reviews.

---

## Sample Prediction

### Input


The movie was amazing with excellent acting and a great story.


### Output


Sentiment: Positive


---

### Input


The movie was boring and the storyline was very poor.


### Output


Sentiment: Negative


---

## Future Enhancements

- Implement advanced NLP models such as BERT and Transformer models
- Improve model accuracy using deep learning techniques
- Add multi-class sentiment classification
- Deploy the application on cloud platforms

---

## Conclusion

Movie Sentiment Analysis demonstrates the use of Natural Language Processing and Machine Learning techniques for text classification.

By combining TF-IDF Vectorization with Logistic Regression, the system can effectively classify 
