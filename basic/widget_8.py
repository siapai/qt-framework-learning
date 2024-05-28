import sys

from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QMainWindow, QSlider


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('My App')

        widget = QSlider(Qt.Orientation.Horizontal)

        widget.setRange(-10, 3)
        widget.setSingleStep(3)

        widget.valueChanged.connect(self.value_changed)
        widget.sliderMoved.connect(self.slider_position)
        widget.sliderPressed.connect(self.slider_pressed)
        widget.sliderReleased.connect(self.slider_released)

        self.setCentralWidget(widget)

    @staticmethod
    def value_changed(value):
        print(f"Value changed: {value}")

    @staticmethod
    def slider_position(pos):
        print(f"Slider position: {pos}")

    @staticmethod
    def slider_pressed():
        print(f"Slider pressed")

    @staticmethod
    def slider_released():
        print(f"Slider released")


app = QApplication(sys.argv)
window = MainWindow()
window.show()

app.exec()
