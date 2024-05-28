import sys
import re

import requests
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
    QPlainTextEdit,
    QPushButton,
    QVBoxLayout,
    QWidget,
)


class WorkerSignals(QObject):
    data = Signal(tuple)


class Worker(QRunnable):
    def __init__(self, id, url, parsers):
        super().__init__()
        self.id = id
        self.url = url
        self.parsers = parsers

        self.signals = WorkerSignals()

    @Slot()
    def run(self):
        r = requests.get(self.url)

        data = {}

        for name, parser in self.parsers.items():
            m = parser.search(r.text)
            if m:
                data[name] = m.group(1).strip()

        self.signals.data.emit((self.id, data))


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.urls = [
            "https://www.pythonguis.com/",
            "https://www.mfitzp.com/",
            "https://www.google.com",
            "https://academy.pythonguis.com/",
        ]

        self.parsers = {  # <1>
            # Regular expression parsers, to extract data from the HTML.
            "title": re.compile(
                r"<title.*?>(.*?)<\/title>", re.M | re.S
            ),
            "h1": re.compile(r"<h1.*?>(.*?)<\/h1>", re.M | re.S),
            "h2": re.compile(r"<h2.*?>(.*?)<\/h2>", re.M | re.S),
        }

        layout = QVBoxLayout()

        self.text = QPlainTextEdit()
        self.text.setReadOnly(True)
        button = QPushButton("Go!")
        button.pressed.connect(self.execute)

        layout.addWidget(self.text)
        layout.addWidget(button)

        w = QWidget()
        w.setLayout(layout)

        self.setCentralWidget(w)

        self.show()

        self.threadpool = QThreadPool()
        print(
            "Multithreading with maximum %d threads"
            % self.threadpool.maxThreadCount()
        )

    def execute(self):
        for n, url in enumerate(self.urls):
            worker = Worker(n, url, self.parsers)
            worker.signals.data.connect(self.display_output)

            self.threadpool.start(worker)

    def display_output(self, data):
        id, s = data
        self.text.appendPlainText(f"WORKER {id}, {s}")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    app.exec()
