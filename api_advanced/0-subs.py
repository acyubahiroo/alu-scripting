#!/usr/bin/python3
"""Retrieve the number of subscribers for a given subreddit."""

import requests


def number_of_subscribers(subreddit):
    """Return the total number of subscribers for a subreddit."""
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)

    headers = {
        "User-Agent": "Mozilla/5.0 (compatible; ALUStudent/1.0)"
    }

    try:
        response = requests.get(
            url,
            headers=headers,
            allow_redirects=False,
            timeout=10
        )

        if response.status_code != 200:
            return 0

        data = response.json().get("data")
        if not data:
            return 0

        return data.get("subscribers", 0)

    except (requests.RequestException, ValueError):
        return 0
