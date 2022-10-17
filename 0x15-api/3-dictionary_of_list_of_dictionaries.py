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
    y = requests.get('https://jsonplaceholder.typicode.com/users/')
    user_id = []
    for dict2 in y.json():
        user_id.append(dict2.get('id'))
    dict2 = {}
    for id in user_id:
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
            dict1.update({"username": name, "task": task.get('title'),
                          "completed": task.get('completed')})
            done_list.append(dict1)
        dict2.update({id: done_list})
    file = "todo_all_employees.json"
    with open(file, 'w') as jsonfile:
        json.dump(dict2, jsonfile)


if __name__ == "__main__":
    get_todos()
