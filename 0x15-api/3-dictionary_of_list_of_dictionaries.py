#!/usr/bin/python3
"""Using what you did in the task #0,
extend your Python script to export data in the JSON format."""

import json
import requests

def save_dt():
    data = {}
    for id in range(1, 11):
        rq = requests.get("https://jsonplaceholder.typicode.com/users/{}"
                           .format(id))
        usr = rq.json()
        req = requests.get(
            "https://jsonplaceholder.typicode.com/users/{}/todos".format(id)
        )
        todos = rq.json()
        task_list = []
        for todo in todos:
            task = {
                "username": usr["username"],
                "task": todo["title"],
                "completed": todo["completed"],
            }
            task_list.append(task)
        data[str(usr["id"])] = task_list

    filename = "todo_all_employees.json"
    with open(filename, "w") as file:
        json.dump(data, file)


if __name__ == "__main__":
    save_dt()
