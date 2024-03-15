#!/usr/bin/python3
"""
Returns information on TODO list progress for Employee ID
"""
import requests
import sys
import csv


args = sys.argv
user_id = args[1]
url = 'https://jsonplaceholder.typicode.com/'

user_result = requests.get(url + "users/" + user_id)
todos_result = requests.get(url + "todos")
user_json = user_result.json()
todos_json = todos_result.json()

EMPLOYEE_NAME = user_json["username"]
user_list = [task for task in todos_json
             if task["userId"] == user_id]

fields = ['USER_ID', 'USERNAME', 'TASK_COMPLETED_STATUS', 'TASK_TITLE']
# writing to csv file
csv_file_path = f'{user_id}.csv'
with open(csv_file_path, 'w', newline='') as csvfile:
    writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
    writer.writerow(fields)

    # writing data
    for task in user_list:
        if str(task['userId']) == user_id:
            completed_status = "True" if task["completed"] else "False"
            writer.writerow([task["userId"],
                EMPLOYEE_NAME, completed_status, 
                task["title"]])

    print(f"Data exported to {csv_file_path}")

if __name__ == "__main__":
    Get_Todo().employee_list()
