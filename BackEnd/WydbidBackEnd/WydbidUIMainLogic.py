import os
import pickle
from PyQt5.QtCore import Qt, QModelIndex
from Data import Kunde
from PyQt5.QtWidgets import QWidget, QMessageBox, QTableWidget, QTableWidgetItem
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

def appendKunden(kundenliste: QTableWidget):
    kundenliste.clear()

    kunden = []
    dateien = os.listdir(f'{Wydbid.firmen_location}Kunden/')

    for datei in dateien:
        kunde: Kunde.Kunde = pickle.load(open(f'{Wydbid.firmen_location}Kunden/{datei}/{datei}.wbk', 'rb'))
        kunden.append(kunde)

    kunden.sort(key=lambda x: x.nachname, reverse=False)

    kundenliste.setRowCount(len(kunden))

    i = 0

    for kunde in kunden:
        kundenliste.setItem(i, 0, QTableWidgetItem(f'{kunde.vorname} {kunde.nachname}'))

        number = QTableWidgetItem()
        number.setData(Qt.DisplayRole, kunde.nummer)

        old = QTableWidgetItem()
        old.setData(Qt.DisplayRole, kunde.geburtsdatum)

        ansicht = QTableWidgetItem()
        ansicht.setData(Qt.DisplayRole, '🔎')
        ansicht.setTextAlignment(Qt.AlignCenter)
        kundenliste.setColumnWidth(3, 40)

        kundenliste.setItem(i, 1, number)
        kundenliste.setItem(i, 2, old)
        kundenliste.setItem(i, 3, ansicht)
        i = i + 1

def contact():
    p = MessageBox.MessageBox(parent=Wydbid.app.parent(), title='Kontakt', text='Bei einem einfachen Fehler kontaktieren Sie bitte den Administrator\n'
                                                                            'Bei einem Softtware-Fehler in Wydbid kontaktieren Sie bitte den Softwareersteller per E-Mail: niklasch1999@gmail.com')
    p.setIcon(QMessageBox.Warning)
    p.setDefaultButton(QMessageBox.StandardButton.Ok)
    p.exec_()