from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from BackEnd.WydbidBackEnd import OrderLogic
from UI.WydbidUI.Prefabs.Orders import EditOrder

class ShowOrder(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__()

        self.layout = QGridLayout()

        self.setLayout(self.layout)
        self.setWindowTitle('Wydbid - Show order')
        self.setGeometry(0, 0, 600, 450)

        self.eo = EditOrder.EditOrder()

        self.order = None
        self.order_id = 0

        self.setupUI()

    def setOrder(self, order_id: int):
        self.order_id = order_id
        OrderLogic.setOrderForShow(self.order_id, self)

    def clear(self):
        self.order = None
        self.order_id = 0
        self.title.setText('')
        self.description.setText('')
        self.price.setText('')
        self.customer.setText('')
        self.closed.setChecked(False)

    def setupUI(self):
        self.layout.setAlignment(Qt.AlignTop | Qt.AlignHCenter)

        title = QLabel('Show order')
        title.setFont(QFont('Montserrat', 30))

        action_box = QGroupBox(parent=self)
        action_box.setFixedHeight(40)
        action_box.setMinimumWidth(500)
        alyt = QHBoxLayout()

        edit = QPushButton(parent=action_box, text='Edit')
        edit.setToolTip('Edit this order')
        edit.clicked.connect(self.startEditOrder)

        delete = QPushButton(parent=action_box, text='Delete')
        delete.setToolTip('Delete this order')
        delete.clicked.connect(self.startDelOrder)

        alyt.setContentsMargins(1, 1, 1, 1)
        alyt.addWidget(edit)
        alyt.addWidget(delete)
        action_box.setLayout(alyt)

        titlenote = QLabel(parent=self, text='Title: ')
        self.title = QLineEdit(parent=self)

        descriptionnote = QLabel(parent=self, text='Description: ')
        self.description = QTextEdit(parent=self)
        self.description.setMaximumHeight(300)

        pricenote = QLabel(parent=self, text='Price: ')
        self.price = QLineEdit(parent=self)

        customernote = QLabel(parent=self, text='Customer ID: ')
        self.customer = QLineEdit(parent=self)
        self.customer_name = QLabel(parent=self, text='')
        self.customer_name.font().setPixelSize(10)
        self.customer.textChanged.connect(lambda: self.startGetCustomer(self.customer, self.customer_name))

        self.closed = QCheckBox(parent=self, text='Closed')
        self.closed.stateChanged.connect(self.editClosed)

        self.title.setEnabled(False)
        self.description.setEnabled(False)
        self.price.setEnabled(False)
        self.customer.setEnabled(False)

        self.layout.addWidget(title, 1, 0, 1, 0, Qt.AlignCenter)

        self.layout.addWidget(action_box, 2, 0, 1, 0, Qt.AlignCenter)

        self.layout.addWidget(titlenote, 3, 0, Qt.AlignLeft)
        self.layout.addWidget(self.title, 3, 1, Qt.AlignRight)

        self.layout.addWidget(descriptionnote, 4, 0, Qt.AlignLeft)
        self.layout.addWidget(self.description, 4, 1, Qt.AlignRight)

        self.layout.addWidget(pricenote, 5, 0, Qt.AlignLeft)
        self.layout.addWidget(self.price, 5, 1, Qt.AlignRight)

        self.layout.addWidget(customernote, 6, 0, Qt.AlignLeft)
        self.layout.addWidget(self.customer, 6, 1, Qt.AlignRight)
        self.layout.addWidget(self.customer_name, 7, 1, Qt.AlignRight)

        self.layout.addWidget(self.closed, 8, 1, Qt.AlignRight)

    def editClosed(self):
        if not self.order_id == 0:
            if not self.order.closed == self.closed.isChecked():
                OrderLogic.editClosed(self.order_id, self.closed, self)

    def startGetCustomer(self, edit: QLineEdit, label: QLabel):
        OrderLogic.getCustomerForLabel(edit, label)

    def startEditOrder(self):
        self.eo.clear()
        self.eo.setOrder(self.order_id)
        self.eo.show()

    def startDelOrder(self):
        OrderLogic.delOrder(self.order_id, self)