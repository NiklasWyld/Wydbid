import os
import pickle
from PyQt5.QtCore import Qt, QModelIndex
from Data import Kunde
from PyQt5.QtWidgets import QWidget, QMessageBox, QTableWidget, QTableWidgetItem, QLineEdit
import Wydbid
from CustomQt import MessageBox
from UI.Login import FirmenLogin, MitarbeiterLogin


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
    kundenliste.setHorizontalHeaderLabels(
        ['Name', 'Nummer', 'Geburtsdatum', ''])
    kundenliste.setColumnWidth(0, 200)
    kundenliste.setColumnWidth(1, 200)
    kundenliste.setColumnWidth(2, 200)

    kunden = []
    dateien = os.listdir(f'{Wydbid.firmen_location}Kunden/')

    for datei in dateien:
        kunde: Kunde.Kunde = pickle.load(
            open(f'{Wydbid.firmen_location}Kunden/{datei}/{datei}.wbk', 'rb'))
        kunden.append(kunde)

    kunden.sort(key=lambda x: x.nachname)

    kundenliste.setRowCount(len(kunden))

    for i, kunde in enumerate(kunden):
        kundenliste.setItem(i, 0, QTableWidgetItem(
            f'{kunde.vorname} {kunde.nachname}'))

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


def searchForName(search: QLineEdit, list: QTableWidget):
    name = search.text().lower()
    for row in range(list.rowCount()):
        item = list.item(row, 0)

        # if the search is not in the item's text do not hide the row
        list.setRowHidden(row, name not in item.text().lower())


def contact():
    p = MessageBox.MessageBox(parent=Wydbid.app.parent(),
                              title='Kontakt',
                              text='Bei einem einfachen Fehler kontaktieren Sie bitte den Administrator\n'
                              'Bei einem Softtware-Fehler in Wydbid kontaktieren Sie bitte den Softwareersteller per E-Mail: niklasch1999@gmail.com'
                              )
    p.setIcon(QMessageBox.Warning)
    p.setDefaultButton(QMessageBox.StandardButton.Ok)
    p.exec_()
