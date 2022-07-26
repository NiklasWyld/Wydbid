import os
import pickle
from PyQt5.QtWidgets import QComboBox, QMessageBox, QWidget
from Data import Company
import Wydbid


def addItems(firma_liste: QComboBox):
    l = f'{Wydbid.location}Companies/'
    files = []

    for folder in os.listdir(l):
        for file in os.listdir(l + folder):
            if file.endswith('.wbf'):
                files.append(f'{l}{folder}/{file}')

    for n_file in files:
        try:
            n = open(n_file, 'rb')
        except:
            QMessageBox.about(Wydbid.app.parent(), 'Warning',
                              'Something went wrong!')
            return

        try:
            firma: Company.Company = pickle.load(n)
        except:
            QMessageBox.about(Wydbid.app.parent(), 'Warning',
                              'Something went wrong!')
            return

        firma_liste.addItem(firma.name, [firma, n_file])


def changePasswortFinal(firma_box: QComboBox, old_passwort: str, new_passwort: str, widget: QWidget):
    if firma_box.currentData() == None or old_passwort == '' or new_passwort == '':
        QMessageBox.warning(Wydbid.app.parent(), 'Warning',
                            'All fields must be filled in!')
        return

    firma: Company.Company = firma_box.currentData()[0]
    if old_passwort != firma.passwort:
        QMessageBox.warning(Wydbid.app.parent(), 'Attention',
                            'The password you entered is incorrect!')
        return
    firma.passwort = new_passwort
    writer = open(firma_box.currentData()[1], 'wb')
    pickle.dump(firma, writer, pickle.HIGHEST_PROTOCOL)
    writer.close()

    QMessageBox.about(Wydbid.app.parent(), 'Process completed',
                      f'The password of {firma.name} was successfully changed.')

    m = QMessageBox.question(Wydbid.app.parent(),
                             'Wydbid neustarten',
                             'Achtung, um die Änderungen auszuführen, müssen Sie Wydbid neustarten! Wollen Sie jetzt neustarten?',
                             QMessageBox.Yes,
                             QMessageBox.No)

    if m == QMessageBox.No:
        widget.close()
        return

    elif m == QMessageBox.Yes:
        Wydbid.app.exit(0)
