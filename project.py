"""
AI Assistance Note:
This module was developed using AI tools (Claude, VS Code AI) for:
- Initial test case generation following TDD patterns
- Debugging and interpreting test failures
All architecture and design decisions and final implementations are my own work.
"""

from collections import Counter
import matplotlib.pyplot as plt
import pandas as pd
from textblob import TextBlob


def main():
    filename = input("Please enter the survey data CSV filename: ")
    data = load_feedback_data(filename)
    metrics = calculate_total_responses(data)
    themes = analyse_sentiment(data)
    descriptors = get_sentiment_descriptors(
        themes["sentiment_polarity"], themes["sentiment_subjectivity"]
    )
    lengths = analyse_response_lengths(data)
    most_common = analyse_word_frequency(data)

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
    print("Average Response Length:", lengths["average_length"])
    print("Shortest Response:", lengths["min_length"])
    print("Longest Response:", lengths["max_length"])
    print("Most Common Words:", most_common)

    # Generate visualisation
    generate_visualisation(metrics, themes, descriptors, "analysis_chart.png")
    print("\nVisualisation saved to analysis_chart.png")


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


def analyse_word_frequency(data):
    text = " ".join(data["response"].astype(str))
    words = text.split()
    word_counts = Counter(words)
    most_common = word_counts.most_common(10)  # get top 10
    return {"top_words": most_common}


# AI-assisted (Claude)
def generate_visualisation(metrics, themes, descriptors, filename):
    """Generate a bar chart visualisation of sentiment analysis results"""
    # Create data for the chart (only sentiment metrics)
    categories = ["Sentiment Polarity", "Sentiment Subjectivity"]
    values = [themes["sentiment_polarity"], themes["sentiment_subjectivity"]]

    # Create the bar chart
    plt.figure(figsize=(10, 6))
    plt.bar(categories, values, color=["green", "orange"])
    plt.title("Sentiment Analysis Results")
    plt.ylabel("Score (0-1)")
    plt.xlabel("Themes")
    plt.ylim(0, 1)  # Set y-axis range from 0 to 1

    # Add value labels with descriptors on top of bars
    plt.text(
        0,
        values[0],
        f'{values[0]:.2f}\n({descriptors["polarity_descriptor"]})',
        ha="center",
        va="bottom",
    )
    plt.text(
        1,
        values[1],
        f'{values[1]:.2f}\n({descriptors["subjectivity_descriptor"]})',
        ha="center",
        va="bottom",
    )

    # Save to file
    plt.savefig(filename)
    plt.close()


if __name__ == "__main__":
    main()
