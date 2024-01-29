#!/usr/bin/python3
"""Using what you did in the task #0,
extend your Python script to export data in the CSV format
"""

import csv
import requests
import sys


def fetch_data(id):
    rq = requests.get("https://jsonplaceholder.typicode.com/users/{}".format(id))
    usr = rq.json()

    rq = requests.get("https://jsonplaceholder.typicode.com/users/{}/todos".format(id))
    todos = rq.json()

    filename = "{}.csv".format(usr["id"])
    with open(filename, "w") as file:
        writer = csv.writer(file, quoting=csv.QUOTE_ALL)
        for todo in todos:
            writer.writerow([usr["id"], usr["username"],
                            todo["completed"], todo["title"]])


if __name__ == "__main__":
    fetch_data(sys.argv[1])
