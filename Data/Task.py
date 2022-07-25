from Data.Employee import Employee

class Task:
    def __init__(self, author: Employee, receiver: Employee, title: str, description: str):
        self.author = author
        self.receiver = receiver
        self.title = title
        self.description = description