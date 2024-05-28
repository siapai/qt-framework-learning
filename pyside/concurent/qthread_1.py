import sys
import time

from PySide6.QtCore import QThread, Signal, Slot
from PySide6.QtWidgets import QApplication, QLabel, QMainWindow


class Thread(QThread):
    result = Signal(str)

    @Slot()
    def run(self):
        print("Thread started")
        counter = 0
        while True:
            time.sleep(0.1)
            self.result.emit(f"The number is {counter}")
            counter += 1
        print("Thread complete")


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.thread = Thread()
        self.thread.start()

        label = QLabel("Hello World")

        self.thread.result.connect(label.setText)

        self.setCentralWidget(label)
        self.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    app.exec()
