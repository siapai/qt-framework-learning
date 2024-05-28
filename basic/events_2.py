import sys

from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QLabel, QMainWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.label = QLabel("Click in this window")
        self.setCentralWidget(self.label)

    def mouseMoveEvent(self, event):
        pos = event.position()
        self.label.setText(f"mouseMoveEVent: {pos}")

    def mousePressEvent(self, event):
        if event.button() == Qt.MouseButton.LeftButton:
            self.label.setText("mousePressEvent: LEFT")
        elif event.button() == Qt.MouseButton.MiddleButton:
            self.label.setText("mousePressEvent: MIDDLE")
        elif event.button() == Qt.MouseButton.RightButton:
            self.label.setText("mousePressEvent: RIGHT")

    def mouseReleaseEvent(self, event):
        if event.button() == Qt.MouseButton.LeftButton:
            self.label.setText("mouseReleaseEvent: LEFT")
        elif event.button() == Qt.MouseButton.MiddleButton:
            self.label.setText("mouseReleaseEvent: MIDDLE")
        elif event.button() == Qt.MouseButton.RightButton:
            self.label.setText("mouseReleaseEvent: RIGHT")


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()
