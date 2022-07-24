import os
import pickle
from PyQt5.QtWidgets import QWidget, QMessageBox
import Wydbid
from UI.Login import FirmenLogin, MitarbeiterLogin
from UI.WydbidUI import WydbidUIMain
from Data import Mitarbeiter

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

def login(username: str, password: str, widget: QWidget):
    if username == '':
        QMessageBox.warning(Wydbid.app.parent(), 'Warnung', 'Alle Felder muessen ausgefuellt werden!')
        return

    if password == '':
        QMessageBox.warning(Wydbid.app.parent(), 'Warnung', 'Alle Felder muessen ausgefuellt werden!')
        return

    if not os.path.exists(f'{Wydbid.firmen_location}Mitarbeiter/{username}.wbm'):
        QMessageBox.warning(Wydbid.app.parent(), 'Achtung', 'Ein Mitarbeiter mit diesen Nutzernamen existiert nicht!')
        return

    mitarbeiter_file = open(f'{Wydbid.firmen_location}Mitarbeiter/{username}.wbm', 'rb')
    mitarbeiter: Mitarbeiter.Mitarbeiter = pickle.load(mitarbeiter_file)
    if not mitarbeiter.passwort == password:
        QMessageBox.warning(Wydbid.app.parent(), 'Achtung', 'Achtung, das eingegebene Passwort ist falsch!')
        return
    elif mitarbeiter.passwort == password:
        Wydbid.mitarbeiter = mitarbeiter

        widget.hide()

        wydbidui = WydbidUIMain.WydbidUIMain()
        wydbidui.setWindowTitle(f'Wydbid - Center | {Wydbid.firma.name} | {mitarbeiter.name}')
        wydbidui.showMaximized()

        Wydbid.wydbidui = wydbidui