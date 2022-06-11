from PyQt5.QtWidgets import QMessageBox, QWidget

class MessageBox(QMessageBox):
    def __init__(self, parent: QWidget, title: str, text: str):
        super().__init__()
        self.setParent(parent)
        self.setWindowTitle(title)
        self.setText(text)
