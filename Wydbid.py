import subprocess
import threading
import requests
import shutil
import sys
import os
import git
from PyQt5 import QtTest
from PyQt5.QtCore import QTimer, Qt
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import *
from CustomQt import MessageBox
from UI.Login import CompanyLogin, LoadingScreen
from UI.WydbidUI import WydbidUIMain
from sqlalchemy.orm import sessionmaker
from UI.WydbidUI.Prefabs import Settings
from BackEnd.WydbidBackEnd import SettingsLogic, WydbidUIMainLogic

location = './WydbidData/'
# Must be set at login
company_location = ''
company = None
employee = None

WYDBID_VERSION = 'V0.24'
# ToDo: On merch in main branch dev -> main
GITHUB_VERSION_SOURCE = 'https://raw.githubusercontent.com/NiklasWyld/Wydbid/main/version.txt'

app = QApplication(sys.argv)

# Variables that are set during runtime
company_login = None
employee_login = None
wydbidui = None


def finalUpdate():
    c = git.cmd.Git(os.getcwd())
    c.pull()


class Update():
    def __init__(self):
        super(Update, self).__init__()
        self.show_if_uptodate = True

    def getVersion(self):
        try:
            respone = requests.get(GITHUB_VERSION_SOURCE)
            r_codes = range(200, 299)

            if respone.status_code in r_codes:
                version = respone.text.strip()

                if version == WYDBID_VERSION:
                    return False
                else:
                    return True
            else:
                return 0
        except:
            return 0

    def checkVersion(self):
        # True = Get answer and there is a never version
        # False = Get answer and Wydbid is on the latest version
        # 0 = Get no answer / No connection

        answer = self.getVersion()

        if answer: # (answer = True)
            update = QMessageBox.question(app.parent(),
                                          'Update available!', 'An update for Wydbid is available. Do you want to install it?',
                                           QMessageBox.Yes, QMessageBox.No)

            if update == QMessageBox.Yes:
                thread = threading.Thread(target=finalUpdate)
                thread.setDaemon(True)
                thread.start()
                QMessageBox.about(app.parent(), 'Updated',
                                  'Wydbid has been updated! Click to restart.')
                app.exit(0)
            else:
                QMessageBox.about(app.parent(), 'Cancled',
                                  'Wydbid will not be updated, but you can update it at any time by checking for an update via the "Check for update" menu item.')

        elif not answer: # (answer = False)
            if self.show_if_uptodate:
                QMessageBox.about(app.parent(), 'Up to date',
                                  'Wydbid is up to date!')
        elif answer == 0:
            if self.show_if_uptodate:
                QMessageBox.about(app.parent(), 'Update Failed',
                                  'Something went wrong. Make sure you\'re connected to the internet and try again.')


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
    sessionmaker.close_all()
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
    i = 0
    for procent in range(20):
        i = i + 5
        loading_screen.progresss_bar.setValue(i)
        QtTest.QTest.qWait(30)

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
