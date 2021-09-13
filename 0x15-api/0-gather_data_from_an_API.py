#!/usr/bin/python3
"""
Write a Python script that, using this REST API,
for a given employee ID,
returns information about his/her TODO list progress
"""
import requests
import sys


def employee_id():
    Title = []
    NUMBER_OF_DONE_TASKS = 0
    TOTAL_NUMBER_OF_TASKS = 0
    employeeId = sys.argv[1]
    url_user = "https://jsonplaceholder.typicode.com/users/" + employeeId
    response1 = requests.get(url_user).json()
    EMPLOYEE_NAME = response1.get('name')
    url_todo = "https://jsonplaceholder.typicode.com/todos/"
    response2 = requests.get(url_todo).json()
    for user in response2:
        if user.get('userId') == int(employeeId):
            if user.get('completed') is True:
                Title.append(user['title'])
                NUMBER_OF_DONE_TASKS += 1
            TOTAL_NUMBER_OF_TASKS += 1
    print("Employee {} is done with tasks({}/{}):"
          .format(EMPLOYEE_NAME, NUMBER_OF_DONE_TASKS, TOTAL_NUMBER_OF_TASKS))
    for x in Title:
        print("\t {}".format(x))

if __name__ == '__main__':
    employee_id()
