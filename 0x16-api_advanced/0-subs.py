#!/usr/bin/python3
"""get subscriber count of a subreddit"""
import os
import requests


def number_of_subscribers(subreddit):
    """subscriber numbers"""
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {'User-Agent': 'Alxdevs1'}
    response = requests.get(url, headers=headers)
    if response.url != url:
        print("None")
        return
    response = response.json()
    if response.get('kind') != "t5":
        return (0)
    data = response.get('data')
    return (data.get('subscribers'))
