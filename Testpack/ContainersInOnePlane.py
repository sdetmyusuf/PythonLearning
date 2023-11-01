import sys
from PyQt6.QtWidgets import QApplication
from PyQt6.QtWidgets import QGridLayout
from PyQt6.QtWidgets import QPushButton
from PyQt6.QtWidgets import QWidget

myApp = QApplication(sys.argv)

myWindow = QWidget()

myWindow.setWindowTitle('Container Parking 2')

gridLayout = QGridLayout()
gridLayout.addWidget(QPushButton('Container 1'), 0, 0)
gridLayout.addWidget(QPushButton('Container 2'), 0, 1)
gridLayout.addWidget(QPushButton('Container 3'), 0, 2)
gridLayout.addWidget(QPushButton('Container 4'), 0, 3)
gridLayout.addWidget(QPushButton('Container 5'), 1, 0)
gridLayout.addWidget(QPushButton('Container 6'), 1, 1)
gridLayout.addWidget(QPushButton('Container 7'), 1, 2)
gridLayout.addWidget(QPushButton('Container 8'), 1, 3)
gridLayout.addWidget(QPushButton('Container 9'), 2, 0)
gridLayout.addWidget(QPushButton('Container 10'), 2, 1)
gridLayout.addWidget(QPushButton('Container 11'), 2, 3)
gridLayout.addWidget(QPushButton('Container 12'), 3, 0)
gridLayout.addWidget(QPushButton('Container 13'), 3, 2)
gridLayout.addWidget(QPushButton('Container 14'), 3, 3)

myWindow.setLayout(gridLayout)

myWindow.show()
sys.exit(myApp.exec())