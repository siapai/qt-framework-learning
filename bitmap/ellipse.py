import sys

from PyQt6.QtCore import QPoint, Qt, QRect
from PyQt6.QtGui import QColor, QPainter, QPen, QPixmap, QBrush
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
        pen.setWidth(3)
        pen.setColor(QColor(75, 75, 200))  # RGB
        painter.setPen(pen)

        # painter.drawEllipse(10, 10, 100, 100)
        # painter.drawEllipse(10, 10, 150, 200)
        # painter.drawEllipse(10, 10, 200, 300)

        painter.drawEllipse(QPoint(100, 100), 10, 10)
        painter.drawEllipse(QPoint(100, 100), 15, 20)
        painter.drawEllipse(QPoint(100, 100), 20, 30)
        painter.drawEllipse(QPoint(100, 100), 25, 40)
        painter.drawEllipse(QPoint(100, 100), 30, 50)
        painter.drawEllipse(QPoint(100, 100), 35, 60)
        painter.end()
        self.label.setPixmap(self.canvas)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()
