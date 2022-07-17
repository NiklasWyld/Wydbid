from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from BackEnd.WydbidBackEnd import SettingsLogic

class Settings(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__()

        self.layout = QGridLayout()

        self.setLayout(self.layout)
        self.setWindowTitle('Wydbid - Einstellungen')
        self.setGeometry(0, 0, 600, 450)

        self.setupUI()
        SettingsLogic.loadSettings()
        SettingsLogic.loadCurrentSettingsToPrefab(settings=self)

    def setupUI(self):
        self.layout.setAlignment(Qt.AlignTop | Qt.AlignHCenter)

        title = QLabel(parent=self, text='Einstellungen')
        title.setFont(QFont('Montserrat', 30))

        iconnote = QLabel(parent=self, text='Programmsymbol: ')
        self.icon = QLineEdit(parent=self)
        selecticon = QPushButton(parent=self, text='...')
        selecticon.clicked.connect(self.selectFile)
        selecticon.setFixedWidth(30)

        modenote = QLabel(parent=self, text='Umgebung: ')
        self.mode = QComboBox(parent=self)

        self.mode.addItem('Hell', 'light')
        self.mode.addItem('Dunkel', 'dark')
        self.mode.setCurrentIndex(1)

        apply = QPushButton(parent=self, text='Anwenden und speichern')
        apply.clicked.connect(lambda: SettingsLogic.saveAndApplySetttings(settings=self))

        self.layout.addWidget(title, 1, 0, 1, 0, Qt.AlignCenter)

        self.layout.addWidget(iconnote, 3, 0, Qt.AlignLeft)
        self.layout.addWidget(self.icon, 3, 1, Qt.AlignRight)
        self.layout.addWidget(selecticon, 3, 1, Qt.AlignRight)

        self.layout.addWidget(modenote, 4, 0, Qt.AlignLeft)
        self.layout.addWidget(self.mode, 4, 1, Qt.AlignRight)

        self.layout.addWidget(apply, 5, 0, 1, 0, Qt.AlignCenter)

    def selectFile(self):
        file, check = QFileDialog.getOpenFileName(None, caption='Wähle das neue Programm-Icon.', directory='',
                                                  filter='PNG Files (*.png);;JPG Files (*.jpg)')

        if check:
            self.icon.setText(file)