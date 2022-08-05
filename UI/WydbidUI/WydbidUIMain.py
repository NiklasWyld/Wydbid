from datetime import datetime
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import Wydbid
from BackEnd.WydbidBackEnd import WydbidUIMainLogic
from CustomQt import ActionButton
from UI.WydbidUI.Prefabs import Settings
from UI.WydbidUI.Prefabs.Customer import ViewCustomer
from UI.WydbidUI.Prefabs.News import ShowAllNews
from UI.WydbidUI.ActionPrefabs import CustomerActions, NewsActions
import screeninfo

class WydbidUIMain(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__()

        self.setWindowTitle('Wydbid - Center')
        width = screeninfo.get_monitors()[0].width
        height = screeninfo.get_monitors()[0].height
        self.setGeometry(0, 0, width, height)

        self.setLayout(QGridLayout())
        self.layout().setContentsMargins(30, 30, 30, 30)

        self.use_close_event = True

        self.vc = ViewCustomer.ViewCustomer()
        self.san = ShowAllNews.ShowAllNews()

        # Tabwidget
        self.tabwidget = QTabWidget(parent=self)

        # Action Widgets
        self.news_actions = NewsActions.NewsActions()
        self.customer_actions = CustomerActions.CustomerActions()

        self.setupUI()
        self.setupMenuBar()

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

    def setupUI(self):
        date_time = QGroupBox(parent=self, title='Date and time')
        date_time.setFixedHeight(150)
        self.setupDateTime(date_time)

        action_list = QGroupBox(parent=self, title='Actions')
        action_list.setFixedWidth(200)
        self.setupActionBox(action_list)

        news_widget = QWidget()
        self.setupNewsWidget(newswidget=news_widget)

        customer_widget = QWidget()
        self.setupCustomerList(customerlist=customer_widget)

        appointment_widget = QWidget()

        order_widget = QWidget()

        event_widget = QWidget()

        task_widget = QWidget()

        email_widget = QWidget()

        self.tabwidget.addTab(news_widget, 'News')
        self.tabwidget.addTab(customer_widget, 'Customer list')
        self.tabwidget.addTab(appointment_widget, 'Appointments')
        self.tabwidget.addTab(order_widget, 'Orders')
        self.tabwidget.addTab(event_widget, 'Events')
        self.tabwidget.addTab(task_widget, 'Tasks')
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

    def setupActionBox(self, action_list: QGroupBox):
        action_list.setLayout(QGridLayout())
        action_list.layout().setAlignment(Qt.AlignTop| Qt.AlignHCenter)

        # News
        news_note = QLabel(parent=action_list, text='News 📰')
        news_actions = ActionButton.ActionButton(parent=action_list, text='News Actions ➜', color='darkcyan', color_hover='teal')

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

        # Tasks
        task_note = QLabel(parent=action_list, text='Tasks ✔️')
        task_actions = ActionButton.ActionButton(parent=action_list, text='Task Actions ➜', color='violet', color_hover='mediumorchid')

        # Emails
        email_note = QLabel(parent=action_list, text='E-Mail ✉')
        email_actions = ActionButton.ActionButton(parent=action_list, text='E-Mail Actions ➜', color='darkslateblue', color_hover='purple')

        # News Layout Management
        action_list.layout().addWidget(news_note, 0, 0, 1, 0, Qt.AlignLeft)
        action_list.layout().addWidget(news_actions, 1, 0, 1, 0, Qt.AlignCenter)

        # Customer Layout Management
        action_list.layout().addWidget(customer_note, 2, 0, 1, 0, Qt.AlignLeft)
        action_list.layout().addWidget(customer_actions, 3, 0, 1, 0, Qt.AlignCenter)

        # Appointment Layout Management
        action_list.layout().addWidget(appointment_note, 4, 0, 1, 0, Qt.AlignLeft)
        action_list.layout().addWidget(appointment_actions, 5, 0, 1, 0, Qt.AlignCenter)

        # Order Layout Management
        action_list.layout().addWidget(order_note, 6, 0, 1, 0, Qt.AlignLeft)
        action_list.layout().addWidget(order_actions, 7, 0, 1, 0, Qt.AlignCenter)

        # Event Layout Management
        action_list.layout().addWidget(event_note, 8, 0, 1, 0, Qt.AlignLeft)
        action_list.layout().addWidget(event_actions, 9, 0, 1, 0, Qt.AlignCenter)

        # Task Layout Management
        action_list.layout().addWidget(task_note, 10, 0, 1, 0, Qt.AlignLeft)
        action_list.layout().addWidget(task_actions, 11, 0, 1, 0, Qt.AlignCenter)

        # E-Mail Layout Management
        action_list.layout().addWidget(email_note, 12, 0, 1, 0, Qt.AlignLeft)
        action_list.layout().addWidget(email_actions, 13, 0, 1, 0, Qt.AlignCenter)

        # ToDo: Event Management

        news_actions.clicked.connect(self.startNewsActions)
        customer_actions.clicked.connect(self.startCustomerActions)

    # Setup tab widgets

    def setupNewsWidget(self, newswidget: QWidget):
        # ToDo: Load newest News

        # Layout declarations
        lyt = QVBoxLayout()
        hlyt = QHBoxLayout()

        self.news_title = QLabel(parent=newswidget)
        self.news_title.setAlignment(Qt.AlignCenter)
        self.news_title.setFont(QFont('Arial', 20))
        self.news_title.setFixedHeight(40)

        self.news_description = QTextEdit(parent=newswidget)
        self.news_description.setEnabled(False)

        self.setLatestNews()

        showall = QPushButton(parent=newswidget, text='Show all')
        showall.clicked.connect(self.startViewAllNews)
        showall.setFixedWidth(120)

        lyt.addWidget(self.news_title, Qt.AlignCenter)
        lyt.addWidget(self.news_description, Qt.AlignCenter)

        hlyt.addWidget(showall)

        lyt.addLayout(hlyt)

        newswidget.setLayout(lyt)

    def setupCustomerList(self, customerlist: QWidget):
        # Layout declarations
        lyt = QVBoxLayout()
        hlyt = QHBoxLayout()

        self.searchbar_first = QLineEdit(parent=customerlist)
        self.searchbar_first.setFixedHeight(40)
        self.searchbar_first.setPlaceholderText('Filter by first name')

        self.searchbar_last = QLineEdit(parent=customerlist)
        self.searchbar_last.setFixedHeight(40)
        self.searchbar_last.setPlaceholderText('Filter by last name')

        self.customerlist = QTableWidget(parent=customerlist)
        self.customerlist.verticalHeader().setVisible(False)

        self.customerlist.setColumnCount(9)
        self.customerlist.setHorizontalHeaderLabels(
        ['Customer id', 'Firstname', 'Lastname', 'E-mail address', 'Adress', 'Number', 'Gender', 'Birth date', ''])

        WydbidUIMainLogic.appendCustomers(customerlist=self.customerlist)

        self.customerlist.setSortingEnabled(True)
        self.customerlist.setFocusPolicy(Qt.NoFocus)
        self.customerlist.setSelectionMode(QAbstractItemView.SelectionMode.NoSelection)
        self.customerlist.setEditTriggers(QAbstractItemView.NoEditTriggers)

        self.searchbar_first.textChanged.connect(
            lambda: WydbidUIMainLogic.searchForFirstName(searchfirst=self.searchbar_first, searchlast=self.searchbar_last,
                                                         list=self.customerlist)
        )

        self.searchbar_last.textChanged.connect(
            lambda: WydbidUIMainLogic.searchForLastName(searchfirst=self.searchbar_first, searchlast=self.searchbar_last,
                                                        list=self.customerlist)
        )

        self.customerlist.clicked.connect(
            self.loadViewCustomer
        )

        # Add customer list and search bar to main layout
        lyt.addWidget(self.searchbar_first, Qt.AlignCenter)
        lyt.addWidget(self.searchbar_last, Qt.AlignCenter)
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

    def loadViewCustomer(self, item):
        if item.data() == '🔎':
            WydbidUIMainLogic.viewCustomer(self.customerlist, self.vc, item)

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

    def startViewAllNews(self):
        self.san.appendNews()
        self.san.show()

    def setNews(self, news):
        self.news_title.setText(news.title)
        self.news_description.setText(news.description)

    def setLatestNews(self):
        news = WydbidUIMainLogic.getLatestNews(self)
        if not news:
            return

        self.news_title.setText(news.title)
        self.news_description.setText(news.description)

    def quit(self):
        self.use_close_event = False

    def closeApp(self):
        Wydbid.app.exit(0)

    # Event Management Methods

    def startNewsActions(self):
        self.news_actions.show()

    def startCustomerActions(self):
        self.customer_actions.show()