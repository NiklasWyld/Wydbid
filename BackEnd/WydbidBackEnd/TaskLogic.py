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

def getNameOfEmployee(username: str):
    engine = create_engine(f'sqlite:///{Wydbid.company_location}database.db')
    _session = sessionmaker()
    session = _session(bind=engine)

    base.metadata.create_all(engine)

    employee = session.query(Employee).filter(Employee.username == username).first()
    name = employee.name

    return name

def appendTasks(list: QTableWidget):
    engine = create_engine(f'sqlite:///{Wydbid.company_location}database.db')
    _session = sessionmaker()
    session = _session(bind=engine)

    base.metadata.create_all(engine)

    tasks = session.query(Task).all()

    list.setSortingEnabled(False)
    list.clear()
    list.clearContents()
    list.setColumnCount(0)
    list.setRowCount(0)

    list.setColumnCount(6)
    list.setHorizontalHeaderLabels(
        ['Title', 'Author', 'Receiver', 'Deadline', 'Done', '']
    )
    list.setColumnWidth(0, 200)
    list.setColumnWidth(1, 200)
    list.setColumnWidth(2, 200)
    list.setColumnWidth(3, 200)
    list.setColumnWidth(4, 100)
    list.setColumnWidth(5, 40)

    tasks.sort(key=lambda x: x.deadline, reverse=False)

    list.setRowCount(len(tasks))

    i = 0

    for task in tasks:
        title = QTableWidgetItem()
        title.setText(task.title)

        author = QTableWidgetItem()
        author_name = getNameOfEmployee(task.author_username)
        author.setText(author_name)

        receiver = QTableWidgetItem()
        receiver_name = getNameOfEmployee(task.receiver_username)
        receiver.setText(receiver_name)

        deadline = QTableWidgetItem()
        deadline.setText(task.deadline)

        done = QTableWidgetItem()

        if task.done == 0 or False:
            done.setText('No')
        else:
            done.setText('Yes')

        view = QTableWidgetItem()
        view.setData(Qt.UserRole, task.id)
        view.setText('🔎')
        view.setTextAlignment(Qt.AlignCenter)

        list.setItem(i, 0, title)
        list.setItem(i, 1, author)
        list.setItem(i, 2, receiver)
        list.setItem(i, 3, deadline)
        list.setItem(i, 4, done)
        list.setItem(i, 5, view)
        i = i + 1

    list.verticalHeader().setVisible(False)
    list.setFocusPolicy(Qt.NoFocus)
    list.setSelectionMode(QAbstractItemView.SelectionMode.NoSelection)
    list.setEditTriggers(QAbstractItemView.NoEditTriggers)
    list.setSortingEnabled(True)

def setTaskForShow(task_id: int, widget):
    engine = create_engine(f'sqlite:///{Wydbid.company_location}database.db')
    _session = sessionmaker()
    session = _session(bind=engine)

    base.metadata.create_all(engine)

    task = session.query(Task).filter(Task.id == task_id).first()

    if not task:
        QMessageBox.warning(widget, 'Error', 'An error has occurred')
        return

    year = int(task.deadline.split('.')[2])
    month = int(task.deadline.split('.')[1])
    day = int(task.deadline.split('.')[0])

    widget.task = task
    widget.author.setText(task.author_username)
    widget.receiver.setText(task.receiver_username)
    widget.title.setText(task.title)
    widget.description.setText(task.description)
    widget.deadline.setDate(QDate(year, month, day))
    widget.done.setChecked(bool(task.done))

def editTaskDone(task_id: int, done: QCheckBox, widget):
    engine = create_engine(f'sqlite:///{Wydbid.company_location}database.db')
    _session = sessionmaker()
    session = _session(bind=engine)

    base.metadata.create_all(engine)

    done = done.isChecked()

    session.query(Task).filter(Task.id == task_id).update(
        {
            Task.done: done
        }
    )

    session.commit()
    QMessageBox.about(widget, 'Successfully changed', f'Task done -> {str(done)}')

def delTask(task_id: int, widget):
    engine = create_engine(f'sqlite:///{Wydbid.company_location}database.db')
    _session = sessionmaker()
    session = _session(bind=engine)

    base.metadata.create_all(engine)

    task = session.query(Task).filter(Task.id == task_id).first()

    if not task:
        QMessageBox.warning(widget, 'Error', 'An error has occurred')
        return

    m = QMessageBox.question(widget,
                             'Confirm deletion',
                             f'Attention, do you really want to delete {task.title}?',
                             QMessageBox.Yes,
                             QMessageBox.No)

    if m == QMessageBox.No:
        QMessageBox.about(widget, 'Cancelled',
                          'The order has not been deleted.')
        return

    session.delete(task)
    session.commit()

    QMessageBox.about(widget, 'Completed',
                      'The task has been deleted!')

    widget.clear()
    widget.hide()

def setTaskForEdit(task_id: int, widget):
    engine = create_engine(f'sqlite:///{Wydbid.company_location}database.db')
    _session = sessionmaker()
    session = _session(bind=engine)

    base.metadata.create_all(engine)

    task = session.query(Task).filter(Task.id == task_id).first()

    if not task:
        QMessageBox.warning(widget, 'Error', 'An error has occurred')
        return

    year = int(task.deadline.split('.')[2])
    month = int(task.deadline.split('.')[1])
    day = int(task.deadline.split('.')[0])

    widget.author.setText(task.author_username)
    widget.receiver.setText(task.receiver_username)
    widget.title.setText(task.title)
    widget.description.setText(task.description)
    widget.deadline.setDate(QDate(year, month, day))