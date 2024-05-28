import os
import sys
from PyQt6.QtCore import Qt, QSize
from PyQt6.QtGui import QAction, QIcon
from PyQt6.QtWidgets import (
    QApplication,
    QMainWindow,
    QLabel,
    QStatusBar,
    QToolBar
)

basedir = os.path.dirname(__file__)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('My App')

        label = QLabel('Hello')
        label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.setCentralWidget(label)

        toolbar = QToolBar('My Toolbar')
        toolbar.setIconSize(QSize(16, 16))
        self.addToolBar(toolbar)

        button_action = QAction(
            QIcon(os.path.join(basedir, 'bug.png')),
            'Your button',
            self
        )
        button_action.setStatusTip('This is your button')
        button_action.triggered.connect(self.on_my_tool_bar_button_click)
        button_action.setCheckable(True)
        toolbar.addAction(button_action)

        self.setStatusBar(QStatusBar(self))

    @staticmethod
    def on_my_tool_bar_button_click(s):
        print(f'click {s}')


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()
