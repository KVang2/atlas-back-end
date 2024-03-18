#!/usr/bin/python3
"""
Returns information on TODO list progress for Employee ID
"""
import requests
import sys
import json


class Get_Todo():
    """ Class for employee info"""

    def employee_list(self):
        """ To grab employee info"""
        args = sys.argv
        user_id = args[1]
        url = 'https://jsonplaceholder.typicode.com/'

        user_result = requests.get(url + "users/" + user_id)
        todos_result = requests.get(url + "todos")
        user_json = user_result.json()
        todos_json = todos_result.json()

        employee_todos = [todo for todo in todos_json if todo['userId'] == int(user_id)]

        data = {
            "USER_ID":[
                {
                    "task": todo['title'],
                    "completed": todo['completed'],
                    "username": user_json['name']
                } for todo in employee_todos
            ]
        }

        with open('data.json', 'w') as file:
            json.dump(data, file, indent=4)


if __name__ == "__main__":
    Get_Todo().employee_list()
