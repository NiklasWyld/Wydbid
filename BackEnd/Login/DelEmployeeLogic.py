from PyQt5.QtWidgets import QWidget, QMessageBox
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from Data.DataCombi import *
import Wydbid

def delEmployeeLinks(username: str):
    engine = create_engine(f'sqlite:///{Wydbid.company_location}database.db')
    _session = sessionmaker()
    session = _session(bind=engine)

    base.metadata.create_all(engine)

    tasks_author = session.query(Task).filter(Task.author_username == username).all()
    tasks_receiver = session.query(Task).filter(Task.receiver_username == username).all()

    for task in tasks_author:
        session.delete(task)

    for task in tasks_receiver:
        session.delete(task)

    session.commit()

def delEmployeeFinal(username: str, password: str, widget):
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

    reply = QMessageBox.question(Wydbid.app.parent(), 'Are you sure?',
                                 f'Are you sure you want to delete {employee.name} and and all his links, such as tasks?',
                                 QMessageBox.Yes, QMessageBox.No)

    if reply == QMessageBox.Yes:
        delEmployeeLinks(employee.username)
        session.delete(employee)
        session.commit()

        QMessageBox.about(Wydbid.app.parent(), 'Completed',
                          'The employee has been deleted!')
    else:
        QMessageBox.about(Wydbid.app.parent(), 'Completed',
                          'The employee has not been deleted!')
        session.commit()

    widget.clear()
    widget.hide()
