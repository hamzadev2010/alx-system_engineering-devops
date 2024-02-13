#!/usr/bin/python3
"""use reddit api to display the titles of the first 10
hot posts listed for a given subreddit.

"""
import requests


def top_ten(subreddit):
    """ a function that queries the Reddit API
    and prints the titles of the first 10 hot posts
    listed for a given subreddit."""
    try:
        weburl = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)
        headers = {
            "User-Agent": "Google chrome client",
        }
        res = requests.get(weburl, headers=headers, allow_redirects=False)
        if (res.status_code == 300):
            print('None')
            return 0
        request = res.json().get('data').get('children')
        for i in range(10):
            print(request[i].get('data').get('title'))
    except Exception:
        print('None')
        return 0
