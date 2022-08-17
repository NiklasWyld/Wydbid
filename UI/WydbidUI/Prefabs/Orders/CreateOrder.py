from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from BackEnd.WydbidBackEnd import OrderLogic

class CreateOrder(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__()

        self.layout = QGridLayout()

        self.setLayout(self.layout)
        self.setWindowTitle('Wydbid - Create order')
        self.setGeometry(0, 0, 600, 450)

        self.setupUI()

    def clear(self):
        self.title.setText('')
        self.description.setText('')
        self.price.setText('')
        self.customer.setText('')
        self.customer_name.setText('')

    def setupUI(self):
        self.layout.setAlignment(Qt.AlignTop | Qt.AlignHCenter)

        title = QLabel('Create order')
        title.setFont(QFont('Montserrat', 30))

        titlenote = QLabel(parent=self, text='Title (*): ')
        self.title = QLineEdit(parent=self)

        descriptionnote = QLabel(parent=self, text='Description: ')
        self.description = QTextEdit(parent=self)
        self.description.setMaximumHeight(300)

        pricenote = QLabel(parent=self, text='Price: ')
        self.price = QLineEdit(parent=self)

        customernote = QLabel(parent=self, text='Customer ID (*): ')
        self.customer = QLineEdit(parent=self)
        self.customer.textChanged.connect(lambda: self.startGetCustomer(self.customer, self.customer_name))
        self.customer_name = QLabel(parent=self, text='')
        self.customer_name.font().setPixelSize(10)

        create = QPushButton(parent=self, text='Create')
        create.clicked.connect(self.startCreateOrder)

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

        self.layout.addWidget(create, 7, 0, 1, 0, Qt.AlignCenter)

    def startGetCustomer(self, edit: QLineEdit, label: QLabel):
        OrderLogic.getCustomerForLabel(edit, label)

    def startCreateOrder(self):
        OrderLogic.createOrder(title=self.title.text(), description=self.description.toPlainText(),
                               price=self.price.text(), customer_id=self.customer.text(), widget=self)