import pandas as pd
from textblob import TextBlob


def load_feedback_data(file_path):
    csv_data = pd.read_csv(file_path)
    return csv_data


def calculate_response_metrics(data):
    return {"total_responses": len(data)}


def analyse_content_themes(data):
    text = " ".join(data["response"].astype(str).tolist())
    blob = TextBlob(text)
    polarity = blob.sentiment.polarity
    subjectivity = blob.sentiment.subjectivity
    return {"sentiment_polarity": polarity, "sentiment_subjectivity": subjectivity}
