# Response Analysis Toolkit
#### Video Demo: <URL HERE>
#### Description:

## Overview

The Response Analysis Toolkit is a Python application designed to help university educators analyse student feedback data. Built as the final project for CS50P (Introduction to Programming with Python), this tool provides sentiment analysis, response length patterns, word frequency analysis and visual charts on survey responses exported from course evaluation systems.

Educators often collect feedback through surveys but lack simple tools to quantify sentiment and extract meaningful insights. This toolkit addresses that gap by processing CSV exports and providing both numerical sentiment scores and human-readable interpretations, making feedback analysis accessible without requiring advanced data science knowledge.

## Project Files

### project.py

This is the main programme file containing all core functionality:

**`main()`** - Orchestrates the complete analysis workflow. It prompts the user for a CSV filename, loads the data, calculates metrics, performs sentiment analysis, analyses response lengths and word frequency, generates a visualisation chart, and displays formatted results with both numerical scores and descriptive labels.

**`load_feedback_data(file_path)`** - Loads survey data from CSV files using the pandas library. Expects a CSV with specific columns: `response_id`, `question`, `response`, and `timestamp`. Returns a pandas DataFrame for further processing.

**`calculate_response_metrics(data)`** - Calculates basic statistics from the loaded data. Currently returns the total number of responses, providing a foundation for more complex metrics in future iterations.

**`analyse_content_themes(data)`** - Performs sentiment analysis on response text using TextBlob, an accessible natural language processing library. Combines all responses into a single text block and calculates two key metrics: sentiment polarity (how positive or negative) and sentiment subjectivity (how opinion-based versus factual).

**`get_sentiment_descriptors(polarity, subjectivity)`** - Converts numerical sentiment scores into human-readable labels. Takes polarity (-1 to 1) and subjectivity (0 to 1) scores and returns descriptive text like "Very Positive" or "Highly Subjective", making results immediately interpretable for non-technical users.

**`analyse_response_lengths(data)`** - Calculates response length statistics including average length, shortest response, and longest response. Helps educators understand engagement levels, as longer responses often indicate more thoughtful feedback.

**`analyse_word_frequency(data)`** - Identifies the most common words appearing in responses using Python's Counter class. Returns the top 10 most frequent words as tuples of (word, count), helping educators quickly identify recurring themes and topics in feedback.

**`generate_visualisation(metrics, themes, descriptors, filename)`** - Creates a bar chart visualisation of sentiment analysis results using matplotlib. The chart displays sentiment polarity and subjectivity scores with descriptive labels, saved as a PNG file that can be included in reports or presentations.

### test_project.py

Contains comprehensive unit tests for all major functions, following Test-Driven Development (TDD) principles inspired by Harry Percival's *Test-Driven Development with Python, 3rd Edition*. Each function has multiple tests covering normal operation and edge cases. The test suite includes 27 unit tests covering data loading, metrics calculation, sentiment analysis with descriptor categorisation, response length calculations, word frequency analysis, and visualisation file creation.

### test_functional.py

Contains the functional test suite that validates the complete user workflow from start to finish. Uses pytest fixtures to simulate user input and capture programme output, ensuring the entire application works correctly when a user runs it. Tests verify that all analysis results appear with proper formatting and that the visualisation file is generated successfully.

### test_data.csv

Sample survey data used for testing. Contains three mock responses with the required column structure (`response_id`, `question`, `response`, `timestamp`). Provides realistic test cases including varied sentiment ("Very satisfied", "Satisfied", "Great course!") to verify the sentiment analysis produces sensible results.

### requirements.txt

Lists all Python package dependencies:
- **pandas** - Data manipulation and CSV loading
- **textblob** - Natural language processing for sentiment analysis
- **matplotlib** - Data visualisation and chart generation
- **pytest** - Testing framework

## Design Decisions

**Why TextBlob?** I chose TextBlob for sentiment analysis because it's straightforward to use and provides sufficiently accurate results for basic sentiment categorisation. For an educational tool, I prioritised ease of implementation over advanced NLP capabilities. TextBlob handles the complexity of sentiment analysis without requiring custom model training or extensive configuration.

**Function abstraction** - I extracted `get_sentiment_descriptors` into its own function rather than embedding the logic in `main()`. This follows the principle of separation of concerns: `main()` handles user interaction and output formatting, whilst the helper function focuses solely on sentiment interpretation. This makes the code more testable, readable, and maintainable.

**Response length analysis** - I implemented response length metrics to provide educators with insights into student engagement. Longer responses often indicate more thoughtful feedback, making this a useful supplementary metric alongside sentiment analysis.

**Word frequency with Counter** - For word frequency analysis, I used Python's built-in `collections.Counter` class rather than building a custom counting solution. This leverages well-tested standard library functionality and keeps the code concise and maintainable.

**Visualisation design** - I initially included total responses in the visualisation but removed it because the vastly different scales (responses = 3, sentiment = 0-1) created a misleading chart. The final design focuses solely on sentiment metrics (polarity and subjectivity) which share the same 0-1 scale, making visual comparisons meaningful.

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
4. View the analysis results including:
   - Total responses
   - Sentiment polarity and subjectivity with descriptive labels
   - Response length statistics (average, shortest, longest)
   - Top 10 most common words
5. Find the generated visualisation saved as `analysis_chart.png`

## Testing

Run the test suite with: `pytest`

All tests should pass, demonstrating that the toolkit correctly loads data, calculates metrics, analyses sentiment, computes response lengths, identifies word frequency, and generates visualisations with appropriate formatting across all scenarios.

## AI Assistance

I used AI tools throughout this project whilst maintaining ownership of all design decisions and core implementations. Claude, my LLM of choice, served multiple roles: writing initial test cases following TDD patterns, helping interpret test failure output, writing the initial draft of the `generate_visualisation` function in project.py, and writing this README after agreeing outline and content with me. During the code integration phases of the TDD cycle, I instructed Claude to act as a tutor rather than writing code directly - guiding me through implementations step-by-step. I modelled this approach on CS50's duck debugger system prompt, introduced to me at a CS50 Hackathon in London in June 2025. Additionally, I used GitHub Copilot in VS Code for code completions. All architectural decisions, feature designs, and final code implementations were my own work, with AI serving as an educational amplifier rather than a replacement for learning.