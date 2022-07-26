import sys
import time
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import Wydbid
from BackEnd import EmployeeLoginLogic
from BackEnd.WydbidBackEnd import WydbidUIMainLogic
from UI.Login.Prefabs import CreateEmployee, DelEmployee, ChangeEmployeePassword
import screeninfo

class EmployeeLogin(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__()

        self.layout = QGridLayout()

        self.setLayout(self.layout)
        self.setWindowTitle('Wydbid - Employee-Login')
        width = screeninfo.get_monitors()[0].width
        height = screeninfo.get_monitors()[0].height
        self.setGeometry(0, 0, width, height)

        self.cm = CreateEmployee.CreateEmployee()
        self.dm = DelEmployee.DelEmployee()
        self.cmp = ChangeEmployeePassword.ChangeEmployeePassword()

        self.setupUI()
        self.setupMenuBar()
        self.repaint()

    def closeEvent(self, event: QCloseEvent):
        reply = QMessageBox.question(self, 'Are you sure?', 'Are you sure you want to quit Wydbid?',
                                     QMessageBox.Yes, QMessageBox.No)

        if reply == QMessageBox.Yes:
            Wydbid.app.exit(0)
        else:
            event.ignore()
            pass

    def startMitarbeiterLogin(self):
        EmployeeLoginLogic.login(self.username.text(),
                                 self.passwort.text(),
                                 self)

    def setupUI(self):
        self.layout.setAlignment(Qt.AlignTop| Qt.AlignHCenter)

        self.title = QLabel(time.strftime('%d.%m.%y'))
        self.title.setFont(QFont('Montserrat', 30))

        username_note = QLabel(parent=self, text='Username: ')
        self.username = QLineEdit(parent=self)
        self.username.returnPressed.connect(self.startMitarbeiterLogin)

        passwort_note = QLabel(parent=self, text='Password: ')
        self.passwort = QLineEdit(parent=self)
        self.passwort.setEchoMode(QLineEdit.Password)
        self.passwort.returnPressed.connect(self.startMitarbeiterLogin)

        submit = QPushButton(parent=self, text='Confirm')
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
        EmployeeLoginLogic.logoutCompany(mitarbeiter_login_widget=self)

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
        help = QMenu(parent=self.menubar, title='Help')

        create_mitarbeiter = QAction('Create employee', self)
        del_mitarbeiter = QAction('Delete employee', self)
        change_mitarbeiter_passwort = QAction('Change employee password', self)
        logout_company = QAction('Log out company', self)
        close = QAction('Exit', self)

        contact = QAction('Contact', self)
        report_bug = QAction('Report error', self)

        create_mitarbeiter.triggered.connect(self.startCreateMitarbeiter)
        del_mitarbeiter.triggered.connect(self.startDelMitarbeiter)
        change_mitarbeiter_passwort.triggered.connect(self.startChangeMitarbeiterPasswort)
        logout_company.triggered.connect(self.logoutCompany)
        close.triggered.connect(self.closeApp)

        contact.triggered.connect(WydbidUIMainLogic.contact)
        report_bug.triggered.connect(WydbidUIMainLogic.contact)

        file.addAction(create_mitarbeiter)
        file.addAction(del_mitarbeiter)
        file.addAction(change_mitarbeiter_passwort)
        file.addSeparator()
        file.addAction(logout_company)
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