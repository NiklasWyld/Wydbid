import os
import pickle
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys
from CreateKunden import Kunde

app = QApplication(sys.argv)

window = QWidget()

list = QTableWidget(parent=window)
list.setGeometry(10, 10, 400, 800)
list.verticalHeader().setVisible(False)

kunden = []
dateien = os.listdir('./Kunden/')

for datei in dateien:
    kunde: Kunde = pickle.load(open(f'./Kunden/{datei}', 'rb'))
    kunden.append(kunde)

kunden.sort(key=lambda x: x.id, reverse=False)

list.setRowCount(len(kunden))
list.setColumnCount(4)
list.setHorizontalHeaderLabels(['Name', 'Kundennummer', 'Alter', ''])

i = 0

list.setSortingEnabled(False)
list.setFocusPolicy(Qt.NoFocus)
list.setSelectionMode(QAbstractItemView.SelectionMode.NoSelection)

for kunde in kunden:
    list.setItem(i, 0, QTableWidgetItem(kunde.name))

    id = QTableWidgetItem()
    id.setData(Qt.DisplayRole, kunde.id)

    old = QTableWidgetItem()
    old.setData(Qt.DisplayRole, kunde.old)

    ansicht = QTableWidgetItem()
    ansicht.setData(Qt.DisplayRole, '🔎')
    ansicht.setTextAlignment(Qt.AlignCenter)
    list.setColumnWidth(3, 40)

    list.setItem(i, 1, id)
    list.setItem(i, 2, old)
    list.setItem(i, 3, ansicht)
    i = i + 1

def test(__item):
    if __item.data() == '🔎':
        getKunde(_item=__item)

def getKunde(_item: QModelIndex):
    kunden_id = list.item(_item.row(), 1).text()
    kunde2: Kunde = pickle.load(open(f'./Kunden/{kunden_id}kunde.kunde', 'rb'))
    p = QMessageBox(parent=window)
    p.setWindowTitle('Hello World')
    p.setText(f'{kunde2.name}, {kunde2.id}, {kunde2.old}')
    p.exec()

list.setSortingEnabled(True)
list.clicked.connect(test)

list.setEditTriggers(QAbstractItemView.NoEditTriggers)

window.showMaximized()

sys.exit(app.exec_())