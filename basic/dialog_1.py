import sys

from PyQt6.QtWidgets import (
    QApplication,
    QDialog,
    QMainWindow,
    QPushButton
)


class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('My App')

        button = QPushButton('Press me for a dialog')
        button.clicked.connect(self.button_clicked)
        self.setCentralWidget(button)

    def button_clicked(self, s):
        print('click', s)

        dlg = QDialog(self)
        dlg.setWindowTitle('?')
        dlg.exec()


app = QApplication(sys.argv)

window = MyWindow()
window.show()

app.exec()

