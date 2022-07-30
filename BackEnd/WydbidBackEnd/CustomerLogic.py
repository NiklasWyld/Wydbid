from PyQt5.QtWidgets import QMessageBox
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
