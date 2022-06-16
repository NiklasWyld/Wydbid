import pickle
from PyQt5.QtWidgets import QComboBox, QMessageBox, QWidget
from Data import Firma
import os
from UI.Login import MitarbeiterLogin
import Wydbid

def login(firmenlogin: QWidget, firma: QComboBox, password: str):
    if firma.currentData() == None:
        QMessageBox.warning(Wydbid.app.parent(), 'Warnung', 'Alle Felder muessen ausgefuellt werden!')
        return

    if password == '':
        QMessageBox.warning(Wydbid.app.parent(), 'Warnung', 'Alle Felder muessen ausgefuellt werden!')
        return

    firma: Firma.Firma = firma.currentData()

    if password == firma.passwort:
        Wydbid.firmen_location = f'{Wydbid.location}Firmen/{firma.id}/'
        Wydbid.firma = firma

        firmenlogin.hide()

        mitarbeiter_login = MitarbeiterLogin.MitarbeiterLogin()
        mitarbeiter_login.title.setText(f'{firma.name}')
        mitarbeiter_login.showMaximized()

        Wydbid.mitarbeiter_login = mitarbeiter_login
    else:
        QMessageBox.warning(Wydbid.app.parent(), 'Achtung', 'Das eingegebene Passwort ist falsch!')
        return

def addItems(firma_liste: QComboBox):
    l = f'{Wydbid.location}Firmen/'
    files = []

    for folder in os.listdir(l):
        for file in os.listdir(l + folder):
            if file.endswith('.wbf'):
                files.append(f'{l}{folder}/{file}')

    for n_file in files:
        try: n = open(n_file, 'rb')
        except:
            QMessageBox.about(Wydbid.app.parent(), 'Warnung', 'Etwas ist schiefgelaufen!')
            return

        try:
            firma: Firma.Firma = pickle.load(n)
        except:
            QMessageBox.about(Wydbid.app.parent(), 'Warnung', 'Etwas ist schiefgelaufen!')
            return

        firma_liste.addItem(firma.name, firma)