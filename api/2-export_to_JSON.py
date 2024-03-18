#!/usr/bin/python3
"""
Returns information on TODO list progress for Employee ID
"""
import requests
import sys


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

        employee_info = []
        for task in todos_json:
            if str(task["userId"]) == user_id:
                task_data = {
                     "task": task['title'],
                    "username": user_json["username"],
                    "completed": task['completed']
                }
                employee_info.append(task_data)

        output_data = {user_id: employee_tasks}

        with open(f"{user_id}.json", "w") as json_file:
            json.dump(output_data, json_file, indent=4)


if __name-- == "__main__":
    Get_Todo().employee_list()
