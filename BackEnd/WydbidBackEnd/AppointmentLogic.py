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

def createAppointment(date, time, title, description, customer_id, widget):
    if not title.strip() or not description.strip() or not customer_id.strip():
        QMessageBox.warning(widget, 'Warning',
                            'All fields must be filled in!')
        return

    engine = create_engine(f'sqlite:///{Wydbid.company_location}database.db')
    _session = sessionmaker()
    session = _session(bind=engine)
    base.metadata.create_all(engine)

    date = date.toString('dd.MM.yyyy')
    time = time.toString('hh:mm')

    try: int(customer_id.strip())
    except:
        QMessageBox.warning(widget, 'Warning',
                            'Customer id must be an number.')
        return

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
    if not title.strip() or not description.strip() or not customer_id.strip():
        QMessageBox.warning(widget, 'Warning',
                            'All fields must be filled in!')
        return

    engine = create_engine(f'sqlite:///{Wydbid.company_location}database.db')
    _session = sessionmaker()
    session = _session(bind=engine)

    base.metadata.create_all(engine)

    try: int(customer_id.strip())
    except:
        QMessageBox.warning(widget, 'Attention', 'Customer id must be an number.')

    date = date.toString('dd.MM.yyyy')
    time = time.toString('hh:mm')

    session.query(Appointment).filter(Appointment.id == id).update(
        {
            Appointment.date: date,
            Appointment.time: time,
            Appointment.title: title,
            Appointment.description: description,
            Appointment.customer_id: int(customer_id.strip())
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
    widget.customer.setText(str(appointment.customer_id))

    session.commit()

def getCustomerForLabel(edit: QLineEdit, label: QLabel):
    id = edit.text().strip()

    if not id:
        label.setText('')
        return

    try: int(id)
    except:
        label.setText('The id must be an number.')
        return

    id = int(id)

    engine = create_engine(f'sqlite:///{Wydbid.company_location}database.db')
    _session = sessionmaker()
    session = _session(bind=engine)

    base.metadata.create_all(engine)

    customer = session.query(Customer).filter(Customer.id == id).first()

    if customer:
        label.setText(f'{customer.firstname} {customer.lastname}')
    else:
        label.setText('A customer with this id doesn\'n exists.')

def delAppointment(list: QListWidget, widget):
    engine = create_engine(f'sqlite:///{Wydbid.company_location}database.db')
    _session = sessionmaker()
    session = _session(bind=engine)

    base.metadata.create_all(engine)

    if not list.selectedItems():
        QMessageBox.warning(widget, 'Warning',
                            'No appointment selected!')
        return

    appointment_id = list.selectedItems()[0].data(Qt.UserRole)

    appointment = session.query(Appointment).filter(Appointment.id == appointment_id).first()

    reply = QMessageBox.question(widget, 'Are you sure?', f'Are you sure you want to delete {appointment.title}?',
                                 QMessageBox.Yes, QMessageBox.No)

    if reply == QMessageBox.No:
        QMessageBox.about(Wydbid.app.parent(), 'Cancled',
                          'The appointment has not been deleted!')
        session.commit()
        return

    session.delete(appointment)
    session.commit()

    QMessageBox.about(Wydbid.app.parent(), 'Completed',
                      'The appointment has been deleted!')

    widget.hide()
    Wydbid.wydbidui.startAppendAppointments()

def getAppointment(appointment_id: int):
    engine = create_engine(f'sqlite:///{Wydbid.company_location}database.db')
    _session = sessionmaker()
    session = _session(bind=engine)

    base.metadata.create_all(engine)

    appointment = session.query(Appointment).filter(Appointment.id == appointment_id).first()

    if not appointment:
        QMessageBox.warning(Wydbid.app.parent(), 'Error occurred', 'Something went wrong')
        return

    return appointment

def editAppointmentAppeared(appointment_id: int, appeared: QCheckBox, widget):
    engine = create_engine(f'sqlite:///{Wydbid.company_location}database.db')
    _session = sessionmaker()
    session = _session(bind=engine)

    base.metadata.create_all(engine)

    appeared = appeared.isChecked()

    session.query(Appointment).filter(Appointment.id == appointment_id).update(
        {
            Appointment.appeared: appeared
        }
    )

    session.commit()
    QMessageBox.about(widget, 'Successfully changed', f'Appointment appeared -> {str(appeared)}')
    Wydbid.wydbidui.startAppendAppointments()

def editAppointmentClosed(appointment_id: int, closed: QCheckBox, widget):
    engine = create_engine(f'sqlite:///{Wydbid.company_location}database.db')
    _session = sessionmaker()
    session = _session(bind=engine)

    base.metadata.create_all(engine)

    closed = closed.isChecked()

    session.query(Appointment).filter(Appointment.id == appointment_id).update(
        {
            Appointment.closed: closed
        }
    )

    session.commit()
    QMessageBox.about(widget, 'Successfully changed', f'Appointment closed -> {str(closed)}')
    Wydbid.wydbidui.startAppendAppointments()