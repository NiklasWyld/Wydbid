from datetime import datetime

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys
import Wydbid
from CustomQt import ActionButton

class WydbidUIMain(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__()

        self.setWindowTitle('Wydbid - Center')
        self.setGeometry(0, 0, 1920, 1080)

        self.setLayout(QGridLayout())
        self.layout().setContentsMargins(30, 30, 30, 30)

        self.setupUI()
        self.setupMenuBar()

    def closeEvent(self, event: QCloseEvent):
        reply = QMessageBox.question(self, 'Bist du sicher?', 'Bist du sicher, Wydbid beenden möchtest?',
                                     QMessageBox.Yes, QMessageBox.No)

        if reply == QMessageBox.Yes:
            sys.exit(0)
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

        customer_list_box = QGroupBox(parent=self, title='Kundenliste')

        self.layout().addWidget(date_time, 0, 0, 1, 2)
        self.layout().addWidget(action_list, 1, 0)
        self.layout().addWidget(customer_list_box, 1, 1)

    def setupMenuBar(self):
        self.menubar = QMenuBar(parent=self)
        file = QMenu(parent=self.menubar, title='Wydbid')
        help = QMenu(parent=self.menubar, title='Hilfe')

        # ToDo: Logic hinzufuegen

        logout_mitarbeiter = QAction('Mitarbeiter abmelden', self)
        logout_company = QAction('Aus Firma abmelden', self)
        reset_programm = QAction('Programm zurücksetzen', self)
        close = QAction('Beenden', self)

        contact = QAction('Kontakt', self)
        report_bug = QAction('Fehler melden', self)

        file.addAction(logout_mitarbeiter)
        file.addAction(logout_company)
        file.addSeparator()
        file.addAction(reset_programm)
        file.addSeparator()
        file.addAction(close)

        help.addAction(contact)
        help.addAction(report_bug)

        self.menubar.addMenu(file)
        self.menubar.addMenu(help)

    def resizeEvent(self, QResizeEvent):
        # Is needed because otherwise the MenuBar is only big enough to show the content
        super().resizeEvent(QResizeEvent)

        self.menubar.resize(self.width(), 20)

    def setupActionBox(self, action_list: QComboBox):
        action_list.setLayout(QGridLayout())
        action_list.layout().setAlignment(Qt.AlignTop| Qt.AlignHCenter)

        customer_note = QLabel(parent=action_list, text='Kunden')
        add_customer = ActionButton.ActionButton(parent=action_list, text='Kunde hinzufügen ➜')

        action_list.layout().addWidget(customer_note, 0, 0, 1, 0, Qt.AlignLeft)
        action_list.layout().addWidget(add_customer, 1, 0, 1, 0, Qt.AlignCenter)

    def setupDateTime(self, date_time: QGroupBox):
        self.time_label = QLabel(parent=date_time)
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