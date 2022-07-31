from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from BackEnd.Login import CreateCompanyLogic


class CreateCompany(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__()

        self.layout = QGridLayout()

        self.setLayout(self.layout)
        self.setWindowTitle('Wydbid - Create company')
        self.setGeometry(0, 0, 600, 450)

        self.widget = self

        self.setupUI()

    def createCompany(self):
        CreateCompanyLogic.getFirma(self.id_field.text(), self.name.text(), self.password.text(), self.widget)

    def clear(self, clearOnlyId: bool = False):
        if not clearOnlyId:
            self.id_field.setText('')
            self.name.setText('')
            self.password.setText('')
        if clearOnlyId:
            self.id_field.setText('')

    def setupUI(self):
        self.layout.setAlignment(Qt.AlignTop | Qt.AlignHCenter)

        title = QLabel('New company')
        title.setFont(QFont('Montserrat', 30))

        # Prove for type of id equals integer

        id_note = QLabel('Company-ID: ')
        self.id_field = QLineEdit()
        self.id_field.returnPressed.connect(self.createCompany)

        name_note = QLabel('Name: ')
        self.name = QLineEdit()
        self.name.returnPressed.connect(self.createCompany)

        password_note = QLabel('Password: ')
        self.password = QLineEdit()
        self.password.setEchoMode(QLineEdit.Password)
        self.password.returnPressed.connect(self.createCompany)

        self.submit = QPushButton('Create')
        self.submit.clicked.connect(self.createCompany)

        self.layout.addWidget(title, 0, 0, 1, 0, Qt.AlignTop|Qt.AlignCenter)

        self.layout.addWidget(id_note, 1, 0, Qt.AlignLeft)
        self.layout.addWidget(self.id_field, 1, 1, Qt.AlignRight)

        self.layout.addWidget(name_note, 2, 0, Qt.AlignLeft)
        self.layout.addWidget(self.name, 2, 1, Qt.AlignRight)

        self.layout.addWidget(password_note, 3, 0, Qt.AlignLeft)
        self.layout.addWidget(self.password, 3, 1, Qt.AlignRight)

        self.layout.addWidget(self.submit, 4, 0, 1, 0,  Qt.AlignCenter)