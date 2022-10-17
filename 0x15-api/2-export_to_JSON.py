#!/usr/bin/python3
"""
for a given employee ID, returns information about his/her
 TODO list progress.
 """

import json
import requests
import sys


def get_todos():
    """get employee task completion status"""
    id = sys.argv[1]
    x = requests.get(
        'https://jsonplaceholder.typicode.com/users/{}'.format(id))
    user = x.json()
    field_names = ['id', 'user', 'status', 'task']
    name = user.get('username')
    x = requests.get(
        'https://jsonplaceholder.typicode.com/users/{}/todos'.format(id))
    tasks = x.json()
    done_list = []
    for task in tasks:
        dict1 = {}
        dict1.update({"task": task.get('title'),
                     "completed": task.get('completed'), "username": name})
        done_list.append(dict1)
    dict2 = {id: done_list}
    file = str(id) + ".json"
    with open(file, 'w') as jsonfile:
        json.dump(dict2, jsonfile)


if __name__ == "__main__":
    get_todos()
