import sys
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QMainWindow, QDial


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('My App')

        widget = QDial()
        widget.setRange(-10, 100)
        widget.setSingleStep(1)

        widget.valueChanged.connect(self.value_changed)
        widget.sliderMoved.connect(self.slider_moved)
        widget.sliderPressed.connect(self.slider_pressed)
        widget.sliderReleased.connect(self.slider_released)

        self.setCentralWidget(widget)

    @staticmethod
    def value_changed(value):
        print(f"Value: {value}")

    @staticmethod
    def slider_moved(pos):
        print(f"Position: {pos}")

    @staticmethod
    def slider_pressed():
        print("Slider Pressed")

    @staticmethod
    def slider_released():
        print("Slider Released")


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()



