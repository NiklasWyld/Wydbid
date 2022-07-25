from Data.Mitarbeiter import Mitarbeiter

class Aufgabe:
    def __init__(self, author: Mitarbeiter, receiver: Mitarbeiter, title: str, description: str):
        self.author = author
        self.receiver = receiver
        self.title = title
        self.description = description