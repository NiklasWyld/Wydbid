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
# ToDo: Fix reload


def handleNextId(create_kunde):
    id_list = os.listdir(f'{Wydbid.firmen_location}Kunden/')
    if not id_list:
        return 1

    id_list = [int(x) for x in id_list]

    id_list.sort()
    print(id_list)
    _number = 0

    for id in id_list:
        if _number + 1 == id:
            _number = _number + 1
        else:
            return _number + 1

    return id_list[-1] + 1


def createKunde(create_kunde):
    if create_kunde.id_tick.isChecked():
        print(handleNextId(create_kunde))
        return
    else:
        new_id = create_kunde.id.text()

    try:
        int(new_id)
    except:
        QMessageBox.warning(Wydbid.app.parent(), 'Warnung',
                            'Die Kundennummer muss eine Zahl sein.')
        return

    if not new_id.strip() or not create_kunde.vorname.text().strip() or not create_kunde.nachname.text().strip():
        QMessageBox.warning(Wydbid.app.parent(), 'Warnung',
                            'Die Pflichtfelder muessen ausgefuellt werden!')
        return

    kunde_new = Kunde.Kunde(id=int(new_id), vorname=create_kunde.vorname.text(), nachname=create_kunde.nachname.text(),
                            email=create_kunde.email.text(), adresse=create_kunde.adresse.text(),
                            nummer=create_kunde.nummer.text(), geschlecht=create_kunde.geschlecht.currentData(),
                            geburtsdatum=create_kunde.geburtsdatum.text(),
                            informationen=create_kunde.informationen.toPlainText())

    kunde_loc_name = new_id

    location = f'{Wydbid.firmen_location}Kunden/{kunde_loc_name}/'

    if os.path.exists(location):
        QMessageBox.warning(Wydbid.app.parent(), 'Achtung',
                            'Ein Kunde mit dieser Kundennummer existiert bereits!')
        return

    os.makedirs(location)
    k_file = open(f'{location}{kunde_loc_name}.wbk', 'wb')

    pickle.dump(kunde_new, k_file, pickle.HIGHEST_PROTOCOL)

    QMessageBox.about(Wydbid.app.parent(), 'Abgeschlossen',
                      f'{kunde_new.vorname} {kunde_new.nachname} wurde erstellt.')

    create_kunde.clear()
    create_kunde.hide()
