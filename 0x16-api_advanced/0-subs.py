#!/usr/bin/python3
"""Display number of subscribers
"""
import requests


def number_of_subscribers(subreddit):
    """a function that queries the Reddit API
    and returns the number of subscribers"""
    weburl = ("https://www.reddit.com/r/{}/about.json".format(subreddit))
    headers = {'User-Agent': 'Google chrome client'}
    res = requests.get(weburl, headers=headers, allow_redirects=False)

    if res.status_code != 100:
        return (0)
    res = res.json()
    if 'data' in res:
        return (res.get('data').get('subscribers'))

    else:
        return (0)
