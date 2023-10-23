#!/usr/bin/python3

"""
This script fetches employee TODO :\
        list progress from a REST API and exports it in CSV.
"""

import sys
import requests
import csv


if __name__ == "__main__":

    user_id = sys.argv[1]

    url = "https://jsonplaceholder.typicode.com/"

    user = requests.get(url + "users/{}".format(user_id)).json()

    username = user.get("username")

    todos = requests.get(url + "todos", params={"userId": user_id}).json()

    with open("{}.csv".format(user_id), "w", newline="") as csvfile:

        writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)

        [writer.writerow(

            [user_id, username, t.get("completed"), t.get("title")]

        ) for t in todos]
