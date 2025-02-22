import sys
from functools import partial

from PyQt6.QtCore import QPoint, QSize, Qt
from PyQt6.QtGui import QColor, QPainter, QPen, QPixmap
from PyQt6.QtWidgets import (
    QApplication,
    QHBoxLayout,
    QLabel,
    QMainWindow,
    QPushButton,
    QVBoxLayout,
    QWidget,
)


COLORS = [
    # 17 undertones https://lospec.com/palette-list/17undertones
    "#000000",
    "#141923",
    "#414168",
    "#3a7fa7",
    "#35e3e3",
    "#8fd970",
    "#5ebb49",
    "#458352",
    "#dcd37b",
    "#fffee5",
    "#ffd035",
    "#cc9245",
    "#a15c3e",
    "#a42f3b",
    "#f45b7a",
    "#c24998",
    "#81588d",
    "#bcb0c2",
    "#ffffff",
]


class QPaletteButton(QPushButton):
    def __init__(self, color):
        super().__init__()
        self.setFixedSize(QSize(24, 24))
        self.color = color
        self.setStyleSheet(f"background-color: {color}")


class Canvas(QLabel):
    def __init__(self):
        super().__init__()
        self._pixmap = QPixmap(600, 300)
        self._pixmap.fill(Qt.GlobalColor.white)
        self.setPixmap(self._pixmap)

        self.last_x, self.last_y = None, None
        self.pen_color = QColor("#000000")

    def set_pen_color(self, c):
        self.pen_color = QColor(c)

    def mouseMoveEvent(self, e):
        pos = e.position()
        if self.last_x is None or self.last_y is None:
            self.last_x = pos.x()
            self.last_y = pos.y()
            return

        painter = QPainter(self._pixmap)
        p = painter.pen()
        p.setWidth(4)
        p.setColor(self.pen_color)
        painter.setPen(p)
        painter.drawLine(self.last_x, self.last_y, pos.x(), pos.y())
        painter.end()

        self.setPixmap(self._pixmap)

        self.last_x, self.last_y = pos.x(), pos.y()

    def mouseReleaseEvent(self, e):
        self.last_x, self.last_y = None, None


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.canvas = Canvas()

        widget = QWidget()
        layout = QVBoxLayout()
        widget.setLayout(layout)
        layout.addWidget(self.canvas)

        palette = QHBoxLayout()
        self.add_palette_buttons(palette)
        layout.addLayout(palette)

        self.setCentralWidget(widget)

    def add_palette_buttons(self, layout):
        for color in COLORS:
            button = QPaletteButton(color)
            button.pressed.connect(lambda c=color: self.canvas.set_pen_color(c))
            layout.addWidget(button)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()
