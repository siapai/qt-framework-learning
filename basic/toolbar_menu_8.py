import os
import sys
from PyQt6.QtCore import Qt, QSize
from PyQt6.QtGui import QAction, QIcon
from PyQt6.QtWidgets import (
    QApplication,
    QMainWindow,
    QLabel,
    QStatusBar,
    QToolBar, QCheckBox
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
            '&Your button',
            self
        )
        button_action.setStatusTip('This is your button')
        button_action.triggered.connect(self.on_my_tool_bar_button_click)
        button_action.setCheckable(True)
        toolbar.addAction(button_action)

        toolbar.addSeparator()

        button_action2 = QAction(
            QIcon(os.path.join(basedir, 'bug.png')),
            'Your &button2',
            self
        )
        button_action2.setStatusTip('This is your button 2')
        button_action2.triggered.connect(self.on_my_tool_bar_button_click)
        button_action2.setCheckable(True)
        toolbar.addAction(button_action2)

        toolbar.addWidget(QLabel('Button 2'))
        toolbar.addWidget(QCheckBox('Yes'))

        self.setStatusBar(QStatusBar(self))

        menu = self.menuBar()

        file_menu = menu.addMenu('&File')
        file_menu.addAction(button_action)
        file_menu.addSeparator()
        file_menu.addAction(button_action2)

    @staticmethod
    def on_my_tool_bar_button_click(s):
        print(f'click {s}')


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()
