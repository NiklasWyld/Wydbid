import pickle
from PyQt5.QtWidgets import QMessageBox
import Wydbid
import os
from Data import Customer


def setupKundenFolder():
    kunden_path = f'{Wydbid.firmen_location}Customers'

    if os.path.exists(kunden_path):
        return
    else:
        os.mkdir(kunden_path)

# ToDo: Add if not / .strip() to prove strings
# ToDo: Fix reload


def handleNextId():
    id_list = os.listdir(f'{Wydbid.firmen_location}Customers/')
    if not id_list:
        return str(1)

    id_list = [int(x) for x in id_list]

    id_list.sort()
    print(id_list)
    _number = 0

    for id in id_list:
        if _number + 1 == id:
            _number = _number + 1
        else:
            return str(_number + 1)

    return str(id_list[-1] + 1)


def createKunde(create_kunde):
    if create_kunde.id_tick.isChecked():
        new_id = handleNextId()
    else:
        new_id = create_kunde.id.text()

    try:
        int(new_id)
    except:
        QMessageBox.warning(Wydbid.app.parent(), 'Warning',
                            'The customer number must be a number.')
        return

    if not new_id.strip() or not create_kunde.vorname.text().strip() or not create_kunde.nachname.text().strip():
        QMessageBox.warning(Wydbid.app.parent(), 'Warning',
                            'The mandatory fields must be filled in!')
        return

    kunde_new = Customer.Customer(id=int(new_id), vorname=create_kunde.vorname.text(), nachname=create_kunde.nachname.text(),
                               email=create_kunde.email.text(), adresse=create_kunde.adresse.text(),
                               nummer=create_kunde.nummer.text(), geschlecht=create_kunde.geschlecht.currentData(),
                               geburtsdatum=create_kunde.geburtsdatum.text(),
                               informationen=create_kunde.informationen.toPlainText())

    kunde_loc_name = new_id

    location = f'{Wydbid.firmen_location}Customers/{kunde_loc_name}/'

    if os.path.exists(location):
        QMessageBox.warning(Wydbid.app.parent(), 'Attention',
                            'A customer with this customer number already exists!')
        return

    os.makedirs(location)
    k_file = open(f'{location}{kunde_loc_name}.wbk', 'wb')

    pickle.dump(kunde_new, k_file, pickle.HIGHEST_PROTOCOL)

    QMessageBox.about(Wydbid.app.parent(), 'Completed',
                      f'{kunde_new. vorname} {kunde_new.nachname} was created.')

    create_kunde.clear()
    create_kunde.hide()
