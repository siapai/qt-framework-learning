import sys
import time
import random

from PySide6.QtCore import (
    QObject,
    QRunnable,
    QThreadPool,
    QTimer,
    Signal,
    Slot,
)
from PySide6.QtWidgets import (
    QApplication,
    QLabel,
    QMainWindow,
    QPushButton,
    QVBoxLayout,
    QWidget
)


class WorkerSignals(QObject):
    """
    Defines the signals available from a running worker thread.

    Supported signals are:

    finished
        No data

    error
        `str` Exception string

    result
        `dict` data returned from processing

    """
    finished = Signal()
    error = Signal(str)
    result = Signal(dict)


class Worker(QRunnable):
    def __init__(self, iterations=5):
        super().__init__()
        self.signals = (
            WorkerSignals()
        )
        self.iterations = iterations

    @Slot()
    def run(self):
        try:
            for n in range(self.iterations):
                time.sleep(0.01)
                v = 5 / (40 - n)
        except Exception as e:
            self.signals.error.emit(str(e))

        else:
            self.signals.finished.emit()
            self.signals.result.emit({"n": n, "value": v})


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.threadpool = QThreadPool()
        print(
            f"Multithreading with maximum {self.threadpool.maxThreadCount()} threads"
        )

        self.counter = 0
        layout = QVBoxLayout()

        self.label = QLabel("Start")
        b = QPushButton("Danger")
        b.pressed.connect(self.oh_no)

        layout.addWidget(self.label)
        layout.addWidget(b)

        widget = QWidget()
        widget.setLayout(layout)

        self.setCentralWidget(widget)
        self.show()

        self.timer = QTimer()
        self.timer.setInterval(1000)
        self.timer.timeout.connect(self.recurring_timer)
        self.timer.start()

    def oh_no(self):
        worker = Worker(iterations=random.randint(10, 50))
        worker.signals.result.connect(self.worker_output)
        worker.signals.finished.connect(self.worker_complete)
        worker.signals.error.connect(self.worker_error)
        self.threadpool.start(worker)

    @staticmethod
    def worker_output(s):
        print(f"Result: {s}")

    @staticmethod
    def worker_complete():
        print("THREAD COMPLETE!")

    @staticmethod
    def worker_error(s):
        print(f"Error: {s}")

    def recurring_timer(self):
        self.counter += 1
        self.label.setText(f"Counter: {self.counter}")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    app.exec()
