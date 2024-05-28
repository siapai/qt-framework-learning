import sys
import time

from PySide6.QtCore import QTimer
from PySide6.QtWidgets import (
    QApplication,
    QLabel,
    QMainWindow,
    QPushButton,
    QVBoxLayout,
    QWidget
)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.message = "Start"

        layout = QVBoxLayout()
        self.label = QLabel(self.message)
        b = QPushButton("DANGER!")
        b.pressed.connect(self.oh_no)

        c = QPushButton("?")
        c.pressed.connect(self.change_message)

        layout.addWidget(self.label)
        layout.addWidget(b)
        layout.addWidget(c)

        widget = QWidget()
        widget.setLayout(layout)

        self.setCentralWidget(widget)
        self.show()

    def oh_no(self):
        self.message = "Pressed"

    def change_message(self):
        self.message = "OH NO"

        for _ in range(100):
            time.sleep(0.1)
            self.label.setText(self.message)
            QApplication.processEvents()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    app.exec()