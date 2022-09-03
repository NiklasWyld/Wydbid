class Task:
    def __init__(self, author_id: int, receiver_id: int, title: str, description: str, deadline: str):
        self.author_id = author_id
        self.receiver_id = receiver_id
        self.title = title
        self.description = description
        self.deadline = deadline
        self.done = False