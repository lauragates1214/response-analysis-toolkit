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
