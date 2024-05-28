import sys

from PyQt6.QtWidgets import (
    QApplication,
    QLabel,
    QMainWindow,
    QPushButton,
    QVBoxLayout,
    QWidget,
)
from random import randint


class AnotherWindow(QWidget):
    """
    This window is a QWidget. If it has no parent
    it will appear as a free-floating window
    """

    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()
        self.label = QLabel(f"Another window: {randint(0, 100)}")
        layout.addWidget(self.label)
        self.setLayout(layout)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.window1 = AnotherWindow()
        self.window2 = AnotherWindow()

        layout = QVBoxLayout()
        button1 = QPushButton("Push for Window 1")
        button1.clicked.connect(lambda: self.toggle_window(self.window1))
        layout.addWidget(button1)

        button2 = QPushButton("Push for Window 2")
        button2.clicked.connect(lambda: self.toggle_window(self.window2))
        layout.addWidget(button2)

        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

    @staticmethod
    def toggle_window(w):
        if w.isVisible():
            w.hide()

        else:
            w.show()

    # def toggle_window2(self, checked):
    #     if self.window2.isVisible():
    #         self.window2.hide()
    #     else:
    #         self.window2.show()


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()
