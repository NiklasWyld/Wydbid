from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import Wydbid
from BackEnd.WydbidBackEnd import TaskLogic

class CreateTask(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__()

        self.layout = QGridLayout()

        self.setLayout(self.layout)
        self.setWindowTitle('Wydbid - Create task')
        self.setGeometry(0, 0, 600, 450)

        self.setupUI()

    def clear(self):
        self.receiver.setText('')
        self.title.setText('')
        self.description.setText('')
        self.deadline.setDate(QDate.currentDate())

    def setupUI(self):
        self.layout.setAlignment(Qt.AlignTop | Qt.AlignHCenter)

        title = QLabel('Create task')
        title.setFont(QFont('Montserrat', 30))

        receivernote = QLabel(parent=self, text='Receiver Username (*):')
        self.receiver = QLineEdit(parent=self)

        titlenote = QLabel(parent=self, text='Title (*): ')
        self.title = QLineEdit(parent=self)

        descriptionnote = QLabel(parent=self, text='Description: ')
        self.description = QTextEdit(parent=self)
        self.description.setMaximumHeight(300)

        deadlinenote = QLabel(parent=self, text='Deadline (*): ')
        self.deadline = QDateEdit(parent=self)

        submit = QPushButton(parent=self, text='Create')
        # ToDo: add logic to create button

        self.layout.addWidget(title, 1, 0, 1, 0, Qt.AlignCenter)

        self.layout.addWidget(receivernote, 2, 0, Qt.AlignLeft)
        self.layout.addWidget(self.receiver, 2, 1, Qt.AlignRight)

        self.layout.addWidget(titlenote, 3, 0, Qt.AlignLeft)
        self.layout.addWidget(self.title, 3, 1, Qt.AlignRight)

        self.layout.addWidget(descriptionnote, 4, 0, Qt.AlignLeft)
        self.layout.addWidget(self.description, 4, 1, Qt.AlignRight)

        self.layout.addWidget(deadlinenote, 5, 0, Qt.AlignLeft)
        self.layout.addWidget(self.deadline, 5, 1, Qt.AlignRight)

        self.layout.addWidget(submit, 6, 0, 1, 0, Qt.AlignCenter)