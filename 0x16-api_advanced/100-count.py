#!/usr/bin/python3
"""get the top ten posts of a subreddit"""
import requests


def count_words(subreddit, word_list):
    """counts words in titles"""
    if type(subreddit) is str:
        subtext = subreddit
        url = "https://www.reddit.com/r/{}/hot.json?limit=100".format(
            subreddit)
    elif type(subreddit) is list:
        subtext = subreddit[0]
        url = "https://www.reddit.com/r/{}/hot.json?limit=99&&after={}".format(
            subreddit[0], subreddit[1])
    else:
        return
    if type(word_list) is list:
        dict1 = {}
        for word in word_list:
            dict1.update({word: 0})
        word_list = dict1
    headers = {'User-Agent': 'Alxdevs2'}
    response = requests.get(url, headers=headers)
    if response.url != url:
        return
    response = response.json()
    if response.get('kind') != "Listing":
        return
    data = response.get('data')
    children = data.get('children')
    for child in children:
        sent = child.get('data').get('title').lower().split(" ")
        for word in word_list.keys():
            x = sent.count(word.lower())
            x = x + word_list.get(word)
            word_list.update({word: x})
    if data.get('after') is None:
        word_lst2 = {}
        if sum(word_list.values()) < 1:
                return
        for k, v in word_list.items():
            if k.lower() in word_lst2:
                x = v + word_list.get(k.lower())
                word_lst2.update({k.lower(): x})
            else:
                word_lst2.update({k.lower(): v})
        sorted_result = sorted(word_lst2.items(), key=lambda x: (-x[1], x[0]))
        for result in sorted_result:
            if result[1] > 0:
                print("{}: {}".format(result[0], result[1]))
        return
    else:
        list1 = [subtext, data.get('after')]
        count_words(list1, word_list)
