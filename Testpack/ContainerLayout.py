import sys
from PyQt6.QtWidgets import QApplication
from PyQt6.QtWidgets import QHBoxLayout
from PyQt6.QtWidgets import QVBoxLayout
from PyQt6.QtWidgets import QPushButton
from PyQt6.QtWidgets import QWidget

myApp = QApplication(sys.argv)


myWindow = QWidget()
myWindow.setWindowTitle('Container parking')


h_layout = QHBoxLayout()
v_layout = QVBoxLayout()

h_layout.addWidget(QPushButton('Container 1'))
h_layout.addWidget(QPushButton('Container 2'))
h_layout.addWidget(QPushButton('Container 3'))
h_layout.addWidget(QPushButton('Container 4'))
h_layout.addWidget(QPushButton('Container 5'))
h_layout.addWidget(QPushButton('Container 6'))

v_layout.addWidget(QPushButton('Container 7'))
v_layout.addWidget(QPushButton('Container 8'))
v_layout.addWidget(QPushButton('Container 9'))
v_layout.addWidget(QPushButton('Container 10'))
v_layout.addWidget(QPushButton('Container 11'))
v_layout.addWidget(QPushButton('Container 12'))

myWindow.setLayout(h_layout)
myWindow.setLayout(v_layout)

myWindow.show()
sys.exit(myApp.exec())