from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from BackEnd.WydbidBackEnd import AppointmentLogic

class DelAppointment(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__()

        self.layout = QGridLayout()

        self.setLayout(self.layout)
        self.setWindowTitle('Wydbid - Delete appointment')
        self.setGeometry(0, 0, 600, 600)

        self.date = ''

        self.setupUI()

    def setDate(self, date):
        self.list.clear()
        self.date = date
        AppointmentLogic.appendAppointmentsForGet(self.date, self.list, self)

    def startDeleteAppointment(self):
        AppointmentLogic.delAppointment(self.list, self)

    def setupUI(self):
        self.layout.setAlignment(Qt.AlignTop | Qt.AlignHCenter)

        title = QLabel('Delete Appointment')
        title.setFont(QFont('Montserrat', 30))

        self.list = QListWidget(parent=self)

        submit = QPushButton(parent=self, text='Delete')
        submit.clicked.connect(self.startDeleteAppointment)

        self.layout.addWidget(title, 1, 0, 1, 0, Qt.AlignCenter)

        self.layout.addWidget(self.list, 2, 0, 1, 0, Qt.AlignCenter)

        self.layout.addWidget(submit, 3, 0, 1, 0, Qt.AlignCenter)