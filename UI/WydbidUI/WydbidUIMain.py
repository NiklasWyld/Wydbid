from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys
import Wydbid

class WydbidUIMain(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__()

        self.setWindowTitle('Wydbid - Center')
        self.setGeometry(0, 0, 1920, 1080)

        self.setupUI()
        self.setupMenuBar()

    def setupUI(self):
        pass

    def setupMenuBar(self):
        self.menubar = QMenuBar(parent=self)

        file = QMenu(parent=self.menubar, title='Wydbid')
        help = QMenu(parent=self.menubar, title='Hilfe')

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