from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from BackEnd.Login import DelCompanyLogic


class DelCompany(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__()

        self.layout = QGridLayout()

        self.setLayout(self.layout)
        self.setWindowTitle('Wydbid - Delete company')
        self.setGeometry(0, 0, 600, 450)

        self.widget = self

        self.setupUI()

    def clear(self):
        self.password.setText('')

    def addItemsToCompany(self):
        DelCompanyLogic.addItems(self.company)

    def delCompany(self):
        DelCompanyLogic.getCompany(self.company, self.password.text(), self.widget)

    def setupUI(self):
        self.layout.setAlignment(Qt.AlignTop | Qt.AlignHCenter)

        title = QLabel('Delete company')
        title.setFont(QFont('Montserrat', 30))

        company_note = QLabel(parent=self, text='Company: ')
        self.company = QComboBox(parent=self)
        self.addItemsToCompany()

        password_note = QLabel(parent=self, text='Password: ')
        self.password = QLineEdit(parent=self)
        self.password.setEchoMode(QLineEdit.Password)
        self.password.returnPressed.connect(self.delCompany)

        submit = QPushButton(parent=self, text='Delete')
        submit.clicked.connect(self.delCompany)

        self.layout.addWidget(title, 1, 0, 1, 0, Qt.AlignCenter)

        self.layout.addWidget(company_note, 2, 0, Qt.AlignLeft)
        self.layout.addWidget(self.company, 2, 1, Qt.AlignRight)

        self.layout.addWidget(password_note, 3, 0, Qt.AlignLeft)
        self.layout.addWidget(self.password, 3, 1, Qt.AlignRight)

        self.layout.addWidget(submit, 4, 0, 1, 0, Qt.AlignCenter)