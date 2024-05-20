#!/usr/bin/python3
""" extends Python script to export data in the JSON format """
import json
import requests
import sys

if __name__ == '__main__':
    u_id = sys.argv[1]
    url = "https://jsonplaceholder.typicode.com/"
    user = requests.get(url + "users/{}".format(u_id)).json()
    username = user.get("username")
    tasks = requests.get(url + "todos", params={"userId": u_id}).json()

    with open("{}.json".format(u_id), "w") as file:
        json.dump({u_id: [{
            "task": task.get("title"),
            "completed": task.get("completed"),
            "username": username
        } for task in tasks]}, file)
