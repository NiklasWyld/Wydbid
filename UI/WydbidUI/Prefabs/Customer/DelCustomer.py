from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from BackEnd.WydbidBackEnd import CustomerLogic

class DelCustomer(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__()

        self.layout = QGridLayout()

        self.setLayout(self.layout)
        self.setWindowTitle('Wydbid - Delete customer')
        self.setGeometry(0, 0, 600, 450)

        self.setupUI()

    def clear(self):
        self.id.setText('')

    def setupUI(self):
        self.layout.setAlignment(Qt.AlignTop | Qt.AlignHCenter)

        title = QLabel('Delete customer')
        title.setFont(QFont('Montserrat', 30))

        id_note = QLabel(parent=self, text='ID: ')
        self.id = QLineEdit(parent=self)

        submit = QPushButton(parent=self, text='Delete')
        submit.clicked.connect(
            lambda: CustomerLogic.delCustomer(widget=self, id=self.id.text())
        )

        self.layout.addWidget(title, 1, 0, 1, 0, Qt.AlignCenter)

        self.layout.addWidget(id_note, 2, 0, Qt.AlignLeft)
        self.layout.addWidget(self.id, 2, 1, Qt.AlignRight)

        self.layout.addWidget(submit, 3, 0, 1, 0, Qt.AlignCenter)