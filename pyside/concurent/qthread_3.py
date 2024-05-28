import sys
import time

from PySide6.QtCore import QThread, Signal, Slot
from PySide6.QtWidgets import (
    QApplication,
    QLabel,
    QMainWindow,
    QPushButton,
    QVBoxLayout,
    QWidget,
)


class Thread(QThread):
    result = Signal(str)

    def __init__(self):
        super().__init__()
        self.is_running = None
        self.data = None

    @Slot()
    def run(self):
        print("Thread started")
        self.data = None
        self.is_running = True
        counter = 0
        while self.is_running:
            time.sleep(0.1)
            self.result.emit(f"The number is {counter}")
            counter += 1

    def stop(self):
        self.is_running = False


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.thread = Thread()
        self.thread.start()

        label = QLabel("Output here")
        button = QPushButton("Stop")
        button.pressed.connect(self.thread.stop)

        self.thread.result.connect(label.setText)
        self.thread.finished.connect(self.thread_has_finished)

        container = QWidget()
        layout = QVBoxLayout()
        layout.addWidget(label)
        layout.addWidget(button)
        container.setLayout(layout)

        self.setCentralWidget(container)
        self.show()

    def thread_has_finished(self):
        print("Thread has finished.")
        print(
            self.thread,
            self.thread.isRunning(),
            self.thread.isFinished(),
        )


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    app.exec()
