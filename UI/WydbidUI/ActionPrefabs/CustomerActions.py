from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from CustomQt import ActionButton
from UI.WydbidUI.Prefabs.Customer import CreateCustomer


class CustomerActions(QDialog):
    def __init__(self):
        super().__init__()

        self.layout = QGridLayout()

        self.setWindowTitle('Wydbid - Customer Actions')
        self.setGeometry(0, 0, 250, 200)

        # Widgets
        self.ck = CreateCustomer.CreateCustomer()

        self.setupUI()
        self.setLayout(self.layout)

    def setupUI(self):
        add_customer = ActionButton.ActionButton(parent=self, text='Add customer ➜', color='lightgreen',
                                                 color_hover='green')
        edit_customer = ActionButton.ActionButton(parent=self, text='Edit customer ➜', color='lightskyblue',
                                                  color_hover='blue')
        del_customer = ActionButton.ActionButton(parent=self, text='Delete customer ➜', color='lightcoral',
                                                 color_hover='red')

        self.layout.addWidget(add_customer, 1, 0, 1, 0, Qt.AlignCenter)
        self.layout.addWidget(edit_customer, 2, 0, 1, 0, Qt.AlignCenter)
        self.layout.addWidget(del_customer, 3, 0, 1, 0, Qt.AlignCenter)

        add_customer.clicked.connect(self.startCreateCustomer)

    def startCreateCustomer(self):
        self.ck.show()
        self.hide()