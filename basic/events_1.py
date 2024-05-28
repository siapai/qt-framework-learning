import sys
from PyQt6.QtWidgets import (
    QApplication,
    QLabel,
    QMainWindow,
    QTextEdit
)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.label = QLabel("Click in this windows")
        self.setCentralWidget(self.label)

    def mouseMoveEvent(self, event):
        self.label.setText("mouseMoveEvent")

    def mousePressEvent(self, event):
        self.label.setText("mousePressEvent")

    def mouseReleaseEvent(self, event):
        self.label.setText("mouseReleaseEvent")

    def mouseDoubleClickEvent(self, event):
        self.label.setText("mouseDoubleClickEvent")


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()
