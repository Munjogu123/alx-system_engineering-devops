#!/usr/bin/python3
""" extends Python script to export data in the CSV format """
import csv
import requests
import sys

if __name__ == '__main__':
    u_id = sys.argv[1]
    url = "https://jsonplaceholder.typicode.com/"
    user = requests.get(url + "users/{}".format(u_id)).json()
    username = user.get("username")
    tasks = requests.get(url + "todos", params={"userId": u_id}).json()

    with open("{}.csv".format(u_id), "w", newline="") as file:
        writer = csv.writer(file, quoting=csv.QUOTE_ALL)
        [writer.writerow(
            [u_id, username, task.get("completed"), task.get("title")]
        ) for task in tasks]
