from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from BackEnd.WydbidBackEnd import CustomerLogic

class CreateCustomer(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__()

        self.layout = QGridLayout()

        self.setLayout(self.layout)
        self.setWindowTitle('Wydbid - Create customer')
        self.setGeometry(0, 0, 600, 600)

        CustomerLogic.setupKundenFolder()
        self.setupUI()

    def setupUI(self):
        self.layout.setAlignment(Qt.AlignTop | Qt.AlignHCenter)

        title = QLabel('Create customer')
        title.setFont(QFont('Montserrat', 30))

        id_note = QLabel(parent=self, text='Customer-ID: ')
        self.id_tick = QCheckBox(parent=self, text='Asign Customer ID automatically')
        self.id = QLineEdit(parent=self)
        self.id.setFixedWidth(60)

        vorname_note = QLabel(parent=self, text='First name: ')
        self.vorname = QLineEdit(parent=self)

        nachname_note = QLabel(parent=self, text='Last name: ')
        self.nachname = QLineEdit(parent=self)

        email_note = QLabel(parent=self, text='E-mail address: ')
        self.email = QLineEdit(parent=self)

        adresse_note = QLabel(parent=self, text='Address: ')
        self.adresse = QLineEdit(parent=self)

        nummer_note = QLabel(parent=self, text='Telephone number: ')
        self.nummer = QLineEdit(parent=self)

        geschlecht_note = QLabel(parent=self, text='Gender: ')
        self.geschlecht = QComboBox(parent=self)
        self.geschlecht.addItem('Männlich', 'men')
        self.geschlecht.addItem('Weiblich', 'women')

        geburtsdatum_note = QLabel(parent=self, text='Birth date: ')
        self.geburtsdatum = QLineEdit(parent=self)

        informationen_note = QLabel(parent=self, text='Information: ')
        self.informationen = QTextEdit(parent=self)

        submit = QPushButton(parent=self, text='Create')
        submit.clicked.connect(lambda: CustomerLogic.createKunde(create_kunde=self))

        self.layout.addWidget(title, 1, 0, 1, 0, Qt.AlignCenter)

        self.layout.addWidget(self.id_tick, 2, 1, Qt.AlignRight)
        self.layout.addWidget(id_note, 3, 0, Qt.AlignLeft)
        self.layout.addWidget(self.id, 3, 1, Qt.AlignRight)

        self.layout.addWidget(vorname_note, 4, 0, Qt.AlignLeft)
        self.layout.addWidget(self.vorname, 4, 1, Qt.AlignRight)

        self.layout.addWidget(nachname_note, 5, 0, Qt.AlignLeft)
        self.layout.addWidget(self.nachname, 5, 1, Qt.AlignRight)

        self.layout.addWidget(email_note, 6, 0, Qt.AlignLeft)
        self.layout.addWidget(self.email, 6, 1, Qt.AlignRight)

        self.layout.addWidget(adresse_note, 7, 0, Qt.AlignLeft)
        self.layout.addWidget(self.adresse, 7, 1, Qt.AlignRight)

        self.layout.addWidget(nummer_note, 8, 0, Qt.AlignLeft)
        self.layout.addWidget(self.nummer, 8, 1, Qt.AlignRight)

        self.layout.addWidget(geschlecht_note, 9, 0, Qt.AlignLeft)
        self.layout.addWidget(self.geschlecht, 9, 1, Qt.AlignRight)

        self.layout.addWidget(geburtsdatum_note, 10, 0, Qt.AlignLeft)
        self.layout.addWidget(self.geburtsdatum, 10, 1, Qt.AlignRight)

        self.layout.addWidget(informationen_note, 11, 0, Qt.AlignLeft)
        self.layout.addWidget(self.informationen, 11, 1, Qt.AlignRight)

        self.layout.addWidget(submit, 12, 0, 1, 0, Qt.AlignCenter)

    def clear(self):
        self.id.setText('')
        self.vorname.setText('')
        self.nachname.setText('')
        self.email.setText('')
        self.adresse.setText('')
        self.nummer.setText('')
        self.geschlecht.setCurrentIndex(0)
        self.geburtsdatum.setText('')
        self.informationen.setText('')