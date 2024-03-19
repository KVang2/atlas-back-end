#!/usr/bin/python3
"""
Returns information on TODO list progress for Employee ID
"""
import requests
import sys
import csv


class Get_Todo():
    """ Class for employee info"""

    def employee_list(self):
        """ To grab employee info"""
        args = sys.argv
        if len(args) != 2:
            print("Usage: python script_name.py USER_ID")
            sys.exit(1)

        user_id = int(args[1])
        url = 'https://jsonplaceholder.typicode.com/'

        user_result = requests.get(url + "users/" + str(user_id))
        todos_result = requests.get(url + "todos")
        user_json = user_result.json()
        todos_json = todos_result.json()

        EMPLOYEE_NAME = user_json["username"]
        user_tasks = [task for task in todos_json
                   if task["userId"] == user_id]

        fields = ['USER_ID', 'USERNAME', 'TASK_COMPLETED_STATUS', 'TASK_TITLE']
        # writing to csv file
        csv_file_path = f'{user_id}.csv'
        with open(csv_file_path, 'w', newline='') as file:
            writer = csv.writer(file, quoting=csv.QUOTE_ALL)

            # writing data
            for task in user_tasks:
                completed_status = "True" if task["completed"] else "False"
                writer.writerow([user_id,
                                 EMPLOYEE_NAME, completed_status,
                                 task["title"]])
