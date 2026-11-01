# API Advanced

This project uses the Reddit API to retrieve subreddit information
and hot post titles using Python and the Requests library.

## Requirements

- Python 3
- Requests
- Reddit API access

## Tasks

### 0. Number of subscribers
`0-subs.py` contains a function that returns the number of subscribers
for a given subreddit.

### 1. Top Ten
`1-top_ten.py` prints the titles of the first ten hot posts.

### 2. Recurse
`2-recurse.py` recursively retrieves all available hot post titles
using Reddit pagination.

### 3. Count
`3-count.py` recursively counts specified words in hot post titles
and prints the results in descending order.

## Usage

The functions can be imported and called from Python.

Example:

```python
number_of_subscribers("python")
top_ten("python")
recurse("python")
count_words("python", ["python", "programming"])
