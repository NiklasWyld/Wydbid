from PyQt5.QtCore import QDate, QTime
import Customer

class Appointment:
    def __init__(self, title: str, description: str, date: QDate, time: QTime, customer: Customer):
        self.title = title
        self.description = description
        self.date = date
        self.time = time
        self.customer = customer