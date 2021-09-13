#!/usr/bin/python3
"""Using what you did in the task #0,
extend your Python script to export data in the JSON format."""

import json
import requests
import sys


def main():

    filename = "todo_all_employees.json"
    response1 = requests.get('https://jsonplaceholder.typicode.com/todos')
    response2 = requests.get('https://jsonplaceholder.typicode.com/users/')
    with open(filename, "w") as f:
        d = {x.get("id"): [{'task': y.get('title'),
             'completed': y.get('completed'),
                            'username': x.get('username')}
                            for y in response1.json()
                           if x.get("id") == y.get('userId')]
             for x in response2.json()}
        json.dump(d, f)

if __name__ == '__main__':
    main()
