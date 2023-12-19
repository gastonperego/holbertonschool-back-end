#!/usr/bin/python3
"""Prints the completed tasks of an employee"""

if __name__ == '__main__':
    from sys import argv
    import requests


    users = requests.get("https://jsonplaceholder.typicode.com/users?id={}".format(argv[1]))
    todos = requests.get("https://jsonplaceholder.typicode.com/todos?userId={}".format(argv[1]))

    users = users.json()
    todos = todos.json()

    num = 0
    for todo in todos:
        if todo['completed'] is True:
            num += 1

    print("Employee {} is done with tasks({}/{}):".format(users[0]['name'], num, len(todos)))

    for todo in todos:
        if users[0]['id'] == todo['userId']:
            if todo["completed"] is True:
                print("\t {}".format(todo["title"]))
