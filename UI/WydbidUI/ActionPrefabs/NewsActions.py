from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from CustomQt import ActionButton
from UI.WydbidUI.Prefabs.News import CreateNews

class NewsActions(QDialog):
    def __init__(self):
        super().__init__()

        self.layout = QGridLayout()

        self.setWindowTitle('Wydbid - News Actions')
        self.setGeometry(0, 0, 250, 200)

        # Widgets
        self.cn = CreateNews.CreateNews()

        self.setupUI()
        self.setLayout(self.layout)

    def setupUI(self):
        add_news = ActionButton.ActionButton(parent=self, text='Add news ➜', color='lightgreen',
                                                 color_hover='green')
        edit_news = ActionButton.ActionButton(parent=self, text='Edit news ➜', color='lightskyblue',
                                                  color_hover='blue')
        del_news = ActionButton.ActionButton(parent=self, text='Delete news ➜', color='lightcoral',
                                             color_hover='red')

        self.layout.addWidget(add_news, 1, 0, 1, 0, Qt.AlignCenter)
        self.layout.addWidget(edit_news, 2, 0, 1, 0, Qt.AlignCenter)
        self.layout.addWidget(del_news, 3, 0, 1, 0, Qt.AlignCenter)

        add_news.clicked.connect(self.startCreateNews)

    def startCreateNews(self):
        self.cn.show()
        self.hide()