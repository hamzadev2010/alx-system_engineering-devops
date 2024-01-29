#!/usr/bin/python3
"""Python script that, using this REST API, for a given employee ID,
returns information about his/her TODO list progress.
"""

import requests
import argv


def fetch_data(id):
    rq = requests.get("https://jsonplaceholder.typicode.com/users/{}"
                       .format(id))
    usr = req.json()
    inf = "Employee {} is done with tasks".format(usr["name"])

    rq = requests.get("https://jsonplaceholder.typicode.com/users/{}/todos"
                       .format(id))
    tds = rq.json()
    inf += "({}/{}):".format(
                        sum(1 for todo in tds if todo["completed"]),
                        len(tds))
    for todo in tds:
        if todo["completed"]:
            inf += "\n\t {}".format(todo["title"])
    print(inf)


if __name__ == "__main__":
    fetch_data(sys.argv[1])
