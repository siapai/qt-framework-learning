import os
import sys

from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QMainWindow, QTableView


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.table = QTableView()
        self.setCentralWidget(self.table)


app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()
