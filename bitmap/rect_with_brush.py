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
        pen.setColor(QColor("#EB5160"))
        painter.setPen(pen)

        brush = QBrush()
        brush.setColor(QColor("#FFD141"))
        brush.setStyle(Qt.BrushStyle.Dense2Pattern)
        painter.setBrush(brush)

        painter.drawRects(
            QRect(50, 50, 100, 100),
            QRect(60, 60, 150, 100),
            QRect(70, 70, 100, 150),
            QRect(80, 80, 150, 100),
            QRect(90, 90, 100, 150),
        )
        painter.end()
        self.label.setPixmap(self.canvas)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()
