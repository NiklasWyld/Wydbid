from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from BackEnd import ChangeEmployeePasswordLogic

class ChangeEmployeePassword(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__()

        self.layout = QGridLayout()

        self.setLayout(self.layout)
        self.setWindowTitle('Wydbid - Change employee password')
        self.setGeometry(0, 0, 600, 450)

        self.setupUI()

    def clear(self):
        self.password.setText('')
        self.new_password.setText('')

    def changePassword(self):
        ChangeEmployeePasswordLogic.changePasswordFinal(self.username.text(),
                                                        self.password.text(),
                                                        self.new_password.text(),
                                                        self)

    def setupUI(self):
        self.layout.setAlignment(Qt.AlignTop | Qt.AlignHCenter)

        title = QLabel('Change employee password')
        title.setFont(QFont('Montserrat', 30))

        username_note = QLabel(parent=self, text='Username: ')
        self.username = QLineEdit(parent=self)
        self.username.returnPressed.connect(self.changePassword)

        password_note = QLabel(parent=self, text='Old password: ')
        self.password = QLineEdit(parent=self)
        self.password.setEchoMode(QLineEdit.Password)
        self.password.returnPressed.connect(self.changePassword)

        new_password_note = QLabel(parent=self, text='New password: ')
        self.new_password = QLineEdit(parent=self)
        self.new_password.setEchoMode(QLineEdit.Password)
        self.new_password.returnPressed.connect(self.changePassword)

        submit = QPushButton(parent=self, text='Change')
        submit.clicked.connect(self.changePassword)

        self.layout.addWidget(title, 1, 0, 1, 0, Qt.AlignCenter)

        self.layout.addWidget(username_note, 2, 0, Qt.AlignLeft)
        self.layout.addWidget(self.username, 2, 1, Qt.AlignRight)

        self.layout.addWidget(password_note, 3, 0, Qt.AlignLeft)
        self.layout.addWidget(self.password, 3, 1, Qt.AlignRight)

        self.layout.addWidget(new_password_note, 4, 0, Qt.AlignLeft)
        self.layout.addWidget(self.new_password, 4, 1, Qt.AlignRight)

        self.layout.addWidget(submit, 5, 0, 1, 0, Qt.AlignCenter)