#!/usr/bin/python3
"""Prints the completed tasks of an employee"""

if __name__ == '__main__':
    import requests
    from sys import argv

    url = "https://jsonplaceholder.typicode.com"
    users = requests.get(f"{url}/users?id={argv[1]}")
    todos = requests.get(f"{url}/todos?userId={argv[1]}")

    users = users.json()
    todos = todos.json()

    n = 0
    for todo in todos:
        if todo['completed'] is True:
            num += 1

    print(f"Employee {users[0]['name']} is done with tasks({n}/{len(todos)}):")

    for todo in todos:
        if users[0]['id'] == todo['userId']:
            if todo["completed"] is True:
                print("\t {}".format(todo["title"]))
