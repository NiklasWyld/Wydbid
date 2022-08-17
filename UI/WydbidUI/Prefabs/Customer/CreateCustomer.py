from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from BackEnd.WydbidBackEnd import CustomerLogic

class CreateCustomer(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__()

        self.layout = QGridLayout()

        self.setLayout(self.layout)
        self.setWindowTitle('Wydbid - Create customer')
        self.setGeometry(0, 0, 600, 600)

        self.setupUI()

    def setupUI(self):
        self.layout.setAlignment(Qt.AlignTop | Qt.AlignHCenter)

        title = QLabel('Create customer')
        title.setFont(QFont('Montserrat', 30))

        firstname_note = QLabel(parent=self, text='First name (*): ')
        self.firstname = QLineEdit(parent=self)

        lastname_note = QLabel(parent=self, text='Last name (*): ')
        self.lastname = QLineEdit(parent=self)

        email_note = QLabel(parent=self, text='E-mail address: ')
        self.email = QLineEdit(parent=self)

        adress_note = QLabel(parent=self, text='Address: ')
        self.adress = QLineEdit(parent=self)

        number_note = QLabel(parent=self, text='Telephone number: ')
        self.number = QLineEdit(parent=self)

        gender_note = QLabel(parent=self, text='Gender: ')
        self.gender = QComboBox(parent=self)
        self.gender.addItem('Male', 'men')
        self.gender.addItem('Female', 'women')

        birthdate_note = QLabel(parent=self, text='Birth date: ')
        self.birthdate = QLineEdit(parent=self)

        information_note = QLabel(parent=self, text='Information: ')
        self.information = QTextEdit(parent=self)

        submit = QPushButton(parent=self, text='Create')
        submit.clicked.connect(lambda: CustomerLogic.createCustomer(create_customer=self))

        self.layout.addWidget(title, 1, 0, 1, 0, Qt.AlignCenter)

        self.layout.addWidget(firstname_note, 2, 0, Qt.AlignLeft)
        self.layout.addWidget(self.firstname, 2, 1, Qt.AlignRight)

        self.layout.addWidget(lastname_note, 3, 0, Qt.AlignLeft)
        self.layout.addWidget(self.lastname, 3, 1, Qt.AlignRight)

        self.layout.addWidget(email_note, 4, 0, Qt.AlignLeft)
        self.layout.addWidget(self.email, 4, 1, Qt.AlignRight)

        self.layout.addWidget(adress_note, 5, 0, Qt.AlignLeft)
        self.layout.addWidget(self.adress, 5, 1, Qt.AlignRight)

        self.layout.addWidget(number_note, 6, 0, Qt.AlignLeft)
        self.layout.addWidget(self.number, 6, 1, Qt.AlignRight)

        self.layout.addWidget(gender_note, 7, 0, Qt.AlignLeft)
        self.layout.addWidget(self.gender, 7, 1, Qt.AlignRight)

        self.layout.addWidget(birthdate_note, 8, 0, Qt.AlignLeft)
        self.layout.addWidget(self.birthdate, 8, 1, Qt.AlignRight)

        self.layout.addWidget(information_note, 9, 0, Qt.AlignLeft)
        self.layout.addWidget(self.information, 9, 1, Qt.AlignRight)

        self.layout.addWidget(submit, 10, 0, 1, 0, Qt.AlignCenter)

    def clear(self):
        self.firstname.setText('')
        self.lastname.setText('')
        self.email.setText('')
        self.adress.setText('')
        self.number.setText('')
        self.gender.setCurrentIndex(0)
        self.birthdate.setText('')
        self.information.setText('')