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
import screeninfo

# ToDo: Update Pictures in Readme
# ToDo: New slogan: There is nothing, oh wait, there is, Wydbid!

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

        news_widget = QWidget()
        self.setupNewsWidget(newswidget=news_widget)

        customer_widget = QWidget()
        self.setupCustomerList(customerlist=customer_widget)

        appointment_widget = QWidget()
        self.setupAppointments(appointment_widget)

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
        self.layout().addWidget(self.tabwidget, 1, 0)

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

    def setupAppointments(self, appointments: QWidget):
        pass

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