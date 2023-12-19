#!/usr/bin/python3
"""Prints the completed tasks of an employee"""

import json

if __name__ == '__main__':
    from sys import argv
    import urllib3

    users = urllib3.request("GET",
                            f"https://jsonplaceholder.typicode.com/users?id={argv[1]}")
    todos = urllib3.request("GET",
                            f"https://jsonplaceholder.typicode.com/todos?userId={argv[1]}")

    users = users.json()
    todos = todos.json()

    dic = {}
    dic[users[0]["id"]] = todos
    
    with open(f"{users[0]['id']}.json", "w", encoding="utf-8") as file:
        file.write(json.dumps(dic))
