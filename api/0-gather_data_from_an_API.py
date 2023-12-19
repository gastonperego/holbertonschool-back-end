#!/usr/bin/python3
"""Prints the completed tasks of an employee"""

if __name__ == '__main__':
    from sys import argv
    import urllib3


    users = urllib3.request("GET",
                            f"https://jsonplaceholder.typicode.com/users?id={argv[1]}")
    todos = urllib3.request("GET",
                            f"https://jsonplaceholder.typicode.com/todos?userId={argv[1]}")

    users = users.json()
    todos = todos.json()

    num = 0
    for todo in todos:
        if todo['completed'] is True:
            num += 1

    print(f"Employee {users[0]['name']} is done with tasks({num}/{len(todos)}):")

    for todo in todos:
        if todo["completed"] is True:
            print(f"    {todo['title']}")
