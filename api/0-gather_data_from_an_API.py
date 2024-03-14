#!/usr/bin/python3
"""
Returns information on TODO list progress for Employee ID
"""
import urllib
import requests


def employee_list(employee_id):
    """ Args: employee_id (_type_):"""
    url = 'https://jsonplaceholder.typicode.com/{id}'
    response = requests.get(url)
    if response.status == 200:
        data = response.json()
        print(f"Employee: {data['EMPLOYEE_NAME']}, is done with tasks(
              {data['NUMBER_OF_DONE_TASKS']}/{data['TOTAL_NUMBER_OF_TASKS']}):")


if __name__ == '__main__':
    app.run(debug=True)