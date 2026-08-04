# Movie Sentiment Analysis Using NLP and Machine Learning

## Project Overview

Movie Sentiment Analysis is a Natural Language Processing (NLP) and Machine Learning based project that classifies movie reviews into Positive and Negative sentiments.

This project uses text preprocessing techniques, TF-IDF Vectorization, and Logistic Regression algorithm to analyze movie reviews and predict sentiment. The trained machine learning model is deployed using Streamlit for real-time sentiment prediction.

---

## Objectives

- Analyze movie reviews using Natural Language Processing techniques
- Clean and preprocess text data
- Convert text data into numerical features using TF-IDF Vectorization
- Build a Machine Learning classification model
- Train and evaluate the sentiment analysis model
- Predict sentiment of new movie reviews
- Deploy the trained model using Streamlit

---

## Technologies Used

- Python
- Pandas
- NumPy
- Scikit-learn
- Natural Language Processing (NLP)
- Regular Expression (Regex)
- TF-IDF Vectorizer
- Logistic Regression
- Joblib
- Streamlit

---

## Machine Learning Algorithm

### Logistic Regression

Logistic Regression is a supervised machine learning algorithm used for binary classification problems.

In this project, Logistic Regression is used to classify movie reviews into:

- Positive Sentiment
- Negative Sentiment

The model learns patterns from previously labeled movie reviews and predicts the sentiment of new reviews.

---

## Project Workflow

### 1. Data Collection

- Load the movie review dataset using Pandas.
- The dataset contains movie reviews along with sentiment labels.

### 2. Text Preprocessing

The review text is cleaned using preprocessing techniques:

- Convert text into lowercase
- Remove special characters
- Remove unnecessary spaces
- Prepare clean text data for model training

### 3. Feature Extraction

TF-IDF (Term Frequency-Inverse Document Frequency) Vectorization is used to convert text reviews into numerical feature vectors.

TF-IDF helps identify important words and patterns from movie reviews.

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

## Project Structure

```text
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
```

---

## Installation and Setup

### Clone the Repository

```bash
git clone <repository-url>
```

### Navigate to Project Directory

```bash
cd Movie-Sentiment-Analysis
```

### Install Required Libraries

```bash
pip install -r requirements.txt
```

---

## Running the Application

Run the Streamlit application using:

```bash
streamlit run app.py
```

The application will open in the browser and users can enter movie reviews to get sentiment predictions.

---

## Sample Prediction

### Positive Review

Input:

```
The movie was amazing with excellent acting and a great storyline.
```

Output:

```
Sentiment: Positive
```

---

### Negative Review

Input:

```
The movie was boring and the story was very disappointing.
```

Output:

```
Sentiment: Negative
```

---

## Model Performance

The model is evaluated using the following metrics:

- Accuracy Score
- Precision
- Recall
- F1-score

These metrics help measure the effectiveness of the sentiment classification model.

---

## Future Enhancements

- Implement advanced NLP models such as BERT and Transformer models
- Improve accuracy using deep learning techniques
- Add multi-class sentiment classification
- Deploy the application on cloud platforms

---

## Conclusion

Movie Sentiment Analysis demonstrates the application of Natural Language Processing and Machine Learning techniques for text classification.

By using TF-IDF Vectorization and Logistic Regression, the system can classify movie reviews into positive and negative sentiments. The Streamlit application provides an interactive interface for real-time sentiment prediction.
