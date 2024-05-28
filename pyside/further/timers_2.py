import sys

from PySide6.QtCore import Qt, QTimer
from PySide6.QtWidgets import QApplication, QMainWindow, QDial, QPushButton


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.button = QPushButton("Press")
        self.button.setCheckable(True)
        self.button.setStyleSheet(
            "QPushButton:checked { background-color: red; }"
        )

        self.button.toggled.connect(self.button_checked)
        self.setCentralWidget(self.button)
        self.show()

    def button_checked(self):
        print("Button checked")
        timer = QTimer()
        timer.setSingleShot(True)
        timer.setInterval(1000)
        # timer.setTimerType(Qt.PreciseTimer)
        timer.timeout.connect(self.uncheck_button)
        timer.start()

    def uncheck_button(self):
        print("Button unchecked")
        self.button.setChecked(False)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = MainWindow()
    app.exec()