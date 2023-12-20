#!/usr/bin/python3
"""Prints the completed tasks of an employee"""

if __name__ == '__main__':
    import json
    import requests
    from sys import argv

    url = "https://jsonplaceholder.typicode.com"

    users = requests.get(f"{url}/users")

    users = users.json()

    dic2 = {}
    for user in users:
        lis = []
        todos = requests.get(f"{url}/todos?userId={user['id']}")
        todos = todos.json()
        for todo in todos:
            dic = {}
            dic["username"] = user["username"]
            dic["task"] = todo["title"]
            dic["completed"] = todo["completed"]
            lis.append(dic)
        dic2[f"{user['id']}"] = lis

    with open("todo_all_employees.json", "w", encoding="utf-8") as file:
        file.write(json.dumps(dic2))
