from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from BackEnd.WydbidBackEnd import EventLogic
from UI.WydbidUI.Prefabs.Events import EditEvent

class ShowEvent(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__()

        self.layout = QGridLayout()

        self.setLayout(self.layout)
        self.setWindowTitle('Wydbid - Show event')
        self.setGeometry(0, 0, 600, 450)

        self.ee = EditEvent.EditEvent()

        self.event_id = 0

        self.setupUI()

    def setEvent(self, event_id: int):
        self.event_id = event_id
        EventLogic.setEventForShow(event_id, self)

    def clear(self):
        self.event_id = 0
        self.title.setText('')
        self.description.setText('')
        self.dateedit.setDate(QDate.currentDate())
        self.timeedit.setDate(QDate.currentDate())

    def setupUI(self):
        self.layout.setAlignment(Qt.AlignTop | Qt.AlignHCenter)

        title = QLabel('Show event')
        title.setFont(QFont('Montserrat', 30))

        action_box = QGroupBox(parent=self)
        action_box.setFixedHeight(40)
        action_box.setMinimumWidth(500)
        alyt = QHBoxLayout()

        edit = QPushButton(parent=action_box, text='Edit')
        edit.setToolTip('Edit this event')
        edit.clicked.connect(self.startEditEvent)

        delete = QPushButton(parent=action_box, text='Delete')
        delete.setToolTip('Delete this event')
        delete.clicked.connect(self.startDelEvent)

        alyt.setContentsMargins(1, 1, 1, 1)
        alyt.addWidget(edit)
        alyt.addWidget(delete)
        action_box.setLayout(alyt)

        titlenote = QLabel(parent=self, text='Title: ')
        self.title = QLineEdit(parent=self)

        descriptionnote = QLabel(parent=self, text='Description: ')
        self.description = QTextEdit(parent=self)
        self.description.setMaximumHeight(300)

        datenote = QLabel(parent=self, text='Date: ')
        self.dateedit = QDateEdit(parent=self)

        timenote = QLabel(parent=self, text='Time: ')
        self.timeedit = QTimeEdit(parent=self)

        self.title.setEnabled(False)
        self.description.setEnabled(False)
        self.dateedit.setEnabled(False)
        self.timeedit.setEnabled(False)

        self.layout.addWidget(title, 1, 0, 1, 0, Qt.AlignCenter)

        self.layout.addWidget(action_box, 2, 0, 1, 0, Qt.AlignCenter)

        self.layout.addWidget(titlenote, 3, 0, Qt.AlignLeft)
        self.layout.addWidget(self.title, 3, 1, Qt.AlignRight)

        self.layout.addWidget(descriptionnote, 4, 0, Qt.AlignLeft)
        self.layout.addWidget(self.description, 4, 1, Qt.AlignRight)

        self.layout.addWidget(datenote, 5, 0, Qt.AlignLeft)
        self.layout.addWidget(self.dateedit, 5, 1, Qt.AlignRight)

        self.layout.addWidget(timenote, 6, 0, Qt.AlignLeft)
        self.layout.addWidget(self.timeedit, 6, 1, Qt.AlignRight)

    def startDelEvent(self):
        EventLogic.delEvent(self.event_id, self)

    def startEditEvent(self):
        self.ee.clear()
        self.ee.setEvent(self.event_id)
        self.ee.show()