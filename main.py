import io
import json
from fastapi import FastAPI, Request
import torchvision.transforms as transforms
from PIL import Image
from string import punctuation
# text preprocessing modules
from nltk.tokenize import word_tokenize
import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
import re  # regular expression
import os
import joblib
from os.path import dirname, join, realpath



nltk.download('stopwords')
nltk.download('wordnet')

app = FastAPI()

with open(
    join(dirname(realpath(__file__)), "models/sentiment_model_pipeline.pkl"), "rb"
) as f:
    model = joblib.load(f)


def text_preprocessing(text, remove_stop_words=True, lemmatize_words=True):

    text = re.sub(r"[^A-Za-z0-9]", " ", text)
    text = re.sub(r"\'s", " ", text)
    text = re.sub(r"http\S+", " link ", text)
    text = re.sub(r"\b\d+(?:\.\d+)?\s+", "", text)  # remove numbers
    # Remove punctuation from text
    text = "".join([c for c in text if c not in punctuation])
    # Optionally, remove stop words
    if remove_stop_words:
        # load stopwords
        stop_words = stopwords.words("english")
        text = text.split()
        text = [w for w in text if not w in stop_words]
        text = " ".join(text)
    # Optionally, shorten words to their stems
    if lemmatize_words:
        text = text.split()
        lemmatizer = WordNetLemmatizer()
        lemmatized_words = [lemmatizer.lemmatize(word) for word in text]
        text = " ".join(lemmatized_words)
    # Return a list of words
    return text



@app.get("/predict-review")
def predict_sentiment(text: str):

    preprocessed_text = text_preprocessing(text)

    prediction = model.predict([preprocessed_text])
    output = int(prediction[0])
    probas = model.predict_proba([preprocessed_text])
    output_probability = "{:.2f}".format(float(probas[:, output]))

    # output dictionary
    sentiments = {0: "Negative", 1: "Positive"}

    # show results
    result = {"prediction": sentiments[output], "Probability": output_probability}
    return result


if __name__ == '__main__':
    app.run()