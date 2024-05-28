import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QSpinBox


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('My App')

        widget = QSpinBox()

        widget.setMinimum(-10)
        widget.setMaximum(3)
        # widget.setRage(-10, 3)

        widget.setPrefix('$')
        widget.setSuffix('c')
        widget.setSingleStep(3)
        widget.valueChanged.connect(self.value_changed)
        widget.textChanged.connect(self.text_changed)

        self.setCentralWidget(widget)

    @staticmethod
    def value_changed(value):
        print(f"Value changed: {value}")

    @staticmethod
    def text_changed(text):
        print(f"Text changed: {text}")


app = QApplication(sys.argv)
window = MainWindow()
window.show()

app.exec()