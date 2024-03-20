#!/usr/bin/python3
"""
Returns information on TODO list progress for Employee ID
"""
import json
import requests
import sys


class Get_Todo():
    """ Class for employee info"""

    def employee_list(self):
        """ To grab employee info"""
        args = sys.argv
        user_id = args[1]
        url = 'https://jsonplaceholder.typicode.com/'

        # Fetch user info from API
        user_result = requests.get(url + "users/" + user_id)
        todos_result = requests.get(url + "todos")

        # Convert API responses to JSON format
        user_json = user_result.json()
        todos_json = todos_result.json()

        # Filter tasks by user ID
        user_tasks = []
        for task in todos_json:
            if str(task["userId"]) == user_id:
                # Add task details to user_tasks list
                user_tasks.append({
                    "task": task["title"],
                    "completed": task["completed"],
                    "username": user_json["username"]
                })

        # Create dictionary to store user tasks with user ID as key
        user_dict = {user_json["id"]: user_tasks}

        # Write suer tasks to JSON file with user ID as filename
        filename = f"{user_id}.json"
        with open(filename, mode='w') as file:
            json.dump(user_dict, file) # Write dictionary to JSON file


if __name__ == "__main__":
    Get_Todo().employee_list() # Call employee_list method when script is executed
