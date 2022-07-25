import os
import pickle
from PyQt5.QtCore import Qt, QModelIndex
from Data import Customer
from PyQt5.QtWidgets import QWidget, QMessageBox, QTableWidget, QTableWidgetItem, QLineEdit
import Wydbid
from CustomQt import MessageBox
from UI.Login import CompanyLogin, EmployeeLogin
from UI.WydbidUI.Prefabs.Customer import CreateCustomer


def logoutCompany(widget: QWidget):
    Wydbid.firma = None
    Wydbid.firmen_location = ''

    widget.hide()

    # Loop through all widgets to get the company login widget to show it and clear the text fields
    for i in Wydbid.app.allWidgets():
        if type(i) == CompanyLogin.CompanyLogin:
            i.passwort.setText('')
            i.showMaximized()


def logoutMitarbeiter(widget: QWidget):
    Wydbid.mitarbeiter = None

    widget.hide()

    # Loop through all widgets to get the company login widget to show it and clear the text fields
    for i in Wydbid.app.allWidgets():
        if type(i) == EmployeeLogin.EmployeeLogin:
            i.passwort.setText('')
            i.showMaximized()

def reloadKunden(kundenliste: QTableWidget):
    kundenliste.setHorizontalHeaderLabels(
        ['Kundennummer', 'Name', 'E-Mail Adresse', 'Adresse', 'Nummer', 'Geschlecht', 'Geburtsdatum', ''])
    kundenliste.setColumnWidth(0, 200)
    kundenliste.setColumnWidth(1, 200)
    kundenliste.setColumnWidth(2, 200)
    kundenliste.setColumnWidth(3, 200)
    kundenliste.setColumnWidth(4, 200)
    kundenliste.setColumnWidth(5, 200)
    kundenliste.setColumnWidth(6, 200)

    kunden = []
    dateien = os.listdir(f'{Wydbid.firmen_location}Kunden/')

    for datei in dateien:
        kunde: Customer.Customer = pickle.load(
            open(f'{Wydbid.firmen_location}Kunden/{datei}/{datei}.wbk', 'rb'))
        kunden.append(kunde)

    kunden.sort(key=lambda x: x.nachname, reverse=False)

    kundenliste.setRowCount(len(kunden))

    i = 0

    for kunde in kunden:
        id = QTableWidgetItem()
        id.setData(Qt.DisplayRole, kunde.id)

        kundenliste.setItem(i, 1, QTableWidgetItem(
            f'{kunde.vorname} {kunde.nachname}'))

        email = QTableWidgetItem()
        email.setData(Qt.DisplayRole, kunde.email)

        adresse = QTableWidgetItem()
        adresse.setData(Qt.DisplayRole, kunde.adresse)

        nummer = QTableWidgetItem()
        nummer.setData(Qt.DisplayRole, kunde.nummer)

        geschlecht = QTableWidgetItem()
        if kunde.geschlecht == 'men':
            d_geschlecht = 'männlich'
        elif kunde.geschlecht == 'women':
            d_geschlecht = 'weiblich'
        geschlecht.setData(Qt.DisplayRole, d_geschlecht)

        geburtsdatum = QTableWidgetItem()
        geburtsdatum.setData(Qt.DisplayRole, kunde.geburtsdatum)

        ansicht = QTableWidgetItem()
        ansicht.setData(Qt.DisplayRole, '🔎')
        ansicht.setTextAlignment(Qt.AlignCenter)
        kundenliste.setColumnWidth(7, 40)

        kundenliste.setItem(i, 0, id)
        kundenliste.setItem(i, 2, email)
        kundenliste.setItem(i, 3, adresse)
        kundenliste.setItem(i, 4, nummer)
        kundenliste.setItem(i, 5, geschlecht)
        kundenliste.setItem(i, 6, geburtsdatum)
        kundenliste.setItem(i, 7, ansicht)
        i = i + 1

def appendKunden(kundenliste: QTableWidget):
    global d_geschlecht
    kundenliste.clear()
    kundenliste.setHorizontalHeaderLabels(
        ['Kundennummer', 'Name', 'E-Mail Adresse', 'Adresse', 'Nummer', 'Geschlecht', 'Geburtsdatum', ''])
    kundenliste.setColumnWidth(0, 200)
    kundenliste.setColumnWidth(1, 200)
    kundenliste.setColumnWidth(2, 200)
    kundenliste.setColumnWidth(3, 200)
    kundenliste.setColumnWidth(4, 200)
    kundenliste.setColumnWidth(5, 200)
    kundenliste.setColumnWidth(6, 200)

    kunden = []
    dateien = os.listdir(f'{Wydbid.firmen_location}Kunden/')

    for datei in dateien:
        kunde: Customer.Customer = pickle.load(
            open(f'{Wydbid.firmen_location}Kunden/{datei}/{datei}.wbk', 'rb'))
        kunden.append(kunde)

    kunden.sort(key=lambda x: x.nachname, reverse=False)

    kundenliste.setRowCount(len(kunden))

    i = 0

    for kunde in kunden:
        id = QTableWidgetItem()
        id.setData(Qt.DisplayRole, kunde.id)

        kundenliste.setItem(i, 1, QTableWidgetItem(
            f'{kunde.vorname} {kunde.nachname}'))

        email = QTableWidgetItem()
        email.setData(Qt.DisplayRole, kunde.email)

        adresse = QTableWidgetItem()
        adresse.setData(Qt.DisplayRole, kunde.adresse)

        nummer = QTableWidgetItem()
        nummer.setData(Qt.DisplayRole, kunde.nummer)

        geschlecht = QTableWidgetItem()
        if kunde.geschlecht == 'men':
            d_geschlecht = 'männlich'
        elif kunde.geschlecht == 'women':
            d_geschlecht = 'weiblich'
        geschlecht.setData(Qt.DisplayRole, d_geschlecht)

        geburtsdatum = QTableWidgetItem()
        geburtsdatum.setData(Qt.DisplayRole, kunde.geburtsdatum)

        ansicht = QTableWidgetItem()
        ansicht.setData(Qt.DisplayRole, '🔎')
        ansicht.setTextAlignment(Qt.AlignCenter)
        kundenliste.setColumnWidth(7, 40)

        kundenliste.setItem(i, 0, id)
        kundenliste.setItem(i, 2, email)
        kundenliste.setItem(i, 3, adresse)
        kundenliste.setItem(i, 4, nummer)
        kundenliste.setItem(i, 5, geschlecht)
        kundenliste.setItem(i, 6, geburtsdatum)
        kundenliste.setItem(i, 7, ansicht)
        i = i + 1


def searchForName(search: QLineEdit, list: QTableWidget):
    name = search.text().lower()
    for row in range(list.rowCount()):
        item = list.item(row, 1)

        # if the search is not in the item's text do not hide the row
        list.setRowHidden(row, name not in item.text().lower())


def contact():
    p = MessageBox.MessageBox(parent=Wydbid.app.parent(),
                              title='Contact',
                              text='In case of a simple error, please contact the administrator\n'
                              'In case of a software error in Wydbid, please contact the software producer by e-mail: niklasch1999@gmail.com')
    p.setIcon(QMessageBox.Warning)
    p.setDefaultButton(QMessageBox.StandardButton.Ok)
    p.exec_()
