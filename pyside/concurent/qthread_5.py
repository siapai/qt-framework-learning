import sys
import time

from PySide6.QtCore import QThread, Signal, Slot
from PySide6.QtWidgets import (
    QApplication,
    QLabel,
    QMainWindow,
    QPushButton,
    QSpinBox,
    QVBoxLayout,
    QWidget,
)


class Thread(QThread):
    result = Signal(str)

    def __init__(self, initial):
        super().__init__()
        self.is_running = None
        self.data = initial

    @Slot()
    def run(self):
        print("Thread started")
        self.is_running = True
        counter = 0
        while True:
            while self.data is None:
                if not self.is_running:
                    return
                time.sleep(0.1)
            counter += self.data
            self.result.emit(f"The cumulative total is {counter}")
            self.data = None

    def send_data(self, data):
        self.data = data

    def stop(self):
        self.is_running = False


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.thread = Thread(500)
        self.thread.start()

        self.numeric_input = QSpinBox()
        button_input = QPushButton("Submit number")

        label = QLabel("Output here")
        button = QPushButton("Stop")
        button.pressed.connect(self.thread.stop)
        button_input.pressed.connect(self.submit_data)
        self.thread.result.connect(label.setText)
        self.thread.finished.connect(self.thread_has_finished)

        container = QWidget()
        layout = QVBoxLayout()
        layout.addWidget(self.numeric_input)
        layout.addWidget(button_input)
        layout.addWidget(label)
        layout.addWidget(button)
        container.setLayout(layout)

        self.setCentralWidget(container)
        self.show()

    def submit_data(self):
        self.thread.send_data(self.numeric_input.value())

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
