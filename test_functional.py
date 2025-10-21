"""
Functional Tests for Feedback Analysis Toolkit
"""

"""
AI Assistance Note:
This module was developed using AI tools (Claude, VS Code AI) for:
- Initial test case generation following TDD patterns
- Debugging and interpreting test failures
All architecture and design decisions and final implementations are my own work.
"""

import io
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
The program processes her data and returns analysis results:
She can now see meaningful insights from her feedback data.
"""


def test_analysis_results_printed(run_analysis):
    # Aya runs the program and enters her filename
    output = run_analysis()

    # She sees 'Analysis Results' displayed
    assert "Analysis Results" in output


def test_total_responses_printed(run_analysis):
    # Aya runs the program and enters her filename
    output = run_analysis()

    # She sees total responses
    assert "Total Responses: 3" in output


def test_sentiment_analysis_printed(run_analysis):
    # Aya runs the program and enters her filename
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
    # Aya runs the program and enters her filename
    output = run_analysis()

    # She sees the response length analysis
    assert "Average Response Length" in output
    assert "Shortest Response" in output
    assert "Longest Response" in output
