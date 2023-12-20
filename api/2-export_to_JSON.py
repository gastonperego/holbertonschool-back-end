#!/usr/bin/python3
"""Prints the completed tasks of an employee"""

import json

if __name__ == '__main__':
    import requests
    from sys import argv

    url = "https://jsonplaceholder.typicode.com"
    users = requests.get(f"{url}/users?id={argv[1]}")
    todos = requests.get(f"{url}/todos?userId={argv[1]}")

    users = users.json()
    todos = todos.json()

    lis = []
    for todo in todos:
        dic = {}
        dic["task"] = todo['title']
        dic["completed"] = todo['completed']
        dic["username"] = users[0]["username"]
        lis.append(dic)
        

    dic2 = {}
    dic2[users[0]["id"]] = lis



    with open(f"{users[0]['id']}.json", "w", encoding="utf-8") as file:
        file.write(json.dumps(dic2))
