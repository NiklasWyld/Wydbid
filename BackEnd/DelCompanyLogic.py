import os
import pickle
import sys
from PyQt5.QtWidgets import QComboBox, QMessageBox, QWidget
from Data import Company
import shutil
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


def delFirmaFinal(file: str, widget: QWidget):
    folder = file.split('/')[-2]
    folder = f'{Wydbid.location}Companies/{folder}/'
    os.remove(file)
    shutil.rmtree(folder, ignore_errors=True)
    QMessageBox.about(Wydbid.app.parent(), 'Completed',
                      'The company has been deleted!')

    m = QMessageBox.question(Wydbid.app.parent(),
                             'Restart Wydbid',
                             'Attention, you need to restart Wydbid to make the changes! Do you want to restart now?',
                             QMessageBox.Yes,
                             QMessageBox.No)

    if m == QMessageBox.No:
        widget.close()
        return

    elif m == QMessageBox.Yes:
        Wydbid.app.exit(0)


def getFirma(firma_box: QComboBox, passwort: str, widget: QWidget):
    firma: Company.Company = firma_box.currentData()[0]

    if passwort == '':
        QMessageBox.warning(Wydbid.app.parent(), 'Warning',
                            'All fields must be filled in!')
        return

    if passwort != firma.passwort:
        QMessageBox.warning(Wydbid.app.parent(), 'Attention',
                            'Attention, the password entered is incorrect!')
        return
    delFirmaFinal(firma_box.currentData()[1], widget)
