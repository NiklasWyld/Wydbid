import os
import pickle
import sys
from PyQt5.QtWidgets import QMessageBox, QWidget
import Wydbid
from Data import Employee


def createEmployeeFinal(name: str, username: str, password: str, widget: QWidget):
    if os.path.exists(f'{Wydbid.company_location}Employees/{str(username)}.wbm'):
        QMessageBox.warning(Wydbid.app.parent(
        ), 'Attention', 'A staff member with these usernames already exists!')
        return

    if name == '' or username == '' or password == '':
        QMessageBox.warning(Wydbid.app.parent(), 'Warning',
                            'All fields must be filled in!')
        return

    if not os.path.exists(f'{Wydbid.company_location}Employees/'):
        os.makedirs(f'{Wydbid.company_location}Employees/')
    employee_file = open(
        f'{Wydbid.company_location}Employees/{str(username)}.wbm', 'wb')
    employee = Employee.Employee(username, name, password)

    pickle.dump(employee, employee_file, pickle.HIGHEST_PROTOCOL)

    QMessageBox.about(Wydbid.app.parent(), 'Completed',
                      f'{name} was created.')

    m = QMessageBox.question(Wydbid.app.parent(),
                             'Restart Wydbid',
                             'Attention, in order to use the new employee, you must first restart the programme! Do you want to restart Wydbid?',
                             QMessageBox.Yes,
                             QMessageBox.No)

    if m == QMessageBox.No:
        widget.close()
        return

    elif m == QMessageBox.Yes:
        Wydbid.app.exit(0)
