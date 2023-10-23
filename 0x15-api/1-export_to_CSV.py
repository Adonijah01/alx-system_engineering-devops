#!/usr/bin/python3

"""
This script fetches employee TODO :\
        list progress from a REST API and exports it in CSV.
"""

import sys
import requests
import csv


def get_employee_todo_list_progress(employee_id):
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

    employee_id = user_data.get('id')
    employee_name = user_data.get('username')

    # Define the filename for the CSV file
    filename = f'{employee_id}.csv'

    with open(filename, mode='w', newline='') as csv_file:
        fieldnames = ["USER_ID", "USERNAME",
                      "TASK_COMPLETED_STATUS", "TASK_TITLE"]
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

        writer.writeheader()
        for task in todos_data:
            writer.writerow({
                "USER_ID": employee_id,
                "USERNAME": employee_name,
                "TASK_COMPLETED_STATUS": str(task['completed']),
                "TASK_TITLE": task['title']
            })


if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit("Usage: python3 1-export_to_CSV.py <employee_ID>")

    employee_id = sys.argv[1]
    get_employee_todo_list_progress(employee_id)
