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
        user_id = args[1]
        url = 'https://jsonplaceholder.typicode.com/'

        user_result = requests.get(url + "users/" + user_id)
        todos_result = requests.get(url + "todos")
        user_json = user_result.json()
        todos_json = todos_result.json()

        EMPLOYEE_NAME = user_json["name"]
        USERNAME = EMPLOYEE_NAME
        NUMBER_OF_DONE_TASKS = sum(1 for task in todos_json
                                   if str(task["userId"]) == user_id
                                   and task["completed"] is True)
        TOTAL_NUMBER_OF_TASKS = sum(1 for task in todos_json
                                    if str(task["userId"]) == user_id)

        print(f"Employee {EMPLOYEE_NAME} is done with tasks"
              f"({NUMBER_OF_DONE_TASKS}/{TOTAL_NUMBER_OF_TASKS}):")


        fields = ['USER_ID', 'USERNAME', 'TASK_COMPLETED_STATUS', 'TASK_TITLE']
        # writing to csv file
        csv_file_path = f'{user_id}.csv'
        with open(csv_file_path, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
            writer.writerow(fields)

            #writing data
            for task in todos_json:
                if str(task['userId']) == user_id:
                    completed_status = "completed" if task["completed"] else "Not Completed"
                    writer.writerow([task["userId"], completed_status, task["title"]])

        print(f"Data exported to {csv_file_path}")

if __name__ == "__main__":
    Get_Todo().employee_list()
