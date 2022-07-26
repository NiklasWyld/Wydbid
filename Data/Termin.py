import Customer

class Termin:
    def __init__(self, id: int, title: str, date: str, customer: Customer):
        self.id = id
        self.title = title
        self.date = date
        self.customer = customer