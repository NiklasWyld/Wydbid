import pickle
from PyQt5.QtWidgets import QComboBox, QMessageBox, QWidget
from Data import Company
import os
from UI.Login import EmployeeLogin
import Wydbid


def login(firmenlogin: QWidget, firma: QComboBox, password: str):
    if firma.currentData() == None or password == '':
        QMessageBox.warning(Wydbid.app.parent(), 'Warning',
                            'All fields must be filled in!')
        return

    firma: Company.Company = firma.currentData()

    if password != firma.passwort:
        QMessageBox.warning(Wydbid.app.parent(), 'Attention',
                            'The password you entered is incorrect!')
        return

    Wydbid.firmen_location = f'{Wydbid.location}Firmen/{firma.id}/'
    Wydbid.firma = firma

    firmenlogin.hide()

    mitarbeiter_login = EmployeeLogin.EmployeeLogin()
    mitarbeiter_login.title.setText(f'{firma.name}')
    mitarbeiter_login.showMaximized()

    Wydbid.mitarbeiter_login = mitarbeiter_login


def addItems(firma_liste: QComboBox):
    l = f'{Wydbid.location}Firmen/'
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

        firma_liste.addItem(firma.name, firma)
