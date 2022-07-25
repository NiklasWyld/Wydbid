import shutil
import sys
import os
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import *
from CustomQt import MessageBox
from UI.Login import FirmenLogin
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
                             'Sicher?',
                             'Bist du sicher, dass du Wydbid zurückstetzen möchtest? Achtung, denn es werden alle Daten gelöscht!',
                             QMessageBox.Yes,
                             QMessageBox.No)

    if m == QMessageBox.No:
        QMessageBox.about(app.parent(), 'Info',
                          'Wydbid wurde nicht zurückgesetzt!')
        return

    elif m == QMessageBox.Yes:
        p = MessageBox.MessageBox(parent=app.parent(
        ), title='Info', text='Wydbid wird jetzt zurückgesetzt. Bitte bestätigen Sie um fortzufahren!')
        p.setIcon(QMessageBox.Warning)
        p.setDefaultButton(QMessageBox.StandardButton.Ok)
        p.exec_()

        shutil.rmtree(location, ignore_errors=True)

        q = MessageBox.MessageBox(parent=app.parent(
        ), title='Info', text='Wydbid wurde erfolgreich zurückgesetzt. Das Programm wird jetzt beendet!')
        q.setIcon(QMessageBox.Warning)
        q.setDefaultButton(QMessageBox.StandardButton.Ok)
        q.exec_()

        app.exit(0)


def close():
    app.exit(0)


def buildLocation():
    if not os.path.exists(location):
        os.makedirs(location)

    if not os.path.exists(f'{location}Firmen'):
        os.makedirs(f'{location}Firmen')

    if not os.path.exists(f'{location}README.txt'):
        open(f'{location}README.txt', 'w').write('Achtung!\n'
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

    firmen_login = FirmenLogin.FirmenLogin()
    firmen_login.showMaximized()

    sys.exit(app.exec_())
