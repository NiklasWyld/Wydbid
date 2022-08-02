from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import Wydbid

class LoadingScreen(QWidget):
    def __init__(self):
        super(LoadingScreen, self).__init__()

        self.setFixedWidth(600)
        self.setFixedHeight(300)

        self.center()
        self.setupUI()

    def setupUI(self):
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setStyleSheet('')

        self.background = QLabel(self)
        self.background_pixmap = QPixmap('./Assets/LoadingScreenImages/Wydbid_Startscreen_Picture.png')
        self.background.setPixmap(self.background_pixmap)
        self.background.move(0, -1)

        self.logo = QLabel(self)
        self.logo_pixmap = QPixmap('./Assets/LoadingScreenImages/WydbidLogo_white.png')
        self.logo.setPixmap(self.logo_pixmap.scaled(150, 150))
        self.logo.setStyleSheet("background-color: transparent;")

        self.title = QLabel(self)
        self.title.setText('Wydbid')
        self.title.setGeometry(170, 50, 220, 60)
        self.title.setFont(QFont('Arial', 40, ))
        self.title.setStyleSheet('font-weight: bold; color: white; background-color: transparent;')

        self.version_info = QLabel(self)
        self.version_info.setText('Version ' + Wydbid.wydbid_version)
        self.version_info.setFixedWidth(250)
        self.version_info.setStyleSheet('font-weight: bold; color: white; background-color: transparent')
        self.version_info.setGeometry(150, 110, 140, 20)
        self.version_info.setAlignment(Qt.AlignCenter)
        self.version_info.setFont(QFont('Arial', 16))


    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def closeEvent(self, event: QCloseEvent):
        event.ignore()