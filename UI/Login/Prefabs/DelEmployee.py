from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from BackEnd.Login import DelEmployeeLogic

class DelEmployee(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__()

        self.layout = QGridLayout()

        self.setLayout(self.layout)
        self.setWindowTitle('Wydbid - Delete employee')
        self.setGeometry(0, 0, 600, 450)

        self.setupUI()

    def clear(self):
        self.username.setText('')
        self.password.setText('')

    def delEmployee(self):
        DelEmployeeLogic.delEmployeeFinal(self.username.text(),
                                          self.password.text(),
                                          self)

    def setupUI(self):
        self.layout.setAlignment(Qt.AlignTop | Qt.AlignHCenter)

        title = QLabel('Delete employee')
        title.setFont(QFont('Montserrat', 30))

        username_note = QLabel(parent=self, text='Username: ')
        self.username = QLineEdit(parent=self)
        self.username.returnPressed.connect(self.delEmployee)

        password_note = QLabel(parent=self, text='Password: ')
        self.password = QLineEdit(parent=self)
        self.password.setEchoMode(QLineEdit.Password)
        self.password.returnPressed.connect(self.delEmployee)

        submit = QPushButton(parent=self, text='Delete')
        submit.clicked.connect(self.delEmployee)

        self.layout.addWidget(title, 1, 0, 1, 0, Qt.AlignCenter)

        self.layout.addWidget(username_note, 2, 0, Qt.AlignLeft)
        self.layout.addWidget(self.username, 2, 1, Qt.AlignRight)

        self.layout.addWidget(password_note, 3, 0, Qt.AlignLeft)
        self.layout.addWidget(self.password, 3, 1, Qt.AlignRight)

        self.layout.addWidget(submit, 4, 0, 1, 0, Qt.AlignCenter)