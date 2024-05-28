import re
import subprocess
import sys
from collections import namedtuple

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


def time_str_to_seconds(s):
    hours, minutes, seconds = s.split(":")
    hours = int(hours) * 3600
    minutes = int(minutes) * 60
    seconds = int(seconds)
    return hours + minutes + seconds


total_re = re.compile("Total time: (\d\d:\d\d:\d\d)")
elapsed_re = re.compile("Elapsed time: (\d\d:\d\d:\d\d)")


def time_to_percent_parser(l):
    total_time = None
    elapsed_time = None

    output = "".join(l)
    m = total_re.findall(output)
    if m:
        total_time = time_str_to_seconds(m[0])

    m = elapsed_re.findall(output)
    if m:
        elapsed_time = time_str_to_seconds(m[-1])

    if total_time and elapsed_time:
        return int(100 * elapsed_time / total_time)


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
                    value = self.parser(result)
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
            parser=time_to_percent_parser
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
