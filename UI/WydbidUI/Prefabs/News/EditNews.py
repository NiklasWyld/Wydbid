from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from BackEnd.WydbidBackEnd import NewsLogic

class EditNews(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__()

        self.layout = QGridLayout()

        self.setLayout(self.layout)
        self.setWindowTitle('Wydbid - Edit news')
        self.setGeometry(0, 0, 600, 600)

        self.news_id = 0

        self.setupUI()

    def clear(self):
        self.title.setText('')
        self.description.setText('')

    def setNews(self, item):
        NewsLogic.setNewsForEdit(item, self)

    def setNewsFinal(self, news):
        self.news_id = news.id
        self.title.setText(news.title)
        self.description.setText(news.description)

    def setupUI(self):
        self.layout.setAlignment(Qt.AlignTop | Qt.AlignHCenter)

        title = QLabel('Edit news')
        title.setFont(QFont('Montserrat', 30))

        title_note = QLabel(parent=self, text='Title (*): ')
        self.title = QLineEdit(parent=self)

        description_note = QLabel(parent=self, text='Description: ')
        self.description = QTextEdit(parent=self)

        edit = QPushButton(parent=self, text='Edit')
        edit.clicked.connect(lambda: NewsLogic.editNews(self.news_id, self.title.text(),
                                                        self.description.toPlainText(), self))

        self.layout.addWidget(title, 1, 0, 1, 0, Qt.AlignCenter)

        self.layout.addWidget(title_note, 2, 0, Qt.AlignLeft)
        self.layout.addWidget(self.title, 2, 1, Qt.AlignRight)

        self.layout.addWidget(description_note, 3, 0, Qt.AlignLeft)
        self.layout.addWidget(self.description, 3, 1, Qt.AlignRight)

        self.layout.addWidget(edit, 4, 0, 1, 0, Qt.AlignCenter)