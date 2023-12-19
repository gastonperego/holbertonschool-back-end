#!/usr/bin/python3
"""Prints the completed tasks of an employee"""

if __name__ == '__main__':
    from sys import argv
    import urllib3


    users = urllib3.request("GET",
                            "https://jsonplaceholder.typicode.com/users?id={}".format(argv[1]))
    todos = urllib3.request("GET",
                            "https://jsonplaceholder.typicode.com/todos?userId={}".format(argv[1]))

    users = users.json()
    todos = todos.json()

    num = 0
    for todo in todos:
        if todo['completed'] is True:
            num += 1

    print("Employee {} is done with tasks({}/{}):".format(users[0]['name'], num, len(todos)))

    for todo in todos:
        if todo["completed"] is True:
            print("\t {}".format(todo["title"]))
