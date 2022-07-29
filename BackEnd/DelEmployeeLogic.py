from PyQt5.QtWidgets import QWidget, QMessageBox
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
import Wydbid
from Data.DataCombi import *

def delEmployeeFinal(username: str, password: str, widget: QWidget):
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

    if not password == employee.password:
        QMessageBox.warning(Wydbid.app.parent(), 'Attention',
                            'Attention, the password entered is incorrect!')
        return

    session.delete(employee)
    session.commit()

    QMessageBox.about(Wydbid.app.parent(), 'Completed',
                      'The employee has been deleted!')
