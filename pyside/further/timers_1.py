import sys

from PySide6.QtCore import QTimer, Qt
from PySide6.QtWidgets import QApplication, QMainWindow, QDial


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.dial = QDial()
        self.dial.setRange(10, 100)
        self.dial.setValue(0)

        self.timer = QTimer()
        self.timer.setInterval(10)
        self.timer.timeout.connect(self.update_dial)
        self.timer.setTimerType(Qt.PreciseTimer)
        self.timer.start()

        self.setCentralWidget(self.dial)
        self.show()

    def update_dial(self):
        value = self.dial.value()
        value += 1
        if value > 100:
            value = 0
        self.dial.setValue(value)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = MainWindow()
    app.exec()