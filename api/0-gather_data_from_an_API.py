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
        # Get user ID from command line arg
        args = sys.argv
        user_id = args[1]

        # URL of JSONPlaceholder API
        url = 'https://jsonplaceholder.typicode.com/'

        # fetch user info and tasks from API
        user_result = requests.get(url + "users/" + user_id)
        todos_result = requests.get(url + "todos")

        # Convert API responses to JSON format
        user_json = user_result.json()
        todos_json = todos_result.json()

        # Extract relevant info about employee
        EMPLOYEE_NAME = user_json["name"]

        # Count number of completed tasks for the employee
        NUMBER_OF_DONE_TASKS = sum(1 for task in todos_json
                                   if str(task["userId"]) == user_id
                                   and task["completed"] is True)

        # Count total number of tasks for the employee
        TOTAL_NUMBER_OF_TASKS = sum(1 for task in todos_json
                                    if str(task["userId"]) == user_id)


        # Print employee's task completion info
        print(f"Employee {EMPLOYEE_NAME} is done with tasks"
              f"({NUMBER_OF_DONE_TASKS}/{TOTAL_NUMBER_OF_TASKS}):")

        # Print titles of completed tasks for employee
        for task in todos_json:
            if str(task["userId"]) == user_id and task["completed"] is True:
                print(f"\t {task['title']}")

# Execute employee_list method when script is run
if __name__ == "__main__":
    Get_Todo().employee_list()
