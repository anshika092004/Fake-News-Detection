from flask import Flask, render_template, request
import pandas as pd
import sklearn
import itertools
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import numpy as np
import seaborn as sb
import re
import nltk
import pickle
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords

import nltk
nltk.download('wordnet')
nltk.download('omw-1.4')   # Optional, helps with multilingual lemmatization
nltk.download('punkt')     # Required for word_tokenize


app = Flask(__name__,template_folder='./templates',static_folder='./static')

loaded_model = pickle.load(open("model.pkl", 'rb'))
vector = pickle.load(open("vectorizer.pkl", 'rb'))
lemmatizer = WordNetLemmatizer()
stpwrds = set(stopwords.words('english'))
corpus = []

stop_words = list(set(stopwords.words('english'))) 
lemmatizer = WordNetLemmatizer()

def clean_text(text):
    text = re.sub(r"http\S+|www\S+|https\S+", '', text)
    text = re.sub(r'\@[\w]+|\#','', text)  # Keep named entities
    text = text.lower()
    text = re.sub(r'[^a-z\s]', '', text)  # Remove only special characters
    tokens = word_tokenize(text)
    stop_words = set(stopwords.words('english'))
    filtered_tokens = [lemmatizer.lemmatize(w) for w in tokens if w not in stop_words and len(w) > 2]
    return " ".join(filtered_tokens)
    

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/predict", methods=["GET", "POST"])
def predict():
    if request.method == "POST":
        news = request.form["news"]
        if news.strip() == "":
            return render_template("prediction.html", prediction="Please enter some text.")
        vectorized_input = vector.transform([clean_text(news)])
        prediction = loaded_model.predict(vectorized_input)[0]
        result = "Fake News" if prediction == 0 else "Real News"
        return render_template("prediction.html", prediction=result)
    return render_template("prediction.html", prediction="")



if __name__ == '__main__':
    app.run(debug=True)