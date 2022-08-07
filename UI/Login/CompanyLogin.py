import time
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import Wydbid
from BackEnd.WydbidBackEnd import WydbidUIMainLogic
from UI.Login.Prefabs import CreateCompany, DelCompany, ChangeCompanyPassword
from BackEnd.Login import CompanyLoginLogic
import screeninfo

class CompanyLogin(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__()

        self.layout = QGridLayout()

        self.setLayout(self.layout)
        self.setWindowTitle('Wydbid - Company-Login')
        width = screeninfo.get_monitors()[0].width
        height = screeninfo.get_monitors()[0].height
        self.setGeometry(0, 0, width, height)

        self.use_close_event = True

        self.cf = CreateCompany.CreateCompany()
        self.del_company = DelCompany.DelCompany()
        self.cfp = ChangeCompanyPassword.ChangeCompanyPassword()

        self.setupUI()
        self.setupMenuBar()
        self.repaint()

    def closeEvent(self, event: QCloseEvent):
        if self.use_close_event:
            reply = QMessageBox.question(self, 'Are you sure?', 'Are you sure you want to quit Wydbid?',
                                         QMessageBox.Yes, QMessageBox.No)

            if reply == QMessageBox.Yes:
                Wydbid.app.exit(0)
            else:
                event.ignore()
                pass
        else:
            event.accept()

    def addItemsToCompany(self):
        CompanyLoginLogic.addItems(self.company)

    def login(self):
        CompanyLoginLogic.login(self, self.company, self.password.text())

    def setupUI(self):
        self.layout.setAlignment(Qt.AlignTop| Qt.AlignHCenter)

        title = QLabel(time.strftime('%d.%m.%y'))
        title.setFont(QFont('Montserrat', 30))

        company_note = QLabel(parent=self, text='Company: ')
        self.company = QComboBox(parent=self)
        self.addItemsToCompany()

        password_note = QLabel(parent=self, text='Password: ')
        self.password = QLineEdit(parent=self)
        self.password.setEchoMode(QLineEdit.Password)
        self.password.returnPressed.connect(self.login)

        submit = QPushButton(parent=self, text='Confirm')
        submit.clicked.connect(self.login)

        verticalSpacer = QSpacerItem(40, 20, QSizePolicy.Minimum, QSizePolicy.Expanding)    
        self.layout.addItem(verticalSpacer, 6, 0, Qt.AlignTop)

        # Set distance between top and content
        self.layout.setContentsMargins(0, 30, 0, 0)

        self.layout.addWidget(title, 1, 0, 1, 0,  Qt.AlignCenter)

        self.layout.addWidget(company_note, 2, 0, Qt.AlignLeft)
        self.layout.addWidget(self.company, 2, 1, Qt.AlignRight)

        self.layout.addWidget(password_note, 3, 0, Qt.AlignLeft)
        self.layout.addWidget(self.password, 3, 1, Qt.AlignRight)

        self.layout.addWidget(submit, 4, 0, 1, 0, Qt.AlignCenter)

    def startCreateCompany(self):
        self.cf.clear(clearOnlyId=False)
        self.cf.show()

    def startDelCompany(self):
        self.del_company.clear()
        self.del_company.show()

    def startChangeCompanyPassword(self):
        self.cfp.show()

    def setupMenuBar(self):
        self.menubar = QMenuBar(parent=self)

        file = QMenu(parent=self.menubar, title='Wydbid')
        help = QMenu(parent=self.menubar, title='Help')

        create_company = QAction('Create company', self)
        del_company = QAction('Delete company', self)
        change_company_password = QAction('Change company password', self)
        close = QAction('Exit', self)

        contact = QAction('Contact', self)
        report_bug = QAction('Report error', self)

        create_company.triggered.connect(self.startCreateCompany)
        del_company.triggered.connect(self.startDelCompany)
        change_company_password.triggered.connect(self.startChangeCompanyPassword)
        close.triggered.connect(self.closeApp)

        contact.triggered.connect(WydbidUIMainLogic.contact)
        report_bug.triggered.connect(WydbidUIMainLogic.contact)

        file.addAction(create_company)
        file.addAction(del_company)
        file.addAction(change_company_password)
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