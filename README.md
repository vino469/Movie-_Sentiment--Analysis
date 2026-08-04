Movie Sentiment Analysis Using NLP and Machine Learning
Project Overview

Movie Sentiment Analysis is a Natural Language Processing (NLP) and Machine Learning based project that classifies movie reviews into two categories: Positive and Negative sentiment.

This project applies text preprocessing techniques to clean movie review data, converts text into numerical features using TF-IDF (Term Frequency-Inverse Document Frequency), and uses the Logistic Regression algorithm for sentiment classification.

The trained machine learning model is deployed using Streamlit, which allows users to enter new movie reviews and get real-time sentiment predictions.

Objectives
Analyze movie reviews using Natural Language Processing techniques
Clean and preprocess text data for better model performance
Convert text data into numerical features using TF-IDF Vectorization
Build a machine learning classification model using Logistic Regression
Train and evaluate the sentiment analysis model
Predict sentiment for new movie reviews
Deploy the trained model using Streamlit for real-time usage
Technologies Used
Python
Pandas
NumPy
Scikit-learn
Natural Language Processing (NLP)
Regular Expression (Regex)
TF-IDF Vectorizer
Logistic Regression
Joblib
Streamlit
Project Structure
Movie-Sentiment-Analysis/
│
├── dataset/
│   └── movie_reviews.csv
│
├── model/
│   ├── sentiment_model.pkl
│   └── tfidf_vectorizer.pkl
│
├── app.py
│
├── train_model.py
│
├── requirements.txt
│
└── README.md
Project Workflow
Data Collection
Load movie review dataset using Pandas.
Dataset contains movie reviews and sentiment labels.
Data Preprocessing
Convert text into lowercase.
Remove special characters and unnecessary symbols.
Remove extra spaces.
Prepare clean text data for machine learning.
Feature Extraction
Use TF-IDF Vectorizer to convert text reviews into numerical feature vectors.
TF-IDF identifies important words based on their frequency and importance in the dataset.
Model Training
Split dataset into training and testing data.
Train Logistic Regression model using TF-IDF features.
The model learns patterns from positive and negative reviews.
Model Evaluation
Evaluate model performance using:
Accuracy Score
Classification Report
Model Deployment
Save trained model and TF-IDF vectorizer using Joblib.
Deploy the application using Streamlit.
Users can enter a movie review and get sentiment prediction instantly.
Machine Learning Algorithm Used
Logistic Regression

Logistic Regression is a supervised machine learning classification algorithm used for predicting binary outcomes.

In this project:

Input: Movie review text
Output: Positive or Negative sentiment

The model learns from previous movie reviews and predicts the sentiment of new reviews.

Expected Output

Example:

Input Review:

The movie was amazing with excellent acting and a great story.

Output:

Sentiment: Positive

Input Review:

The movie was boring and the storyline was very poor.

Output:

Sentiment: Negative
Conclusion

The Movie Sentiment Analysis project demonstrates how Natural Language Processing and Machine Learning techniques can be used to analyze customer opinions from text data. By using TF-IDF Vectorization and Logistic Regression, the system can classify movie reviews accurately and provide real-time sentiment predictions through a Streamlit application.
