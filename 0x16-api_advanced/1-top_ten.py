#!/usr/bin/python3
""" a function that queries the Reddit API and prints
the titles of the first 10 hot posts listed
for a given subreddit
"""

import json
import requests


def top_ten(subreddit):
    user = {"User-Agent": "Maroua-Alaya"}
    request = requests.get("https://www.reddit.com/r/{}/hot/.json"
                           .format(subreddit), headers=user)
    if request.status_code == 200:
        count = 0
        for posts in request.json().get("data").get("children"):
            if count < 10:
                print(posts.get("data").get("title"))
                count += 1
    else:
        print(None)
