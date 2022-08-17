from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *
from sqlalchemy.orm import sessionmaker
from Data.DataCombi import *
import Wydbid

def appendEvents(list: QTableWidget):
    engine = create_engine(f'sqlite:///{Wydbid.company_location}database.db')
    _session = sessionmaker()
    session = _session(bind=engine)

    base.metadata.create_all(engine)

    events = session.query(Event).all()

    list.setSortingEnabled(False)
    list.clear()
    list.clearContents()
    list.setColumnCount(0)
    list.setRowCount(0)

    list.setColumnCount(4)
    list.setHorizontalHeaderLabels(
        ['Title', 'Date', 'Time', '']
    )
    list.setColumnWidth(0, 200)
    list.setColumnWidth(1, 200)
    list.setColumnWidth(2, 200)
    list.setColumnWidth(3, 40)

    events.sort(key=lambda x: x.date, reverse=False)

    list.setRowCount(len(events))

    i = 0

    for event in events:
        title = QTableWidgetItem()
        title.setText(event.title)

        date = QTableWidgetItem()
        date.setText(event.date)

        time = QTableWidgetItem()
        time.setText(event.time)

        view = QTableWidgetItem()
        view.setData(Qt.UserRole, event.id)
        view.setText('🔎')
        view.setTextAlignment(Qt.AlignCenter)

        list.setItem(i, 0, title)
        list.setItem(i, 1, date)
        list.setItem(i, 2, time)
        list.setItem(i, 3, view)
        i = i + 1

    list.verticalHeader().setVisible(False)
    list.setFocusPolicy(Qt.NoFocus)
    list.setSelectionMode(QAbstractItemView.SelectionMode.NoSelection)
    list.setEditTriggers(QAbstractItemView.NoEditTriggers)
    list.setSortingEnabled(True)

def createEvent(title: str, description: str, date, time, widget):
    engine = create_engine(f'sqlite:///{Wydbid.company_location}database.db')
    _session = sessionmaker()
    session = _session(bind=engine)

    base.metadata.create_all(engine)

    if not title.strip():
        QMessageBox.warning(widget, 'Warning',
                            'All fields must be filled in!')
        return

    date = date.toString('dd.MM.yyyy')
    time = time.toString('hh:mm')

    event = Event(title, description, date, time)

    session.add(event)
    session.commit()

    QMessageBox.about(widget, 'Completed',
                      f'{title} was created.')

    widget.clear()
    widget.hide()