
# Job Skill Analysis from Y Combinator's "Ask HN: Who is Hiring?" Section

This Python script scrapes the Y Combinator "Ask HN: Who is Hiring?" thread, analyzes comments, and provides insights into the most mentioned technologies and programming languages.

## Features
- Scrapes job postings from the "Who is hiring?" section of Y Combinator’s Ask HN.
- Counts the mentions of specific programming languages and technologies.
- Displays a bar chart of the most sought-after skills based on user comments.

## Requirements
- `requests` — for sending HTTP requests.
- `beautifulsoup4` — for parsing the HTML content.
- `matplotlib` — for plotting the bar chart.

## Installation

1. Install the required libraries:
   ```bash
   pip install requests beautifulsoup4 matplotlib
   ```

2. Run the script:
   ```bash
   python3 your_script_name.py
   ```

## Usage

1. When you run the script, it prompts you for the URL of a Y Combinator “Ask HN: Who is Hiring?” post.
2. The script will scrape the page, find job-related comments, and count the mentions of specific technologies (e.g., Python, JavaScript, React, etc.).
3. The results will be displayed in a bar chart with the technologies on the x-axis and the count of mentions on the y-axis.

## Example Output

The output will show a bar graph where each bar represents a technology (like Python, JavaScript, etc.), and the height of each bar corresponds to the number of mentions in the comments.

