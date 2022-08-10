from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from Data.DataCombi import *
import Wydbid

def appendAppointments(date_: str, calendar: QCalendarWidget, list: QTableWidget):
    engine = create_engine(f'sqlite:///{Wydbid.company_location}database.db')
    _session = sessionmaker()
    session = _session(bind=engine)

    base.metadata.create_all(engine)

    appointments = session.query(Appointment).filter(Appointment.date == date_).all()

    list.setSortingEnabled(False)
    list.clear()
    list.clearContents()
    list.setColumnCount(0)
    list.setRowCount(0)

    list.setColumnCount(7)
    list.setHorizontalHeaderLabels(
        ['Title', 'Date', 'Time', 'Customer', 'Appeared', 'Closed', '']
    )
    list.setColumnWidth(0, 200)
    list.setColumnWidth(1, 150)
    list.setColumnWidth(2, 150)
    list.setColumnWidth(3, 200)
    list.setColumnWidth(4, 100)
    list.setColumnWidth(5, 100)
    list.setColumnWidth(6, 40)

    appointments.sort(key=lambda x: x.time, reverse=False)

    list.setRowCount(len(appointments))
    
    i = 0
    
    for appointment in appointments:
        title = QTableWidgetItem()
        title.setText(appointment.title)

        date = QTableWidgetItem()
        date.setText(appointment.date)

        time = QTableWidgetItem()
        time.setText(appointment.time)
        
        _customer_f_i_c = session.query(Customer).filter(Customer.id == appointment.customer_id).first()
        customer_name = f'{_customer_f_i_c.firstname} {_customer_f_i_c.lastname}'
        
        customer = QTableWidgetItem()
        customer.setText(customer_name)
        
        appeared = QTableWidgetItem()

        if appointment.appeared == 0 or False:
            appeared.setText('No')
        else:
            appeared.setText('Yes')

        closed = QTableWidgetItem()

        if appointment.closed == 0 or False:
            closed.setText('No')
        else:
            closed.setText('Yes')

        view = QTableWidgetItem()
        view.setData(Qt.UserRole, appointment.id)
        view.setText('🔎')
        view.setTextAlignment(Qt.AlignCenter)

        list.setItem(i, 0, title)
        list.setItem(i, 1, date)
        list.setItem(i, 2, time)
        list.setItem(i, 3, customer)
        list.setItem(i, 4, appeared)
        list.setItem(i, 5, closed)
        list.setItem(i, 6, view)
        i = i + 1

    list.verticalHeader().setVisible(False)
    list.setFocusPolicy(Qt.NoFocus)
    list.setSelectionMode(QAbstractItemView.SelectionMode.NoSelection)
    list.setEditTriggers(QAbstractItemView.NoEditTriggers)
    list.setSortingEnabled(True)
            
def appendCustomer(box):
    engine = create_engine(f'sqlite:///{Wydbid.company_location}database.db')
    _session = sessionmaker()
    session = _session(bind=engine)

    base.metadata.create_all(engine)

    customers = session.query(Customer).all()

    customers.sort(key=lambda x: x.id)

    for customer in customers:
        name = customer.firstname + ' ' + customer.lastname
        box.addItem(name, customer.id)

def createAppointment(date, time, title, description, customer_id, widget):
    if not title.strip() or not description.strip() or not customer_id:
        QMessageBox.warning(widget, 'Warning',
                            'All fields must be filled in!')
        return

    engine = create_engine(f'sqlite:///{Wydbid.company_location}database.db')
    _session = sessionmaker()
    session = _session(bind=engine)
    base.metadata.create_all(engine)

    date = date.toString('dd.MM.yyyy')
    time = time.toString('hh:mm')

    appointment = Appointment(title=title, description=description, date=date, time=time,
                              customer_id=customer_id)

    session.add(appointment)
    session.commit()

    QMessageBox.about(widget, 'Completed',
                      f'{title} was created.')

    widget.clear()
    widget.hide()
    Wydbid.wydbidui.startAppendAppointments()

def editAppointment(id, date, time, title, description, customer_id, widget):
    if not title.strip() or not description.strip() or not customer_id:
        QMessageBox.warning(widget, 'Warning',
                            'All fields must be filled in!')
        return

    engine = create_engine(f'sqlite:///{Wydbid.company_location}database.db')
    _session = sessionmaker()
    session = _session(bind=engine)

    base.metadata.create_all(engine)

    date = date.toString('dd.MM.yyyy')
    time = time.toString('hh:mm')

    session.query(Appointment).filter(Appointment.id == id).update(
        {
            Appointment.date: date,
            Appointment.time: time,
            Appointment.title: title,
            Appointment.description: description,
            Appointment.customer_id: customer_id
        }
    )

    session.commit()

    QMessageBox.about(widget, 'Completed',
                      f'{title} was edited.')

    widget.clear()
    widget.hide()
    Wydbid.wydbidui.startAppendAppointments()

def appendAppointmentsForGet(date: str, list: QListWidget, widget):
    engine = create_engine(f'sqlite:///{Wydbid.company_location}database.db')
    _session = sessionmaker()
    session = _session(bind=engine)

    base.metadata.create_all(engine)

    appointments = session.query(Appointment).filter(Appointment.date == date).all()

    for appointment in appointments:
        item = QListWidgetItem(parent=list)
        item.setData(Qt.UserRole, appointment.id)
        item.setText(f'{appointment.title} - {appointment.date}')

        list.addItem(item)

    session.commit()

def setAppointmentForEdit(appointment_id, widget):
    engine = create_engine(f'sqlite:///{Wydbid.company_location}database.db')
    _session = sessionmaker()
    session = _session(bind=engine)

    base.metadata.create_all(engine)

    appointment = session.query(Appointment).filter(Appointment.id == appointment_id).first()

    year = int(appointment.date.split('.')[2])
    month = int(appointment.date.split('.')[1])
    day = int(appointment.date.split('.')[0])

    hour = int(appointment.time.split(':')[0])
    minute = int(appointment.time.split(':')[1])

    widget.dateedit.setDate(QDate(year, month, day))
    widget.timeedit.setTime(QTime(hour, minute))
    widget.title.setText(appointment.title)
    widget.description.setText(appointment.description)
    widget.customer.clear()
    appendCustomer(widget.customer)

    widget.customer.setCurrentIndex(appointment.customer_id - 1)

    if not appointment.customer_id-1 < 0:
        widget.customer.setCurrentIndex(appointment.customer_id)

    session.commit()