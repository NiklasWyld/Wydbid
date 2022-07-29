from PyQt5.QtWidgets import QWidget, QMessageBox
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
import Wydbid
from Data import DataCombi

def delEmployeeFinal(username: str, password: str, widget: QWidget):
    if username == '' or password == '':
        QMessageBox.warning(Wydbid.app.parent(), 'Warning',
                            'All fields must be filled in!')
        return

    engine = create_engine(f'sqlite:///{Wydbid.company_location}database.db')
    _session = sessionmaker()
    base = declarative_base()
    session = _session(bind=engine)

    class BaseEmployee(DataCombi.Employee, base): pass
    print(username)
    employee = session.query(BaseEmployee).filter(BaseEmployee.username == username).first()
    print(employee)

    return

    if not password == employee.password:
        QMessageBox.warning(Wydbid.app.parent(), 'Attention',
                            'Attention, the password entered is incorrect!')
        return

    QMessageBox.about(Wydbid.app.parent(), 'Completed',
                      'The employee has been deleted!')
