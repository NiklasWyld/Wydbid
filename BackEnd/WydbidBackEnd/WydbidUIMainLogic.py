from PyQt5.QtWidgets import QWidget, QMessageBox
import Wydbid
from CustomQt import MessageBox
from UI.Login import FirmenLogin, MitarbeiterLogin
from UI.WydbidUI.Prefabs.Kunde import CreateKunde

def logoutCompany(widget: QWidget):
    Wydbid.firma = None
    Wydbid.firmen_location = ''

    widget.hide()

    # Loop through all widgets to get the company login widget to show it and clear the text fields
    for i in Wydbid.app.allWidgets():
        if type(i) == FirmenLogin.FirmenLogin:
            i.passwort.setText('')
            i.showMaximized()

def logoutMitarbeiter(widget: QWidget):
    Wydbid.mitarbeiter = None

    widget.hide()

    # Loop through all widgets to get the company login widget to show it and clear the text fields
    for i in Wydbid.app.allWidgets():
        if type(i) == MitarbeiterLogin.MitarbeiterLogin:
            i.passwort.setText('')
            i.showMaximized()

def contact():
    p = MessageBox.MessageBox(parent=Wydbid.app.parent(), title='Kontakt', text='Bei einem einfachen Fehler kontaktieren Sie bitte den Administrator\n'
                                                                            'Bei einem Softtware-Fehler in Wydbid kontaktieren Sie bitte den Softwareersteller per E-Mail: niklasch1999@gmail.com')
    p.setIcon(QMessageBox.Warning)
    p.setDefaultButton(QMessageBox.StandardButton.Ok)
    p.exec_()