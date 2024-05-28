import sys

from PyQt6.QtCore import Qt
from PyQt6.QtGui import QAction
from PyQt6.QtWidgets import (
    QApplication,
    QMainWindow,
    QLabel,
    QStatusBar,
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

        button_action = QAction('Your button', self)
        button_action.setStatusTip('This is your button')
        button_action.triggered.connect(self.on_my_tool_bar_button_click)
        toolbar.addAction(button_action)

        self.setStatusBar(QStatusBar(self))

    @staticmethod
    def on_my_tool_bar_button_click(s):
        print(f'click {s}')


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()
