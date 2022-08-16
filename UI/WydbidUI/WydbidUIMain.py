from datetime import datetime
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import Wydbid
from BackEnd.WydbidBackEnd import WydbidUIMainLogic, AppointmentLogic, OrderLogic
from UI.WydbidUI.Prefabs import Settings
from UI.WydbidUI.Prefabs.Customer import ViewCustomer, CreateCustomer, EditCustomer, DelCustomer
from UI.WydbidUI.Prefabs.Appointments import CreateAppointment, EditAppointment, DelAppointment, ShowAppointment
from UI.WydbidUI.Prefabs.News import ShowAllNews
import screeninfo
import threading

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

        # Widgets
        self.cc = CreateCustomer.CreateCustomer()
        self.ec = EditCustomer.EditCustomer()
        self.dc = DelCustomer.DelCustomer()

        self.ca = CreateAppointment.CreateAppointment()
        self.gafe = EditAppointment.GetAppointment()
        self.da = DelAppointment.DelAppointment()
        self.sa = ShowAppointment.ShowAppointment()

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
        self.setupOrders(order_widget)

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
        update_programm = QAction('Check for Updates', self)
        settings = QAction('Settings', self)
        close = QAction('Exit', self)

        contact = QAction('Contact', self)
        report_bug = QAction('Report error', self)

        logout_employee.triggered.connect(lambda: WydbidUIMainLogic.logoutEmployee(self))
        logout_company.triggered.connect(self.startCompanyLogout)
        reset_programm.triggered.connect(Wydbid.reset)
        update_programm.triggered.connect(lambda: self.startUpdate(p=True))
        settings.triggered.connect(self.startSettings)
        close.triggered.connect(self.closeApp)

        contact.triggered.connect(WydbidUIMainLogic.contact)
        report_bug.triggered.connect(WydbidUIMainLogic.contact)

        file.addAction(logout_employee)
        file.addAction(logout_company)
        file.addSeparator()
        file.addAction(update_programm)
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

        actions = QGroupBox(parent=self)
        actions.setFixedHeight(40)
        nlyt = QHBoxLayout()
        nlyt.setContentsMargins(1, 1, 1, 1)

        add = QPushButton(parent=self, text='Create')
        add.setToolTip('Create customer')
        add.clicked.connect(self.startCreateCustomer)

        edit = QPushButton(parent=self, text='Edit')
        edit.setToolTip('Edit customer')
        edit.clicked.connect(self.startEditCustomer)

        delete = QPushButton(parent=self, text='Delete')
        delete.setToolTip('Delete customer')
        delete.clicked.connect(self.startDelCustomer)

        nlyt.addWidget(add)
        nlyt.addWidget(edit)
        nlyt.addWidget(delete)
        actions.setLayout(nlyt)

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
        lyt.addWidget(actions, Qt.AlignCenter)
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
        lyt = QHBoxLayout()
        vl = QVBoxLayout()

        action_box = QGroupBox(parent=appointments)
        action_box.setFixedHeight(40)
        alyt = QHBoxLayout()

        goto_current_date = QPushButton(parent=action_box, text='Jump to current date')
        goto_current_date.clicked.connect(self.gotoCurrentDate)

        add = QPushButton(parent=self, text='Create')
        add.setToolTip('Create new appointment on selected date')
        add.clicked.connect(self.startCreateAppointment)

        edit = QPushButton(parent=self, text='Edit')
        edit.setToolTip('Edit a appointment on selected date')
        edit.clicked.connect(self.startEditAppointment)

        delete = QPushButton(parent=self, text='Delete')
        delete.setToolTip('Delete a appointment on selected date')
        delete.clicked.connect(self.startDelAppointment)

        alyt.setContentsMargins(1, 1, 1, 1)
        alyt.addWidget(goto_current_date)
        alyt.addWidget(add)
        alyt.addWidget(edit)
        alyt.addWidget(delete)
        action_box.setLayout(alyt)

        # Widget content

        self.calander = QCalendarWidget(parent=self)
        if Wydbid.app.styleSheet().strip():
            self.calander.setStyleSheet('''
            QAbstractItemView {
                alternate-background-color: #2d3640;
            }
            ''')
        self.calander.setGridVisible(True)

        ngroup = QGroupBox()
        ngroup.setMaximumWidth(700)

        self.appointment_search_bar = QLineEdit(parent=ngroup)
        self.appointment_search_bar.setPlaceholderText('Filter by customer')
        self.appointment_search_bar.setFixedHeight(40)
        self.appointment_search_bar.textChanged.connect(self.filterForCustomerInAppointments)

        self.appointment_list = QTableWidget(parent=ngroup)
        self.appointment_list.clicked.connect(self.startShowAppointment)

        nlyt = QVBoxLayout()

        lyt.addWidget(self.calander, Qt.AlignLeft)
        nlyt.addWidget(self.appointment_search_bar, Qt.AlignTop)
        nlyt.addWidget(self.appointment_list, Qt.AlignBottom)
        lyt.addWidget(ngroup, Qt.AlignRight)

        ngroup.setLayout(nlyt)

        vl.addWidget(action_box)
        vl.addLayout(lyt)

        appointments.setLayout(vl)
        self.startAppendAppointments()
        self.calander.selectionChanged.connect(self.startAppendAppointments)

    def setupOrders(self, orders_widget: QWidget):
        lyt = QVBoxLayout()

        action_box = QGroupBox(parent=orders_widget)
        action_box.setFixedHeight(40)
        alyt = QHBoxLayout()

        add = QPushButton(parent=action_box, text='Create')
        add.setToolTip('Create new order')
        #add.clicked.connect(self.startCreateAppointment)

        edit = QPushButton(parent=action_box, text='Edit')
        edit.setToolTip('Edit a order')
        #edit.clicked.connect(self.startEditAppointment)

        delete = QPushButton(parent=action_box, text='Delete')
        delete.setToolTip('Delete a order')
        #delete.clicked.connect(self.startDelAppointment)

        reload = QPushButton(parent=action_box, text='Reload')
        reload.setToolTip('Reload all orders')
        reload.clicked.connect(self.startAppendOrders)

        alyt.setContentsMargins(1, 1, 1, 1)
        alyt.addWidget(add)
        alyt.addWidget(edit)
        alyt.addWidget(delete)
        alyt.addWidget(reload)
        action_box.setLayout(alyt)

        self.order_search_bar = QLineEdit(parent=orders_widget)
        self.order_search_bar.setPlaceholderText('Filter by customer')
        self.order_search_bar.setFixedHeight(40)
        self.order_search_bar.textChanged.connect(self.filterForCustomerInOrders)

        self.order_list = QTableWidget(parent=orders_widget)
        self.startAppendOrders()

        lyt.addWidget(action_box)
        lyt.addWidget(self.order_search_bar)
        lyt.addWidget(self.order_list)

        orders_widget.setLayout(lyt)

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
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.updateClock)
        self.timer.start(1000)

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

    def startUpdate(self, p: bool):
        updater = Wydbid.Update()
        if not p: updater.show_if_uptodate = False
        updater.checkVersion()

    def closeApp(self):
        Wydbid.app.exit(0)

    # Event Management Methods

    def startCreateCustomer(self):
        self.cc.show()

    def startEditCustomer(self):
        self.ec.show()
        self.ec.setCustomer()

    def startDelCustomer(self):
        self.dc.show()

    def gotoCurrentDate(self):
        self.calander.showToday()
        self.calander.setSelectedDate(QDate.currentDate())

    def startCreateAppointment(self):
        self.ca.show()
        self.ca.clear()

    def startEditAppointment(self):
        self.gafe.setDate(self.calander.selectedDate().toString('dd.MM.yyyy'))
        self.gafe.show()

    def startDelAppointment(self):
        self.da.setDate(self.calander.selectedDate().toString('dd.MM.yyyy'))
        self.da.show()

    def startShowAppointment(self, item):
        if item.data() == '🔎':
            id = item.data(Qt.UserRole)
            appointment = AppointmentLogic.getAppointment(id)
            self.sa.clear()
            self.sa.setAppointment(appointment)
            self.sa.show()

    def startAppendAppointments(self):
        date = self.calander.selectedDate().toString('dd.MM.yyyy')
        AppointmentLogic.appendAppointments(date, self.calander, self.appointment_list)

    def filterForCustomerInAppointments(self):
        customer = self.appointment_search_bar.text().lower()
        for row in range(self.appointment_list.rowCount()):
            item = self.appointment_list.item(row, 3)

            # if the search is not in the item's text do not hide the row
            self.appointment_list.setRowHidden(row, customer not in item.text().lower())

    def filterForCustomerInOrders(self):
        customer = self.order_search_bar.text().lower()
        for row in range(self.order_list.rowCount()):
            item = self.appointment_list.item(row, 3)

            # if the search is not in the item's text do not hide the row
            self.order_list.setRowHidden(row, customer not in item.text().lower())

    def startAppendOrders(self):
        OrderLogic.appendOrders(self.order_list)

'''
Date/Time Formats:

QDate -> 'dd.MM.yyyy'
Day.Month.Year

QTime -> 'hh:mm'
Hour:Minute
'''