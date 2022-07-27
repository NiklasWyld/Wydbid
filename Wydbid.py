import shutil
import sys
import os
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import *
from CustomQt import MessageBox
from UI.Login import CompanyLogin
from UI.WydbidUI.Prefabs import Settings
from BackEnd.WydbidBackEnd import SettingsLogic

location = './WydbidData/'
# Must be set at login
company_location = ''
company = None
employee = None

app = QApplication(sys.argv)

# Variables that are set during runtime
company_login = None
employee_login = None
wydbidui = None


def reset():
    m = QMessageBox.question(app.parent(),
                             'Sure?',
                             'Are you sure you want to reset Wydbid? Attention, because all data will be deleted!',
                             QMessageBox.Yes,
                             QMessageBox.No)

    if m == QMessageBox.No:
        QMessageBox.about(app.parent(), 'Info', 'Wydbid has not been reset!')
        return

    elif m == QMessageBox.Yes:
        p = MessageBox.MessageBox(parent=app.parent(
        ), title='Info', text='Wydbid will now reset. Please confirm to continue!')
        p.setIcon(QMessageBox.Warning)
        p.setDefaultButton(QMessageBox.StandardButton.Ok)
        p.exec_()

        shutil.rmtree(location, ignore_errors=True)

        q = MessageBox.MessageBox(parent=app.parent(
        ), title='Info', text='Wydbid has been successfully reset. The programme will now be terminated!')
        q.setIcon(QMessageBox.Warning)
        q.setDefaultButton(QMessageBox.StandardButton.Ok)
        q.exec_()

        app.exit(0)


def close():
    app.exit(0)


def buildLocation():
    if not os.path.exists(location):
        os.makedirs(location)

    if not os.path.exists(f'{location}Companies'):
        os.makedirs(f'{location}Companies')

    if not os.path.exists(f'{location}IMPORTANT.txt'):
        with open(f'{location}IMPORTANT.txt', 'w') as f:
            f.write('Attention!\n'
                    'Do not delete or move this folder under any conditions! Otherwise, data such as companies, employees, customers, ... will no longer work!\n'
                    'Only delete files or folders from this folders if you know exactly what you want and what you are doing!')
    # ...


if __name__ == '__main__':
    buildLocation()

    # Set icon for all widgets
    app.setWindowIcon(QIcon('./Assets/Icon.jpeg'))

    with open('./Assets/stylesheet', 'r') as f:
        app.setStyleSheet(f.read())

    SettingsLogic.loadSettings()

    company_login = CompanyLogin.CompanyLogin()
    company_login.showMaximized()

    sys.exit(app.exec_())
