from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from Data.DataCombi import *
import Wydbid

class ViewCustomer(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__()

        self.layout = QGridLayout()

        self.setLayout(self.layout)
        self.setWindowTitle('Wydbid - View customer')
        self.setGeometry(0, 0, 600, 600)

        self.setupUI()

    def setupUI(self):
        title = QLabel('View customer')
        title.setFont(QFont('Montserrat', 30))

        id_note = QLabel(parent=self, text='ID')
        self.id = QLineEdit(parent=self)

        firstname_note = QLabel(parent=self, text='First name: ')
        self.firstname = QLineEdit(parent=self)

        lastname_note = QLabel(parent=self, text='Last name: ')
        self.lastname = QLineEdit(parent=self)

        email_note = QLabel(parent=self, text='E-mail address: ')
        self.email = QLineEdit(parent=self)

        adress_note = QLabel(parent=self, text='Address: ')
        self.adress = QLineEdit(parent=self)

        number_note = QLabel(parent=self, text='Telephone number: ')
        self.number = QLineEdit(parent=self)

        gender_note = QLabel(parent=self, text='Gender: ')
        self.gender = QLineEdit(parent=self)

        birthdate_note = QLabel(parent=self, text='Birth date: ')
        self.birthdate = QLineEdit(parent=self)

        information_note = QLabel(parent=self, text='Information: ')
        self.information = QTextEdit(parent=self)

        self.layout.addWidget(title, 0, 0, 1, 0, Qt.AlignCenter)

        self.layout.addWidget(id_note, 1, 0, Qt.AlignLeft)
        self.layout.addWidget(self.id, 1, 1, Qt.AlignRight)

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

    def setCustomer(self, customer: Customer):
        self.id.setText(str(customer.id))
        self.firstname.setText(customer.firstname)
        self.lastname.setText(customer.lastname)
        self.email.setText(customer.email)
        self.adress.setText(customer.adress)
        self.number.setText(customer.number)
        self.gender.setText(customer.gender)
        self.birthdate.setText(customer.birthdate)
        self.information.setText(customer.information)

        self.id.setEnabled(False)
        self.firstname.setEnabled(False)
        self.lastname.setEnabled(False)
        self.email.setEnabled(False)
        self.adress.setEnabled(False)
        self.number.setEnabled(False)
        self.gender.setEnabled(False)
        self.birthdate.setEnabled(False)
        self.information.setEnabled(False)

    def clear(self):
        self.id.setText('')
        self.firstname.setText('')
        self.lastname.setText('')
        self.email.setText('')
        self.adress.setText('')
        self.number.setText('')
        self.gender.setText('')
        self.birthdate.setText('')
        self.information.setText('')