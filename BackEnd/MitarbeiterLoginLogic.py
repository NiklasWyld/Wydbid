from PyQt5.QtWidgets import QWidget
from UI.Login import MitarbeiterLogin
import Wydbid
from UI.Login import FirmenLogin

def logoutCompany(mitarbeiter_login_widget: MitarbeiterLogin):
    Wydbid.firma = None
    Wydbid.firmen_location = ''

    mitarbeiter_login_widget.clear()
    mitarbeiter_login_widget.hide()

    # Loop through all widgets to get the company login widget to show it and clear the text fields
    for i in Wydbid.app.allWidgets():
        if type(i) == FirmenLogin.FirmenLogin:
            i.passwort.setText('')
            i.showMaximized()