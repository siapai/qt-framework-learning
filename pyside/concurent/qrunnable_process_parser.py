import re
import subprocess
import sys

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
    QProgressBar,
    QPushButton,
    QVBoxLayout,
    QWidget,
)

progress_re = re.compile("Total complete: (\d+)%")


def simple_percent_parser(output):
    m = progress_re.search(output)
    if m:
        pc_complete = m.group(1)
        return int(pc_complete)


class WorkerSignals(QObject):
    result = Signal(str)
    progress = Signal(int)
    finished = Signal()


class SubProcessWorker(QRunnable):
    def __init__(self, command, parser=None):
        super().__init__()

        self.signals = WorkerSignals()
        self.command = command
        self.parser = parser

    @Slot()
    def run(self):
        result = []
        with subprocess.Popen(
            self.command,
            bufsize=-1,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            universal_newlines=True
        ) as proc:
            while proc.poll() is None:
                data = proc.stdout.readline()
                result.append(data)
                if self.parser:
                    value = self.parser(data)
                    if value:
                        self.signals.progress.emit(value)

        output = "".join(result)
        self.signals.result.emit(output)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.runner = None
        layout = QVBoxLayout()

        self.text = QPlainTextEdit()
        layout.addWidget(self.text)

        self.progress = QProgressBar()
        self.progress.setRange(0, 100)
        self.progress.setValue(0)
        layout.addWidget(self.progress)

        btn_run = QPushButton("Execute")
        btn_run.clicked.connect(self.start)

        layout.addWidget(btn_run)

        w = QWidget()
        w.setLayout(layout)
        self.setCentralWidget(w)

        self.threadpool = QThreadPool()
        self.show()

    def start(self):
        self.runner = SubProcessWorker(
            command=["python", "dummy_script.py"],
            parser=simple_percent_parser
        )
        self.runner.signals.result.connect(self.result)
        self.runner.signals.progress.connect(self.progress.setValue)
        self.threadpool.start(self.runner)

    def result(self, data):
        self.text.appendPlainText(data)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    app.exec()
