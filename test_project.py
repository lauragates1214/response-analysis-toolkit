"""
Unit tests for the Response Analysis Toolkit
"""

from project import load_feedback_data, calculate_response_metrics


def test_load_feedback_data_returns_data():
    data = load_feedback_data("test_data.csv")
    assert data is not None


def test_calculate_response_metrics_returns_dict():
    data = load_feedback_data("test_data.csv")
    metrics = calculate_response_metrics(data)

    assert isinstance(metrics, dict)
    assert "total_responses" in metrics


def test_calculate_response_metrics_counts_correctly():
    data = load_feedback_data("test_data.csv")
    metrics = calculate_response_metrics(data)

    assert metrics["total_responses"] == 3
