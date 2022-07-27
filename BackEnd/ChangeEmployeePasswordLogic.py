import os
import pickle
import sys
from PyQt5.QtWidgets import QMessageBox, QWidget
import Wydbid
from Data import Employee


def changePasswordFinal(username: str, password: str, new_password: str, widget: QWidget):
    if username == '' or password == '' or new_password == '':
        QMessageBox.warning(Wydbid.app.parent(), 'Warning',
                            'All fields must be filled in!')
        return

    if not os.path.exists(f'{Wydbid.company_location}Employees/{username}.wbm'):
        QMessageBox.warning(Wydbid.app.parent(
        ), 'Attention', 'The user name or employee you entered does not exist.')
        return

    employee_file = open(
        f'{Wydbid.company_location}Employees/{username}.wbm', 'rb')
    employee: Employee.Employee = pickle.load(employee_file)
    employee_file.close()

    if not employee.password == password:
        QMessageBox.warning(Wydbid.app.parent(), 'Attention',
                            'Attention, the password entered is incorrect!')
        return

    employee_file_new = open(
        f'{Wydbid.company_location}Employees/{username}.wbm', 'wb')
    employee.password = new_password
    pickle.dump(employee, employee_file_new, pickle.HIGHEST_PROTOCOL)

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
