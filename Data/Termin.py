import Customer

class Termin:
    def __init__(self, id: int, titel: str, datum: str, kunde: Customer):
        self.id = id
        self.titel = titel
        self.datum = datum
        self.kunde = kunde