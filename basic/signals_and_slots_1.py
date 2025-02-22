import sys
from PyQt6.QtWidgets import (
    QApplication,
    QMainWindow,
    QLabel,
    QLineEdit,
    QVBoxLayout,
    QWidget, QPushButton
)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('My App')
        button = QPushButton('Press Me!')
        button.setCheckable(True)
        button.clicked.connect(self.the_button_was_clicked)
        button.clicked.connect(self.the_button_was_toggled)

        # Set the central widget of the Window
        self.setCentralWidget(button)

    @staticmethod
    def the_button_was_clicked():
        print("clicked!")

    @staticmethod
    def the_button_was_toggled(checked):
        print("Checked?", checked)


app = QApplication(sys.argv)
window = MainWindow()
window.show()

app.exec()