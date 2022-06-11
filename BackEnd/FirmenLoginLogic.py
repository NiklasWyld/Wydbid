import pickle
from PyQt5.QtWidgets import QComboBox, QMessageBox
from Data import Firma
import Wydbid
import os

def addItems(firma_liste: QComboBox):
    l = f'{Wydbid.location}Firmen/'
    files = []

    for folder in os.listdir(l):
        for file in os.listdir(l + folder):
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