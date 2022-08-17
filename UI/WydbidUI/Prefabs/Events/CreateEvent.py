from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from BackEnd.WydbidBackEnd import EventLogic

class CreateEvent(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__()

        self.layout = QGridLayout()

        self.setLayout(self.layout)
        self.setWindowTitle('Wydbid - Create event')
        self.setGeometry(0, 0, 600, 450)

        self.setupUI()

    def clear(self):
        self.title.setText('')
        self.description.setText('')
        self.dateedit.setDate(QDate.currentDate())
        self.timeedit.setTime(QTime.currentTime())

    def setupUI(self):
        self.layout.setAlignment(Qt.AlignTop | Qt.AlignHCenter)

        title = QLabel('Create event')
        title.setFont(QFont('Montserrat', 30))

        titlenote = QLabel(parent=self, text='Title (*): ')
        self.title = QLineEdit(parent=self)

        descriptionnote = QLabel(parent=self, text='Description: ')
        self.description = QTextEdit(parent=self)
        self.description.setMaximumHeight(300)

        datenote = QLabel(parent=self, text='Date (*): ')
        self.dateedit = QDateEdit(parent=self)

        timenote = QLabel(parent=self, text='Time (*): ')
        self.timeedit = QTimeEdit(parent=self)

        create = QPushButton(parent=self, text='Create')
        create.clicked.connect(self.startCreateEvent)

        self.layout.addWidget(title, 1, 0, 1, 0, Qt.AlignCenter)

        self.layout.addWidget(titlenote, 2, 0, Qt.AlignLeft)
        self.layout.addWidget(self.title, 2, 1, Qt.AlignRight)

        self.layout.addWidget(descriptionnote, 3, 0, Qt.AlignLeft)
        self.layout.addWidget(self.description, 3, 1, Qt.AlignRight)

        self.layout.addWidget(datenote, 4, 0, Qt.AlignLeft)
        self.layout.addWidget(self.dateedit, 4, 1, Qt.AlignRight)

        self.layout.addWidget(timenote, 5, 0, Qt.AlignLeft)
        self.layout.addWidget(self.timeedit, 5, 1, Qt.AlignRight)

        self.layout.addWidget(create, 6, 0, 1, 0, Qt.AlignCenter)

    def startCreateEvent(self):
        EventLogic.createEvent(self.title.text(), self.description.toPlainText(),
                               self.dateedit.date(), self.timeedit.time(), self)