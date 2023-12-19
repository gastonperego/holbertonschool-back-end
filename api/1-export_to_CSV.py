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

    with open(f"{users[0]['id']}.csv", "w", encoding="utf-8") as file:
        for todo in todos:
            string = f"\"{users[0]['id']}\", \"{users[0]['name']}\", \"{todo['completed']}\", \"{todo['title']}\"\n"
            file.write(string)
        
