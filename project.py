import pandas as pd


def load_feedback_data(file_path):
    csv_data = pd.read_csv(file_path)
    return csv_data


def calculate_response_metrics(data):
    return {"total_responses": len(data)}
