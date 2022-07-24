from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from Data import Kunde

class ShowKunde(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__()

        self.layout = QGridLayout()

        self.setLayout(self.layout)
        self.setWindowTitle('Wydbid - Kunde ansehen')
        self.setGeometry(0, 0, 600, 600)

        self.setupUI()

    def setupUI(self):
        pass

    def setKunde(self, kunde: Kunde.Kunde):
        pass

    def clear(self):
        pass