from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import *

class ActionButton(QPushButton):
    def __init__(self, parent: QWidget, text: str):
        super().__init__(parent=parent, text=text)

        self.setStyleSheet('''
                        QPushButton {
                            background-color: lightskyblue;
                            border: 1px solid gray;
                            padding: 3px;
                            border-radius: 10px;
                            color: black;
                        }

                        QPushButton:hover {
                            background-color: lightblue;
                        }
                        ''')

        self.setFixedSize(150, 30)