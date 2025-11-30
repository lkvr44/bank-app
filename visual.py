from PyQt5.QtWidgets import (QApplication, QWidget, QPushButton, QLabel, QVBoxLayout, QHBoxLayout, QListWidget, QFileDialog) 
from PyQt5.QtCore import Qt
import pandas as pd
import sys
import datetime
amount = 50.0
balance = 0.0
print(datetime.datetime.now())
df = pd.read_csv('bank.csv')

def do_withdraw ():
    global amount
    global balance
    balance = balance - amount 
    BLabel.setText(f'У вас: {str(balance)} деняк')
   
def do_get ():
    global amount
    global balance
    balance = balance + amount  
    BLabel.setText(f'У вас: {str(balance)} деняк')


def bank_safe ():
    pass
    # df.to_csv('bank.csv', index=False, header = ['a','b','c'])

app = QApplication([])
window = QWidget()
window.setWindowTitle('Your Bank')
window.resize(700, 500)

withdraw = QPushButton('Снять деньги')
get = QPushButton('Получить деньги')
history = QPushButton('История')
withdraws = QPushButton('Снятия')
diogram = QPushButton('Диаграмма')
BLabel = QLabel(f'У вас: {str(balance)} деняк')


col = QVBoxLayout()
row = QHBoxLayout()
row2 = QHBoxLayout()
row3 = QHBoxLayout()

row.addWidget(BLabel, alignment= Qt.AlignCenter)

row2.addWidget(withdraw)
row2.addWidget(get)

row3.addWidget(history)
row3.addWidget(withdraws)
row3.addWidget(diogram)

col.addLayout(row)
col.addLayout(row2)
col.addLayout(row3)


window.setLayout(col)
window.show()

withdraw.clicked.connect(do_withdraw)
get.clicked.connect(do_get)

app.exec_()
bank_safe()