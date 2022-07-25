class Customer:
    def __init__(self, id: int, vorname: str, nachname: str, email: str, adresse: str, nummer: str, geschlecht: str, geburtsdatum: str, informationen: str):
        self.id = id
        self.vorname = vorname
        self.nachname = nachname
        self.email = email
        self.adresse = adresse
        self.nummer = nummer
        self.geschlecht = geschlecht
        self.geburtsdatum = geburtsdatum
        self.informationen = informationen