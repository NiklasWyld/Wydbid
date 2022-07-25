from Data.Employee import Mitarbeiter

class Task:
    def __init__(self, author: Mitarbeiter, receiver: Mitarbeiter, title: str, description: str):
        self.author = author
        self.receiver = receiver
        self.title = title
        self.description = description