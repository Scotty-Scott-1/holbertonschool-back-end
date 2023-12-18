#!/usr/bin/python3
"""a module to get data from an API"""
import requests
from sys import argv


def get_employee_todos(user_id):
    """get the reponse and format and print data"""
    number_completed = 0

    todos_url = "https://jsonplaceholder.typicode.com/todos?userId={}".format(
        user_id)
    todos_response = requests.get(todos_url)
    todos = todos_response.json()

    user_url = "https://jsonplaceholder.typicode.com/users/{}".format(user_id)
    user_response = requests.get(user_url)
    user = user_response.json()

    employee_name = user.get("name")

    for task in todos:
        if task.get("completed"):
            number_completed += 1

    print("Employee {} is done with tasks({}/{}):".format(
        employee_name, number_completed, len(todos)))
    for task in todos:
        if task.get("completed"):
            print("	 {}".format(task.get("title")))


if __name__ == "__main__":
    """main function"""
    get_employee_todos(argv[1])
