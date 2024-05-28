import subprocess
import sys
from multiprocessing.pool import ThreadPool

from PySide6.QtCore import (
    QObject,
    QRunnable,
    QThreadPool,
    Signal,
    Slot,
)
from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QPlainTextEdit,
    QPushButton,
    QVBoxLayout,
    QWidget,
)


class WorkerSignals(QObject):
    result = Signal(str)
    finished = Signal()


class SubProcessWorker(QRunnable):
    def __init__(self, command):
        super().__init__()

        self.signals = WorkerSignals()
        self.command = command

    @Slot()
    def run(self):
        output = subprocess.getoutput(self.command)
        self.signals.result.emit(output)
        self.signals.finished.emit()


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.runner = None
        layout = QVBoxLayout()
        self.text = QPlainTextEdit()
        layout.addWidget(self.text)
        btn_run = QPushButton("Execute")
        btn_run.clicked.connect(self.start)
        layout.addWidget(btn_run)
        w = QWidget()
        w.setLayout(layout)
        self.setCentralWidget(w)

        self.threadpool = QThreadPool()
        self.show()

    def start(self):
        self.runner = SubProcessWorker("python dummy_script.py")
        self.runner.signals.result.connect(self.result)
        self.threadpool.start(self.runner)

    def result(self, s):
        self.text.insertPlainText(s)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    app.exec()
