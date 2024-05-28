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
    QLineEdit,
    QMainWindow,
    QPushButton,
    QSpinBox,
    QVBoxLayout,
    QWidget,
)


def extract_vars(l):
    data = {}
    for s in l.splitlines():
        if "=" in s:
            name, value = s.split("=")
            data[name] = value

    data["number_of_lines"] = len(l)
    return data


class WorkerSignals(QObject):
    result = Signal(dict)
    finished = Signal()


class SubProcessWorker(QRunnable):
    def __init__(self, command, process_result=None):
        super().__init__()

        self.signals = WorkerSignals()
        self.command = command
        self.process_result = process_result

    @Slot()
    def run(self):
        output = subprocess.getoutput(self.command)
        if self.process_result:
            output = self.process_result(output)

        self.signals.result.emit(output)
        self.signals.finished.emit()


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.runner = None
        layout = QVBoxLayout()

        self.name = QLineEdit()
        layout.addWidget(self.name)

        self.country = QLineEdit()
        layout.addWidget(self.country)

        self.website = QLineEdit()
        layout.addWidget(self.website)

        self.number_of_lines = QSpinBox()
        layout.addWidget(self.number_of_lines)

        btn_run = QPushButton("Execute")
        btn_run.clicked.connect(self.start)

        layout.addWidget(btn_run)

        w = QWidget()
        w.setLayout(layout)
        self.setCentralWidget(w)

        self.threadpool = QThreadPool()
        self.show()

    def start(self):
        self.runner = SubProcessWorker("python dummy_script.py", process_result=extract_vars)
        self.runner.signals.result.connect(self.result)
        self.threadpool.start(self.runner)

    def result(self, data):
        print(data)
        self.name.setText(data["name"])
        self.country.setText(data["country"])
        self.website.setText(data["website"])
        self.number_of_lines.setValue(data["number_of_lines"])


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    app.exec()
