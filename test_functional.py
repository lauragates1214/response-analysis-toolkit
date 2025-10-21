"""
Functional Tests for Feedback Analysis Toolkit
"""

"""
AI Assistance Note:
This module was developed using AI tools (Claude, GitHub Copilot) for:
- Initial test case generation following TDD patterns
- Debugging and interpreting test failures
- Writing the initial draft of the get_visualisation function
All architecture and design decisions and final implementations are my own work.
"""

import io
import os
import pytest
from unittest.mock import patch

from project import main


@pytest.fixture
def run_analysis():
    """Fixture that runs the program with test_data.csv
        The program processes her data and displays:
    - The total number of responses she received
    - The overall sentiment (how positive the feedback was), with descriptive text
    - How subjective vs objective the responses were, with descriptive text
    - Response length statistics (average, min, max)"""

    def _run():
        with patch("builtins.input", return_value="test_data.csv"):
            with patch("sys.stdout", new=io.StringIO()) as fake_output:
                main()
                return fake_output.getvalue()

    return _run


"""
Aya, a course instructor who has collected student feedback, runs the program
and enters her filename.
The program processes her data and returns analysis results.
She can now see meaningful insights from her feedback data.
"""


def test_analysis_results_printed(run_analysis):
    # Aya runs the program and enters her filename
    output = run_analysis()

    # She sees 'Analysis Results' displayed
    assert "Analysis Results" in output


def test_total_responses_printed(run_analysis):
    """
    Aya wants to see how many students responded to the survey.
    """
    output = run_analysis()

    # She sees total responses
    assert "Total Responses: 3" in output


def test_sentiment_analysis_printed(run_analysis):
    """
    Aya wants to see an sentiment analysis to gauge course satisfaction.
    """
    output = run_analysis()

    # She sees the sentiment analysis
    assert "Sentiment Polarity" in output
    assert "Sentiment Subjectivity" in output

    # The sentiment scores are visible
    assert "0.7" in output  # Approximate polarity score
    assert "0.9" in output  # Approximate subjectivity score

    # There is descriptive text for each of the scores
    assert "Positive" in output  # Descriptive text for polarity
    assert "Subjective" in output  # Descriptive text for subjectivity


def test_response_length_analysis_printed(run_analysis):
    """
    Aya wants to see an analysis of length of responses to assess engagement.
    """
    output = run_analysis()

    # She sees the response length analysis
    assert "Average Response Length" in output
    assert "Shortest Response" in output
    assert "Longest Response" in output


def test_displays_word_frequency_analysis(run_analysis):
    """
    Aya wants to see which words appear most frequently in responses
    to identify common themes.
    """
    output = run_analysis()

    # She sees word frequency analysis
    assert "Most Common Words" in output
    # Common words from test data should appear
    assert "satisfied" in output.lower() or "course" in output.lower()


def test_generates_visualisation(run_analysis):
    """
    Aya wants a visual chart of her analysis results
    that she can include in reports.
    """
    # Remove any existing chart
    if os.path.exists("analysis_chart.png"):
        os.remove("analysis_chart.png")

    output = run_analysis()

    # Chart should be created
    assert os.path.exists("analysis_chart.png")

    # Cleanup
    os.remove("analysis_chart.png")
