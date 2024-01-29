#!/usr/bin/python3
""" Using what you did in the task #0,
extend your Python script to export data in the JSON format."""
import csv
import json
from requests import get
import sys


if __name__ == '__main__':
    usrs = get('https://jsonplaceholder.typicode.com/users').json()

    todo = get('https://jsonplaceholder.typicode.com/todos/').json()

    id_dict = {}
    username_dict = {}

    for user in usrs:
        empl_id = user.get("id")
        id_dict[emp_id] = []
        username_dict[empl_id] = user.get('username')
    for task in todo:
        dictt = {}
        empl_id = task.get('userId')
        dictt["task"] = task.get('title')
        dictt["completed"] = task.get('completed')
        dictt["username"] = username_dict.get(empl_id)
        id_dict.get(empl_id).append(dictt)
    with open("todo_all_employees.json", 'w') as ajsonfile:
        json.dump(id_dict, ajsonfile)
