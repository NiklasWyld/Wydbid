import shutil
import subprocess
import sys
import os
from PyQt5 import QtTest
from PyQt5.QtCore import QTimer, Qt
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import *
from CustomQt import MessageBox
from UI.Login import CompanyLogin, LoadingScreen
from sqlalchemy.orm import sessionmaker
from UI.WydbidUI.Prefabs import Settings
from BackEnd.WydbidBackEnd import SettingsLogic, WydbidUIMainLogic

# ToDo: Write wydbid start fail linux fix in readme: sudo ln -s /usr/lib/x86_64-linux-gnu/libxcb-util.so.1

location = './WydbidData/'
# Must be set at login
company_location = ''
company = None
employee = None
wydbid_version = 'Beta 1.0'

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
        p = MessageBox.MessageBox(parent=app.parent(),
                                  title='Info', text='Wydbid will now reset. Please confirm to continue!')
        p.setIcon(QMessageBox.Warning)
        p.setDefaultButton(QMessageBox.StandardButton.Ok)
        p.exec_()

        company = None
        company_location = ''

        for i in app.allWidgets():
            try:
                i.use_close_event = False
            except:
                i.close()
            i.close()

        sessionmaker.close_all()

        shutil.rmtree(location, ignore_errors=True)

        q = MessageBox.MessageBox(parent=app.parent(),
                                  title='Info', text='Wydbid has been successfully reset. The programme will now be terminated!')
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


def handleLoadingScreen(loading_screen, company_login):
    for procent in range(101):
        loading_screen.progresss_bar.setValue(procent + 1)
        QtTest.QTest.qWait(20)

    loading_screen.hide()
    company_login.showMaximized()


if __name__ == '__main__':
    # Make loading screen and show it
    loading_screen = LoadingScreen.LoadingScreen()
    loading_screen.show()

    buildLocation()

    # Set icon for all widgets
    app.setWindowIcon(QIcon('./Assets/Icon.jpeg'))

    with open('./Assets/stylesheet', 'r') as f:
        app.setStyleSheet(f.read())

    SettingsLogic.loadSettings()

    # Make company login
    company_login = CompanyLogin.CompanyLogin()

    # Start loading in loading screen
    handleLoadingScreen(loading_screen, company_login)

    # Set loading screen in foreground
    loading_screen.setWindowState(Qt.WindowActive)
    loading_screen.activateWindow()

    sys.exit(app.exec_())