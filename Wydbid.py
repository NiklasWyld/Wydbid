import base64
import requests
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
from UI.WydbidUI import WydbidUIMain
from sqlalchemy.orm import sessionmaker
from UI.WydbidUI.Prefabs import Settings
from BackEnd.WydbidBackEnd import SettingsLogic, WydbidUIMainLogic

location = './WydbidData/'
# Must be set at login
company_location = ''
company = None
employee = None
wydbid_version = 'Beta 2.0'
github_version_source = 'https://api.github.com/repos/NiklasWyld/Wydbid/contents/version.txt'
download_source = ""

app = QApplication(sys.argv)

# Variables that are set during runtime
company_login = None
employee_login = None
wydbidui = None

class Update():
    def __init__(self):
        super(Update, self).__init__()

    def getVersion(self):
        try:
            req = requests.get(github_version_source)
            if req.status_code == requests.codes.ok:
                req = req.json()  # the response is a JSON
                # req is now a dict with keys: name, encoding, url, size ...
                # and content. But it is encoded with base64.
                content = base64.b64decode(req['content'])
                split = str(content).split("'")[1]
                version = split.split("\\")[0]
                return version

            else:
                return "Failed"

        except:
            return "Failed"

    def check_version(self):
        version = self.getVersion()

        if version == "Failed":
            return "Failed"

        else:
            if wydbid_version == version:
                return "Uptodate"

            else:
                return "NotUptodate"




    def start(self):
        version_check = self.check_version()
        if version_check == "Failed":
            failed_info = QMessageBox.question(WydbidUIMain.WydbidUIMain(), "Update Failed!", "Something went wrong. Make sure you're connected to the internet and try again.", QMessageBox.Ok)


        if version_check == "Uptodate":
            info = QMessageBox.question(WydbidUIMain.WydbidUIMain(), "Up to date!", "Wydbid is up to date and no updates needed!", QMessageBox.Ok)


        if version_check == "NotUptodate":
            update_info = QMessageBox.question(WydbidUIMain.WydbidUIMain(), "Update available!", "An update for Wydbid is available. Do you want to install it?", QMessageBox.Yes, QMessageBox.No)

            if update_info == QMessageBox.Yes:
                pass

            else:
                pass


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