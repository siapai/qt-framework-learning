import sys
import time
import traceback

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
    progress = Signal(int)


class Worker(QRunnable):
    def __init__(self, *args, **kwargs):
        super().__init__()
        self.args = args
        self.kwargs = kwargs
        self.signals = WorkerSignals()

    @Slot()
    def run(self):
        total_n = 1000
        for n in range(total_n):
            progress_pc = int(
                100 * float(n + 1) / total_n
            )
            self.signals.progress.emit(progress_pc)
            time.sleep(0.01)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        layout = QVBoxLayout()
        self.progress = QProgressBar()

        button = QPushButton("START")
        button.pressed.connect(self.execute)

        layout.addWidget(button)
        layout.addWidget(self.progress)

        w = QWidget()
        w.setLayout(layout)

        self.setCentralWidget(w)

        self.show()

        self.threadpool = QThreadPool()
        print(
            f"Multithreading with maximum {self.threadpool.maxThreadCount()} threads"
        )

    def execute(self):
        worker = Worker()
        worker.signals.progress.connect(self.update_progress)
        self.threadpool.start(worker)

    def update_progress(self, progress):
        self.progress.setValue(progress)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    app.exec()
