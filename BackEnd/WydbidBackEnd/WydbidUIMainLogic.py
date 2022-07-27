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
    Wydbid.company = None
    Wydbid.company_location = ''

    widget.hide()

    # Loop through all widgets to get the company login widget to show it and clear the text fields
    for i in Wydbid.app.allWidgets():
        if type(i) == CompanyLogin.CompanyLogin:
            i.password.setText('')
            i.showMaximized()


def logoutEmployee(widget: QWidget):
    Wydbid.employee = None

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

    customers = []
    files = os.listdir(f'{Wydbid.company_location}Customers/')

    for file in files:
        customer: Customer.Customer = pickle.load(
            open(f'{Wydbid.company_location}Customers/{file}/{file}.wbk', 'rb'))
        customers.append(customer)

    customers.sort(key=lambda x: x.lastname, reverse=False)

    customerlist.setRowCount(len(customers))

    i = 0

    for customer in customers:
        id = QTableWidgetItem()
        id.setData(Qt.DisplayRole, customer.id)

        customerlist.setItem(i, 1, QTableWidgetItem(
            f'{customer.firstname} {customer.lastname}'))

        email = QTableWidgetItem()
        email.setData(Qt.DisplayRole, customer.email)

        adress = QTableWidgetItem()
        adress.setData(Qt.DisplayRole, customer.adress)

        number = QTableWidgetItem()
        number.setData(Qt.DisplayRole, customer.number)

        gender = QTableWidgetItem()
        if customer.gender == 'men':
            d_gender = 'Male'
        elif customer.gender == 'women':
            d_gender = 'Female'
        gender.setData(Qt.DisplayRole, d_gender)

        birthdate = QTableWidgetItem()
        birthdate.setData(Qt.DisplayRole, customer.birthdate)

        view = QTableWidgetItem()
        view.setData(Qt.DisplayRole, '🔎')
        view.setTextAlignment(Qt.AlignCenter)
        customerlist.setColumnWidth(7, 40)

        customerlist.setItem(i, 0, id)
        customerlist.setItem(i, 2, email)
        customerlist.setItem(i, 3, adress)
        customerlist.setItem(i, 4, number)
        customerlist.setItem(i, 5, gender)
        customerlist.setItem(i, 6, birthdate)
        customerlist.setItem(i, 7, view)
        i = i + 1

def appendCustomers(customerlist: QTableWidget):
    global d_gender
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

    customers = []
    files = os.listdir(f'{Wydbid.company_location}Customers/')

    for file in files:
        customer: Customer.Customer = pickle.load(
            open(f'{Wydbid.company_location}Customers/{file}/{file}.wbk', 'rb'))
        customers.append(customer)

    customers.sort(key=lambda x: x.lastname, reverse=False)

    customerlist.setRowCount(len(customers))

    i = 0

    for customer in customers:
        id = QTableWidgetItem()
        id.setData(Qt.DisplayRole, customer.id)

        customerlist.setItem(i, 1, QTableWidgetItem(
            f'{customer.firstname} {customer.lastname}'))

        email = QTableWidgetItem()
        email.setData(Qt.DisplayRole, customer.email)

        adress = QTableWidgetItem()
        adress.setData(Qt.DisplayRole, customer.adress)

        number = QTableWidgetItem()
        number.setData(Qt.DisplayRole, customer.number)

        gender = QTableWidgetItem()
        if customer.gender == 'men':
            d_gender = 'Male'
        elif customer.gender == 'women':
            d_gender = 'Female'
        gender.setData(Qt.DisplayRole, d_gender)

        birthdate = QTableWidgetItem()
        birthdate.setData(Qt.DisplayRole, customer.birthdate)

        view = QTableWidgetItem()
        view.setData(Qt.DisplayRole, '🔎')
        view.setTextAlignment(Qt.AlignCenter)
        customerlist.setColumnWidth(7, 40)

        customerlist.setItem(i, 0, id)
        customerlist.setItem(i, 2, email)
        customerlist.setItem(i, 3, adress)
        customerlist.setItem(i, 4, number)
        customerlist.setItem(i, 5, gender)
        customerlist.setItem(i, 6, birthdate)
        customerlist.setItem(i, 7, view)
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
