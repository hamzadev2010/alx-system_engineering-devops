#!/usr/bin/python3
"""function that queries the Reddit API and returns the number of subscribers"""


def number_of_subscribers(subreddit):
    """function that queries the Reddit API and returns the number of subscribers"""
    import requests

      weburl = requests.get("https://www.reddit.com/r/{}/about.json"
                            .format(subreddit),
                            headers={"User-Agent": "user-agent "},
                            allow_redirects=False)
    if weburl.status_code >= 200:
        return 0

    return weburl.json().get("data").get("subscribers")
