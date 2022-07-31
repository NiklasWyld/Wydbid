from PyQt5.QtWidgets import *
from sqlalchemy.orm import sessionmaker
from Data.DataCombi import *
import Wydbid

# ToDo: Add if not / .strip() to prove strings

def createCustomer(create_customer):
    if not create_customer.firstname.text().strip() or not create_customer.lastname.text().strip():
        QMessageBox.warning(Wydbid.app.parent(), 'Warning',
                            'The mandatory fields must be filled in!')
        return

    engine = create_engine(f'sqlite:///{Wydbid.company_location}database.db')
    session = sessionmaker()
    my_session = session(bind=engine)

    base.metadata.create_all(engine)

    customer_new = Customer(firstname=create_customer.firstname.text(), lastname=create_customer.lastname.text(),
                                  email=create_customer.email.text(), adress=create_customer.adress.text(),
                                  number=create_customer.number.text(), gender=create_customer.gender.currentData(),
                                  birthdate=create_customer.birthdate.text(),
                                  information=create_customer.information.toPlainText())

    my_session.add(customer_new)
    my_session.commit()

    QMessageBox.about(Wydbid.app.parent(), 'Completed',
                      f'{customer_new.firstname} {customer_new.lastname} was created under the id {str(customer_new.id)}.')

    create_customer.clear()
    create_customer.hide()

def setCustomerForEditFinal(widget, id):
    try:
        int(id)
    except:
        QMessageBox.warning(Wydbid.app.parent(
        ), 'Warning', 'A number must be entered in the ID field!')
        widget.hide()
        return

    id = int(id)

    engine = create_engine(f'sqlite:///{Wydbid.company_location}database.db')
    session = sessionmaker()
    my_session = session(bind=engine)

    base.metadata.create_all(engine)

    customer = my_session.query(Customer).filter(Customer.id == id).first()

    if not customer:
        QMessageBox.warning(Wydbid.app.parent(), 'Attention',
                            'Attention, the customer you entered does not exist.')
        widget.hide()
        return

    my_session.commit()

    widget.setCustomerFinal(customer)

def setCustomerForEdit(widget):
    id, ok_pressed = QInputDialog.getText(widget, 'Get customer', 'Enter the ID of the customer you want to edit: ',
                                          QLineEdit.Normal, '')

    if id and ok_pressed != '':
        setCustomerForEditFinal(widget, id)
    else:
        widget.hide()

def editCustomer(customer_id, edit_customer):
    engine = create_engine(f'sqlite:///{Wydbid.company_location}database.db')
    _session = sessionmaker()
    session = _session(bind=engine)

    base.metadata.create_all(engine)

    session.query(Customer).filter(Customer.id == customer_id).update(
        {
            Customer.firstname: edit_customer.firstname.text(),
            Customer.lastname: edit_customer.lastname.text(),
            Customer.email: edit_customer.email.text(),
            Customer.adress: edit_customer.adress.text(),
            Customer.number: edit_customer.number.text(),
            Customer.gender: edit_customer.gender.currentData(),
            Customer.birthdate: edit_customer.birthdate.text(),
            Customer.information: edit_customer.information.toPlainText()
        }
    )

    session.commit()

    QMessageBox.about(Wydbid.app.parent(), 'Process completed',
                      f'{edit_customer.firstname.text()} {edit_customer.lastname.text()} has been successfully updated.')

    edit_customer.clear()
    edit_customer.hide()


def delCustomer(widget, id):
    try:
        int(id)
    except:
        QMessageBox.warning(Wydbid.app.parent(), 'Warning', 'A number must be entered in the ID field!')
        widget.clear()
        return

    engine = create_engine(f'sqlite:///{Wydbid.company_location}database.db')
    _session = sessionmaker()
    session = _session(bind=engine)

    base.metadata.create_all(engine)

    customer = session.query(Customer).filter(Customer.id == int(id)).first()

    if not customer:
        QMessageBox.warning(Wydbid.app.parent(), 'Attention',
                            'Attention, the customer you entered does not exist.')
        return

    reply = QMessageBox.question(Wydbid.app.parent(), 'Are you sure?',
                                 f'Are you sure you want to delete {customer.firstname} {customer.lastname}?',
                                 QMessageBox.Yes, QMessageBox.No)

    if reply == QMessageBox.Yes:
        session.delete(customer)
        session.commit()

        QMessageBox.about(Wydbid.app.parent(), 'Completed',
                          'The customer has been deleted!')
    else:
        QMessageBox.about(Wydbid.app.parent(), 'Completed',
                          'The customer has not been deleted!')
        session.commit()

    widget.clear()
    widget.hide()