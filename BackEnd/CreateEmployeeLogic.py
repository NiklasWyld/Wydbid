import os
import pickle
import sys
from PyQt5.QtWidgets import QMessageBox, QWidget
import Wydbid
from Data import Employee


def createEmployeeFinal(name: str, username: str, passwort: str, widget: QWidget):
    if os.path.exists(f'{Wydbid.firmen_location}Employees/{str(username)}.wbm'):
        QMessageBox.warning(Wydbid.app.parent(
        ), 'Attention', 'A staff member with these usernames already exists!')
        return

    if name == '' or username == '' or passwort == '':
        QMessageBox.warning(Wydbid.app.parent(), 'Warning',
                            'All fields must be filled in!')
        return

    if not os.path.exists(f'{Wydbid.firmen_location}Employees/'):
        os.makedirs(f'{Wydbid.firmen_location}Employees/')
    mitarbeiter_file = open(
        f'{Wydbid.firmen_location}Employees/{str(username)}.wbm', 'wb')
    mitarbeiter = Employee.Employee(username, name, passwort)

    pickle.dump(mitarbeiter, mitarbeiter_file, pickle.HIGHEST_PROTOCOL)

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
