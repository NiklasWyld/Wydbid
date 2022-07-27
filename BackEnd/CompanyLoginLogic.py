import pickle
from PyQt5.QtWidgets import QComboBox, QMessageBox, QWidget
from Data import Company
import os
from UI.Login import EmployeeLogin
import Wydbid


def login(companylogin: QWidget, company: QComboBox, password: str):
    if company.currentData() == None or password == '':
        QMessageBox.warning(Wydbid.app.parent(), 'Warning',
                            'All fields must be filled in!')
        return

    company: Company.Company = company.currentData()

    if password != company.password:
        QMessageBox.warning(Wydbid.app.parent(), 'Attention',
                            'The password you entered is incorrect!')
        return

    Wydbid.firmen_location = f'{Wydbid.location}Companies/{company.id}/'
    Wydbid.firma = company

    companylogin.hide()

    mitarbeiter_login = EmployeeLogin.EmployeeLogin()
    mitarbeiter_login.title.setText(f'{company.name}')
    mitarbeiter_login.showMaximized()

    Wydbid.mitarbeiter_login = mitarbeiter_login


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

        firma_liste.addItem(firma.name, firma)
