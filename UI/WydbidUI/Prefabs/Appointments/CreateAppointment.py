from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from BackEnd.WydbidBackEnd import AppointmentLogic

class CreateAppointment(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__()

        self.layout = QGridLayout()

        self.setLayout(self.layout)
        self.setWindowTitle('Wydbid - Create appointment')
        self.setGeometry(0, 0, 600, 600)

        self.date = QDate.currentDate()

        self.setupUI()

    def setDate(self, date: QDate):
        self.date = date
        self.dateedit.setDate(self.date)

    def appendCustomers(self):
        AppointmentLogic.appendCustomer(self.customer)

    def clear(self):
        self.date = QDate.currentDate()
        self.dateedit.setDate(self.date)
        self.timeedit.setTime(QTime.currentTime())
        self.title.setText('')
        self.description.setText('')
        self.customer.clear()

    def setupUI(self):
        self.layout.setAlignment(Qt.AlignTop | Qt.AlignHCenter)

        title = QLabel('Create Appointment')
        title.setFont(QFont('Montserrat', 30))

        dateeditnote = QLabel(parent=self, text='Date: ')
        self.dateedit = QDateEdit(parent=self)

        timeeditnote = QLabel(parent=self, text='Time: ')
        self.timeedit = QTimeEdit(parent=self)
        self.timeedit.setTime(QTime.currentTime())

        titlenote = QLabel(parent=self, text='Title: ')
        self.title = QLineEdit(parent=self)

        descriptionnote = QLabel(parent=self, text='Description: ')
        self.description = QTextEdit(parent=self)
        self.description.setMaximumHeight(300)

        customernote = QLabel(parent=self, text='Customer: ')
        self.customer = QComboBox(parent=self)

        create = QPushButton(parent=self, text='Create')

        self.layout.addWidget(title, 1, 0, 1, 0, Qt.AlignCenter)

        self.layout.addWidget(dateeditnote, 2, 0, Qt.AlignLeft)
        self.layout.addWidget(self.dateedit, 2, 1, Qt.AlignRight)

        self.layout.addWidget(timeeditnote, 3, 0, Qt.AlignLeft)
        self.layout.addWidget(self.timeedit, 3, 1, Qt.AlignRight)

        self.layout.addWidget(titlenote, 4, 0, Qt.AlignLeft)
        self.layout.addWidget(self.title, 4, 1, Qt.AlignRight)

        self.layout.addWidget(descriptionnote, 5, 0, Qt.AlignLeft)
        self.layout.addWidget(self.description, 5, 1, Qt.AlignRight)

        self.layout.addWidget(customernote, 6, 0, Qt.AlignLeft)
        self.layout.addWidget(self.customer, 6, 1, Qt.AlignRight)

        self.layout.addWidget(create, 7, 0, 1, 0, Qt.AlignCenter)