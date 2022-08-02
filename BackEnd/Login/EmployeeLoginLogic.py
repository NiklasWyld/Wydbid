from PyQt5.QtWidgets import QWidget, QMessageBox
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from UI.Login import CompanyLogin, EmployeeLogin
from UI.WydbidUI import WydbidUIMain
from Data.DataCombi import *
import Wydbid

def logoutCompany(employee_login_widget: EmployeeLogin):
    Wydbid.company = None
    Wydbid.company_location = ''

    employee_login_widget.clear()
    employee_login_widget.hide()

    # Loop through all widgets to get the company login widget to show it and clear the text fields
    for i in Wydbid.app.allWidgets():
        if type(i) == CompanyLogin.CompanyLogin:
            i.password.setText('')
            i.showMaximized()


def login(username: str, password: str, widget: QWidget):
    if username == '' or password == '':
        QMessageBox.warning(Wydbid.app.parent(), 'Warning',
                            'All fields must be filled in!')
        return

    engine = create_engine(f'sqlite:///{Wydbid.company_location}database.db')
    _session = sessionmaker()
    session = _session(bind=engine)

    base.metadata.create_all(engine)

    employee = session.query(Employee).filter(Employee.username == username).first()

    if not employee:
        QMessageBox.warning(Wydbid.app.parent(), 'Attention',
                            'Attention, the username or employee you entered does not exist.')
        return

    if not employee.password == password:
        QMessageBox.warning(Wydbid.app.parent(), 'Attention',
                            'Attention, the password entered is incorrect!')
        return

    Wydbid.employee = employee

    session.commit()

    widget.hide()

    wydbidui = WydbidUIMain.WydbidUIMain()
    wydbidui.setWindowTitle(
        f'Wydbid - Center | {Wydbid.company.name} | {employee.name}')
    wydbidui.showMaximized()

    Wydbid.wydbidui = wydbidui
