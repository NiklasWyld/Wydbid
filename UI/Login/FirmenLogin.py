import time
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import Wydbid
from BackEnd.WydbidBackEnd import WydbidUIMainLogic
from UI.Login.Prefabs import CreateFirma, DelFirma, ChangeFirmenPasswort
from BackEnd import FirmenLoginLogic
import screeninfo


class FirmenLogin(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__()

        self.layout = QGridLayout()

        self.setLayout(self.layout)
        self.setWindowTitle('Wydbid - Firmen-Login')
        width = screeninfo.get_monitors()[0].width
        height = screeninfo.get_monitors()[0].height
        self.setGeometry(0, 0, width, height)

        self.cf = CreateFirma.CreateFirma()
        self.del_firma = DelFirma.DelFirma()
        self.cfp = ChangeFirmenPasswort.ChangeFirmenPasswort()

        self.setupUI()
        self.setupMenuBar()
        self.repaint()

    def closeEvent(self, event: QCloseEvent):
        reply = QMessageBox.question(self, 'Bist du sicher?', 'Bist du sicher, Wydbid beenden möchtest?',
                                     QMessageBox.Yes, QMessageBox.No)

        if reply == QMessageBox.Yes:
            Wydbid.app.exit(0)
        else:
            event.ignore()
            pass

    def addItemsToFirma(self):
        FirmenLoginLogic.addItems(self.firma)

    def login(self):
        FirmenLoginLogic.login(self, self.firma, self.passwort.text())

    def setupUI(self):
        self.layout.setAlignment(Qt.AlignTop | Qt.AlignHCenter)

        title = QLabel(time.strftime('%d.%m.%y'))
        title.setFont(QFont('Montserrat', 30))

        firmen_note = QLabel(parent=self, text='Firma: ')
        self.firma = QComboBox(parent=self)
        self.addItemsToFirma()

        passwort_note = QLabel(parent=self, text='Passwort: ')
        self.passwort = QLineEdit(parent=self)
        self.passwort.setEchoMode(QLineEdit.Password)
        self.passwort.returnPressed.connect(self.login)

        submit = QPushButton(parent=self, text='Bestätigen')
        submit.clicked.connect(self.login)

        verticalSpacer = QSpacerItem(
            40, 20, QSizePolicy.Minimum, QSizePolicy.Expanding)
        self.layout.addItem(verticalSpacer, 6, 0, Qt.AlignTop)

        # Set distance between top and content
        self.layout.setContentsMargins(0, 30, 0, 0)

        self.layout.addWidget(title, 1, 0, 1, 0, Qt.AlignCenter)

        self.layout.addWidget(firmen_note, 2, 0, Qt.AlignLeft)
        self.layout.addWidget(self.firma, 2, 1, Qt.AlignRight)

        self.layout.addWidget(passwort_note, 3, 0, Qt.AlignLeft)
        self.layout.addWidget(self.passwort, 3, 1, Qt.AlignRight)

        self.layout.addWidget(submit, 4, 0, 1, 0, Qt.AlignCenter)

    def startCreateFirma(self):
        self.cf.clear(clearOnlyId=False)
        self.cf.show()

    def startDelFirma(self):
        self.del_firma.clear()
        self.del_firma.show()

    def startChangeFirmenPasswort(self):
        self.cfp.show()

    def setupMenuBar(self):
        self.menubar = QMenuBar(parent=self)

        file = QMenu(parent=self.menubar, title='Wydbid')
        help = QMenu(parent=self.menubar, title='Hilfe')

        create_company = QAction('Firma erstellen', self)
        del_company = QAction('Firma löschen', self)
        change_company_password = QAction('Firmenpasswort ändern', self)
        reset = QAction('Programm zurücksetzen', self)
        close = QAction('Beenden', self)

        contact = QAction('Kontakt', self)
        report_bug = QAction('Fehler melden', self)

        create_company.triggered.connect(self.startCreateFirma)
        del_company.triggered.connect(self.startDelFirma)
        change_company_password.triggered.connect(
            self.startChangeFirmenPasswort)
        reset.triggered.connect(Wydbid.reset)
        close.triggered.connect(self.closeApp)

        contact.triggered.connect(WydbidUIMainLogic.contact)
        report_bug.triggered.connect(WydbidUIMainLogic.contact)

        file.addAction(create_company)
        file.addAction(del_company)
        file.addAction(change_company_password)
        file.addSeparator()
        file.addAction(reset)
        file.addSeparator()
        file.addAction(close)
        self.menubar.addMenu(file)

        help.addAction(contact)
        help.addAction(report_bug)

        self.menubar.addMenu(help)

    def resizeEvent(self, QResizeEvent):
        # Is needed because otherwise the MenuBar is only big enough to show the content
        super().resizeEvent(QResizeEvent)

        self.menubar.resize(self.width(), 20)

    def closeApp(self):
        Wydbid.app.exit(0)
