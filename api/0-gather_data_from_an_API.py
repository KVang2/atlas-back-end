#!/usr/bin/python3
"""
Returns information on TODO list progress for Employee ID
"""
import requests

url = 'https://jsonplaceholder.typicode.com/{employee_id}'
response = requests.get(url)
EMPLOYEE_NAME = response.json()
NUMBER_OF_DONE_TASKS = response.json()
TOTAL_NUMBER_OF_TASKS = response.json()


def employee_list(employee_id):
    """ Args: employee_id (_type_):"""
    if response.status_code == 200:
        print(f"Employee: {[EMPLOYEE_NAME]},
              is done with tasks({[NUMBER_OF_DONE_TASKS]}/
              {[TOTAL_NUMBER_OF_TASKS]}):")

if __name__ == '__main__':
    Get_Todo().todo
