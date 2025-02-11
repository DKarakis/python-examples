  import json
from typing import List, Dict

class User:
    def __init__(self, username: str, password: str):
        self.username = username
        self.password = password  # In real applications, hash the password!
        self.tasks = []

    def add_task(self, task: str):
        self.tasks.append(task)

    def remove_task(self, task: str):
        if task in self.tasks:
            self.tasks.remove(task)

    def list_tasks(self) -> List[str]:
        return self.tasks

class TaskManager:
    def __init__(self):
        self.users: Dict[str, User] = {}

    def register_user(self, username: str, password: str) -> str:
        if username in self.users:
            return "User already exists."
        self.users[username] = User(username, password)
        return "User registered successfully."

    def authenticate_user(self, username: str, password: str) -> bool:
        user = self.users.get(username)
        return user is not None and user.password == password

    def add_task(self, username: str, task: str) -> str:
        if username not in self.users:
            return "User not found."
        self.users[username].add_task(task)
        return "Task added successfully."

    def remove_task(self, username: str, task: str) -> str:
        if username not in self.users:
            return "User not found."
        self.users[username].remove_task(task)
        return "Task removed successfully."

    def list_tasks(self, username: str) -> List[str]:
        if username not in self.users:
            return []
        return self.users[username].list_tasks()

if __name__ == "__main__":
    manager = TaskManager()
    
    print(manager.register_user("alice", "password123"))
    print(manager.add_task("alice", "Buy groceries"))
    print(manager.add_task("alice", "Read a book"))
    print("Tasks for Alice:", manager.list_tasks("alice"))
    print(manager.remove_task("alice", "Read a book"))
    print("Tasks for Alice:", manager.list_tasks("alice"))
