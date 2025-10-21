"""
Unit tests for the Response Analysis Toolkit
"""

"""
AI Assistance Note:
This module was developed using AI tools (Claude, VS Code AI) for:
- Initial test case generation following TDD patterns
- Debugging and interpreting test failures
All architecture and design decisions and final implementations are my own work.
"""

from project import (
    load_feedback_data,
    calculate_total_responses,
    analyse_sentiment,
    get_sentiment_descriptors,
    analyse_response_lengths,
)


### Load feedback data tests ###
def test_load_feedback_data_returns_data():
    data = load_feedback_data("test_data.csv")
    assert data is not None


def test_load_feedback_data_has_rows():
    data = load_feedback_data("test_data.csv")
    assert len(data) > 0


### Calculate total responses tests ###
def test_calculate_total_responses_returns_dict():
    data = load_feedback_data("test_data.csv")
    metrics = calculate_total_responses(data)

    assert isinstance(metrics, dict)
    assert "total_responses" in metrics


def test_calculate_total_responses_counts_correctly():
    data = load_feedback_data("test_data.csv")
    metrics = calculate_total_responses(data)

    assert metrics["total_responses"] == 3


### Sentiment analysis tests ###
def test_analyse_sentiment_returns_dict():
    data = load_feedback_data("test_data.csv")
    themes = analyse_sentiment(data)

    assert isinstance(themes, dict)


def test_analyse_sentiment_sentiment_polarity_exists():
    data = load_feedback_data("test_data.csv")
    themes = analyse_sentiment(data)

    assert "sentiment_polarity" in themes
    assert themes["sentiment_polarity"] is not None


def test_analyse_sentiment_sentiment_polarity_is_numeric():
    data = load_feedback_data("test_data.csv")
    themes = analyse_sentiment(data)

    assert isinstance(themes["sentiment_polarity"], (int, float))


def test_analyse_sentiment_sentiment_subjectivity_exists():
    data = load_feedback_data("test_data.csv")
    themes = analyse_sentiment(data)

    assert "sentiment_subjectivity" in themes
    assert themes["sentiment_subjectivity"] is not None


def test_analyse_sentiment_sentiment_subjectivity_is_numeric():
    data = load_feedback_data("test_data.csv")
    themes = analyse_sentiment(data)

    assert isinstance(themes["sentiment_subjectivity"], (int, float))


### Sentiment descriptors tests ###
def test_get_sentiment_descriptors_very_negative():
    result = get_sentiment_descriptors(-0.8, 0.5)
    assert result["polarity_descriptor"] == "Very Negative"


def test_get_sentiment_descriptors_negative():
    result = get_sentiment_descriptors(-0.3, 0.5)
    assert result["polarity_descriptor"] == "Negative"


def test_get_sentiment_descriptors_neutral():
    result = get_sentiment_descriptors(0.0, 0.5)
    assert result["polarity_descriptor"] == "Neutral"


def test_get_sentiment_descriptors_positive():
    result = get_sentiment_descriptors(0.3, 0.5)
    assert result["polarity_descriptor"] == "Positive"


def test_get_sentiment_descriptors_very_positive():
    result = get_sentiment_descriptors(0.7, 0.5)
    assert result["polarity_descriptor"] == "Very Positive"


def test_get_sentiment_descriptors_highly_objective():
    result = get_sentiment_descriptors(0.0, 0.2)
    assert result["subjectivity_descriptor"] == "Highly Objective"


def test_get_sentiment_descriptors_objective():
    result = get_sentiment_descriptors(0.0, 0.4)
    assert result["subjectivity_descriptor"] == "Somewhat Objective"


def test_get_sentiment_descriptors_subjective():
    result = get_sentiment_descriptors(0.0, 0.6)
    assert result["subjectivity_descriptor"] == "Somewhat Subjective"


def test_get_sentiment_descriptors_highly_subjective():
    result = get_sentiment_descriptors(0.0, 0.8)
    assert result["subjectivity_descriptor"] == "Highly Subjective"


### Response length analysis tests ###
def test_analyse_response_lengths_returns_dict():
    data = load_feedback_data("test_data.csv")
    length_analysis = analyse_response_lengths(data)

    assert isinstance(length_analysis, dict)


def test_analyse_response_lengths_calculates_average():
    data = load_feedback_data("test_data.csv")
    length_analysis = analyse_response_lengths(data)

    assert "average_length" in length_analysis
    assert isinstance(length_analysis["average_length"], (int, float))


def test_analyse_response_lengths_finds_min_and_max():
    data = load_feedback_data("test_data.csv")
    length_analysis = analyse_response_lengths(data)

    assert "min_length" in length_analysis
    assert "max_length" in length_analysis
    assert isinstance(length_analysis["min_length"], int)
    assert isinstance(length_analysis["max_length"], int)


def test_analyse_response_lengths_correct_average():
    data = load_feedback_data("test_data.csv")
    length_analysis = analyse_response_lengths(data)

    # test_data.csv has: "Very satisfied" (14), "Satisfied" (9), "Great course!" (13)
    # Average = (14 + 9 + 13) / 3 = 12
    assert length_analysis["average_length"] == 12


def test_analyse_response_lengths_correct_min():
    data = load_feedback_data("test_data.csv")
    length_analysis = analyse_response_lengths(data)

    # Shortest is "Satisfied" (9 characters)
    assert length_analysis["min_length"] == 9


def test_analyse_response_lengths_correct_max():
    data = load_feedback_data("test_data.csv")
    length_analysis = analyse_response_lengths(data)

    # Longest is "Very satisfied" (14 characters)
    assert length_analysis["max_length"] == 14
