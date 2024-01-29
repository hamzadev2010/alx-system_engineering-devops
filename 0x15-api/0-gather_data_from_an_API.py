#!/usr/bin/python3
"""Python script that, using this REST API, for a given employee ID,
returns information about his/her TODO list progress.
"""

import requests
import argv


if __name__ == "__main__":
    usrid = sys.argv[1]
    rq = requests.get('https://jsonplaceholder.typicode.com/users/{}'
                        .format(usrid)).json()

    todo = requests.get('https://jsonplaceholder.typicode.com/todos?userId={}'
                        .format(usrid)).json()
    cmpp = []
    for task in todo:
        if task.get('completed') is True:
            cmpp.append(task.get('title'))
    print("Employee {} is done with tasks({}/{}):".
          format(rq.get('name'), len(cmpp), len(todo)))
    for task in cmpp:
        print("\t {}".format(task))
