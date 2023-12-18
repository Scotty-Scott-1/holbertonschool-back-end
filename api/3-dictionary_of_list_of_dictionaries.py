#!/usr/bin/python3
"""a module to get data from an API"""
from sys import argv
import json
import requests


def get_employee_todos():
    """get the reponse and format and print data"""
    number_completed = 0

    todos_url = "https://jsonplaceholder.typicode.com/todos"
    todos_response = requests.get(todos_url)
    todos = todos_response.json()

    user_url = "https://jsonplaceholder.typicode.com/users"
    user_response = requests.get(user_url)
    user = user_response.json()

    data = {
        user.get("id"):
            [
                {
                    "username": user.get("username"),
                    "task": task.get("title"),
                    "completed": task.get("completed")
                } for task in todos if task.get("userId") == user.get("id")
            ] for user in user
            }

    file_name = "todo_all_employees.json"

    with open(file_name, "w") as file:
        json.dump(data, file)


if __name__ == "__main__":
    """main function"""
    get_employee_todos()
