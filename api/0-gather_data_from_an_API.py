#!/usr/bin/python3
"""
Returns information on TODO list progress for Employee ID
"""
import urllib, requests


url = 'https://jsonplaceholder.typicode.com'
TODO_list = [{"employee_id": 1, "title": "NUMBER_OF_DONE_TASKS", "content": "TOTAL_NUMBER_OF_TASKS"}]

def employee_name(employee_id):
    print("EMPLOYEE_NAME", employee_id)

def employee_todo_list(employee_id):
    print("Employee EMPLOYEE_NAME is done with tasks(NUMBER_OF_DONE_TASKS/TOTAL_NUMBER_OF_TASKS):, employee")
