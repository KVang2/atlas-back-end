#!/usr/bin/python3
"""
Returns information on TODO list progress for Employee ID
"""
import requests
import sys


class Get_Todo():
    """ Class for employee info"""


    def employee_list(self, user_id):
        """ To grab employee info"""
        url = 'https://jsonplaceholder.typicode.com/'

        user_result = requests.get(url + "users/" + user_id)
        todos_result = requests.get(url + "todo")
        user_json = user_result.json()
        todos_result = todo_result.json()


        EMPLOYEE_NAME = user.json("name")
        NUMBER_OF_DONE_TASKS = sum(1 for task in todo_json
                           if str(task["userId"]) == str(user_id)
                           and task["completed"] is True)
        TOTAL_NUMBER_OF_TASKS = sum(1 for task in todos_json
                            if str(task["userId"]) == str(user_id))


        print(f"Employee {EMPLOYEE_NAME} is done with tasks"
              f"({NUMBER_OF_DONE_TASKS}/{TOTAL_NUMBER_OF_TASKS}):")
        for task in todo_json:
            if str(task["userId"]) == str(user_id) and task["completed"] is True:
                print(f"|t {task['title']}")

if __name__ == '__main__':
    user_id = input("Enter user ID: ")
    Get_Todo().todo
