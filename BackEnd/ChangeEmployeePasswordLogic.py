import os
import pickle
import sys
from PyQt5.QtWidgets import QMessageBox, QWidget
import Wydbid
from Data import Employee


def changePasswordFinal(username: str, passwort: str, new_passwort: str, widget: QWidget):
    if username == '' or passwort == '' or new_passwort == '':
        QMessageBox.warning(Wydbid.app.parent(), 'Warning',
                            'All fields must be filled in!')
        return

    if not os.path.exists(f'{Wydbid.firmen_location}Employees/{username}.wbm'):
        QMessageBox.warning(Wydbid.app.parent(
        ), 'Attention', 'The user name or employee you entered does not exist.')
        return

    mitarbeiter_file = open(
        f'{Wydbid.firmen_location}Employees/{username}.wbm', 'rb')
    mitarbeiter: Employee.Employee = pickle.load(mitarbeiter_file)
    mitarbeiter_file.close()

    if not mitarbeiter.password == passwort:
        QMessageBox.warning(Wydbid.app.parent(), 'Attention',
                            'Attention, the password entered is incorrect!')
        return

    mitarbeiter_file_new = open(
        f'{Wydbid.firmen_location}Employees/{username}.wbm', 'wb')
    mitarbeiter.password = new_passwort
    pickle.dump(mitarbeiter, mitarbeiter_file_new, pickle.HIGHEST_PROTOCOL)

    QMessageBox.about(Wydbid.app.parent(), 'Process completed',
                      f'The password of {username} has been successfully changed.')

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
