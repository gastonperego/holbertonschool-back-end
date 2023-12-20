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

    with open(f"{users[0]['id']}.csv", "w", encoding="utf-8") as file:
        for todo in todos:
            uId = users[0]['id']
            uname = users[0]['name']
            state = todo['completed']
            tname = todo['title']
            string = (f"\"{uId}\",\"{uname}\",\"{state}\",\"{tname}\"\n")
            file.write(string)
