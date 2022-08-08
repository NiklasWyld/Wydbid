import threading

from PyQt5.QtWidgets import QMessageBox
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from Data.DataCombi import *
import Wydbid

def appendCustomer(box):
    engine = create_engine(f'sqlite:///{Wydbid.company_location}database.db')
    _session = sessionmaker()
    session = _session(bind=engine)

    base.metadata.create_all(engine)

    customers = session.query(Customer).all()

    for customer in customers:
        name = customer.firstname + ' ' + customer.lastname
        box.addItem(name, customer.id)

def createAppointment(date, time, title, description, customer_id, widget):
    if not title.strip() or not description.strip() or not customer_id:
        QMessageBox.warning(widget, 'Warning',
                            'All fields must be filled in!')
        return

    print(date.toString('yyyy/MM/dd'))
    print(time.toString())

    engine = create_engine(f'sqlite:///{Wydbid.company_location}database.db')
    _session = sessionmaker()
    session = _session(bind=engine)
    base.metadata.create_all(engine)
    print('vor appointment')
    print(customer_id)
    appointment = Appointment(title=title, description=description, date=date.toString(), time=time.toString(),
                              customer_id=customer_id)

    session.add(appointment)
    session.commit()

    QMessageBox.about(widget, 'Completed',
                      f'{title} was created.')

    widget.clear()
    widget.hide()