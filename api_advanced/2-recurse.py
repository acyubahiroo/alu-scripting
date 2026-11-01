#!/usr/bin/python3
"""Recursively retrieve all hot article titles from a subreddit."""

import requests


def recurse(subreddit, hot_list=[], after=None):
    """Return a list of all hot article titles using recursion."""
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
            return None if not hot_list else hot_list

        data = response.json().get("data", {})
        posts = data.get("children", [])

        if not posts:
            return hot_list if hot_list else None

        for post in posts:
            title = post.get("data", {}).get("title")
            if title:
                hot_list.append(title)

        next_after = data.get("after")

        if next_after:
            return recurse(subreddit, hot_list, next_after)

        return hot_list if hot_list else None

    except (requests.RequestException, ValueError):
        return None if not hot_list else hot_list
