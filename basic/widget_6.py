import sys
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QMainWindow, QLineEdit


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('My App')

        widget = QLineEdit()
        widget.setMaxLength(10)
        widget.setPlaceholderText('Enter your text')

        widget.returnPressed.connect(self.return_pressed)
        widget.selectionChanged.connect(self.selection_changed)
        widget.textChanged.connect(self.text_changed)
        widget.textEdited.connect(self.text_edited)

        self.setCentralWidget(widget)

    def return_pressed(self):
        print('return_pressed')
        self.centralWidget().setText("Boom!")

    def selection_changed(self):
        print('selection_changed')
        print(self.centralWidget().selectedText())

    @staticmethod
    def text_changed(text):
        print(f"Text changed: {text}")

    @staticmethod
    def text_edited(text):
        print(f"Text Edited: {text}")


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()