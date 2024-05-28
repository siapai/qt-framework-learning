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
        self.input_add = None
        self.input_multiply = None
        self.waiting_for_data = True
        self.is_running = True
        self.counter = initial

    @Slot()
    def run(self):
        print("Thread started")
        self.is_running = True
        self.waiting_for_data = True
        while True:
            while self.waiting_for_data:
                if not self.is_running:
                    return
                time.sleep(0.1)
            self.counter += self.input_add
            self.counter *= self.input_multiply
            self.result.emit(f"The cumulative total is {self.counter}")
            self.waiting_for_data = True

    def send_data(self, add, multiply):
        self.input_add = add
        self.input_multiply = multiply
        self.waiting_for_data = False

    def stop(self):
        self.is_running = False


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.thread = Thread(500)
        self.thread.start()

        self.add_input = QSpinBox()
        self.mult_input = QSpinBox()
        button_input = QPushButton("Submit number")

        label = QLabel("Output here")
        button = QPushButton("Stop")
        button.pressed.connect(self.thread.stop)
        button_input.pressed.connect(self.submit_data)
        self.thread.result.connect(label.setText)
        self.thread.finished.connect(self.thread_has_finished)

        container = QWidget()
        layout = QVBoxLayout()
        layout.addWidget(self.add_input)
        layout.addWidget(self.mult_input)
        layout.addWidget(button_input)
        layout.addWidget(label)
        layout.addWidget(button)
        container.setLayout(layout)

        self.setCentralWidget(container)
        self.show()

    def submit_data(self):
        self.thread.send_data(self.add_input.value(), self.mult_input.value())

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
