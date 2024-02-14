#!/usr/bin/python3
"""
Display the titles of the first 10 hot posts listed for a given subreddit
"""
import requests


def top_ten(subreddit):
    """
    function that queries the Reddit API and prints the titles
    of the first 10 hot posts listed for a given subreddit.
    """
    weburl = ("https://api.reddit.com/r/{}?sort=hot&limit=10".format(subreddit))
    headers = {'User-Agent': 'CustomClient/1.0'}
    res = requests.get(weburl, headers=headers, allow_redirects=False)

    if res.status_code != 200:
        print(None)
        return
    res = res.json()
    if 'data' in res:
        for posts in res.get('data').get('children'):
            print(posts.get('data').get('title'))

    else:
        print(None)
