import sys
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QMainWindow, QComboBox, QApplication


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('My App')

        widget = QComboBox()
        widget.addItems(['One', 'Two', 'Three'])

        widget.currentIndexChanged.connect(self.index_changed)
        widget.currentTextChanged.connect(self.text_changed)

        self.setCentralWidget(widget)

    @staticmethod
    def index_changed(index):
        print(index)

    @staticmethod
    def text_changed(text):
        print(text)


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()
