import pickle
import sys
from PyQt5.QtWidgets import QMessageBox, QWidget
from UI.Login.Prefabs import CreateFirma
from Data import Firma
import os
import Wydbid

def writeFirma(id: int, name: str, passwort: str, widget: QWidget):
    location = Wydbid.location

    if os.path.exists(f'{location}Firmen/{str(id)}/'):
        QMessageBox.warning(Wydbid.app.parent(), 'Achtung', 'Eine Firma mit dieser ID existiert bereits!')
        return

    '''try: firma_file = open(f'{location}Firmen/{str(id)}.wbf', 'wb')
    except: open(f'{location}Firmen/{str(id)}.wbf', 'x')'''

    os.makedirs(f'{location}Firmen/{str(id)}/')
    firma_file = open(f'{location}Firmen/{str(id)}/{str(id)}.wbf', 'wb')
    firma = Firma.Firma(id, name, passwort)

    pickle.dump(firma, firma_file, pickle.HIGHEST_PROTOCOL)

    QMessageBox.about(Wydbid.app.parent(), 'Abgeschlossen', f'{name} wurde erstellt.')

    m = QMessageBox.question(Wydbid.app.parent(),
                             'Wydbid neustarten',
                             'Achtung, um dich in die neue Firma einzuloggen, muessen Sie zuerst das Programm neustarten! Wollen Sie Wydbid neustarten?',
                             QMessageBox.Yes,
                             QMessageBox.No)

    if m == QMessageBox.No:
        widget.close()
        return

    elif m == QMessageBox.Yes:
        Wydbid.app.exit(0)

def getFirma(id: str, name: str, passwort: str, widget: QWidget):
    if id == '':
        QMessageBox.warning(Wydbid.app.parent(), 'Warnung', 'Alle Felder muessen ausgefuellt werden!')
        return
    if name == '':
        QMessageBox.warning(Wydbid.app.parent(), 'Warnung', 'Alle Felder muessen ausgefuellt werden!')
        return
    if passwort == '':
        QMessageBox.warning(Wydbid.app.parent(), 'Warnung', 'Alle Felder muessen ausgefuellt werden!')
        return

    try: int(id)
    except:
        QMessageBox.warning(Wydbid.app.parent(), 'Warnung', 'Es muss eine Zahl in das Firmen-ID Feld eingetragen werden!')
        CreateFirma.CreateFirma().clear(clearOnlyId=True)
        return

    id = int(id)
    passwort = passwort

    writeFirma(id, name, passwort, widget)