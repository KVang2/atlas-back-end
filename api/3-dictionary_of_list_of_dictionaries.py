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
        args = sys.argv
        user_id = args[1]
        url = 'https://jsonplaceholder.typicode.com/'

        user_result = requests.get(url + "users/" + user_id)
        todos_result = requests.get(url + "todos")
        user_json = user_result.json()
        todos_json = todos_result.json()
