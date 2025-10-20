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

from project import get_sentiment_descriptors


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
