import os
import pickle
import sys
from PyQt5.QtWidgets import QComboBox, QMessageBox, QWidget
from Data import Company
import shutil
import Wydbid


def addItems(companylist: QComboBox):
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

        companylist.addItem(firma.name, [firma, n_file])


def delCompanyFinal(file: str, widget: QWidget):
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


def getCompany(companybox: QComboBox, password: str, widget: QWidget):
    firma: Company.Company = companybox.currentData()[0]

    if password == '':
        QMessageBox.warning(Wydbid.app.parent(), 'Warning',
                            'All fields must be filled in!')
        return

    if password != firma.password:
        QMessageBox.warning(Wydbid.app.parent(), 'Attention',
                            'Attention, the password entered is incorrect!')
        return
    delCompanyFinal(companybox.currentData()[1], widget)
