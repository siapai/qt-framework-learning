import sys

from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtCore import Qt


class _Bar(QtWidgets.QWidget):
    def __init__(self, steps):
        super().__init__()
        self.setSizePolicy(
            QtWidgets.QSizePolicy.Policy.MinimumExpanding,
            QtWidgets.QSizePolicy.Policy.MinimumExpanding
        )

        if isinstance(steps, list):
            self.n_steps = len(steps)
            self.steps = steps

        elif isinstance(steps, int):
            self.n_steps = steps
            self.steps = ["red"] * steps

        else:
            raise TypeError(f"steps must be a list or int")

        self._bar_solid_percent = 0.8
        self._background_color = QtGui.QColor(0, 0, 0)
        self._padding = 4

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

        d_height = painter.device().height() - (self._padding * 2)
        d_width = painter.device().width() - (self._padding * 2)

        step_size = d_height / self.n_steps
        bar_height = step_size * self._bar_solid_percent

        pc = (value - v_min) / (v_max - v_min)
        n_steps_to_draw = int(pc * self.n_steps)

        for n in range(n_steps_to_draw):
            brush.setColor(QtGui.QColor(self.steps[n]))
            y_pos = (1 + n) * step_size
            rect = QtCore.QRect(
                self._padding,
                self._padding + d_height - int(y_pos),
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
        self._bar = _Bar(steps)
        layout.addWidget(self._bar)

        self.dial = QtWidgets.QDial()
        self.dial.valueChanged.connect(self._bar.trigger_refresh)
        layout.addWidget(self.dial)

        self.setLayout(layout)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    volume = PowerBar(
        steps=[
            "#5e4fa2",
            "#3288bd",
            "#66c2a5",
            "#abdda4",
            "#e6f598",
            "#ffffbf",
            "#fee08b",
            "#fdae61",
            "#f46d43",
            "#d53e4f",
            "#9e0142",
        ]
    )
    volume.show()
    app.exec()
