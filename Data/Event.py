import Customer

class Event:
    def __init__(self, id: int, customer: Customer, title: str, description: str):
        self.id = id
        self.customer = customer
        self.title = title
        self.description = description