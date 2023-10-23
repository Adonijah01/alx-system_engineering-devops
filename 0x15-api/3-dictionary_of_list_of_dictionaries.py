#!/usr/bin/python3
import json
import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) != 1:
        sys.exit()

    base_url = "https://jsonplaceholder.typicode.com"

    # Fetch user data
    users_response = requests.get(f"{base_url}/users")
    users = users_response.json()

    all_user_data = {}

    for user in users:
        user_id = user["id"]
        username = user["username"]

        # Fetch tasks for the current user
        tasks_response = requests.get(f"{base_url}/todos?userId={user_id}")
        tasks = tasks_response.json()

        user_tasks = [{"username": username, "task": task["title"],
                       "completed": task["completed"]} for task in tasks]

        all_user_data[user_id] = user_tasks

    # Write the data to JSON file
    with open("todo_all_employees.json", "w") as json_file:
        json.dump(all_user_data, json_file)
