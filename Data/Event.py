import Customer

class Event:
    def __init__(self, id: int, kunde: Customer, titel: str, beschreibung: str):
        self.id = id
        self.kunde = kunde
        self.titel = titel
        self.beschreibung = beschreibung