from PyQt5.QtWidgets import QWidget
import Wydbid
from UI.Login import FirmenLogin

def logoutCompany(widget: QWidget):
    Wydbid.firma = None
    Wydbid.firmen_location = ''

    widget.hide()

    # Loop through all widgets to get the company login widget to show it and clear the text fields
    for i in Wydbid.app.allWidgets():
        if type(i) == FirmenLogin.FirmenLogin:
            i.passwort.setText('')
            i.showMaximized()