from PyQt6.QtCore import QT_VERSION_STR
from PyQt6.QtWidgets import QApplication, QWidget, QHBoxLayout, QPushButton
import sys


def main():
    application = QApplication(sys.argv)
    widget = QWidget()
    widget.resize(250, 250)
    widget.setWindowTitle("Parking Lot")
    widget.show()
    sys.exit(application.exec())


print(QT_VERSION_STR)


class MainLayout(QWidget):
    def __init__(self):
        super().__init__()
        self.okButton = None
        self.twoWidgets()

    def twoWidgets(self):
        self.okButton = QPushButton("OK", self)

    def horizontalLayout(self):
        horizontalBar = QHBoxLayout()


if __name__ == '__main__':
    main()
