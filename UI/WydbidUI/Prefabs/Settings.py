from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from BackEnd.WydbidBackEnd import SettingsLogic

class Settings(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__()

        self.layout = QGridLayout()

        self.setLayout(self.layout)
        self.setWindowTitle('Wydbid - Settings')
        self.setGeometry(0, 0, 600, 450)

        self.setupUI()
        SettingsLogic.loadSettings()
        SettingsLogic.loadCurrentSettingsToPrefab(settings=self)

    def setupUI(self):
        self.layout.setAlignment(Qt.AlignTop | Qt.AlignHCenter)

        title = QLabel(parent=self, text='Settings')
        title.setFont(QFont('Montserrat', 30))

        iconnote = QLabel(parent=self, text='Programm icon: ')
        self.icon = QLineEdit(parent=self)
        selecticon = QPushButton(parent=self, text='...')
        selecticon.clicked.connect(self.selectFile)
        selecticon.setFixedWidth(30)

        modenote = QLabel(parent=self, text='Theme: ')
        self.mode = QComboBox(parent=self)

        self.mode.addItem('Light', 'light')
        self.mode.addItem('Dark', 'dark')
        self.mode.setCurrentIndex(1)

        apply = QPushButton(parent=self, text='Apply and save')
        apply.clicked.connect(lambda: SettingsLogic.saveAndApplySetttings(settings=self))

        self.layout.addWidget(title, 1, 0, 1, 0, Qt.AlignCenter)

        self.layout.addWidget(iconnote, 3, 0, Qt.AlignLeft)
        self.layout.addWidget(self.icon, 3, 1, Qt.AlignRight)
        self.layout.addWidget(selecticon, 3, 1, Qt.AlignRight)

        self.layout.addWidget(modenote, 4, 0, Qt.AlignLeft)
        self.layout.addWidget(self.mode, 4, 1, Qt.AlignRight)

        self.layout.addWidget(apply, 5, 0, 1, 0, Qt.AlignCenter)

    def selectFile(self):
        file, check = QFileDialog.getOpenFileName(None, caption='Select the new programm icon.', directory='',
                                                  filter='PNG Files (*.png);;JPG Files (*.jpg);;JPEG Files (*.jpeg)')

        if check:
            self.icon.setText(file)