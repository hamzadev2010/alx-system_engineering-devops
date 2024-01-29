#!/usr/bin/python3

"""Using what you did in the task #0,
extend your Python script to export data in the JSON format
"""

import json
import sys
import requests


if __name__ == "__main__":
    res = requests.get('https://jsonplaceholder.typicode.com/todos/')
    dt = res.json()

    row = []
    res2 = requests.get('https://jsonplaceholder.typicode.com/users')
    dt2 = res2.json()

    for i in dt2:
        if i['id'] == int(sys.argv[1]):
            u_name = i['username']
            id_no = i['id']

    row = []

    for i in dt:

        new_dict = {}

        if i['userId'] == int(sys.argv[1]):
            new_dict['username'] = u_name
            new_dict['task'] = i['title']
            new_dict['completed'] = i['completed']
            row.append(new_dict)

    final_dict = {}
    final_dict[id_no] = row
    json_obj = json.dumps(final_dict)

    with open(argv[1] + ".json",  "w") as f:
        f.write(json_obj)
