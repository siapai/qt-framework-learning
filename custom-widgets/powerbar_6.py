import sys

from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtCore import Qt


class _Bar(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setSizePolicy(
            QtWidgets.QSizePolicy.Policy.MinimumExpanding,
            QtWidgets.QSizePolicy.Policy.MinimumExpanding
        )

    def sizeHint(self):
        return QtCore.QSize(40, 120)

    def paintEvent(self, e):
        painter = QtGui.QPainter(self)

        brush = QtGui.QBrush()
        brush.setColor(QtGui.QColor("black"))
        brush.setStyle(Qt.BrushStyle.SolidPattern)
        rect = QtCore.QRect(
            0,
            0,
            painter.device().width(),
            painter.device().height()
        )

        painter.fillRect(rect, brush)

        # Get current state
        dial = self.parent().dial
        v_min, v_max = dial.minimum(), dial.maximum()
        value = dial.value()

        pc = (value - v_min) / (v_max - v_min)
        n_steps_to_draw = int(pc * 5)

        padding = 5

        d_height = painter.device().height() - (padding * 2)
        d_width = painter.device().width() - (padding * 2)

        step_size = d_height / 5
        bar_height = step_size * 0.6

        brush.setColor(QtGui.QColor("red"))

        for n in range(n_steps_to_draw):
            y_pos = (1 + n) * step_size
            rect = QtCore.QRect(
                padding,
                padding + d_height - int(y_pos),
                d_width,
                int(bar_height)
            )
            painter.fillRect(rect, brush)
        painter.end()

    def trigger_refresh(self):
        self.update()


class PowerBar(QtWidgets.QWidget):
    def __init__(self, parent=None, steps=5):
        super().__init__(parent)

        layout = QtWidgets.QVBoxLayout()
        self._bar = _Bar()
        layout.addWidget(self._bar)

        self.dial = QtWidgets.QDial()
        self.dial.valueChanged.connect(self._bar.trigger_refresh)
        layout.addWidget(self.dial)

        self.setLayout(layout)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    volume = PowerBar()
    volume.show()
    app.exec()
