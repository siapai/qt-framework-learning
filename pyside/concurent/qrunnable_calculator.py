import random
import sys
import time
import traceback
import uuid

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
    QMainWindow,
    QPushButton,
    QVBoxLayout,
    QWidget,
)

import pyqtgraph as pg


class WorkerSignals(QObject):
    data = Signal(tuple)


class Worker(QRunnable):
    def __init__(self):
        super().__init__()
        self.worker_id = uuid.uuid4().hex
        self.signals = WorkerSignals()

    @Slot()
    def run(self):
        total_n = 1000
        y2 = random.randint(0, 10)
        delay = random.random() / 100
        value = 0

        for n in range(total_n):
            y = random.randint(0, 10)
            value += n * y2 - n * y

            self.signals.data.emit((self.worker_id, n, value))
            time.sleep(delay)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.threadpool = QThreadPool()

        self.x = {}
        self.y = {}
        self.lines = {}

        layout = QVBoxLayout()
        self.graphWidget = pg.PlotWidget()
        self.graphWidget.setBackground('w')
        layout.addWidget(self.graphWidget)

        button = QPushButton('Create New Worker')
        button.clicked.connect(self.execute)

        layout.addWidget(button)

        w = QWidget()
        w.setLayout(layout)

        self.setCentralWidget(w)

        self.show()

    def execute(self):
        worker = Worker()
        worker.signals.data.connect(self.receive_data)
        self.threadpool.start(worker)

    def receive_data(self, data):
        worker_id, x, y = data

        if worker_id not in self.lines:
            self.x[worker_id] = [x]
            self.y[worker_id] = [y]

            pen = pg.mkPen(
                width=2,
                color=(
                    random.randint(100, 255),
                    random.randint(100, 255),
                    random.randint(100, 255)
                )
            )

            self.lines[worker_id] = self.graphWidget.plot(
                self.x[worker_id], self.y[worker_id], pen=pen
            )

            return
        # Update existing plot
        self.x[worker_id].append(x)
        self.y[worker_id].append(y)

        self.lines[worker_id].setData(self.x[worker_id], self.y[worker_id])


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    app.exec()
