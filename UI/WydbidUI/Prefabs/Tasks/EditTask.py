from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from BackEnd.WydbidBackEnd import TaskLogic

class EditTask(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__()

        self.layout = QGridLayout()

        self.setLayout(self.layout)
        self.setWindowTitle('Wydbid - Edit task')
        self.setGeometry(0, 0, 600, 450)

        self.task_id = 0

        self.setupUI()

    def setTask(self, task_id: int):
        self.task_id = task_id
        TaskLogic.setTaskForEdit(self.task_id, self)

    def clear(self):
        self.task_id = 0
        self.author.setText('')
        self.receiver.setText('')
        self.title.setText('')
        self.description.setText('')
        self.deadline.setDate(QDate.currentDate())

    def setupUI(self):
        self.layout.setAlignment(Qt.AlignTop | Qt.AlignHCenter)

        title = QLabel('Edit task')
        title.setFont(QFont('Montserrat', 30))

        authornote = QLabel(parent=self, text='Author Username (*):')
        self.author = QLineEdit(parent=self)
        self.author.setMinimumWidth(450)

        receivernote = QLabel(parent=self, text='Receiver Username (*):')
        self.receiver = QLineEdit(parent=self)
        self.receiver.setMinimumWidth(450)

        titlenote = QLabel(parent=self, text='Title (*): ')
        self.title = QLineEdit(parent=self)
        self.title.setMinimumWidth(450)

        descriptionnote = QLabel(parent=self, text='Description: ')
        self.description = QTextEdit(parent=self)
        self.description.setMaximumHeight(300)
        self.description.setMinimumWidth(450)

        deadlinenote = QLabel(parent=self, text='Deadline (*): ')
        self.deadline = QDateEdit(parent=self)
        self.deadline.setMinimumWidth(450)

        edit = QPushButton(parent=self, text='Edit')
        edit.clicked.connect(lambda: TaskLogic.editTask(self.task_id, self.author.text(), self.receiver.text(),
                                                        self.title.text(), self.description.toPlainText(),
                                                        self.deadline, self))

        self.layout.addWidget(title, 1, 0, 1, 0, Qt.AlignCenter)

        self.layout.addWidget(authornote, 2, 0, Qt.AlignLeft)
        self.layout.addWidget(self.author, 2, 1, Qt.AlignRight)

        self.layout.addWidget(receivernote, 3, 0, Qt.AlignLeft)
        self.layout.addWidget(self.receiver, 3, 1, Qt.AlignRight)

        self.layout.addWidget(titlenote, 4, 0, Qt.AlignLeft)
        self.layout.addWidget(self.title, 4, 1, Qt.AlignRight)

        self.layout.addWidget(descriptionnote, 5, 0, Qt.AlignLeft)
        self.layout.addWidget(self.description, 5, 1, Qt.AlignRight)

        self.layout.addWidget(deadlinenote, 6, 0, Qt.AlignLeft)
        self.layout.addWidget(self.deadline, 6, 1, Qt.AlignRight)

        self.layout.addWidget(edit, 7, 0, 1, 0, Qt.AlignCenter)