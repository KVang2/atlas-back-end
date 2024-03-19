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

        # Filter tasks by user ID
        user_tasks = [{"task": task["title"], "completed": task["completed"],
                       "username": user_json["username"]}
                      for task in todos_json
                      if str(task["userId"]) == user_id]
        user_dict = {user_json["id"]: user_tasks}

        filename = f"{user_id}.json"
        with open(filename, mode='w') as file:
            json.dump(user_dict, file)


if __name__ == "__main__":
    Get_Todo().employee_list()
