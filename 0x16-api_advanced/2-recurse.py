#!/usr/bin/python3
"""get the top ten posts of a subreddit"""
import os
import requests


def recurse(subreddit, hot_list=[]):
    """subscriber numbers"""
    if type(subreddit) is str:
        subtext = subreddit
        url = "https://www.reddit.com/r/{}/hot.json?limit=100".format(
            subreddit)
    elif type(subreddit) is list:
        subtext = subreddit[0]
        url = "https://www.reddit.com/r/{}/hot.json?limit=99&&after={}".format(
            subreddit[0], subreddit[1])
    else:
        return None
    headers = {'User-Agent': 'Alxdevs2'}
    response = requests.get(url, headers=headers)
    if response.url != url:
        return None
    response = response.json()
    if response.get('kind') != "Listing":
        return None
    data = response.get('data')
    children = data.get('children')
    count = 0
    for child in children:
        hot_list.append(child.get('data').get('title'))
        count = count + 1
    if data.get('after') is None:
        return(hot_list)
    else:
        list1 = [subtext, data.get('after')]
        return(recurse(list1, hot_list))
