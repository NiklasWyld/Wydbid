import os
import pickle
import shutil
import sys
from PyQt5.QtWidgets import QWidget, QMessageBox
import Wydbid
from Data import Employee


def delMitarbeiterFinal(username: str, passwort: str, widget: QWidget):
    if username == '' or passwort == '':
        QMessageBox.warning(Wydbid.app.parent(), 'Warning',
                            'All fields must be filled in!')
        return

    # See if the file or employee exists
    if not os.path.exists(f'{Wydbid.firmen_location}Employees/{username}.wbm'):
        QMessageBox.warning(Wydbid.app.parent(
        ), 'Attention', 'The user name or employee you entered does not exist.')
        return

    readable_file = open(
        f'{Wydbid.firmen_location}Employees/{username}.wbm', 'rb')
    file_path = f'{Wydbid.firmen_location}Employees/{username}.wbm'

    mitarbeiter: Employee.Employee = pickle.load(readable_file)
    readable_file.close()

    if not passwort == mitarbeiter.password:
        QMessageBox.warning(Wydbid.app.parent(), 'Attention',
                            'Attention, the password entered is incorrect!')
        return

    os.remove(file_path)

    QMessageBox.about(Wydbid.app.parent(), 'Completed',
                      'The employee has been deleted!')

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
