from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *
from sqlalchemy.orm import sessionmaker
from Data.DataCombi import *
import Wydbid

def appendOrders(list: QTableWidget):
    engine = create_engine(f'sqlite:///{Wydbid.company_location}database.db')
    _session = sessionmaker()
    session = _session(bind=engine)

    base.metadata.create_all(engine)

    orders = session.query(Order).all()

    list.setSortingEnabled(False)
    list.clear()
    list.clearContents()
    list.setColumnCount(0)
    list.setRowCount(0)

    list.setColumnCount(5)
    list.setHorizontalHeaderLabels(
        ['Title', 'Price', 'Customer', 'Closed', '']
    )
    list.setColumnWidth(0, 200)
    list.setColumnWidth(1, 200)
    list.setColumnWidth(2, 200)
    list.setColumnWidth(3, 100)
    list.setColumnWidth(4, 40)

    orders.sort(key=lambda x: x.title, reverse=False)

    list.setRowCount(len(orders))

    i = 0

    for order in orders:
        title = QTableWidgetItem()
        title.setText(order.title)

        price = QTableWidgetItem()
        price.setData(Qt.DisplayRole, order.price)

        _customer_f_i_c = session.query(Customer).filter(Customer.id == order.customer_id).first()
        customer_name = f'{_customer_f_i_c.firstname} {_customer_f_i_c.lastname}'

        customer = QTableWidgetItem()
        customer.setText(customer_name)

        closed = QTableWidgetItem()

        if order.closed == 0 or False:
            closed.setText('No')
        else:
            closed.setText('Yes')

        view = QTableWidgetItem()
        view.setData(Qt.UserRole, order.id)
        view.setText('🔎')
        view.setTextAlignment(Qt.AlignCenter)

        list.setItem(i, 0, title)
        list.setItem(i, 1, price)
        list.setItem(i, 2, customer)
        list.setItem(i, 3, closed)
        list.setItem(i, 4, view)
        i = i + 1

    list.verticalHeader().setVisible(False)
    list.setFocusPolicy(Qt.NoFocus)
    list.setSelectionMode(QAbstractItemView.SelectionMode.NoSelection)
    list.setEditTriggers(QAbstractItemView.NoEditTriggers)
    list.setSortingEnabled(True)

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
        label.setText('A customer with this id doesn\'t exist.')

def createOrder(title: str, description: str, price: str, customer_id: str, widget):
    engine = create_engine(f'sqlite:///{Wydbid.company_location}database.db')
    _session = sessionmaker()
    session = _session(bind=engine)

    base.metadata.create_all(engine)

    if not title.strip() or not price.strip() or not customer_id.strip():
        QMessageBox.warning(widget, 'Warning',
                            'All fields must be filled in!')
        return

    try: int(customer_id.strip())
    except:
        QMessageBox.warning(widget, 'Warning',
                            'Customer ID must be an number!')
        return

    customer = session.query(Customer).filter(Customer.id == customer_id).first()

    if not customer:
        QMessageBox.warning(widget, 'Warning',
                            'A customer with this id doesn\'t exist.')
        return

    order = Order(title=title, description=description, price=price, customer_id=int(customer_id.strip()))

    session.add(order)
    session.commit()

    QMessageBox.about(widget, 'Completed',
                      f'{title} was created.')

    widget.clear()
    widget.hide()

def getCustomerForDel(widget):
    id, ok_pressed = QInputDialog.getText(widget, 'Get customer', 'Enter the ID of the customer you entered in the order you want to delete.',
                                          QLineEdit.Normal, '')

    if id and ok_pressed != '':
        return id
    else:
        widget.hide()
        return 0