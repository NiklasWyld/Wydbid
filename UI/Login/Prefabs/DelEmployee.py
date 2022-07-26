from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from BackEnd import DelEmployeeLogic

class DelEmployee(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__()

        self.layout = QGridLayout()

        self.setLayout(self.layout)
        self.setWindowTitle('Wydbid - Delete employee')
        self.setGeometry(0, 0, 600, 450)

        self.widget = self

        self.setupUI()

    def clear(self):
        self.username.setText('')
        self.passwort.setText('')

    def delEmployee(self):
        DelEmployeeLogic.delEmployeeFinal(self.username.text(),
                                          self.passwort.text(),
                                          self.widget)

    def setupUI(self):
        self.layout.setAlignment(Qt.AlignTop | Qt.AlignHCenter)

        title = QLabel('Delete employee')
        title.setFont(QFont('Montserrat', 30))

        username_note = QLabel(parent=self, text='Username: ')
        self.username = QLineEdit(parent=self)
        self.username.returnPressed.connect(self.delEmployee)

        passwort_note = QLabel(parent=self, text='Password: ')
        self.passwort = QLineEdit(parent=self)
        self.passwort.setEchoMode(QLineEdit.Password)
        self.passwort.returnPressed.connect(self.delEmployee)

        submit = QPushButton(parent=self, text='Delete')
        submit.clicked.connect(self.delEmployee)

        self.layout.addWidget(title, 1, 0, 1, 0, Qt.AlignCenter)

        self.layout.addWidget(username_note, 2, 0, Qt.AlignLeft)
        self.layout.addWidget(self.username, 2, 1, Qt.AlignRight)

        self.layout.addWidget(passwort_note, 3, 0, Qt.AlignLeft)
        self.layout.addWidget(self.passwort, 3, 1, Qt.AlignRight)

        self.layout.addWidget(submit, 4, 0, 1, 0, Qt.AlignCenter)