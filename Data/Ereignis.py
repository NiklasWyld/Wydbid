import Kunde

class Ereignis:
    def __init__(self, id: int, kunde: Kunde, titel: str, beschreibung: str):
        self.id = id
        self.kunde = kunde
        self.titel = titel
        self.beschreibung = beschreibung