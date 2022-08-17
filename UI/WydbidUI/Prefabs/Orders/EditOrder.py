from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from BackEnd.WydbidBackEnd import OrderLogic

class EditOrder(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__()

        self.layout = QGridLayout()

        self.setLayout(self.layout)
        self.setWindowTitle('Wydbid - Edit order')
        self.setGeometry(0, 0, 600, 450)

        self.order_id = 0

        self.setupUI()

    def setOrder(self, order_id: int):
        self.order_id = order_id
        OrderLogic.setOrderForEdit(self.order_id, self)

    def clear(self):
        self.order_id = 0
        self.title.setText('')
        self.description.setText('')
        self.price.setText('')
        self.customer.setText('')

    def setupUI(self):
        self.layout.setAlignment(Qt.AlignTop | Qt.AlignHCenter)

        title = QLabel('Edit order')
        title.setFont(QFont('Montserrat', 30))

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

        edit = QPushButton(parent=self, text='Edit')
        edit.clicked.connect(self.startEditOrder)

        self.layout.addWidget(title, 1, 0, 1, 0, Qt.AlignCenter)

        self.layout.addWidget(titlenote, 2, 0, Qt.AlignLeft)
        self.layout.addWidget(self.title, 2, 1, Qt.AlignRight)

        self.layout.addWidget(descriptionnote, 3, 0, Qt.AlignLeft)
        self.layout.addWidget(self.description, 3, 1, Qt.AlignRight)

        self.layout.addWidget(pricenote, 4, 0, Qt.AlignLeft)
        self.layout.addWidget(self.price, 4, 1, Qt.AlignRight)

        self.layout.addWidget(customernote, 5, 0, Qt.AlignLeft)
        self.layout.addWidget(self.customer, 5, 1, Qt.AlignRight)
        self.layout.addWidget(self.customer_name, 6, 1, Qt.AlignRight)

        self.layout.addWidget(edit, 7, 0, 1, 0, Qt.AlignCenter)

    def startGetCustomer(self, edit: QLineEdit, label: QLabel):
        OrderLogic.getCustomerForLabel(edit, label)

    def startEditOrder(self):
        OrderLogic.editOrder(self.order_id, self.title.text(), self.description.toPlainText(),
                             self.price.text(), self.customer.text(), self)