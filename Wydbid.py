import shutil
import sys
import os
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import *
from UI.Login import FirmenLogin
from CustomQt import MessageBox

location = './Daten/'
# Muss bei Login gesetzt werden
firmen_location = ''
app = QApplication(sys.argv)

def reset():
    m = QMessageBox.question(app.parent(),
                             'Sicher?',
                             'Bist du sicher, dass du Wydbid zurückstetzen möchtest? Achtung, denn es werden alle Daten gelöscht!',
                             QMessageBox.Yes,
                             QMessageBox.No)

    if m == QMessageBox.No:
        QMessageBox.about(app.parent(), 'Info', 'Wydbid wurde nicht zurückgesetzt!')
        return

    elif m == QMessageBox.Yes:
        p = MessageBox.MessageBox(parent=app.parent(), title='Info', text='Wydbid wird jetzt zurückgesetzt. Bitte bestätigen Sie um fortzufahren!')
        p.setIcon(QMessageBox.Warning)
        p.setDefaultButton(QMessageBox.StandardButton.Ok)
        p.exec_()

        shutil.rmtree(location, ignore_errors=True)

        q = MessageBox.MessageBox(parent=app.parent(), title='Info', text='Wydbid wurde erfolgreich zurückgesetzt. Das Programm wird jetzt beendet!')
        q.setIcon(QMessageBox.Warning)
        q.setDefaultButton(QMessageBox.StandardButton.Ok)
        q.exec_()

        exit()

def buildLocation():
    if os.path.exists(location): pass
    else: os.makedirs(location)

    if os.path.exists(f'{location}Firmen'): pass
    else: os.makedirs(f'{location}Firmen')
    # ...

def main():
    buildLocation()

    firmen_login = FirmenLogin.FirmenLogin()
    firmen_login.show()

    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
