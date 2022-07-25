import shutil
import sys
import os
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import *
from CustomQt import MessageBox
from UI.Login import CompanyLogin
from UI.WydbidUI.Prefabs import Settings
from BackEnd.WydbidBackEnd import SettingsLogic

location = './Daten/'
# Must be set at login
firmen_location = ''
firma = None
mitarbeiter = None

app = QApplication(sys.argv)

# Variables that are set during runtime
firmen_login = None
mitarbeiter_login = None
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
        p = MessageBox.MessageBox(parent=app.parent(), title='Info', text='Wydbid will now reset. Please confirm to continue!')
        p.setIcon(QMessageBox.Warning)
        p.setDefaultButton(QMessageBox.StandardButton.Ok)
        p.exec_()

        shutil.rmtree(location, ignore_errors=True)

        q = MessageBox.MessageBox(parent=app.parent(), title='Info', text='Wydbid has been successfully reset. The programme will now be terminated!')
        q.setIcon(QMessageBox.Warning)
        q.setDefaultButton(QMessageBox.StandardButton.Ok)
        q.exec_()

        app.exit(0)

def close():
    app.exit(0)

def buildLocation():
    if os.path.exists(location): pass
    else: os.makedirs(location)

    if os.path.exists(f'{location}Firmen'): pass
    else: os.makedirs(f'{location}Firmen')

    if os.path.exists(f'{location}WICHTIG.txt'): pass
    else: open(f'{location}WICHTIG.txt', 'w').write('Achtung!\n'
                                                   'Loeschen oder verschieben Sie diesen Ordner auf keinen Fall! Sonst werden Daten, wie Firmen, Mitarbeiter, Kunden, ... nicht mehr funktionieren!\n'
                                                   'Loeschen Sie Datein oder Ordner aus diesen Ordner nur, wenn Sie genau wissen, was Sie wollen und was Sie tun!')

    # ...

if __name__ == '__main__':
    buildLocation()

    # Set icon for all widgets
    app.setWindowIcon(QIcon('./Assets/Icon.jpeg'))

    stylesheet = open('./Assets/stylesheet', 'r').read()

    app.setStyleSheet(stylesheet)

    SettingsLogic.loadSettings()

    firmen_login = CompanyLogin.CompanyLogin()
    firmen_login.showMaximized()

    sys.exit(app.exec_())