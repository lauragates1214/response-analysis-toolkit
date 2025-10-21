"""
AI Assistance Note:
This module was developed using AI tools (Claude, VS Code AI) for:
- Initial test case generation following TDD patterns
- Debugging and interpreting test failures
All architecture and design decisions and final implementations are my own work.
"""

import pandas as pd
from textblob import TextBlob


def main():
    filename = input("Please enter the survey data CSV filename: ")
    data = load_feedback_data(filename)
    total = calculate_total_responses(data)
    sentiment = analyse_sentiment(data)
    descriptors = get_sentiment_descriptors(
        sentiment["sentiment_polarity"], sentiment["sentiment_subjectivity"]
    )
    lengths = analyse_response_lengths(data)

    print("Analysis Results:")
    print("Total Responses:", total["total_responses"])
    print(
        "Sentiment Polarity:",
        descriptors["polarity_descriptor"],
        "(" + str(sentiment["sentiment_polarity"]) + ")",
    )
    print(
        "Sentiment Subjectivity:",
        descriptors["subjectivity_descriptor"],
        "(" + str(sentiment["sentiment_subjectivity"]) + ")",
    )
    print("Average Response Length:", lengths["average_length"])
    print("Shortest Response:", lengths["min_length"])
    print("Longest Response:", lengths["max_length"])


def load_feedback_data(filename):
    csv_data = pd.read_csv(filename)
    return csv_data


def calculate_total_responses(data):
    return {"total_responses": len(data)}


def analyse_sentiment(data):
    text = " ".join(data["response"].astype(str).tolist())
    blob = TextBlob(text)
    polarity = blob.sentiment.polarity
    subjectivity = blob.sentiment.subjectivity
    return {"sentiment_polarity": polarity, "sentiment_subjectivity": subjectivity}


def get_sentiment_descriptors(polarity, subjectivity):
    if polarity > 0.5:
        polarity_descriptor = "Very Positive"
    elif polarity > 0.1:
        polarity_descriptor = "Positive"
    elif polarity < -0.5:
        polarity_descriptor = "Very Negative"
    elif polarity < -0.1:
        polarity_descriptor = "Negative"
    else:
        polarity_descriptor = "Neutral"

    if subjectivity > 0.7:
        subjectivity_descriptor = "Highly Subjective"
    elif subjectivity > 0.5:
        subjectivity_descriptor = "Somewhat Subjective"
    elif subjectivity > 0.3:
        subjectivity_descriptor = "Somewhat Objective"
    else:
        subjectivity_descriptor = "Highly Objective"

    return {
        "polarity_descriptor": polarity_descriptor,
        "subjectivity_descriptor": subjectivity_descriptor,
    }


def analyse_response_lengths(data):
    lengths = data["response"].astype(str).apply(len)
    average_length = sum(lengths) / len(lengths)
    min_length = min(lengths)
    max_length = max(lengths)
    return {
        "average_length": average_length,
        "min_length": min_length,
        "max_length": max_length,
    }


if __name__ == "__main__":
    main()
