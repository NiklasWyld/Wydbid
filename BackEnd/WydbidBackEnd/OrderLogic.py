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

def setOrderForShow(order_id: int, widget):
    engine = create_engine(f'sqlite:///{Wydbid.company_location}database.db')
    _session = sessionmaker()
    session = _session(bind=engine)

    base.metadata.create_all(engine)

    order = session.query(Order).filter(Order.id == order_id).first()

    if not order:
        QMessageBox.warning(widget, 'Error', 'An error has occurred')
        return

    widget.order = order
    widget.title.setText(order.title)
    widget.description.setText(order.description)
    widget.price.setText(order.price)
    widget.customer.setText(str(order.customer_id))
    widget.closed.setChecked(bool(order.closed))

def editClosed(order_id: int, check: QCheckBox, widget):
    engine = create_engine(f'sqlite:///{Wydbid.company_location}database.db')
    _session = sessionmaker()
    session = _session(bind=engine)

    base.metadata.create_all(engine)

    order = session.query(Order).filter(Order.id == order_id).first()

    if not order:
        QMessageBox.warning(widget, 'Error', 'An error has occurred')
        return

    if bool(order.closed) == check.isChecked():
        return

    session.query(Order).filter(Order.id == order_id).update(
        {
            Order.closed: check.isChecked()
        }
    )
    session.commit()

    QMessageBox.about(widget, 'Successfully changed', f'Order closed -> {str(check.isChecked())}')

def delOrder(order_id: int, widget):
    engine = create_engine(f'sqlite:///{Wydbid.company_location}database.db')
    _session = sessionmaker()
    session = _session(bind=engine)

    base.metadata.create_all(engine)

    order = session.query(Order).filter(Order.id == order_id).first()

    if not order:
        QMessageBox.warning(widget, 'Error', 'An error has occurred')
        return

    m = QMessageBox.question(widget,
                             'Confirm deletion',
                             f'Attention, do you really want to delete {order.title}?',
                             QMessageBox.Yes,
                             QMessageBox.No)

    if m == QMessageBox.No:
        QMessageBox.about(widget, 'Cancelled',
                          'The order has not been deleted.')
        return

    session.delete(order)
    session.commit()

    QMessageBox.about(widget, 'Completed',
                      'The order has been deleted!')

    widget.clear()
    widget.hide()

def setOrderForEdit(order_id: int, widget):
    engine = create_engine(f'sqlite:///{Wydbid.company_location}database.db')
    _session = sessionmaker()
    session = _session(bind=engine)

    base.metadata.create_all(engine)

    order = session.query(Order).filter(Order.id == order_id).first()

    if not order:
        QMessageBox.warning(widget, 'Error', 'An error has occurred')
        return

    widget.title.setText(order.title)
    widget.description.setText(order.description)
    widget.price.setText(order.price)
    widget.customer.setText(str(order.customer_id))

def editOrder(order_id: int, title: str, description: str, price: str, customer_id: str, widget):
    engine = create_engine(f'sqlite:///{Wydbid.company_location}database.db')
    _session = sessionmaker()
    session = _session(bind=engine)

    base.metadata.create_all(engine)

    order = session.query(Order).filter(Order.id == order_id).first()

    if not order:
        QMessageBox.warning(widget, 'Error', 'An error has occurred')
        return

    if not title.strip() or not price.strip() or not customer_id.strip():
        QMessageBox.warning(Wydbid.app.parent(), 'Warning',
                            'All fields must be filled in!')
        return

    try: int(customer_id.strip())
    except:
        QMessageBox.warning(widget, 'Warning',
                            'Customer ID must be an number!')
        return

    customer = session.query(Customer).filter(Customer.id == int(customer_id.strip())).first()
    if not customer:
        QMessageBox.warning(Wydbid.app.parent(), 'Attention',
                            'Attention, the customer you entered does not exist.')

    session.query(Order).filter(Order.id == order_id).update(
        {
            Order.title: title,
            Order.description: description,
            Order.price: price,
            Order.customer_id: int(customer_id.strip()),
        }
    )

    session.commit()

    QMessageBox.about(widget, 'Updated order', f'Updated {order.title} successfully.')

    widget.clear()
    widget.hide()