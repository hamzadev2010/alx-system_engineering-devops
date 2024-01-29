#!/usr/bin/python3
"""Using what you did in the task #0,
extend your Python script to export data in the JSON format."""

import json
import requests
from sys import argv

if __name__ == "__main__":
    usrs = requests.get("https://jsonplaceholder.typicode.com/users")
    usrs = usr.json()
    todos = requests.get('https://jsonplaceholder.typicode.com/todos')
    todos = todos.json()
    todoAll = {}

    for usr in usrs:
        taskList = []
        for task in todos:
            if task.get('userId') == usr.get('id'):
                taskDict = {"username": usr.get('username'),
                            "task": task.get('title'),
                            "completed": task.get('completed')}
                taskList.append(taskDict)
        todoAll[usr.get('id')] = taskList

    with open('todo_all_employees.json', mode='w') as f:
        json.dump(todoAll, f)
