import sys

from PyQt6.QtCore import QPoint, Qt, QRect
from PyQt6.QtGui import QColor, QPainter, QPen, QPixmap, QBrush, QFont
from PyQt6.QtWidgets import QApplication, QLabel, QMainWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.label = QLabel()
        self.canvas = QPixmap(400, 300)
        self.canvas.fill(Qt.GlobalColor.white)
        self.label.setPixmap(self.canvas)
        self.setCentralWidget(self.label)

        self.last_x, self.last_y = None, None

    def mouseMoveEvent(self, event):
        pos = event.position()
        if self.last_x is None or self.last_y is None:
            self.last_x = pos.x()
            self.last_y = pos.y()

        painter = QPainter(self.canvas)
        painter.drawLine(self.last_x, self.last_y, pos.x(), pos.y())
        painter.end()

        self.label.setPixmap(self.canvas)

        # Update origin next time
        self.last_x, self.last_y = pos.x(), pos.y()

    def mouseReleaseEvent(self, event):
        self.last_x, self.last_y = None, None


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()
