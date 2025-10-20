import pandas as pd
from textblob import TextBlob


def main():
    filename = input("Please enter the survey data CSV filename: ")
    data = load_feedback_data(filename)
    metrics = calculate_response_metrics(data)
    themes = analyse_content_themes(data)
    descriptors = get_sentiment_descriptors(
        themes["sentiment_polarity"], themes["sentiment_subjectivity"]
    )

    print("Analysis Results:")
    print("Total Responses:", metrics["total_responses"])
    print(
        "Sentiment Polarity:",
        descriptors["polarity_descriptor"],
        "(" + str(themes["sentiment_polarity"]) + ")",
    )
    print(
        "Sentiment Subjectivity:",
        descriptors["subjectivity_descriptor"],
        "(" + str(themes["sentiment_subjectivity"]) + ")",
    )


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


if __name__ == "__main__":
    main()
