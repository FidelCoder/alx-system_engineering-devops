#!/usr/bin/python3
"""
for a given employee ID, returns information about his/her
 TODO list progress."""

import csv
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
        dict1 = {"id": id, "user": name}
        dict1.update({"task": task.get('title'),
                     "status": str(task.get('completed'))})
        done_list.append(dict1)
    file = str(id) + ".csv"
    with open(file, 'w') as csvfile:
        writer = csv.DictWriter(
            csvfile, fieldnames=field_names, quoting=csv.QUOTE_NONNUMERIC)
        writer.writerows(done_list)


if __name__ == "__main__":
    get_todos()
