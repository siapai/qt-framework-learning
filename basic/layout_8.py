import sys

from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (
    QApplication,
    QMainWindow,
    QHBoxLayout,
    QLabel,
    QPushButton,
    QStackedLayout,
    QVBoxLayout,
    QWidget
)

from layout_color_widget import Color


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My App")

        page_layout = QVBoxLayout()
        button_layout = QHBoxLayout()
        self.stack_layout = QStackedLayout()

        page_layout.addLayout(button_layout)
        page_layout.addLayout(self.stack_layout)

        btn = QPushButton("red")
        btn.pressed.connect(lambda: self.activate_tab(0))
        button_layout.addWidget(btn)
        self.stack_layout.addWidget(Color("red"))

        btn = QPushButton("green")
        btn.pressed.connect(lambda: self.activate_tab(1))
        button_layout.addWidget(btn)
        self.stack_layout.addWidget(Color("green"))

        btn = QPushButton("yellow")
        btn.pressed.connect(lambda: self.activate_tab(2))
        button_layout.addWidget(btn)
        self.stack_layout.addWidget(Color("yellow"))

        widget = QWidget()
        widget.setLayout(page_layout)
        self.setCentralWidget(widget)

    def activate_tab(self, index):
        self.stack_layout.setCurrentIndex(index)

    def activate_tab_1(self):
        self.stack_layout.setCurrentIndex(0)

    def activate_tab_2(self):
        self.stack_layout.setCurrentIndex(1)

    def activate_tab_3(self):
        self.stack_layout.setCurrentIndex(2)


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()


