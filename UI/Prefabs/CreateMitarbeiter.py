from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from BackEnd import CreateMitarbeiterLogic

class CreateMitarbeiter(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__()

        self.layout = QGridLayout()

        self.setLayout(self.layout)
        self.setWindowTitle('Wydbid - Mitarbeiter erstellen')
        self.setGeometry(0, 0, 600, 450)

        self.widget = self

        self.setupUI()

    def clear(self):
        self.id_field.setText('')
        self.name.setText('')
        self.username.setText('')
        self.passwort.setText('')

    def createMitarbeiter(self):
        CreateMitarbeiterLogic.createMitarbeiterFinal(self.id_field.text(),
                                                      self.name.text(),
                                                      self.username.text(),
                                                      self.passwort.text(),
                                                      self.widget)

    def setupUI(self):
        self.layout.setAlignment(Qt.AlignTop | Qt.AlignHCenter)

        title = QLabel('Neuer Mitarbeiter')
        title.setFont(QFont('Montserrat', 30))

        id_note = QLabel('Mitarbeiter-ID: ')
        self.id_field = QLineEdit()

        name_note = QLabel('Name: ')
        self.name = QLineEdit()

        username_note = QLabel('Nutzername: ')
        self.username = QLineEdit()

        passwort_note = QLabel('Passwort: ')
        self.passwort = QLineEdit()
        self.passwort.setEchoMode(QLineEdit.Password)

        self.submit = QPushButton('Erstellen')
        self.submit.clicked.connect(self.createMitarbeiter)

        self.layout.addWidget(title, 0, 0, 1, 0, Qt.AlignTop|Qt.AlignCenter)

        self.layout.addWidget(id_note, 1, 0, Qt.AlignLeft)
        self.layout.addWidget(self.id_field, 1, 1, Qt.AlignRight)

        self.layout.addWidget(name_note, 2, 0, Qt.AlignLeft)
        self.layout.addWidget(self.name, 2, 1, Qt.AlignRight)

        self.layout.addWidget(username_note, 3, 0, Qt.AlignLeft)
        self.layout.addWidget(self.username, 3, 1, Qt.AlignRight)

        self.layout.addWidget(passwort_note, 4, 0, Qt.AlignLeft)
        self.layout.addWidget(self.passwort, 4, 1, Qt.AlignRight)

        self.layout.addWidget(self.submit, 5, 0, 1, 0,  Qt.AlignCenter)