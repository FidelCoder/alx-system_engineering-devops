#!/usr/bin/python3
"""get the top ten posts of a subreddit"""
import requests


def top_ten(subreddit):
    """get top ten posts"""
    url = "https://www.reddit.com/r/{}/hot.json?limit=9".format(subreddit)
    headers = {'User-Agent': 'Alxdevs2'}
    response = requests.get(url, headers=headers)
    if response.url != url:
        print("None")
        return
    response = response.json()
    if response.get('kind') != "Listing":
        print("None")
        return
    data = response.get('data')
    children = data.get('children')
    count = 0
    for child in children:
        if count == 10:
            return
        print(child.get('data').get('title'))
        count += 1
