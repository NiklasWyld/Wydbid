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
            i.password.setText('')
            i.showMaximized()


def logoutEmployee(widget: QWidget):
    Wydbid.mitarbeiter = None

    widget.hide()

    # Loop through all widgets to get the company login widget to show it and clear the text fields
    for i in Wydbid.app.allWidgets():
        if type(i) == EmployeeLogin.EmployeeLogin:
            i.password.setText('')
            i.showMaximized()

def reloadCustomers(customerlist: QTableWidget):
    customerlist.setHorizontalHeaderLabels(
        ['Customer id', 'Name', 'E-mail address', 'Adress', 'Number', 'Gender', 'Birth date', ''])
    customerlist.setColumnWidth(0, 200)
    customerlist.setColumnWidth(1, 200)
    customerlist.setColumnWidth(2, 200)
    customerlist.setColumnWidth(3, 200)
    customerlist.setColumnWidth(4, 200)
    customerlist.setColumnWidth(5, 200)
    customerlist.setColumnWidth(6, 200)

    kunden = []
    dateien = os.listdir(f'{Wydbid.firmen_location}Customers/')

    for datei in dateien:
        kunde: Customer.Customer = pickle.load(
            open(f'{Wydbid.firmen_location}Customers/{datei}/{datei}.wbk', 'rb'))
        kunden.append(kunde)

    kunden.sort(key=lambda x: x.lastname, reverse=False)

    customerlist.setRowCount(len(kunden))

    i = 0

    for kunde in kunden:
        id = QTableWidgetItem()
        id.setData(Qt.DisplayRole, kunde.id)

        customerlist.setItem(i, 1, QTableWidgetItem(
            f'{kunde.firstname} {kunde.lastname}'))

        email = QTableWidgetItem()
        email.setData(Qt.DisplayRole, kunde.email)

        adresse = QTableWidgetItem()
        adresse.setData(Qt.DisplayRole, kunde.adress)

        nummer = QTableWidgetItem()
        nummer.setData(Qt.DisplayRole, kunde.number)

        geschlecht = QTableWidgetItem()
        if kunde.gender == 'men':
            d_geschlecht = 'Male'
        elif kunde.gender == 'women':
            d_geschlecht = 'Female'
        geschlecht.setData(Qt.DisplayRole, d_geschlecht)

        geburtsdatum = QTableWidgetItem()
        geburtsdatum.setData(Qt.DisplayRole, kunde.birthdate)

        ansicht = QTableWidgetItem()
        ansicht.setData(Qt.DisplayRole, '🔎')
        ansicht.setTextAlignment(Qt.AlignCenter)
        customerlist.setColumnWidth(7, 40)

        customerlist.setItem(i, 0, id)
        customerlist.setItem(i, 2, email)
        customerlist.setItem(i, 3, adresse)
        customerlist.setItem(i, 4, nummer)
        customerlist.setItem(i, 5, geschlecht)
        customerlist.setItem(i, 6, geburtsdatum)
        customerlist.setItem(i, 7, ansicht)
        i = i + 1

def appendCustomers(customerlist: QTableWidget):
    global d_geschlecht
    customerlist.clear()
    customerlist.setHorizontalHeaderLabels(
        ['Customer id', 'Name', 'E-mail address', 'Adress', 'Number', 'Gender', 'Birth date', ''])
    customerlist.setColumnWidth(0, 200)
    customerlist.setColumnWidth(1, 200)
    customerlist.setColumnWidth(2, 200)
    customerlist.setColumnWidth(3, 200)
    customerlist.setColumnWidth(4, 200)
    customerlist.setColumnWidth(5, 200)
    customerlist.setColumnWidth(6, 200)

    kunden = []
    dateien = os.listdir(f'{Wydbid.firmen_location}Customers/')

    for datei in dateien:
        kunde: Customer.Customer = pickle.load(
            open(f'{Wydbid.firmen_location}Customers/{datei}/{datei}.wbk', 'rb'))
        kunden.append(kunde)

    kunden.sort(key=lambda x: x.lastname, reverse=False)

    customerlist.setRowCount(len(kunden))

    i = 0

    for kunde in kunden:
        id = QTableWidgetItem()
        id.setData(Qt.DisplayRole, kunde.id)

        customerlist.setItem(i, 1, QTableWidgetItem(
            f'{kunde.firstname} {kunde.lastname}'))

        email = QTableWidgetItem()
        email.setData(Qt.DisplayRole, kunde.email)

        adresse = QTableWidgetItem()
        adresse.setData(Qt.DisplayRole, kunde.adress)

        nummer = QTableWidgetItem()
        nummer.setData(Qt.DisplayRole, kunde.number)

        geschlecht = QTableWidgetItem()
        if kunde.gender == 'men':
            d_geschlecht = 'Male'
        elif kunde.gender == 'women':
            d_geschlecht = 'Female'
        geschlecht.setData(Qt.DisplayRole, d_geschlecht)

        geburtsdatum = QTableWidgetItem()
        geburtsdatum.setData(Qt.DisplayRole, kunde.birthdate)

        ansicht = QTableWidgetItem()
        ansicht.setData(Qt.DisplayRole, '🔎')
        ansicht.setTextAlignment(Qt.AlignCenter)
        customerlist.setColumnWidth(7, 40)

        customerlist.setItem(i, 0, id)
        customerlist.setItem(i, 2, email)
        customerlist.setItem(i, 3, adresse)
        customerlist.setItem(i, 4, nummer)
        customerlist.setItem(i, 5, geschlecht)
        customerlist.setItem(i, 6, geburtsdatum)
        customerlist.setItem(i, 7, ansicht)
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
