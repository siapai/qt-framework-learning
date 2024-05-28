import sys
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QMainWindow, QCheckBox


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('My App')
        widget = QCheckBox("This is a checkbox")
        widget.setCheckState(Qt.CheckState.Checked)

        widget.stateChanged.connect(self.show_state)
        self.setCentralWidget(widget)

    @staticmethod
    def show_state(state):
        print(Qt.CheckState(state) == Qt.CheckState.Checked)
        print(state)


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()
