from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from BackEnd import CreateEmployeeLogic

class CreateEmployee(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__()

        self.layout = QGridLayout()

        self.setLayout(self.layout)
        self.setWindowTitle('Wydbid - Create employee')
        self.setGeometry(0, 0, 600, 450)

        self.widget = self

        self.setupUI()

    def clear(self):
        self.name.setText('')
        self.username.setText('')
        self.passwort.setText('')

    def createEmployee(self):
        CreateEmployeeLogic.createEmployeeFinal(self.name.text(),
                                                self.username.text(),
                                                self.passwort.text(),
                                                self.widget)

    def setupUI(self):
        self.layout.setAlignment(Qt.AlignTop | Qt.AlignHCenter)

        title = QLabel('New employee')
        title.setFont(QFont('Montserrat', 30))

        name_note = QLabel('Name: ')
        self.name = QLineEdit()
        self.name.returnPressed.connect(self.createEmployee)

        username_note = QLabel('Username: ')
        self.username = QLineEdit()
        self.username.returnPressed.connect(self.createEmployee)

        passwort_note = QLabel('Password: ')
        self.passwort = QLineEdit()
        self.passwort.setEchoMode(QLineEdit.Password)
        self.passwort.returnPressed.connect(self.createEmployee)

        self.submit = QPushButton('Create')
        self.submit.clicked.connect(self.createEmployee)

        self.layout.addWidget(title, 0, 0, 1, 0, Qt.AlignTop|Qt.AlignCenter)

        self.layout.addWidget(name_note, 1, 0, Qt.AlignLeft)
        self.layout.addWidget(self.name, 1, 1, Qt.AlignRight)

        self.layout.addWidget(username_note, 2, 0, Qt.AlignLeft)
        self.layout.addWidget(self.username, 2, 1, Qt.AlignRight)

        self.layout.addWidget(passwort_note, 3, 0, Qt.AlignLeft)
        self.layout.addWidget(self.passwort, 3, 1, Qt.AlignRight)

        self.layout.addWidget(self.submit, 4, 0, 1, 0,  Qt.AlignCenter)