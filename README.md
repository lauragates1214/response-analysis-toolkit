# Response Analysis Toolkit
#### Video Demo: <URL HERE>
#### Description:

## Overview

The Response Analysis Toolkit is a Python application designed to help university educators analyse student feedback data. This tool provides sentiment analysis and basic statistics on survey responses exported from course evaluation systems.

Educators often collect feedback through surveys but lack simple tools to quantify sentiment and extract meaningful insights. This toolkit addresses that gap by processing CSV exports and providing both numerical sentiment scores and human-readable interpretations, making feedback analysis accessible without requiring advanced data science knowledge.

## Project Files

### project.py

This is the main programme file containing all core functionality:

**`main()`** - Orchestrates the complete analysis workflow. It prompts the user for a CSV filename, loads the data, calculates metrics, performs sentiment analysis, and displays formatted results with both numerical scores and descriptive labels.

**`load_feedback_data(file_path)`** - Loads survey data from CSV files using the pandas library. Expects a CSV with specific columns: `response_id`, `question`, `response`, and `timestamp`. Returns a pandas DataFrame for further processing.

**`calculate_response_metrics(data)`** - Calculates basic statistics from the loaded data. Currently returns the total number of responses, providing a foundation for more complex metrics in future iterations.

**`analyse_content_themes(data)`** - Performs sentiment analysis on response text using TextBlob, an accessible natural language processing library. Combines all responses into a single text block and calculates two key metrics: sentiment polarity (how positive or negative) and sentiment subjectivity (how opinion-based versus factual).

**`get_sentiment_descriptors(polarity, subjectivity)`** - Converts numerical sentiment scores into human-readable labels. Takes polarity (-1 to 1) and subjectivity (0 to 1) scores and returns descriptive text like "Very Positive" or "Highly Subjective", making results immediately interpretable for non-technical users.

### test_project.py

Contains comprehensive unit tests for all major functions, following Test-Driven Development (TDD) principles inspired by Harry Percival's *Test-Driven Development with Python, 3rd Edition*. Each function has multiple tests covering normal operation and edge cases. Notably, the sentiment descriptor function includes nine separate tests to verify correct categorisation across the full range of possible sentiment scores (Very Negative, Negative, Neutral, Positive, Very Positive for polarity; Highly Objective, Objective, Subjective, Highly Subjective for subjectivity).

### test_functional.py

Contains the functional test suite that validates the complete user workflow from start to finish. Rather than testing individual functions in isolation, this file ensures the entire programme works correctly when a user runs it. The main test simulates user input, captures programme output, and verifies that all expected analysis results appear with proper formatting.

### test_data.csv

Sample survey data used for testing. Contains three mock responses with the required column structure (`response_id`, `question`, `response`, `timestamp`). Provides realistic test cases including varied sentiment ("Very satisfied", "Satisfied", "Great course!") to verify the sentiment analysis produces sensible results.

### requirements.txt

Lists all Python package dependencies:
- **pandas** - Data manipulation and CSV loading
- **textblob** - Natural language processing for sentiment analysis
- **pytest** - Testing framework

## Design Decisions

**Why TextBlob?** I chose TextBlob for sentiment analysis because it's straightforward to use and provides sufficiently accurate results for basic sentiment categorisation. For an educational tool, I prioritised ease of implementation over advanced NLP capabilities. TextBlob handles the complexity of sentiment analysis without requiring custom model training or extensive configuration.

**Function abstraction** - I extracted `get_sentiment_descriptors` into its own function rather than embedding the logic in `main()`. This follows the principle of separation of concerns: `main()` handles user interaction and output formatting, whilst the helper function focuses solely on sentiment interpretation. This makes the code more testable, readable, and maintainable.

**Test-Driven Development** - I followed TDD methodology strictly throughout development, inspired by Harry Percival's approach. Every feature began with a failing test, followed by minimal implementation to pass that test, then refactoring. This ensured comprehensive test coverage and prevented scope creep.

**UK spelling** - I use British English spelling throughout (`analyse` rather than `analyze`) as I'm based in the UK. Consistency in spelling conventions improves code readability and reflects regional standards.

## CSV Format Requirements

The toolkit expects CSV files with the following columns:
- `response_id` - Unique identifier for each response
- `question` - The survey question text
- `response` - The participant's response text
- `timestamp` - When the response was submitted

## How to Use

1. Install dependencies: `pip install -r requirements.txt`
2. Run the programme: `python project.py`
3. Enter your CSV filename when prompted
4. View the analysis results including total responses, sentiment polarity, and subjectivity with descriptive labels

## Testing

Run the test suite with: `pytest`

All tests should pass, demonstrating that the toolkit correctly loads data, calculates metrics, analyses sentiment, and provides appropriate descriptive labels across all sentiment ranges.

## AI Assistance

I used AI tools throughout this project whilst maintaining ownership of all design decisions and core implementations. Claude served multiple roles: writing initial test cases following TDD patterns, helping interpret test failure output, explaining Django and htmx concepts, and debugging configuration issues. During the code integration phases of the TDD cycle, I instructed Claude to act as a tutor rather than writing code directly - guiding me through implementations step-by-step. I modelled this approach on CS50's duck debugger system prompt, introduced to me at a CS50 Hackathon in London in June 2025. Additionally, I used VS Code's integrated AI for code completions. All architectural decisions, feature designs, and final code implementations were my own work, with AI serving as an educational amplifier rather than a replacement for learning.