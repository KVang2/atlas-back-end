#!/usr/bin/python3
"""
Returns information on TODO list progress for Employee ID
"""
import json
import requests


class Get_Todo():
    """ Class for employee info"""

    def employee_list(self):
        """ To grab employee info"""
        url = 'https://jsonplaceholder.typicode.com/'

        # Fetch users and todos from the API
        users_response = requests.get(url + "users")
        todos_response = requests.get(url + "todos")

        # Convert API responses to JSON format        
        users = users_response.json()
        todos = todos_response.json()

        # Constructing user tasks dictionary
        user_tasks_dict = {} # Dictionary to store user tasks
        for user in users:
            user_tasks = [] # List to store tasks for each user
            for task in todos:
                if task["userId"] == user["id"]:
                    # Add task details to user_tasks list
                    user_tasks.append({
                        "task": task["title"],
                        "completed": task["completed"],
                        "username": user["username"]
                    })
            # Assign user tasks list to user ID in the dictionary
            user_tasks_dict[user["id"]] = user_tasks

        # Exporting user info to JSON file
        with open("todo_all_employees.json", "w") as file:
            json.dump(user_tasks_dict, file) # Write dictionary to JSON file


if __name__ == "__main__":
    Get_Todo().employee_list()
