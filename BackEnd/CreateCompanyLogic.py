import pickle
import sys
from PyQt5.QtWidgets import QMessageBox, QWidget
from UI.Login.Prefabs import CreateCompany
from Data import Company
import os
import Wydbid


def writeCompany(id: int, name: str, password: str, widget: QWidget):
    location = Wydbid.location

    if os.path.exists(f'{location}Companies/{str(id)}/'):
        QMessageBox.warning(Wydbid.app.parent(), 'Attention',
                            'A company with this ID already exists!')
        return

    os.makedirs(f'{location}Companies/{str(id)}/')
    company_file = open(f'{location}Companies/{str(id)}/{str(id)}.wbf', 'wb')
    company = Company.Company(id, name, password)

    pickle.dump(company, company_file, pickle.HIGHEST_PROTOCOL)

    QMessageBox.about(Wydbid.app.parent(), 'Completed',
                      f'{name} was created.')

    m = QMessageBox.question(Wydbid.app.parent(),
                             'Restart Wydbid',
                             'Attention, to log in to the new company, you must first restart the programme! Do you want to restart Wydbid?',
                             QMessageBox.Yes,
                             QMessageBox.No)

    if m == QMessageBox.No:
        widget.close()
        return

    elif m == QMessageBox.Yes:
        Wydbid.app.exit(0)


def getFirma(id: str, name: str, password: str, widget: QWidget):
    if id == '' or name == '' or password == '':
        QMessageBox.warning(Wydbid.app.parent(), 'Warning',
                            'All fields must be filled in!')
        return

    try:
        id = int(id)
    except:
        QMessageBox.warning(Wydbid.app.parent(
        ), 'Warning', 'A number must be entered in the company ID field!')
        CreateCompany.CreateCompany().clear(clearOnlyId=True)
        return

    writeCompany(id, name, password, widget)
