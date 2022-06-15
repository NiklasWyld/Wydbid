import time
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from BackEnd import MitarbeiterLoginLogic

class MitarbeiterLogin(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__()

        self.layout = QGridLayout()

        self.setLayout(self.layout)
        self.setWindowTitle('Wydbid - Mitarbeiter-Login')
        self.setGeometry(0, 0, 1920, 1080)

        self.setupUI()
        self.setupMenuBar()
        self.repaint()

    def setupUI(self):
        self.layout.setAlignment(Qt.AlignTop| Qt.AlignHCenter)

        self.title = QLabel(time.strftime('%d.%m.%y'))
        self.title.setFont(QFont('Montserrat', 30))

        username_note = QLabel(parent=self, text='Nutzername: ')
        self.username = QLineEdit(parent=self)

        passwort_note = QLabel(parent=self, text='Passwort: ')
        self.passwort = QLineEdit(parent=self)
        self.passwort.setEchoMode(QLineEdit.Password)

        submit = QPushButton(parent=self, text='Bestätigen')
        # ToDo: Add Mitarbeiter Login

        verticalSpacer = QSpacerItem(40, 20, QSizePolicy.Minimum, QSizePolicy.Expanding)
        self.layout.addItem(verticalSpacer, 6, 0, Qt.AlignTop)

        # Set distance between top and content
        self.layout.setContentsMargins(0, 30, 0, 0)

        self.layout.addWidget(self.title, 1, 0, 1, 0, Qt.AlignCenter)

        self.layout.addWidget(username_note, 2, 0, Qt.AlignLeft)
        self.layout.addWidget(self.username, 2, 1, Qt.AlignRight)

        self.layout.addWidget(passwort_note, 3, 0, Qt.AlignLeft)
        self.layout.addWidget(self.passwort, 3, 1, Qt.AlignRight)

        self.layout.addWidget(submit, 4, 0, 1, 0, Qt.AlignCenter)
    
    def clear(self):
        self.username.setText('')
        self.passwort.setText('')
    
    def logoutCompany(self):
        MitarbeiterLoginLogic.logoutCompany(mitarbeiter_login_widget=self)
    
    def setupMenuBar(self):
        self.menubar = QMenuBar(parent=self)

        file = QMenu(parent=self.menubar, title='Wydbid')

        create_company = QAction('Mitarbeiter erstellen', self)
        del_company = QAction('Mitarbeiter löschen', self)
        logout_company = QAction('Firma abmelden', self)
        close = QAction('Beenden', self)

        # ToDo: Add Mitarbeiter erstellen
        # ToDo: Add Mitarbeiter loeschen
        # ToDo: Add Mitarbeiter Passwort aendern
        logout_company.triggered.connect(self.logoutCompany)
        close.triggered.connect(exit)

        file.addAction(create_company)
        file.addAction(del_company)
        file.addSeparator()
        file.addAction(logout_company)
        file.addSeparator()
        file.addAction(close)
        self.menubar.addMenu(file)

    def resizeEvent(self, QResizeEvent):
        # Is needed because otherwise the MenuBar is only big enough to show the content
        super().resizeEvent(QResizeEvent)

        self.menubar.resize(self.width(), 20)