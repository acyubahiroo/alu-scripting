#!/usr/bin/python3
"""Count keyword occurrences in hot subreddit post titles."""

import re

import requests


def count_words(subreddit, word_list, after=None, counts=None):
    """Recursively count words in hot post titles."""
    if counts is None:
        counts = {}

    for word in word_list:
        key = word.lower()
        if key not in counts:
            counts[key] = 0

    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)

    headers = {
        "User-Agent": "linux:alu_api_advanced:v1.0"
    }

    params = {"limit": 100}
    if after:
        params["after"] = after

    try:
        response = requests.get(
            url,
            headers=headers,
            allow_redirects=False,
            params=params,
            timeout=10
        )

        if response.status_code != 200:
            return

        data = response.json().get("data", {})
        posts = data.get("children", [])

        if not posts:
            return

        for post in posts:
            title = post.get("data", {}).get("title", "").lower()
            words = re.sub(r"[^\w\s]", "", title).split()

            for word in word_list:
                counts[word.lower()] += words.count(word.lower())

        next_after = data.get("after")

        if next_after:
            count_words(subreddit, word_list, next_after, counts)
        else:
            results = [
                (word, count)
                for word, count in counts.items()
                if count > 0
            ]

            results.sort(key=lambda item: (-item[1], item[0]))

            for word, count in results:
                print("{}: {}".format(word, count))

    except (requests.RequestException, ValueError):
        return
