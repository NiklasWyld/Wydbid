from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from BackEnd.WydbidBackEnd import OrderLogic

class DelOrder(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__()

        self.layout = QGridLayout()

        self.setLayout(self.layout)
        self.setWindowTitle('Wydbid - Delete order')
        self.setGeometry(0, 0, 600, 450)

        self.customer_id = 0

        self.startGetCustomer()
        self.setupUI()

    def startGetCustomer(self):
        customer_id = OrderLogic.getCustomerForDel(self)
        if customer_id == 0:
            self.hide()
            return
        self.customer_id = customer_id

    def setupUI(self):
        pass