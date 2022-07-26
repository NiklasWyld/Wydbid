import Customer

class Order:
    def __init__(self, id: int, customer: Customer.Customer, title: str, description: str, price: str):
        self.id = id
        self.customer = customer
        self.title = title
        self.description = description
        self.price = price