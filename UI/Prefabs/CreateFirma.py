from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from BackEnd import CreateFirmaLogic

class CreateFirma(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__()

        self.layout = QGridLayout()

        self.setLayout(self.layout)
        self.setWindowTitle('Wydbid - Firma erstellen')
        self.setGeometry(0, 0, 600, 450)

        self.widget = self

        self.setupUI()

    def createFirma(self):
        CreateFirmaLogic.getFirma(self.id_field.text(), self.name.text(), self.passwort.text(), self.widget)

    def clear(self, clearOnlyId: bool = False):
        if not clearOnlyId:
            self.id_field.setText('')
            self.name.setText('')
            self.passwort.setText('')
        if clearOnlyId:
            self.id_field.setText('')

    def setupUI(self):
        self.layout.setAlignment(Qt.AlignTop | Qt.AlignHCenter)

        title = QLabel('Neue Firma')
        title.setFont(QFont('Montserrat', 30))

        # Prove for type of id equals integer

        id_note = QLabel('Firmen-ID: ')
        self.id_field = QLineEdit()

        name_note = QLabel('Name: ')
        self.name = QLineEdit()

        passwort_note = QLabel('Passwort: ')
        self.passwort = QLineEdit()
        self.passwort.setEchoMode(QLineEdit.Password)

        self.submit = QPushButton('Erstellen')
        self.submit.clicked.connect(self.createFirma)

        self.layout.addWidget(title, 0, 0, 1, 0, Qt.AlignTop|Qt.AlignCenter)

        self.layout.addWidget(id_note, 1, 0, Qt.AlignLeft)
        self.layout.addWidget(self.id_field, 1, 1, Qt.AlignRight)

        self.layout.addWidget(name_note, 2, 0, Qt.AlignLeft)
        self.layout.addWidget(self.name, 2, 1, Qt.AlignRight)

        self.layout.addWidget(passwort_note, 3, 0, Qt.AlignLeft)
        self.layout.addWidget(self.passwort, 3, 1, Qt.AlignRight)

        self.layout.addWidget(self.submit, 4, 0, 1, 0,  Qt.AlignCenter)