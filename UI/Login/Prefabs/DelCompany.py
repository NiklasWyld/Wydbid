from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from BackEnd import CreateCompanyLogic, CompanyLoginLogic, DelCompanyLogic


class DelCompany(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__()

        self.layout = QGridLayout()

        self.setLayout(self.layout)
        self.setWindowTitle('Wydbid - Delete company')
        self.setGeometry(0, 0, 600, 450)

        self.widget = self

        self.setupUI()

    def clear(self):
        self.passwort.setText('')

    def addItemsToFirma(self):
        DelCompanyLogic.addItems(self.firma)

    def delFirma(self):
        DelCompanyLogic.getFirma(self.firma, self.passwort.text(), self.widget)

    def setupUI(self):
        self.layout.setAlignment(Qt.AlignTop | Qt.AlignHCenter)

        title = QLabel('Delete company')
        title.setFont(QFont('Montserrat', 30))

        firmen_note = QLabel(parent=self, text='Company: ')
        self.firma = QComboBox(parent=self)
        self.addItemsToFirma()

        passwort_note = QLabel(parent=self, text='Password: ')
        self.passwort = QLineEdit(parent=self)
        self.passwort.setEchoMode(QLineEdit.Password)
        self.passwort.returnPressed.connect(self.delFirma)

        submit = QPushButton(parent=self, text='Delete')
        submit.clicked.connect(self.delFirma)

        self.layout.addWidget(title, 1, 0, 1, 0, Qt.AlignCenter)

        self.layout.addWidget(firmen_note, 2, 0, Qt.AlignLeft)
        self.layout.addWidget(self.firma, 2, 1, Qt.AlignRight)

        self.layout.addWidget(passwort_note, 3, 0, Qt.AlignLeft)
        self.layout.addWidget(self.passwort, 3, 1, Qt.AlignRight)

        self.layout.addWidget(submit, 4, 0, 1, 0, Qt.AlignCenter)