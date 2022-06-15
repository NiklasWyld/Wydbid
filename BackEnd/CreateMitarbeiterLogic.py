import os
import pickle
import sys
from PyQt5.QtWidgets import QMessageBox, QWidget
import Wydbid
from Data import Mitarbeiter

def createMitarbeiterFinal(id: str, name: str, username: str, passwort: str, widget: QWidget):
    if id == '':
        QMessageBox.warning(Wydbid.app.parent(), 'Warnung', 'Alle Felder muessen ausgefuellt werden!')
        return

    if name == '':
        QMessageBox.warning(Wydbid.app.parent(), 'Warnung', 'Alle Felder muessen ausgefuellt werden!')
        return

    if username == '':
        QMessageBox.warning(Wydbid.app.parent(), 'Warnung', 'Alle Felder muessen ausgefuellt werden!')
        return

    if passwort == '':
        QMessageBox.warning(Wydbid.app.parent(), 'Warnung', 'Alle Felder muessen ausgefuellt werden!')
        return

    try: int(id)
    except:
        QMessageBox.warning(Wydbid.app.parent(), 'Warnung', 'Es muss eine Zahl in das Firmen-ID Feld eingetragen werden!')
        return

    id = int(id)

    os.makedirs(f'{Wydbid.firmen_location}/Mitarbeiter/')
    mitarbeiter_file = open(f'{Wydbid.firmen_location}/Mitarbeiter/{str(id)}.wbm', 'wb')
    mitarbeiter = Mitarbeiter.Mitarbeiter(id, username, name, passwort)

    pickle.dump(mitarbeiter, mitarbeiter_file, pickle.HIGHEST_PROTOCOL)

    QMessageBox.about(Wydbid.app.parent(), 'Abgeschlossen', f'{name} wurde erstellt.')

    m = QMessageBox.question(Wydbid.app.parent(),
                             'Wydbid neustarten',
                             'Achtung, um den neuen Mitarbeiter zu nutzen, muessen Sie zuerst das Programm neustarten! Wollen sie Wydbid neustarten?',
                             QMessageBox.Yes,
                             QMessageBox.No)

    if m == QMessageBox.No:
        widget.close()
        return

    elif m == QMessageBox.Yes:
        sys.exit(0)