Movie Sentiment Analysis Using NLP and Machine Learning
Project Overview

Movie Sentiment Analysis is a Natural Language Processing (NLP) and Machine Learning based project that classifies movie reviews into two categories: Positive and Negative sentiment.

This project uses text preprocessing techniques, TF-IDF Vectorization, and Logistic Regression algorithm to analyze movie reviews and predict sentiment.

The trained Machine Learning model is deployed using Streamlit, allowing users to enter new movie reviews and receive real-time sentiment predictions.

Objectives
Analyze movie reviews using Natural Language Processing techniques
Clean and preprocess text data
Convert text data into numerical features using TF-IDF Vectorization
Build a Machine Learning classification model
Train and evaluate the sentiment analysis model
Predict sentiment for new movie reviews
Deploy the trained model using Streamlit
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
1. Data Collection
Load the movie review dataset using Pandas.
Dataset contains movie reviews with sentiment labels.
2. Text Preprocessing
Convert text into lowercase.
Remove special characters and unwanted symbols.
Remove extra spaces.
Prepare clean text data for model training.
3. Feature Extraction
Use TF-IDF Vectorizer to convert text reviews into numerical values.
Extract important features from movie review text.
4. Model Training
Split the dataset into training and testing data.
Train the Logistic Regression model using TF-IDF features.
The model learns patterns from positive and negative reviews.
5. Model Evaluation

The model performance is evaluated using:

Accuracy Score
Classification Report
6. Model Deployment
Save the trained model and vectorizer using Joblib.
Deploy the application using Streamlit.
Users can enter movie reviews and get sentiment predictions.
Machine Learning Algorithm Used
Logistic Regression

Logistic Regression is a supervised machine learning algorithm used for binary classification problems.

In this project:

Input:

Movie review text

Output:

Positive sentiment
Negative sentiment

The model analyzes the review text patterns and predicts the sentiment category.

Expected Output

Example 1:

Input:

The movie was amazing with excellent acting and a great story.

Output:

Sentiment: Positive

Example 2:

Input:

The movie was boring and the storyline was very poor.

Output:

Sentiment: Negative
Conclusion

The Movie Sentiment Analysis project demonstrates the application of Natural Language Processing and Machine Learning techniques for text classification.

By using TF-IDF Vectorization and Logistic Regression, the system can classify movie reviews into positive and negative sentiments. The Streamlit deployment provides an interactive interface for real-time sentiment prediction.
