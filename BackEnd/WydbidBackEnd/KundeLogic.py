import pickle
from PyQt5.QtWidgets import QMessageBox
import Wydbid
import os
from Data import Kunde

def setupKundenFolder():
    kunden_path = f'{Wydbid.firmen_location}Kunden'

    if os.path.exists(kunden_path):
        return
    else:
        os.mkdir(kunden_path)

# ToDo: Add if not / .strip() to prove strings

def createKunde(create_kunde):
    if not create_kunde.vorname.text().strip():
        QMessageBox.warning(Wydbid.app.parent(), 'Warnung', 'Alle Felder muessen ausgefuellt werden!')
        return

    if not create_kunde.nachname.text().strip():
        QMessageBox.warning(Wydbid.app.parent(), 'Warnung', 'Alle Felder muessen ausgefuellt werden!')
        return

    kunde_new = Kunde.Kunde(vorname=create_kunde.vorname.text(), nachname=create_kunde.nachname.text(),
                            adresse=create_kunde.adresse.text(), nummer=create_kunde.nummer.text(),
                            geschlecht=create_kunde.geschlecht.currentData(),
                            geburtsdatum=create_kunde.geburtsdatum.text(),
                            informationen=create_kunde.informationen.toPlainText())

    kunde_old_loc_name = kunde_new.vorname + kunde_new.nachname
    kunde_loc_name = ''.join(e for e in kunde_old_loc_name if e.isalnum())

    location = f'{Wydbid.firmen_location}Kunden/{kunde_loc_name}/'

    if os.path.exists(location):
        QMessageBox.warning(Wydbid.app.parent(), 'Achtung', 'Ein Kunde mit diesen Namen existiert bereits!')
        return

    os.makedirs(location)
    k_file = open(f'{location}{kunde_loc_name}.wbk', 'wb')

    pickle.dump(kunde_new, k_file, pickle.HIGHEST_PROTOCOL)

    QMessageBox.about(Wydbid.app.parent(), 'Abgeschlossen', f'{kunde_new.vorname} {kunde_new.nachname} wurde erstellt.')

    create_kunde.clear()
    create_kunde.hide()