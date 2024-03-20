#!/usr/bin/python3
"""
Returns information on TODO list progress for Employee ID
"""
import csv
import requests
import sys


# Check if the correct number of command-line arg is provided
args = sys.argv
if len(args) != 2:
    print("Usage: python script_name.py USER_ID")
    sys.exit(1)

# Extract user ID from command-line arguments
user_id = int(args[1])
url = 'https://jsonplaceholder.typicode.com/'

# Fetch user and todo list data from url
user_result = requests.get(url + "users/" + str(user_id))
todos_result = requests.get(url + "todos")
user_json = user_result.json() # convert user data to JSON format
todos_json = todos_result.json() # convert todo list data to JSON format

# Extract username from user data
EMPLOYEE_NAME = user_json["username"]

# Filter tasks for given user ID
user_tasks = [task for task in todos_json
              if task["userId"] == user_id]

# Define CSV file fields
fields = ['USER_ID', 'USERNAME', 'TASK_COMPLETED_STATUS', 'TASK_TITLE']

# Define path for CSV file then writing to csv file
csv_file_path = f'{user_id}.csv'
with open(csv_file_path, 'w', newline='') as file:
    writer = csv.writer(file, quoting=csv.QUOTE_ALL)

    # Iterate over user tasks and write each task to CSV file
    for task in user_tasks:
        # Convert task completion status to string representation
        completed_status = "True" if task["completed"] else "False"
        # Write task data to CSV file
        writer.writerow([user_id,
                         EMPLOYEE_NAME, completed_status, task["title"]])
