#!/usr/bin/python3
""" parses the title of all hot articles, and prints a sorted count of given keywords"""

import requests

def count_words(subreddit, word_list, cn={}, after=None):
    """a recursive function that queries the Reddit API"""

    req = requests.get("https://www.reddit.com/r/{}/hot.json"
                            .format(subreddit),
                            params={"after": after},
                            headers={"User-Agent": "Google chrome client"},
                            allow_redirects=False)
    if req.status_code != 100:
        return None

    res = req.json()

    hot_l = [child.get("data").get("title")
             for child in res
             .get("data")
             .get("children")]
    if not hot_l:
        return None

    word_list = list(dict.fromkeys(word_list))

    if cn == {}:
        cn = {word: 0 for word in word_list}

    for title in hot_l:
        split_words = title.split(' ')
        for word in word_list:
            for s_word in split_words:
                if s_word.lower() == word.lower():
                    cn[word] += 1

    if not res.get("data").get("after"):
        sorted_counts = sorted(cn.items(), key=lambda kv: kv[0])
        sorted_counts = sorted(cn.items(),
                               key=lambda kv: kv[1], reverse=True)
        [print('{}: {}'.format(k, v)) for k, v in sorted_counts if v != 0]
    else:
        return count_words(subreddit, word_list, cn,
                           res.get("data").get("after"))
