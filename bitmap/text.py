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
        self.setCentralWidget(self.label)
        self.draw_something()

    def draw_something(self):
        painter = QPainter(self.canvas)
        pen = QPen()
        pen.setWidth(1)
        pen.setColor(QColor("green"))
        painter.setPen(pen)

        font = QFont()
        font.setFamily("Times")
        font.setBold(True)
        font.setPointSize(40)

        painter.setFont(font)

        # painter.drawText(100, 100, "Hello World!")
        painter.drawText(100, 100, 100, 100, Qt.AlignmentFlag.AlignHCenter, 'Hello, world!')

        painter.end()
        self.label.setPixmap(self.canvas)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()
