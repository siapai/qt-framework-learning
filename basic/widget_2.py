import os
import sys
from PyQt6.QtGui import QPixmap
from PyQt6.QtWidgets import QApplication, QLabel, QMainWindow

basedir = os.path.dirname(__file__)
print(f"Current working folder: {os.getcwd()}")
print(f"Paths are relative to: {basedir}")


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('My App')

        widget = QLabel('Hello World')
        # tag::scaledContents[]
        widget.setPixmap(QPixmap(os.path.join(basedir, "otje.jpg")))
        widget.setScaledContents(True)
        # end::scaledContents[]

        self.setCentralWidget(widget)


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()