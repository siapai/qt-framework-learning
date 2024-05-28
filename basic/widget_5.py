import sys

from PyQt6.QtWidgets import QMainWindow, QListWidget, QApplication


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('My App')

        widget = QListWidget()
        widget.addItems(['One', 'Two', 'Three'])

        widget.currentItemChanged.connect(self.item_changed)
        widget.currentTextChanged.connect(self.text_changed)

        self.setCentralWidget(widget)

    @staticmethod
    def item_changed(item):
        print(item)

    @staticmethod
    def text_changed(text):
        print(text)


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()
