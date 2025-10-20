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

from unittest.mock import patch
import io

from project import (
    main,
    load_feedback_data,
    calculate_response_metrics,
    analyse_content_themes,
)


def test_complete_user_workflow():
    """
    Sarah is a course coordinator who has collected feedback from students.
    She has exported the responses as 'test_data.csv' and wants to analyse it.

    She runs the Response Analysis Toolkit from her terminal.
    The program asks her for the CSV filename.
    She types 'test_data.csv' and presses enter.

    The program processes her data and displays:
    - The total number of responses she received
    - The overall sentiment (how positive the feedback was), with descriptive text
    - How subjective vs objective the responses were, with descriptive text

    She can now see meaningful insights from her feedback data.
    """

    # Sarah runs the program and enters her filename
    with patch("builtins.input", return_value="test_data.csv"):
        with patch("sys.stdout", new=io.StringIO()) as fake_output:
            main()
            output = fake_output.getvalue()

            # She sees the analysis results displayed
            assert "Analysis Results" in output
            assert "Total Responses: 3" in output
            assert "Sentiment Polarity" in output
            assert "Sentiment Subjectivity" in output

            # The sentiment scores are visible
            assert "0.7" in output  # Approximate polarity score
            assert "0.9" in output  # Approximate subjectivity score
            assert "Positive" in output  # Descriptive text for polarity
            assert "Subjective" in output  # Descriptive text for subjectivity
