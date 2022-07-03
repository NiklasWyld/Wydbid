from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

###

class Settings(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__()

        self.layout = QGridLayout()

        self.setLayout(self.layout)
        self.setWindowTitle('Wydbid - Einstellungen')
        self.setGeometry(0, 0, 600, 450)

        self.setupUI()

    def setupUI(self):
        self.layout.setAlignment(Qt.AlignTop | Qt.AlignHCenter)

        title = QLabel(parent=self, text='Einstellungen')
        title.setFont(QFont('Montserrat', 30))

        pathnote = QLabel(parent=self, text='Datenpfad: ')
        self.path = QLineEdit(parent=self)
        selectpath = QPushButton(parent=self, text='...')

        iconnote = QLabel(parent=self, text='Programmsymbol: ')
        self.icon = QLineEdit(parent=self)
        selecticon = QPushButton(parent=self, text='...')

        modenote = QLabel(parent=self, text='Umgebung: ')
        self.mode = QComboBox(parent=self)

        self.mode.addItem('Hell', 'light')
        self.mode.addItem('Dunkel', 'dark')
        self.mode.setCurrentIndex(1)

        apply = QPushButton(parent=self, text='Anwenden und speichern')

        self.layout.addWidget(title, 1, 0, 1, 0, Qt.AlignCenter)

        self.layout.addWidget(pathnote, 2, 0, Qt.AlignLeft)
        self.layout.addWidget(self.path, 2, 1, Qt.AlignRight)
        self.layout.addWidget(selectpath, 2, 1, Qt.AlignRight)

        self.layout.addWidget(iconnote, 3, 0, Qt.AlignLeft)
        self.layout.addWidget(self.icon, 3, 1, Qt.AlignRight)
        self.layout.addWidget(selecticon, 3, 1, Qt.AlignRight)

        self.layout.addWidget(modenote, 4, 0, Qt.AlignLeft)
        self.layout.addWidget(self.mode, 4, 1, Qt.AlignRight)

        self.layout.addWidget(apply, 5, 0, 1, 0, Qt.AlignCenter)