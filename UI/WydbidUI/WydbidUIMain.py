from datetime import datetime
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import Wydbid
from BackEnd.WydbidBackEnd import WydbidUIMainLogic
from CustomQt import ActionButton
from UI.WydbidUI.Prefabs import Settings
from UI.WydbidUI.Prefabs.Customer import CreateCustomer
import screeninfo

# ToDo: Update pictures in README.md
# ToDo: Tasks and News / New Tabs in Main / ...
# ToDo: Translate into English

class WydbidUIMain(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__()

        self.setWindowTitle('Wydbid - Center')
        width = screeninfo.get_monitors()[0].width
        height = screeninfo.get_monitors()[0].height
        self.setGeometry(0, 0, width, height)

        self.setLayout(QGridLayout())
        self.layout().setContentsMargins(30, 30, 30, 30)

        # Tabwidget
        self.tabwidget = QTabWidget(parent=self)

        # Widgets
        self.ck = CreateCustomer.CreateCustomer()

        self.setupUI()
        self.setupMenuBar()

    def closeEvent(self, event: QCloseEvent):
        reply = QMessageBox.question(self, 'Are you sure?', 'Are you sure you want to quit Wydbid?',
                                     QMessageBox.Yes, QMessageBox.No)

        if reply == QMessageBox.Yes:
            Wydbid.app.exit(0)
        else:
            event.ignore()
            pass

    def setupUI(self):
        date_time = QGroupBox(parent=self, title='Date and time')
        date_time.setFixedHeight(150)
        self.setupDateTime(date_time)

        action_list = QGroupBox(parent=self, title='Actions')
        action_list.setFixedWidth(200)
        self.setupActionBox(action_list)

        customer_widget = QWidget()
        self.setupCustomerList(customerlist=customer_widget)

        appointment_widget = QWidget()

        order_widget = QWidget()

        event_widget = QWidget()

        email_widget = QWidget()

        self.tabwidget.addTab(customer_widget, 'Customer list')
        self.tabwidget.addTab(appointment_widget, 'Appointments')
        self.tabwidget.addTab(order_widget, 'Orders')
        self.tabwidget.addTab(event_widget, 'Events')
        self.tabwidget.addTab(email_widget, 'Emails')

        self.layout().addWidget(date_time, 0, 0, 1, 0)
        self.layout().addWidget(action_list, 1, 0)
        self.layout().addWidget(self.tabwidget, 1, 1)

    def setupMenuBar(self):
        self.menubar = QMenuBar(parent=self)
        file = QMenu(parent=self.menubar, title='Wydbid')
        help = QMenu(parent=self.menubar, title='Help')

        logout_employee = QAction('Deregister employee', self)
        logout_company = QAction('Log out from company', self)
        reset_programm = QAction('Reset Wydbid', self)
        settings = QAction('Settings', self)
        close = QAction('Exit', self)

        contact = QAction('Contact', self)
        report_bug = QAction('Report error', self)

        logout_employee.triggered.connect(lambda: WydbidUIMainLogic.logoutEmployee(self))
        logout_company.triggered.connect(self.startCompanyLogout)
        reset_programm.triggered.connect(Wydbid.reset)
        settings.triggered.connect(self.startSettings)
        close.triggered.connect(self.closeApp)

        contact.triggered.connect(WydbidUIMainLogic.contact)
        report_bug.triggered.connect(WydbidUIMainLogic.contact)

        file.addAction(logout_employee)
        file.addAction(logout_company)
        file.addSeparator()
        file.addAction(reset_programm)
        file.addSeparator()
        file.addAction(settings)
        file.addSeparator()
        file.addAction(close)

        help.addAction(contact)
        help.addAction(report_bug)

        self.menubar.addMenu(file)
        self.menubar.addMenu(help)

    def startSettings(self):
        settings = Settings.Settings()
        settings.show()

    def startCompanyLogout(self):
        WydbidUIMainLogic.logoutCompany(widget=self)

    def resizeEvent(self, QResizeEvent):
        # Is needed because otherwise the MenuBar is only big enough to show the content
        super().resizeEvent(QResizeEvent)

        self.menubar.resize(self.width(), 20)

    def setupActionBox(self, action_list: QComboBox):
        action_list.setLayout(QGridLayout())
        action_list.layout().setAlignment(Qt.AlignTop| Qt.AlignHCenter)

        # Customers
        customer_note = QLabel(parent=action_list, text='Customers 👨')
        customer_actions = ActionButton.ActionButton(parent=action_list, text='Customer Actions ➜', color='lightskyblue', color_hover='blue')

        # Appointments
        appointment_note = QLabel(parent=action_list, text='Appointments 📅')
        appointment_actions = ActionButton.ActionButton(parent=action_list, text='Appointment Actions ➜', color='lightgreen', color_hover='green')

        # Orders
        order_note = QLabel(parent=action_list, text='Orders 📦')
        order_actions = ActionButton.ActionButton(parent=action_list, text='Order Actions ➜', color='lightcoral', color_hover='red')

        # Events
        event_note = QLabel(parent=action_list, text='Events 📝')
        event_actions = ActionButton.ActionButton(parent=action_list, text='Event Actions ➜', color='lightsalmon', color_hover='orange')

        # Emails
        email_note = QLabel(parent=action_list, text='E-Mail ✉')
        email_actions = ActionButton.ActionButton(parent=action_list, text='E-Mail Actions ➜', color='darkslateblue', color_hover='purple')

        # Customer Layout Management
        action_list.layout().addWidget(customer_note, 0, 0, 1, 0, Qt.AlignLeft)
        action_list.layout().addWidget(customer_actions, 2, 0, 1, 0, Qt.AlignCenter)

        # Appointment Layout Management
        action_list.layout().addWidget(appointment_note, 5, 0, 1, 0, Qt.AlignLeft)
        action_list.layout().addWidget(appointment_actions, 7, 0, 1, 0, Qt.AlignCenter)

        # Order Layout Management
        action_list.layout().addWidget(order_note, 10, 0, 1, 0, Qt.AlignLeft)
        action_list.layout().addWidget(order_actions, 12, 0, 1, 0, Qt.AlignCenter)

        # Event Layout Management
        action_list.layout().addWidget(event_note, 15, 0, 1, 0, Qt.AlignLeft)
        action_list.layout().addWidget(event_actions, 17, 0, 1, 0, Qt.AlignCenter)

        # E-Mail Layout Management
        action_list.layout().addWidget(email_note, 19, 0, 1, 0, Qt.AlignLeft)
        action_list.layout().addWidget(email_actions, 22, 0, 1, 0, Qt.AlignCenter)

        # ToDo: Event Management

        # Customer Event Management
        #add_customer.clicked.connect(self.startCreateCustomer)

    # Setup tab widgets

    def setupCustomerList(self, customerlist: QWidget):
        # Layout declarations
        lyt = QVBoxLayout()
        hlyt = QHBoxLayout()

        self.searchbar = QLineEdit(parent=customerlist)
        self.searchbar.setFixedHeight(40)
        self.searchbar.setPlaceholderText('Filter by name')

        self.customerlist = QTableWidget(parent=customerlist)
        self.customerlist.verticalHeader().setVisible(False)

        self.customerlist.setColumnCount(8)
        self.customerlist.setHorizontalHeaderLabels(['Customer id', 'Name', 'E-mail address', 'Adress', 'Number', 'Gender', 'Birth date', ''])

        WydbidUIMainLogic.appendCustomers(customerlist=self.customerlist)

        self.customerlist.setSortingEnabled(True)
        self.customerlist.setFocusPolicy(Qt.NoFocus)
        self.customerlist.setSelectionMode(QAbstractItemView.SelectionMode.NoSelection)
        self.customerlist.setEditTriggers(QAbstractItemView.NoEditTriggers)

        self.searchbar.textChanged.connect(
            lambda: WydbidUIMainLogic.searchForName(search=self.searchbar, list=self.customerlist)
        )

        # Add customer list and search bar to main layout
        lyt.addWidget(self.searchbar, Qt.AlignCenter)
        lyt.addWidget(self.customerlist, Qt.AlignCenter)

        reload = QPushButton('Reload')
        reload.setFixedWidth(120)
        reload.clicked.connect(lambda: WydbidUIMainLogic.reloadCustomers(customerlist=self.customerlist))

        # Add reload button to bottom layout
        hlyt.addWidget(reload)

        # Add bottom layout to main layout
        lyt.addLayout(hlyt)

        # Set layout of customer list tab widget
        customerlist.setLayout(lyt)

    def setupDateTime(self, date_time: QGroupBox):
        self.time_label = QLabel(parent=date_time)
        self.time_label.setText('00:00:00')
        self.date_label = QLabel(parent=date_time)
        self.date_label.setText(datetime.now().date().strftime("%d.%m.%y"))

        self.time_label.setFont(QFont('Montserrat', 40))
        self.date_label.setFont(QFont('Montserrat', 25))

        date_time_layout = QGridLayout()

        date_time_layout.addWidget(self.time_label, 0, 0, 1, 0, Qt.AlignCenter)
        date_time_layout.addWidget(self.date_label, 1, 0, 1, 0, Qt.AlignCenter)

        date_time.setLayout(date_time_layout)

        # Loop to update the time
        timer = QTimer(self)
        timer.timeout.connect(self.updateClock)
        timer.start(1000)

    def updateClock(self):
        self.time_label.setText(datetime.now().strftime("%H:%M:%S"))

    def closeApp(self):
        Wydbid.app.exit(0)

    # Event Management Methods

    def startCreateCustomer(self):
        self.ck.show()
