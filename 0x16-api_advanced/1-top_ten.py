#!/usr/bin/python3

"""
Display the titles of the first 10 hot posts listed for a given subreddit.
"""

from requests import get


def top_ten(subreddit):
    """
    function that queries the Reddit API and prints the titles
    of the first 10 hot posts listed for a given subreddit.
    """

    if subreddit is None or not isinstance(subreddit, str):
        print("None")

    headers = {'User-agent': 'Google Chrome client'}
    params = {'limit': 10}
    weburl = 'https://www.reddit.com/r/{}/hot/.json'.format(subreddit)

    res = get(weburl, headers, params=params)
    all_data = res.json()

    try:
        req = all_data.get('data').get('children')

        for i in req:
            print(i.get('data').get('title'))

    except:
        print("None")
