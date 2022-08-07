from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from BackEnd.WydbidBackEnd import NewsLogic

class DelNews(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__()

        self.layout = QGridLayout()

        self.setLayout(self.layout)
        self.setWindowTitle('Wydbid - Delete news')
        self.setGeometry(0, 0, 600, 600)

        self.setupUI()

    def setupUI(self):
        self.layout.setAlignment(Qt.AlignTop | Qt.AlignHCenter)

        title = QLabel('Delete news')
        title.setFont(QFont('Montserrat', 30))

        self.news_list = QListWidget(parent=self)
        self.news_list.setFixedWidth(500)
        self.news_list.setFixedHeight(500)

        delete = QPushButton(parent=self, text='Delete selected news')
        delete.clicked.connect(lambda: NewsLogic.delNews(self.news_list, self))

        self.layout.addWidget(title, 1, 0, 1, 0, Qt.AlignCenter)

        self.layout.addWidget(self.news_list, 2, 0, 1, 0, Qt.AlignCenter)

        self.layout.addWidget(delete, 3, 0, 1, 0, Qt.AlignCenter)

    def appendNews(self):
        NewsLogic.appendNews(self.news_list)