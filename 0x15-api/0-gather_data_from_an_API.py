#!/usr/bin/python3
"""for a given employee ID, returns information about their tasks"""


import requests
import sys


def get_todos():
    """get employee"""
    id = sys.argv[1]
    x = requests.get(
        'https://jsonplaceholder.typicode.com/users/{}'.format(id))
    user = x.json()
    name = user.get('name')
    x = requests.get(
        'https://jsonplaceholder.typicode.com/users/{}/todos'.format(id))
    tasks = x.json()
    count = 0
    done_list = []
    tasks_no = len(tasks)
    for task in tasks:
        if task.get('completed'):
            done_list.append(task.get('title'))
            count += 1
    str2 = '\n\t '.join(done_list)
    print("Employee {} is done with tasks({}/{}):".format(name,
                                                          count, tasks_no))
    print("\t {}".format(str2))


if __name__ == "__main__":
    get_todos()
