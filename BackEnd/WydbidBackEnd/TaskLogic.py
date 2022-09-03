from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from Data.DataCombi import *
import Wydbid

# ToDo: Del task too, when del employee (receiver, author)

def createTask(author_username: str, receiver_username: str, title: str, description: str, deadline, widget):
    engine = create_engine(f'sqlite:///{Wydbid.company_location}database.db')
    _session = sessionmaker()
    session = _session(bind=engine)

    base.metadata.create_all(engine)

    if not author_username.split():
        QMessageBox.about(widget, 'Warning',
                          'Something went wrong!')
        return

    if not receiver_username.split() or not title.split():
        QMessageBox.warning(widget, 'Warning',
                            'All mandatory fields (*) must be filled in.')
        return

    author = session.query(Employee).filter(Employee.username == author_username).first()
    receiver = session.query(Employee).filter(Employee.username == receiver_username).first()

    if not author:
        QMessageBox.about(widget, 'Warning',
                          'Something went wrong!')
        return

    if not receiver:
        QMessageBox.warning(widget, 'Warning',
                            'A employee with this username does not exist.')
        return

    deadline = deadline.date().toString('dd.MM.yyyy')

    task = Task(author_username, receiver_username, title, description, deadline)

    session.add(task)
    session.commit()

    QMessageBox.about(widget, 'Completed',
                      f'{title} was created.')

    widget.clear()
    widget.hide()