import os
import pickle
from PyQt5.QtWidgets import QWidget, QMessageBox
import Wydbid
from UI.Login import CompanyLogin, EmployeeLogin
from UI.WydbidUI import WydbidUIMain
from Data import Employee


def logoutCompany(employee_login_widget: EmployeeLogin):
    Wydbid.company = None
    Wydbid.company_location = ''

    employee_login_widget.clear()
    employee_login_widget.hide()

    # Loop through all widgets to get the company login widget to show it and clear the text fields
    for i in Wydbid.app.allWidgets():
        if type(i) == CompanyLogin.CompanyLogin:
            i.password.setText('')
            i.showMaximized()


def login(username: str, password: str, widget: QWidget):
    if username == '' or password == '':
        QMessageBox.warning(Wydbid.app.parent(), 'Warning',
                            'All fields must be filled in!')
        return

    if not os.path.exists(f'{Wydbid.company_location}Employees/{username}.wbm'):
        QMessageBox.warning(Wydbid.app.parent(
        ), 'Attention', 'A staff member with these usernames does not exist!')
        return

    employee_file = open(
        f'{Wydbid.company_location}Employees/{username}.wbm', 'rb')
    employee: Employee.Employee = pickle.load(employee_file)
    if employee.password != password:
        QMessageBox.warning(Wydbid.app.parent(), 'Attention',
                            'Attention, the password entered is incorrect!')
        return

    Wydbid.employee = employee

    widget.hide()

    wydbidui = WydbidUIMain.WydbidUIMain()
    wydbidui.setWindowTitle(
        f'Wydbid - Center | {Wydbid.company.name} | {employee.name}')
    wydbidui.showMaximized()

    Wydbid.wydbidui = wydbidui
