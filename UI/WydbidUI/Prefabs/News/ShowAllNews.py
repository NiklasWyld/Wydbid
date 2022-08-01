from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import Qt
from BackEnd.WydbidBackEnd import NewsLogic

class ShowAllNews(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__()

        self.layout = QGridLayout()

        self.setLayout(self.layout)
        self.setWindowTitle('Wydbid - Show all news')
        self.setGeometry(0, 0, 600, 600)

        self.setupUI()

    def setupUI(self):
        self.layout.setAlignment(Qt.AlignTop | Qt.AlignHCenter)

        title = QLabel('Show all news')
        title.setFont(QFont('Montserrat', 30))

        self.news_list = QListWidget(parent=self)
        self.news_list.setFixedWidth(500)
        self.news_list.setFixedHeight(500)

        self.news_list.itemDoubleClicked.connect(self.setNewsToMainUI)

        ok = QPushButton(parent=self, text='Ok')
        ok.clicked.connect(
            lambda: self.hide()
        )

        reload = QPushButton(parent=self, text='Reload')
        reload.clicked.connect(
            lambda: NewsLogic.appendNews(self.news_list)
        )

        self.layout.addWidget(title, 1, 0, 1, 0, Qt.AlignCenter)

        self.layout.addWidget(self.news_list, 2, 0, 1, 0, Qt.AlignCenter)

        self.layout.addWidget(ok, 3, 0, Qt.AlignLeft)
        self.layout.addWidget(reload, 3, 1, Qt.AlignRight)

    def setNewsToMainUI(self, item):
        news = item.data(Qt.UserRole)
        #print(news.id)

    def appendNews(self):
        NewsLogic.appendNews(self.news_list)