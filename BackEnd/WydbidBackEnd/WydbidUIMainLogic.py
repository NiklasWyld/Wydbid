from PyQt5.QtCore import Qt, QModelIndex
from sqlalchemy.orm import sessionmaker
from Data.DataCombi import *
from PyQt5.QtWidgets import QWidget, QMessageBox, QTableWidget, QTableWidgetItem, QLineEdit
from CustomQt import MessageBox
from UI.Login import CompanyLogin, EmployeeLogin
import Wydbid
from UI.WydbidUI.Prefabs.Customer import ViewCustomer

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
    global d_gender
    customerlist.setSortingEnabled(False)
    customerlist.clear()
    customerlist.clearContents()
    customerlist.setColumnCount(0)
    customerlist.setRowCount(0)

    customerlist.setColumnCount(9)
    customerlist.setHorizontalHeaderLabels(
        ['Customer id', 'Firstname', 'Lastname', 'E-mail address', 'Adress', 'Number', 'Gender', 'Birth date', ''])
    customerlist.setColumnWidth(0, 100)
    customerlist.setColumnWidth(1, 200)
    customerlist.setColumnWidth(2, 200)
    customerlist.setColumnWidth(3, 200)
    customerlist.setColumnWidth(4, 200)
    customerlist.setColumnWidth(5, 200)
    customerlist.setColumnWidth(6, 200)
    customerlist.setColumnWidth(7, 200)

    engine = create_engine(f'sqlite:///{Wydbid.company_location}database.db')
    _session = sessionmaker()
    session = _session(bind=engine)

    base.metadata.create_all(engine)

    customers = session.query(Customer).all()

    customers.sort(key=lambda x: x.id, reverse=False)

    customerlist.setRowCount(len(customers))

    i = 0

    for customer in customers:
        id = QTableWidgetItem()
        id.setData(Qt.DisplayRole, customer.id)

        customerlist.setItem(i, 1, QTableWidgetItem(
            f'{customer.firstname}'))

        customerlist.setItem(i, 2, QTableWidgetItem(
            f'{customer.lastname}'))

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
        customerlist.setColumnWidth(8, 40)

        customerlist.setItem(i, 0, id)
        customerlist.setItem(i, 3, email)
        customerlist.setItem(i, 4, adress)
        customerlist.setItem(i, 5, number)
        customerlist.setItem(i, 6, gender)
        customerlist.setItem(i, 7, birthdate)
        customerlist.setItem(i, 8, view)
        i = i + 1

    customerlist.setSortingEnabled(True)

def appendCustomers(customerlist: QTableWidget):
    global d_gender
    customerlist.clear()
    customerlist.setHorizontalHeaderLabels(
        ['Customer id', 'Firstname', 'Lastname', 'E-mail address', 'Adress', 'Number', 'Gender', 'Birth date', ''])
    customerlist.setColumnWidth(0, 100)
    customerlist.setColumnWidth(1, 200)
    customerlist.setColumnWidth(2, 200)
    customerlist.setColumnWidth(3, 200)
    customerlist.setColumnWidth(4, 200)
    customerlist.setColumnWidth(5, 200)
    customerlist.setColumnWidth(6, 200)
    customerlist.setColumnWidth(7, 200)

    engine = create_engine(f'sqlite:///{Wydbid.company_location}database.db')
    _session = sessionmaker()
    session = _session(bind=engine)

    base.metadata.create_all(engine)

    customers = session.query(Customer).all()

    customers.sort(key=lambda x: x.id, reverse=False)

    customerlist.setRowCount(len(customers))

    i = 0

    for customer in customers:
        id = QTableWidgetItem()
        id.setData(Qt.DisplayRole, customer.id)

        customerlist.setItem(i, 1, QTableWidgetItem(
            f'{customer.firstname}'))

        customerlist.setItem(i, 2, QTableWidgetItem(
            f'{customer.lastname}'))

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
        customerlist.setColumnWidth(8, 40)

        customerlist.setItem(i, 0, id)
        customerlist.setItem(i, 3, email)
        customerlist.setItem(i, 4, adress)
        customerlist.setItem(i, 5, number)
        customerlist.setItem(i, 6, gender)
        customerlist.setItem(i, 7, birthdate)
        customerlist.setItem(i, 8, view)
        i = i + 1

def viewCustomer(customerlist, viewcustomer: ViewCustomer.ViewCustomer, item):
    customerid = customerlist.item(item.row(), 0).text()
    engine = create_engine(f'sqlite:///{Wydbid.company_location}database.db')
    _session = sessionmaker()
    session = _session(bind=engine)

    base.metadata.create_all(engine)

    customer = session.query(Customer).filter(Customer.id == customerid).first()

    viewcustomer.hide()
    viewcustomer.clear()
    viewcustomer.setCustomer(customer)
    viewcustomer.show()

def searchForFirstName(searchfirst: QLineEdit, searchlast: QLineEdit, list: QTableWidget):
    name = searchfirst.text().lower()
    for row in range(list.rowCount()):
        item = list.item(row, 1)

        # if the search is not in the item's text do not hide the row
        list.setRowHidden(row, name not in item.text().lower())
    searchlast.setText('')

def searchForLastName(searchfirst: QLineEdit, searchlast: QLineEdit, list: QTableWidget):
    name = searchlast.text().lower()
    for row in range(list.rowCount()):
        item = list.item(row, 2)

        # if the search is not in the item's text do not hide the row
        list.setRowHidden(row, name not in item.text().lower())
    searchfirst.setText('')

def createFirstNews():
    engine = create_engine(f'sqlite:///{Wydbid.company_location}database.db')
    _session = sessionmaker()
    session = _session(bind=engine)

    base.metadata.create_all(engine)

    news = News(title='Welcome to Wydbid!',
                description='''Welcome to Wydbid!

Hello, we are glad you chose us, Wydbid! 

You can now start using Wydbid completely free of charge with all its features.
                ''')

    session.add(news)
    session.commit()

    Wydbid.wydbidui.setLatestNews()

def getLatestNews(wydbidui):
    engine = create_engine(f'sqlite:///{Wydbid.company_location}database.db')
    _session = sessionmaker()
    session = _session(bind=engine)

    base.metadata.create_all(engine)

    news = session.query(News).all()

    if not news:
        createFirstNews()
        return

    news.sort(key=lambda x: x.id, reverse=False)
    news = news[-1]

    return news

def contact():
    p = MessageBox.MessageBox(parent=Wydbid.app.parent(),
                              title='Contact',
                              text='In case of a simple error, please contact the administrator\n'
                              'In case of a software error in Wydbid, please contact the software producer by e-mail: niklasch1999@gmail.com')
    p.setIcon(QMessageBox.Warning)
    p.setDefaultButton(QMessageBox.StandardButton.Ok)
    p.exec_()
