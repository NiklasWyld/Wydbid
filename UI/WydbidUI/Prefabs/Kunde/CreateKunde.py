from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from BackEnd.WydbidBackEnd import KundeLogic

class CreateKunde(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__()

        self.layout = QGridLayout()

        self.setLayout(self.layout)
        self.setWindowTitle('Wydbid - Kunde erstellen')
        self.setGeometry(0, 0, 600, 600)

        KundeLogic.setupKundenFolder()
        self.setupUI()

    def setupUI(self):
        self.layout.setAlignment(Qt.AlignTop | Qt.AlignHCenter)

        title = QLabel('Kunde erstellen')
        title.setFont(QFont('Montserrat', 30))

        vorname_note = QLabel(parent=self, text='Vorname: ')
        self.vorname = QLineEdit(parent=self)

        nachname_note = QLabel(parent=self, text='Nachname: ')
        self.nachname = QLineEdit(parent=self)

        adresse_note = QLabel(parent=self, text='Adresse: ')
        self.adresse = QLineEdit(parent=self)

        nummer_note = QLabel(parent=self, text='Telefonnummer: ')
        self.nummer = QLineEdit(parent=self)

        geschlecht_note = QLabel(parent=self, text='Geschlecht: ')
        self.geschlecht = QComboBox(parent=self)
        self.geschlecht.addItem('Männlich', 'men')
        self.geschlecht.addItem('Weiblich', 'women')

        geburtsdatum_note = QLabel(parent=self, text='Geburtsdatum: ')
        self.geburtsdatum = QLineEdit(parent=self)

        informationen_note = QLabel(parent=self, text='Informationen: ')
        self.informationen = QTextEdit(parent=self)

        submit = QPushButton(parent=self, text='Erstellen')
        submit.clicked.connect(lambda: KundeLogic.createKunde(create_kunde=self))

        self.layout.addWidget(title, 1, 0, 1, 0, Qt.AlignCenter)

        self.layout.addWidget(vorname_note, 2, 0, Qt.AlignLeft)
        self.layout.addWidget(self.vorname, 2, 1, Qt.AlignRight)

        self.layout.addWidget(nachname_note, 3, 0, Qt.AlignLeft)
        self.layout.addWidget(self.nachname, 3, 1, Qt.AlignRight)

        self.layout.addWidget(adresse_note, 4, 0, Qt.AlignLeft)
        self.layout.addWidget(self.adresse, 4, 1, Qt.AlignRight)

        self.layout.addWidget(nummer_note, 5, 0, Qt.AlignLeft)
        self.layout.addWidget(self.nummer, 5, 1, Qt.AlignRight)

        self.layout.addWidget(geschlecht_note, 6, 0, Qt.AlignLeft)
        self.layout.addWidget(self.geschlecht, 6, 1, Qt.AlignRight)

        self.layout.addWidget(geburtsdatum_note, 7, 0, Qt.AlignLeft)
        self.layout.addWidget(self.geburtsdatum, 7, 1, Qt.AlignRight)

        self.layout.addWidget(informationen_note, 8, 0, Qt.AlignLeft)
        self.layout.addWidget(self.informationen, 8, 1, Qt.AlignRight)

        self.layout.addWidget(submit, 9, 0, 1, 0, Qt.AlignCenter)

    def clear(self):
        self.vorname.setText('')
        self.nachname.setText('')
        self.adresse.setText('')
        self.nummer.setText('')
        self.geschlecht.setCurrentIndex(0)
        self.geburtsdatum.setText('')
        self.informationen.setText('')