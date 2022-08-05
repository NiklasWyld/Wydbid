from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import Qt
import Wydbid
from BackEnd.WydbidBackEnd import NewsLogic
from UI.WydbidUI.Prefabs.News import CreateNews, EditNews

class ShowAllNews(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__()

        self.layout = QGridLayout()

        self.setLayout(self.layout)
        self.setWindowTitle('Wydbid - Show all news')
        self.setGeometry(0, 0, 600, 600)

        self.cn = CreateNews.CreateNews()
        self.gen = EditNews.EditNews()

        self.setupUI()

    def setupUI(self):
        self.layout.setAlignment(Qt.AlignTop | Qt.AlignHCenter)

        title = QLabel('Show all news')
        title.setFont(QFont('Montserrat', 30))

        actions = QGroupBox(parent=self)
        actions.setFixedWidth(500)
        lyt = QHBoxLayout()

        add = QPushButton(parent=self, text='Add')
        add.setToolTip('Add news')
        add.clicked.connect(self.startCreateNews)

        edit = QPushButton(parent=self, text='Edit')
        edit.setToolTip('Edit selected news')
        edit.clicked.connect(self.startEditNews)

        delete = QPushButton(parent=self, text='Delete')
        delete.setToolTip('Delete selected news')
        delete.clicked.connect(self.startDelNews)

        lyt.addWidget(add)
        lyt.addWidget(edit)
        lyt.addWidget(delete)
        actions.setLayout(lyt)

        self.news_list = QListWidget(parent=self)
        self.news_list.setFixedWidth(500)
        self.news_list.setFixedHeight(500)

        self.news_list.itemDoubleClicked.connect(self.setNewsToMainUI)

        ok = QPushButton(parent=self, text='Ok')
        ok.clicked.connect(
            lambda: self.setNewsToMainUIWithOK()
        )

        reload = QPushButton(parent=self, text='Reload')
        reload.clicked.connect(
            lambda: NewsLogic.appendNews(self.news_list)
        )

        self.layout.addWidget(title, 1, 0, 1, 0, Qt.AlignCenter)

        self.layout.addWidget(actions, 2, 0, 1, 0, Qt.AlignCenter)

        self.layout.addWidget(self.news_list, 3, 0, 1, 0, Qt.AlignCenter)

        self.layout.addWidget(ok, 4, 0, Qt.AlignLeft)
        self.layout.addWidget(reload, 4, 1, Qt.AlignRight)

    def setNewsToMainUIWithOK(self):
        item = self.news_list.selectedItems()[0]

        news = item.data(Qt.UserRole)
        final_news = NewsLogic.getNews(news)

        self.hide()
        Wydbid.wydbidui.setNews(final_news)

    def setNewsToMainUI(self, item: QListWidgetItem):
        news = item.data(Qt.UserRole)
        final_news = NewsLogic.getNews(news)

        self.hide()
        Wydbid.wydbidui.setNews(final_news)

    def appendNews(self):
        NewsLogic.appendNews(self.news_list)

    def startCreateNews(self):
        self.cn.show()

    def startEditNews(self):
        if not self.news_list.selectedItems():
            QMessageBox.warning(self, 'Warning',
                                'No news selected!')
            return

        self.gen.show()
        self.gen.setNews(self.news_list.selectedItems()[0].data(Qt.UserRole))

    def startDelNews(self):
        if not self.news_list.selectedItems():
            QMessageBox.warning(self, 'Warning',
                                'No news selected!')
            return

        NewsLogic.delNews(self.news_list, self)