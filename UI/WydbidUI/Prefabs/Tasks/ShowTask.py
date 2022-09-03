from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from BackEnd.WydbidBackEnd import TaskLogic
from UI.WydbidUI.Prefabs.Tasks import EditTask

# ToDo: Make all shows more width (qlineedits)

class ShowTask(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__()

        self.layout = QGridLayout()

        self.setLayout(self.layout)
        self.setWindowTitle('Wydbid - Show task')
        self.setGeometry(0, 0, 600, 450)

        self.et = EditTask.EditTask()

        self.task = None
        self.task_id = 0

        self.setupUI()

    def setTask(self, task_id: int):
        self.task_id = task_id
        TaskLogic.setTaskForShow(self.task_id, self)

    def clear(self):
        self.task = None
        self.task_id = 0
        self.author.setText('')
        self.receiver.setText('')
        self.title.setText('')
        self.description.setText('')
        self.deadline.setDate(QDate.currentDate())
        self.done.setChecked(False)

    def setupUI(self):
        self.layout.setAlignment(Qt.AlignTop | Qt.AlignHCenter)

        title = QLabel('Show task')
        title.setFont(QFont('Montserrat', 30))

        action_box = QGroupBox(parent=self)
        action_box.setFixedHeight(40)
        action_box.setMinimumWidth(500)
        alyt = QHBoxLayout()

        # ToDo: Add logic for edit and del task

        edit = QPushButton(parent=action_box, text='Edit')
        edit.setToolTip('Edit this task')
        #edit.clicked.connect(self.startEditOrder)

        delete = QPushButton(parent=action_box, text='Delete')
        delete.setToolTip('Delete this task')
        #delete.clicked.connect(self.startDelOrder)

        alyt.setContentsMargins(1, 1, 1, 1)
        alyt.addWidget(edit)
        alyt.addWidget(delete)
        action_box.setLayout(alyt)

        authornote = QLabel(parent=self, text='Author Username')
        self.author = QLineEdit(parent=self)
        self.author.setMinimumWidth(450)

        receivernote = QLabel(parent=self, text='Receiver Username:')
        self.receiver = QLineEdit(parent=self)
        self.receiver.setMinimumWidth(450)

        titlenote = QLabel(parent=self, text='Title: ')
        self.title = QLineEdit(parent=self)
        self.title.setMinimumWidth(450)

        descriptionnote = QLabel(parent=self, text='Description: ')
        self.description = QTextEdit(parent=self)
        self.description.setMaximumHeight(300)
        self.description.setMinimumWidth(450)

        deadlinenote = QLabel(parent=self, text='Deadline: ')
        self.deadline = QDateEdit(parent=self)
        self.deadline.setMinimumWidth(450)

        self.done = QCheckBox(parent=self, text='Done')
        self.done.stateChanged.connect(self.editClosed)

        self.author.setEnabled(False)
        self.receiver.setEnabled(False)
        self.title.setEnabled(False)
        self.description.setEnabled(False)
        self.deadline.setEnabled(False)

        self.layout.addWidget(title, 1, 0, 1, 0, Qt.AlignCenter)

        self.layout.addWidget(action_box, 2, 0, 1, 0, Qt.AlignCenter)

        self.layout.addWidget(authornote, 3, 0, Qt.AlignLeft)
        self.layout.addWidget(self.author, 3, 1, Qt.AlignRight)

        self.layout.addWidget(receivernote, 4, 0, Qt.AlignLeft)
        self.layout.addWidget(self.receiver, 4, 1, Qt.AlignRight)

        self.layout.addWidget(titlenote, 5, 0, Qt.AlignLeft)
        self.layout.addWidget(self.title, 5, 1, Qt.AlignRight)

        self.layout.addWidget(descriptionnote, 6, 0, Qt.AlignLeft)
        self.layout.addWidget(self.description, 6, 1, Qt.AlignRight)

        self.layout.addWidget(deadlinenote, 7, 0, Qt.AlignLeft)
        self.layout.addWidget(self.deadline, 7, 1, Qt.AlignRight)

        self.layout.addWidget(self.done, 8, 1, Qt.AlignRight)

    def editClosed(self):
        if not self.task_id == 0:
            if not self.task.done == self.done.isChecked():
                TaskLogic.editTaskDone(self.task.id, self.done, self)