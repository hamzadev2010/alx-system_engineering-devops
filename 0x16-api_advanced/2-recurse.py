#!/usr/bin/python3
"""Display  list containing the titles of all hot articles for a given subreddit."""

import requests

def recurse(subreddit, hot_list=[], cn=0, after=None):
    """ecursive function that queries the Reddit API
    and returns a list containing the titles
    of all hot articles for a given subreddit.
    If no results are found for the given subreddit,
    the function should return None."""


    req = requests.get("https://www.reddit.com/r/{}/hot.json"
                            .format(subreddit),
                            params={"cn": cn, "after": after},
                            headers={"User-Agent": "Google chrome client"},
                            allow_redirects=False)
    if req.status_code >= 300:
        return None

    hot_l = hot_list + [child.get("data").get("title")
                        for child in req.json()
                        .get("data")
                        .get("children")]

    res = req.json()
    if not res("data").get("after"):
        return hot_l

    return recurse(subreddit, hot_l, res("data").get("count"),
                   res("data").get("after"))
