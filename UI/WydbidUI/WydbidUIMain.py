from datetime import datetime
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import Wydbid
from BackEnd.WydbidBackEnd import WydbidUIMainLogic
from CustomQt import ActionButton
from UI.WydbidUI.Prefabs import Settings
from UI.WydbidUI.Prefabs.Kunde import CreateKunde

class WydbidUIMain(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__()

        self.setWindowTitle('Wydbid - Center')
        self.setGeometry(0, 0, 1920, 1080)

        self.setLayout(QGridLayout())
        self.layout().setContentsMargins(30, 30, 30, 30)

        # Widgets
        self.ck = CreateKunde.CreateKunde()

        self.setupUI()
        self.setupMenuBar()

    def closeEvent(self, event: QCloseEvent):
        reply = QMessageBox.question(self, 'Bist du sicher?', 'Bist du sicher, Wydbid beenden möchtest?',
                                     QMessageBox.Yes, QMessageBox.No)

        if reply == QMessageBox.Yes:
            Wydbid.app.exit(0)
        else:
            event.ignore()
            pass

    def setupUI(self):
        date_time = QGroupBox(parent=self, title='Datum und Uhrzeit')
        date_time.setFixedHeight(150)
        self.setupDateTime(date_time)

        action_list = QGroupBox(parent=self, title='Aktionen')
        action_list.setFixedWidth(200)
        self.setupActionBox(action_list)

        customer_widget = QWidget()
        self.setupKundenListe(kunden_liste=customer_widget)

        termin_widget = QWidget()

        auftrag_widget = QWidget()

        ereignis_widget = QWidget()

        self.tabwidget = QTabWidget(parent=self)
        self.tabwidget.addTab(customer_widget, 'Kundenliste')
        self.tabwidget.addTab(termin_widget, 'Termine')
        self.tabwidget.addTab(auftrag_widget, 'Aufträge')
        self.tabwidget.addTab(ereignis_widget, 'Ereignisse')

        self.layout().addWidget(date_time, 0, 0, 1, 0)
        self.layout().addWidget(action_list, 1, 0)
        self.layout().addWidget(self.tabwidget, 1, 1)

    def setupMenuBar(self):
        self.menubar = QMenuBar(parent=self)
        file = QMenu(parent=self.menubar, title='Wydbid')
        help = QMenu(parent=self.menubar, title='Hilfe')

        logout_mitarbeiter = QAction('Mitarbeiter abmelden', self)
        logout_company = QAction('Aus Firma abmelden', self)
        reset_programm = QAction('Programm zurücksetzen', self)
        settings = QAction('Einstellungen', self)
        close = QAction('Beenden', self)

        contact = QAction('Kontakt', self)
        report_bug = QAction('Fehler melden', self)

        logout_mitarbeiter.triggered.connect(lambda: WydbidUIMainLogic.logoutMitarbeiter(self))
        logout_company.triggered.connect(self.startCompanyLogout)
        reset_programm.triggered.connect(Wydbid.reset)
        settings.triggered.connect(self.startSettings)
        close.triggered.connect(self.closeApp)

        contact.triggered.connect(WydbidUIMainLogic.contact)
        report_bug.triggered.connect(WydbidUIMainLogic.contact)

        file.addAction(logout_mitarbeiter)
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

        # Kunden
        customer_note = QLabel(parent=action_list, text='Kunden 👨')
        add_customer = ActionButton.ActionButton(parent=action_list, text='Kunde hinzufügen ➜', color='lightgreen', color_hover='green')
        edit_customer = ActionButton.ActionButton(parent=action_list, text='Kunde bearbeiten ➜', color='lightskyblue', color_hover='blue')
        del_customer = ActionButton.ActionButton(parent=action_list, text='Kunde löschen ➜', color='lightcoral', color_hover='red')

        # Termine
        termin_note = QLabel(parent=action_list, text='Termine 📅')
        add_termin = ActionButton.ActionButton(parent=action_list, text='Termin hinzufügen ➜', color='lightgreen', color_hover='green')
        edit_termin = ActionButton.ActionButton(parent=action_list, text='Termin bearbeiten ➜', color='lightskyblue', color_hover='blue')
        del_termin = ActionButton.ActionButton(parent=action_list, text='Termin löschen ➜', color='lightcoral', color_hover='red')

        # Auftraege
        auftrag_note = QLabel(parent=action_list, text='Aufträge 📦')
        add_auftrag = ActionButton.ActionButton(parent=action_list, text='Auftrag hinzufügen ➜', color='lightgreen', color_hover='green')
        edit_auftrag = ActionButton.ActionButton(parent=action_list, text='Auftrag bearbeiten ➜', color='lightskyblue', color_hover='blue')
        del_auftrag = ActionButton.ActionButton(parent=action_list, text='Auftrag löschen ➜', color='lightcoral', color_hover='red')

        # Ereignisse
        ereignis_note = QLabel(parent=action_list, text='Ereignis 📝')
        add_ereignis = ActionButton.ActionButton(parent=action_list, text='Ereignis hinzufügen ➜', color='lightgreen', color_hover='green')
        edit_ereignis = ActionButton.ActionButton(parent=action_list, text='Ereignis bearbeiten ➜', color='lightskyblue', color_hover='blue')
        del_ereignis = ActionButton.ActionButton(parent=action_list, text='Ereignis löschen ➜', color='lightcoral', color_hover='red')

        # Kunden Layout Management
        action_list.layout().addWidget(customer_note, 0, 0, 1, 0, Qt.AlignLeft)
        action_list.layout().addWidget(add_customer, 1, 0, 1, 0, Qt.AlignCenter)
        action_list.layout().addWidget(edit_customer, 2, 0, 1, 0, Qt.AlignCenter)
        action_list.layout().addWidget(del_customer, 3, 0, 1, 0, Qt.AlignCenter)

        # Termin Layout Management
        action_list.layout().addWidget(termin_note, 5, 0, 1, 0, Qt.AlignLeft)
        action_list.layout().addWidget(add_termin, 6, 0, 1, 0, Qt.AlignCenter)
        action_list.layout().addWidget(edit_termin, 7, 0, 1, 0, Qt.AlignCenter)
        action_list.layout().addWidget(del_termin, 8, 0, 1, 0, Qt.AlignCenter)

        # Auftrag Layout Management
        action_list.layout().addWidget(auftrag_note, 10, 0, 1, 0, Qt.AlignLeft)
        action_list.layout().addWidget(add_auftrag, 11, 0, 1, 0, Qt.AlignCenter)
        action_list.layout().addWidget(edit_auftrag, 12, 0, 1, 0, Qt.AlignCenter)
        action_list.layout().addWidget(del_auftrag, 13, 0, 1, 0, Qt.AlignCenter)

        # Ereignis Layout Management
        action_list.layout().addWidget(ereignis_note, 15, 0, 1, 0, Qt.AlignLeft)
        action_list.layout().addWidget(add_ereignis, 16, 0, 1, 0, Qt.AlignCenter)
        action_list.layout().addWidget(edit_ereignis, 17, 0, 1, 0, Qt.AlignCenter)
        action_list.layout().addWidget(del_ereignis, 18, 0, 1, 0, Qt.AlignCenter)

        # ToDo: Event Management

        # Kunden Event Management
        add_customer.clicked.connect(self.startCreateKunde)

    # Setup tab widgets

    def setupKundenListe(self, kunden_liste: QWidget):
        ###

        #lyt = QGridLayout()
        #kunden_liste.setLayout(lyt)
        self.kundenliste = QTableWidget(parent=kunden_liste)
        self.kundenliste.setStyleSheet('background-color: green;')

        #kunden_liste.layout().addWidget(self.kundenliste, 1, 0, 1, 0, Qt.AlignCenter)

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

    def startCreateKunde(self):
        self.ck.show()
