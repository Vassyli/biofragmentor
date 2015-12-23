import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import uic

class MainWindow(QMainWindow):
    app = None
    def __init__(self):
        self.app = QApplication(sys.argv)
        super().__init__()

        self.ui = uic.loadUi("gui/main.ui")
        self.ui.show()

        self.app.exec_()