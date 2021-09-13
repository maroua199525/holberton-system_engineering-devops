#!/usr/bin/python3
"""
Write a Python script that, using this REST API,
for a given employee ID,
returns information about his/her TODO list progress
"""
import requests
import sys
import csv


def employee_csv():
    
    employeeId = sys.argv[1]
    url_user = "https://jsonplaceholder.typicode.com/users/" + employeeId
    response = requests.get(url_user).json()
    EMPLOYEE_NAME = response.get('name')
    url_todo = "https://jsonplaceholder.typicode.com/users/" + employeeId + '/todos'
    response1 = requests.get(url_todo).json()
    with open("{}.csv".format(employeeId), mode='w') as csv_file:
        writer = csv.writer(csv_file, quoting=csv.QUOTE_ALL)
        for user in response1:
            writer.writerow([employeeId, EMPLOYEE_NAME, user.get("completed"), user.get("title")])

if __name__ == '__main__':
    employee_csv()
