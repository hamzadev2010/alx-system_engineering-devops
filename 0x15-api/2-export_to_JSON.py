#!/usr/bin/python3

"""Using what you did in the task #0,
extend your Python script to export data in the JSON format
"""

import json
import requests
import sys


def fetch_data(id):
    rq = requests.get("https://jsonplaceholder.typicode.com/users/{}"
                       .format(id))
    usr = rq.json()

    rq = requests.get("https://jsonplaceholder.typicode.com/users/{}/todos"
                       .format(id))
    todos = rq.json()
    task_list = []
    for todo in todos:
        tsk = {
            "task": todo["title"],
            "completed": todo["completed"],
            "username": usr["username"],
        }
        task_list.append(tsk)

    data = {str(usr["id"]): task_list}
    filename = "{}.json".format(usr["id"])
    with open(filename, "w") as file:
        json.dump(data, file)


if __name__ == "__main__":
    fetch_data(sys.argv[1])
