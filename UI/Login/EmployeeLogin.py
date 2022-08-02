import time
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import Wydbid
from BackEnd.Login import EmployeeLoginLogic
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

    def startEmployeeLogin(self):
        EmployeeLoginLogic.login(self.username.text(),
                                 self.password.text(),
                                 self)

    def setupUI(self):
        self.layout.setAlignment(Qt.AlignTop| Qt.AlignHCenter)

        self.title = QLabel(time.strftime('%d.%m.%y'))
        self.title.setFont(QFont('Montserrat', 30))

        username_note = QLabel(parent=self, text='Username: ')
        self.username = QLineEdit(parent=self)
        self.username.returnPressed.connect(self.startEmployeeLogin)

        password_note = QLabel(parent=self, text='Password: ')
        self.password = QLineEdit(parent=self)
        self.password.setEchoMode(QLineEdit.Password)
        self.password.returnPressed.connect(self.startEmployeeLogin)

        submit = QPushButton(parent=self, text='Confirm')
        submit.clicked.connect(self.startEmployeeLogin)

        verticalSpacer = QSpacerItem(40, 20, QSizePolicy.Minimum, QSizePolicy.Expanding)
        self.layout.addItem(verticalSpacer, 6, 0, Qt.AlignTop)

        # Set distance between top and content
        self.layout.setContentsMargins(0, 30, 0, 0)

        self.layout.addWidget(self.title, 1, 0, 1, 0, Qt.AlignCenter)

        self.layout.addWidget(username_note, 2, 0, Qt.AlignLeft)
        self.layout.addWidget(self.username, 2, 1, Qt.AlignRight)

        self.layout.addWidget(password_note, 3, 0, Qt.AlignLeft)
        self.layout.addWidget(self.password, 3, 1, Qt.AlignRight)

        self.layout.addWidget(submit, 4, 0, 1, 0, Qt.AlignCenter)
    
    def clear(self):
        self.username.setText('')
        self.password.setText('')
    
    def logoutCompany(self):
        EmployeeLoginLogic.logoutCompany(employee_login_widget=self)

    def startCreateEmployee(self):
        self.cm.clear()
        self.cm.show()

    def startDelEmployee(self):
        self.dm.show()
        self.dm.clear()

    def startChangeEmployeePassword(self):
        self.cmp.clear()
        self.cmp.show()

    def setupMenuBar(self):
        self.menubar = QMenuBar(parent=self)

        file = QMenu(parent=self.menubar, title='Wydbid')
        help = QMenu(parent=self.menubar, title='Help')

        create_employee = QAction('Create employee', self)
        del_employee = QAction('Delete employee', self)
        change_employee_password = QAction('Change employee password', self)
        logout_company = QAction('Log out company', self)
        close = QAction('Exit', self)

        contact = QAction('Contact', self)
        report_bug = QAction('Report error', self)

        create_employee.triggered.connect(self.startCreateEmployee)
        del_employee.triggered.connect(self.startDelEmployee)
        change_employee_password.triggered.connect(self.startChangeEmployeePassword)
        logout_company.triggered.connect(self.logoutCompany)
        close.triggered.connect(self.closeApp)

        contact.triggered.connect(WydbidUIMainLogic.contact)
        report_bug.triggered.connect(WydbidUIMainLogic.contact)

        file.addAction(create_employee)
        file.addAction(del_employee)
        file.addAction(change_employee_password)
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