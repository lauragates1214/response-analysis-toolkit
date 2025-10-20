import pandas as pd
from textblob import TextBlob


def main():
    filename = input("Please enter the survey data CSV filename: ")
    data = load_feedback_data(filename)
    metrics = calculate_response_metrics(data)
    themes = analyse_content_themes(data)

    print("Analysis Results:")
    print("Total Responses:", metrics["total_responses"])
    print("Sentiment Polarity:", themes["sentiment_polarity"])
    print("Sentiment Subjectivity:", themes["sentiment_subjectivity"])


def load_feedback_data(filename):
    csv_data = pd.read_csv(filename)
    return csv_data


def calculate_response_metrics(data):
    return {"total_responses": len(data)}


def analyse_content_themes(data):
    text = " ".join(data["response"].astype(str).tolist())
    blob = TextBlob(text)
    polarity = blob.sentiment.polarity
    subjectivity = blob.sentiment.subjectivity
    return {"sentiment_polarity": polarity, "sentiment_subjectivity": subjectivity}


if __name__ == "__main__":
    main()
