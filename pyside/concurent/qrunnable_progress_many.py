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
    QLabel,
    QMainWindow,
    QProgressBar,
    QPushButton,
    QVBoxLayout,
    QWidget,
)


class WorkerSignals(QObject):
    progress = Signal(str, int)
    finished = Signal(str)


class Worker(QRunnable):
    def __init__(self):
        super().__init__()
        self.job_id = uuid.uuid4().hex
        self.signals = WorkerSignals()

    @Slot()
    def run(self):
        total_n = 1000
        delay = random.random() / 100
        for n in range(total_n):
            progress_pc = int(
                100 * float(n + 1) / total_n
            )
            self.signals.progress.emit(self.job_id, progress_pc)
            time.sleep(delay)
        self.signals.finished.emit(self.job_id)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        layout = QVBoxLayout()
        self.progress = QProgressBar()

        button = QPushButton("START")
        button.pressed.connect(self.execute)

        self.status = QLabel("0 workers")

        layout.addWidget(self.progress)
        layout.addWidget(button)
        layout.addWidget(self.status)

        w = QWidget()
        w.setLayout(layout)

        self.worker_progress = {}

        self.setCentralWidget(w)

        self.show()

        self.threadpool = QThreadPool()
        print(
            f"Multithreading with maximum {self.threadpool.maxThreadCount()} threads"
        )

        self.timer = QTimer()
        self.timer.setInterval(1000)
        self.timer.timeout.connect(self.refresh_progress)
        self.timer.start()

    def execute(self):
        worker = Worker()
        worker.signals.progress.connect(self.update_progress)
        worker.signals.finished.connect(self.cleanup)
        self.threadpool.start(worker)

    def update_progress(self, job_id, progress):
        self.worker_progress[job_id] = progress

    def cleanup(self, job_id):
        if job_id in self.worker_progress:
            del self.worker_progress[job_id]
            self.refresh_progress()

    def refresh_progress(self):
        progress = self.calculate_progress()
        print(self.worker_progress)
        self.progress.setValue(progress)
        self.status.setText(f"{len(self.worker_progress)} workers")

    def calculate_progress(self):
        if not self.worker_progress:
            return 0
        return sum(v for v in self.worker_progress.values()) / len(self.worker_progress)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    app.exec()
