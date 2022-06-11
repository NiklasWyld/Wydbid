import Kunde

class Auftrag:
    def __init__(self, id: int, kunde: Kunde, titel: str, beschreibung: str, preis: str):
        self.id = id
        self.kunde = kunde
        self.titel = titel
        self.beschreibung = beschreibung
        self.preis = preis