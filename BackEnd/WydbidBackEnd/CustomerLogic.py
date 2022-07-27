import pickle
from PyQt5.QtWidgets import QMessageBox
import Wydbid
import os
from Data import Customer


def setupCustomerFolder():
    customer_path = f'{Wydbid.company_location}Customers'

    if os.path.exists(customer_path):
        return
    else:
        os.mkdir(customer_path)

# ToDo: Add if not / .strip() to prove strings
# ToDo: Fix reload


def handleNextId():
    id_list = os.listdir(f'{Wydbid.company_location}Customers/')
    if not id_list:
        return str(1)

    id_list = [int(x) for x in id_list]

    id_list.sort()

    _number = 0

    for id in id_list:
        if _number + 1 == id:
            _number = _number + 1
        else:
            return str(_number + 1)

    return str(id_list[-1] + 1)


def createCustomer(create_customer):
    if create_customer.id_tick.isChecked():
        new_id = handleNextId()
    else:
        new_id = create_customer.id.text()

    try:
        int(new_id)
    except:
        QMessageBox.warning(Wydbid.app.parent(), 'Warning',
                            'The customer number must be a number.')
        return

    if not new_id.strip() or not create_customer.firstname.text().strip() or not create_customer.lastname.text().strip():
        QMessageBox.warning(Wydbid.app.parent(), 'Warning',
                            'The mandatory fields must be filled in!')
        return

    customer_new = Customer.Customer(id=int(new_id), firstname=create_customer.firstname.text(), lastname=create_customer.lastname.text(),
                                  email=create_customer.email.text(), adress=create_customer.adress.text(),
                                  number=create_customer.number.text(), gender=create_customer.gender.currentData(),
                                  birthdate=create_customer.birthdate.text(),
                                  information=create_customer.information.toPlainText())

    customer_loc_name = new_id

    location = f'{Wydbid.company_location}Customers/{customer_loc_name}/'

    if os.path.exists(location):
        QMessageBox.warning(Wydbid.app.parent(), 'Attention',
                            'A customer with this customer number already exists!')
        return

    os.makedirs(location)
    k_file = open(f'{location}{customer_loc_name}.wbk', 'wb')

    pickle.dump(customer_new, k_file, pickle.HIGHEST_PROTOCOL)

    QMessageBox.about(Wydbid.app.parent(), 'Completed',
                      f'{customer_new. firstname} {customer_new.lastname} was created.')

    create_customer.clear()
    create_customer.hide()
