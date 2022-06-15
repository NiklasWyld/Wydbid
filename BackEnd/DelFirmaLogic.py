import os
import pickle
import sys
from PyQt5.QtWidgets import QComboBox, QMessageBox, QWidget
from Data import Firma
import shutil
import Wydbid

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

        firma_liste.addItem(firma.name, [firma, n_file])

def delFirmaFinal(file: str, widget: QWidget):
    folder = file.split('/')[-2]
    folder = f'{Wydbid.location}Firmen/{folder}/'
    os.remove(file)
    shutil.rmtree(folder, ignore_errors=True)
    QMessageBox.about(Wydbid.app.parent(), 'Abgeschlossen', 'Die Firma wurde gelöscht!')

    m = QMessageBox.question(Wydbid.app.parent(),
                             'Wydbid neustarten',
                             'Achtung, um die Änderungen auszuführen, müssen Sie Wydbid neustarten! Wollen sie jetzt neustarten?',
                             QMessageBox.Yes,
                             QMessageBox.No)

    if m == QMessageBox.No:
        widget.close()
        return

    elif m == QMessageBox.Yes:
        sys.exit(0)

def getFirma(firma_box: QComboBox, passwort: str, widget: QWidget):
    firma: Firma.Firma = firma_box.currentData()[0]

    if passwort == '':
        QMessageBox.warning(Wydbid.app.parent(), 'Warnung', 'Alle Felder muessen ausgefuellt werden!')
        return

    if passwort == firma.passwort:
        delFirmaFinal(firma_box.currentData()[1], widget)
    else:
        QMessageBox.warning(Wydbid.app.parent(), 'Achtung', 'Achtung, das eingegebene Passwort ist falsch!')
        return