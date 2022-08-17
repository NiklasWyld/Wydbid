from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from BackEnd.WydbidBackEnd import AppointmentLogic

class ShowAppointment(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__()

        self.layout = QGridLayout()

        self.setLayout(self.layout)
        self.setWindowTitle('Wydbid - Show Appointment')
        self.setGeometry(0, 0, 600, 600)

        self.appointment = None

        self.setupUI()

    def setAppointment(self, appointment):
        self.appointment = appointment

        year = int(appointment.date.split('.')[2])
        month = int(appointment.date.split('.')[1])
        day = int(appointment.date.split('.')[0])

        hour = int(appointment.time.split(':')[0])
        minute = int(appointment.time.split(':')[1])

        self.dateedit.setDate(QDate(year, month, day))
        self.timeedit.setTime(QTime(hour, minute))
        self.title.setText(appointment.title)
        self.description.setText(appointment.description)
        self.customer.setText(str(appointment.customer_id))
        self.appeared.setChecked(appointment.appeared)
        self.closed.setChecked(appointment.closed)

    def clear(self):
        self.dateedit.setDate(QDate.currentDate())
        self.timeedit.setTime(QTime.currentTime())
        self.title.setText('')
        self.description.setText('')
        self.customer.clear()
        self.appeared.setChecked(False)
        self.closed.setChecked(False)

    def setupUI(self):
        self.layout.setAlignment(Qt.AlignTop | Qt.AlignHCenter)

        title = QLabel('Show Appointment')
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
        self.customer = QLineEdit(parent=self)
        self.customer.textChanged.connect(lambda: self.startGetCustomer(self.customer, self.customer_name))
        self.customer_name = QLabel(parent=self, text='')
        self.customer_name.font().setPixelSize(10)

        self.appeared = QCheckBox(parent=self, text='Appeared')
        self.appeared.stateChanged.connect(self.editAppeared)

        self.closed = QCheckBox(parent=self, text='Closed')
        self.closed.stateChanged.connect(self.editClosed)

        self.dateedit.setEnabled(False)
        self.timeedit.setEnabled(False)
        self.title.setEnabled(False)
        self.description.setEnabled(False)
        self.customer.setEnabled(False)

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
        self.layout.addWidget(self.customer_name, 7, 1, Qt.AlignRight)

        self.layout.addWidget(self.appeared, 8, 1, Qt.AlignRight)

        self.layout.addWidget(self.closed, 9, 1, Qt.AlignRight)

    def startGetCustomer(self, edit: QLineEdit, label: QLabel):
        AppointmentLogic.getCustomerForLabel(edit, label)

    def editAppeared(self):
        if not self.appointment.appeared == self.appeared.isChecked():
            AppointmentLogic.editAppointmentAppeared(self.appointment.id, self.appeared, self)

    def editClosed(self):
        if not self.appointment.closed == self.closed.isChecked():
            AppointmentLogic.editAppointmentClosed(self.appointment.id, self.closed, self)