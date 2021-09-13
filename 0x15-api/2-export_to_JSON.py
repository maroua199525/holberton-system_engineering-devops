#!/usr/bin/python3
"""
Using what you did in the i #0, extend your
Python script to export data in the JSON format
"""
import json
import requests
import sys


def employee_json():
    employeId = sys.argv[1]
    users = requests.get("https://jsonplaceholder.typicode.com/users/{}"
                         .format(employeId)).json()
    todos = requests.get("https://jsonplaceholder.typicode.com/todos?userId={}"
                         .format(employeId)).json()

    with open("{}.json".format(employeId), "w") as id:
            json.dump({employeId: [{
                    'task': i.get('title'),
                    'completed': i.get('completed'),
                    'username': users.get('username')
            } for i in todos]}, id)
if __name__ == '__main__':
    employee_json()
