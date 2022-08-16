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

    list.setEditTriggers(QAbstractItemView.NoEditTriggers)
    list.setSortingEnabled(True)