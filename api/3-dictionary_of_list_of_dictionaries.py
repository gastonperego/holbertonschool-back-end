#!/usr/bin/python3
"""Prints the completed tasks of an employee"""

if __name__ == '__main__':
    from sys import argv
    import urllib3

    users = urllib3.request("GET",
                            f"https://jsonplaceholder.typicode.com/users")

    users = users.json()

    dic = {}
    
    for user in users:
        todos = urllib3.request("GET", f"https://jsonplaceholder.typicode.com/todos?userId={user['id']}")
        todos = todos.json()
        lis = []
        for todo in todos:
            dic["username"] = user["username"]
            dic["task"] = todo["title"]
            dic["completed"] = todo["completed"]
            lis.append(dic)
        dic2 = {}
        dic2[f"{user['id']}"] = lis
    
    print(dic2)
        
    
        

        