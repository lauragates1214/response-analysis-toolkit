"""
Functional Tests for Feedback Analysis Toolkit
"""

from project import load_feedback_data, calculate_response_metrics


def test_user_can_load_and_analyze_feedback_data():
    """
    Sarah is a course coordinator who has exported feedback responses
    from her survey platform as a CSV file. She wants to analyse the data.

    She runs the feedback analysis toolkit and loads her CSV file.
    The program successfully reads the file and shows her some basic
    statistics about the responses.
    """
    # Sarah has a CSV file with feedback data
    from project import load_feedback_data

    test_file = "test_data.csv"

    # She loads the file using the toolkit
    # This should not crash
    data = load_feedback_data(test_file)

    # She can see that data was loaded successfully
    assert data is not None

    # She can see how many responses were collected
    assert len(data) > 0


def test_user_can_calculate_basic_response_metrics():
    """
    Sarah has loaded her feedback data and now wants to see
    some basic statistics about the responses.

    She calculates response metrics which tells her:
    - Total number of responses
    - Response rate (if applicable)
    - Any other useful statistics
    """

    # Sarah loads her data
    data = load_feedback_data("test_data.csv")

    # She calculates basic metrics
    metrics = calculate_response_metrics(data)

    # She can see the total number of responses
    assert metrics is not None
    assert "total_responses" in metrics
    assert metrics["total_responses"] == 3
