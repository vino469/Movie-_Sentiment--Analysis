Movie Sentiment Analysis Using NLP and Machine Learning
Project Overview

Movie Sentiment Analysis is a Natural Language Processing (NLP) and Machine Learning project that classifies movie reviews into Positive and Negative sentiment categories.

The project applies various NLP techniques, including text preprocessing and TF-IDF Vectorization, to transform review text into numerical features. A Logistic Regression classification algorithm is trained to identify sentiment patterns from movie reviews.

The trained model is deployed using Streamlit, providing an interactive web application where users can enter movie reviews and receive real-time sentiment predictions.

Project Objectives
Perform sentiment analysis on movie review data using NLP techniques.
Clean and preprocess raw text data for machine learning.
Convert textual data into numerical features using TF-IDF Vectorization.
Build and train a machine learning classification model.
Evaluate model performance using classification metrics.
Deploy the trained sentiment analysis model using Streamlit.
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
Machine Learning Algorithm
Logistic Regression

Logistic Regression is a supervised machine learning algorithm used for binary classification problems.

In this project, Logistic Regression is used to classify movie reviews into:

Positive Sentiment
Negative Sentiment

The model learns from previously labeled movie reviews and predicts the sentiment of new unseen reviews.

Project Workflow
1. Data Collection
Load the movie review dataset using Pandas.
The dataset contains movie reviews along with sentiment labels.
2. Data Preprocessing

Text preprocessing is performed to improve model performance:

Convert text into lowercase.
Remove special characters and unnecessary symbols.
Remove extra spaces.
Clean and prepare text data for feature extraction.
3. Feature Extraction

TF-IDF (Term Frequency-Inverse Document Frequency) Vectorization is used to convert text data into numerical feature vectors.

TF-IDF helps identify important words in movie reviews based on their frequency and importance within the dataset.

4. Model Training
Split the dataset into training and testing data.
Train the Logistic Regression model using TF-IDF features.
Learn patterns from positive and negative movie reviews.
5. Model Evaluation

The trained model is evaluated using:

Accuracy Score
Classification Report
6. Model Deployment
Save the trained model and TF-IDF vectorizer using Joblib.
Deploy the application using Streamlit.
Provide real-time sentiment prediction through a web interface.
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
├── train_model.py
├── requirements.txt
└── README.md
Installation and Setup
Clone the Repository
git clone <repository-url>
Navigate to Project Directory
cd Movie-Sentiment-Analysis
Install Required Libraries
pip install -r requirements.txt
Running the Application

Run the Streamlit application using:

streamlit run app.py

The application will open in your browser, where users can enter movie reviews and get sentiment predictions.

Sample Prediction
Input
The movie was excellent with great acting and an amazing storyline.
Output
