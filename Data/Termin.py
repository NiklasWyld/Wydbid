import Kunde

class Termin:
    def __init__(self, id: int, titel: str, datum: str, kunde: Kunde):
        self.id = id
        self.titel = titel
        self.datum = datum
        self.kunde = kunde