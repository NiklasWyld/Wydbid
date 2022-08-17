from PyQt5.QtWidgets import QMessageBox
from sqlalchemy.orm import sessionmaker
from Data.DataCombi import *
import Wydbid

def changePasswordFinal(username: str, password: str, new_password: str, widget):
    if username == '' or password == '' or new_password == '':
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

    session.query(Employee).filter(Employee.username == username).update(
        {
            Employee.password: new_password
        }
    )

    session.commit()

    QMessageBox.about(Wydbid.app.parent(), 'Process completed',
                      f'The password of {username} has been successfully changed.')

    widget.clear()
    widget.hide()