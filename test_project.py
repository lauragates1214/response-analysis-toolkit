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
    calculate_response_metrics,
    analyse_content_themes,
    analyse_response_lengths,
)


def test_load_feedback_data_returns_data():
    data = load_feedback_data("test_data.csv")
    assert data is not None


def test_load_feedback_data_has_rows():
    data = load_feedback_data("test_data.csv")
    assert len(data) > 0


def test_calculate_response_metrics_returns_dict():
    data = load_feedback_data("test_data.csv")
    metrics = calculate_response_metrics(data)

    assert isinstance(metrics, dict)
    assert "total_responses" in metrics


def test_calculate_response_metrics_counts_correctly():
    data = load_feedback_data("test_data.csv")
    metrics = calculate_response_metrics(data)

    assert metrics["total_responses"] == 3


def test_analyse_content_themes_returns_dict():
    data = load_feedback_data("test_data.csv")
    themes = analyse_content_themes(data)

    assert isinstance(themes, dict)


def test_analyse_content_themes_sentiment_polarity_exists():
    data = load_feedback_data("test_data.csv")
    themes = analyse_content_themes(data)

    assert "sentiment_polarity" in themes
    assert themes["sentiment_polarity"] is not None


def test_analyse_content_themes_sentiment_polarity_is_numeric():
    data = load_feedback_data("test_data.csv")
    themes = analyse_content_themes(data)

    assert isinstance(themes["sentiment_polarity"], (int, float))


def test_analyse_content_themes_sentiment_subjectivity_exists():
    data = load_feedback_data("test_data.csv")
    themes = analyse_content_themes(data)

    assert "sentiment_subjectivity" in themes
    assert themes["sentiment_subjectivity"] is not None


def test_analyse_content_themes_sentiment_subjectivity_is_numeric():
    data = load_feedback_data("test_data.csv")
    themes = analyse_content_themes(data)

    assert isinstance(themes["sentiment_subjectivity"], (int, float))


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
