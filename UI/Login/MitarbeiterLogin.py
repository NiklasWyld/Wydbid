import sys
import time
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import Wydbid
from BackEnd import MitarbeiterLoginLogic
from UI.Prefabs import CreateMitarbeiter, DelMitarbeiter, ChangeMitarbeiterPasswort

class MitarbeiterLogin(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__()

        self.layout = QGridLayout()

        self.setLayout(self.layout)
        self.setWindowTitle('Wydbid - Mitarbeiter-Login')
        self.setGeometry(0, 0, 1920, 1080)

        self.cm = CreateMitarbeiter.CreateMitarbeiter()
        self.dm = DelMitarbeiter.DelMitarbeiter()
        self.cmp = ChangeMitarbeiterPasswort.ChangeMitarbeiterPasswort()

        self.setupUI()
        self.setupMenuBar()
        self.repaint()

    def closeEvent(self, event: QCloseEvent):
        reply = QMessageBox.question(self, 'Bist du sicher?', 'Bist du sicher, Wydbid beenden möchtest?',
                                     QMessageBox.Yes, QMessageBox.No)

        if reply == QMessageBox.Yes:
            sys.exit(0)
        else:
            event.ignore()
            pass

    def startMitarbeiterLogin(self):
        MitarbeiterLoginLogic.login(self.username.text(),
                                    self.passwort.text(),
                                    self)

    def setupUI(self):
        self.layout.setAlignment(Qt.AlignTop| Qt.AlignHCenter)

        self.title = QLabel(time.strftime('%d.%m.%y'))
        self.title.setFont(QFont('Montserrat', 30))

        username_note = QLabel(parent=self, text='Nutzername: ')
        self.username = QLineEdit(parent=self)
        self.username.returnPressed.connect(self.startMitarbeiterLogin)

        passwort_note = QLabel(parent=self, text='Passwort: ')
        self.passwort = QLineEdit(parent=self)
        self.passwort.setEchoMode(QLineEdit.Password)
        self.passwort.returnPressed.connect(self.startMitarbeiterLogin)

        submit = QPushButton(parent=self, text='Bestätigen')
        submit.clicked.connect(self.startMitarbeiterLogin)

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

    def startCreateMitarbeiter(self):
        self.cm.clear()
        self.cm.show()

    def startDelMitarbeiter(self):
        self.dm.show()
        self.dm.clear()

    def startChangeMitarbeiterPasswort(self):
        self.cmp.clear()
        self.cmp.show()

    def setupMenuBar(self):
        self.menubar = QMenuBar(parent=self)

        file = QMenu(parent=self.menubar, title='Wydbid')

        create_mitarbeiter = QAction('Mitarbeiter erstellen', self)
        del_mitarbeiter = QAction('Mitarbeiter löschen', self)
        change_mitarbeiter_passwort = QAction('Mitarbeiterpasswort ändern', self)
        logout_company = QAction('Firma abmelden', self)
        close = QAction('Beenden', self)

        create_mitarbeiter.triggered.connect(self.startCreateMitarbeiter)
        del_mitarbeiter.triggered.connect(self.startDelMitarbeiter)
        change_mitarbeiter_passwort.triggered.connect(self.startChangeMitarbeiterPasswort)
        logout_company.triggered.connect(self.logoutCompany)
        close.triggered.connect(Wydbid.close)

        file.addAction(create_mitarbeiter)
        file.addAction(del_mitarbeiter)
        file.addAction(change_mitarbeiter_passwort)
        file.addSeparator()
        file.addAction(logout_company)
        file.addSeparator()
        file.addAction(close)
        self.menubar.addMenu(file)

    def resizeEvent(self, QResizeEvent):
        # Is needed because otherwise the MenuBar is only big enough to show the content
        super().resizeEvent(QResizeEvent)

        self.menubar.resize(self.width(), 20)