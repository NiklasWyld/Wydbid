from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from BackEnd.WydbidBackEnd import AppointmentLogic

class GetAppointment(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__()

        self.layout = QGridLayout()

        self.setLayout(self.layout)
        self.setWindowTitle('Wydbid - Get appointment for edit')
        self.setGeometry(0, 0, 600, 600)

        self.ea = EditAppointment()

        self.date = ''

        self.setupUI()

    def setDate(self, date):
        self.list.clear()
        self.date = date
        AppointmentLogic.appendAppointmentsForGet(self.date, self.list, self)

    def startEditAppointment(self):
        if not self.list.selectedItems():
            QMessageBox.about(self, 'Warning',
                              'An appointment must be selected to continue.')
            return

        self.ea.show()
        self.ea.customer.clear()
        self.ea.setAppointment(self.list.selectedItems()[0].data(Qt.UserRole))
        self.hide()

    def setupUI(self):
        self.layout.setAlignment(Qt.AlignTop | Qt.AlignHCenter)

        title = QLabel('Get appointment for edit')
        title.setFont(QFont('Montserrat', 30))

        self.list = QListWidget(parent=self)

        submit = QPushButton(parent=self, text='Continue')
        submit.clicked.connect(self.startEditAppointment)

        self.layout.addWidget(title, 1, 0, 1, 0, Qt.AlignCenter)

        self.layout.addWidget(self.list, 2, 0, 1, 0, Qt.AlignCenter)

        self.layout.addWidget(submit, 3, 0, 1, 0, Qt.AlignCenter)


class EditAppointment(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__()

        self.layout = QGridLayout()

        self.setLayout(self.layout)
        self.setWindowTitle('Wydbid - Edit appointment')
        self.setGeometry(0, 0, 600, 600)

        self.appointment_id = 0

        self.setupUI()

    def setAppointment(self, appointment_id: int):
        self.appointment_id = appointment_id
        AppointmentLogic.setAppointmentForEdit(self.appointment_id, self)

    def clear(self):
        self.date = QDate.currentDate()
        self.dateedit.setDate(self.date)
        self.timeedit.setTime(QTime.currentTime())
        self.title.setText('')
        self.description.setText('')
        self.customer.clear()

    def setupUI(self):
        self.layout.setAlignment(Qt.AlignTop | Qt.AlignHCenter)

        title = QLabel('Edit Appointment')
        title.setFont(QFont('Montserrat', 30))

        dateeditnote = QLabel(parent=self, text='Date (*): ')
        self.dateedit = QDateEdit(parent=self)

        timeeditnote = QLabel(parent=self, text='Time (*): ')
        self.timeedit = QTimeEdit(parent=self)
        self.timeedit.setTime(QTime.currentTime())

        titlenote = QLabel(parent=self, text='Title (*): ')
        self.title = QLineEdit(parent=self)

        descriptionnote = QLabel(parent=self, text='Description: ')
        self.description = QTextEdit(parent=self)
        self.description.setMaximumHeight(300)

        customernote = QLabel(parent=self, text='Customer (*): ')
        self.customer = QLineEdit(parent=self)
        self.customer.textChanged.connect(lambda: self.startGetCustomer(self.customer, self.customer_name))
        self.customer_name = QLabel(parent=self, text='')
        self.customer_name.font().setPixelSize(10)

        edit = QPushButton(parent=self, text='Edit')
        edit.clicked.connect(self.startEditAppointment)

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

        self.layout.addWidget(edit, 8, 0, 1, 0, Qt.AlignCenter)

    def startGetCustomer(self, edit: QLineEdit, label: QLabel):
        AppointmentLogic.getCustomerForLabel(edit, label)

    def startEditAppointment(self):
        AppointmentLogic.editAppointment(id=self.appointment_id, date=self.dateedit.date(), time=self.timeedit.time(), title=self.title.text(),
                                           description=self.description.toPlainText(),
                                           customer_id=self.customer.text(), widget=self)