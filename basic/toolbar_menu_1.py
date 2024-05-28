import sys

from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (
    QApplication,
    QMainWindow,
    QLabel,
    QToolBar
)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('My App')

        label = QLabel('Hello')
        label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.setCentralWidget(label)

        toolbar = QToolBar('My Toolbar')
        self.addToolBar(toolbar)

    def onMyToolBarButtonClick(self, s):
        print(f'click {s}')


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()
