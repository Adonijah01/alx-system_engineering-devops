#!/usr/bin/python3

"""
This script fetches and displays the TODO :\
        list progress for a given employee ID from  REST API.

"""

import sys
import requests


def get_employee_todo_list_progress(employee_id):
    """
    Fetch and display the employee's TODO list progress.

    :param employee_id: The employee's ID to retrieve data for.
    """
    base_url = 'https://jsonplaceholder.typicode.com'
    user_url = f'{base_url}/users/{employee_id}'
    todos_url = f'{base_url}/todos?userId={employee_id}'

    user_response = requests.get(user_url)
    todos_response = requests.get(todos_url)

    if user_response.status_code != 200:
        sys.exit(
            f"Error: Unable to retrieve user data for employee {employee_id}")
    if todos_response.status_code != 200:
        sys.exit(
            f"Error: Unable to retrieve TODO list for employee {employee_id}")

    user_data = user_response.json()
    todos_data = todos_response.json()

    employee_name = user_data.get('name')
    completed_tasks = [task for task in todos_data if task['completed']]
    total_tasks = len(todos_data)

    print(
            f"Employee {employee_name} is done with tasks:\
                    ({len(completed_tasks)}/{total_tasks}):")

    for task in completed_tasks:
        print(f"\t{task['title']}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit("Usage: python3 0-gather_data_from_an_API.py <employee_ID>")

    employee_id = sys.argv[1]
    get_employee_todo_list_progress(employee_id)
