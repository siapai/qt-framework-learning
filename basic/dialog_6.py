import sys

from PyQt6.QtWidgets import (
    QApplication,
    QDialog,
    QMainWindow,
    QMessageBox,
    QPushButton,
)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('My App')

        button = QPushButton('Press me for a dialog!')
        button.clicked.connect(self.button_clicked)
        self.setCentralWidget(button)

    def button_clicked(self, s):
        button = QMessageBox.critical(
            self, "Omg!", "Something went very wrong",
            buttons=QMessageBox.StandardButton.Discard
            | QMessageBox.StandardButton.NoToAll
            | QMessageBox.StandardButton.Ignore,
            defaultButton=QMessageBox.StandardButton.Discard
        )

        if button == QMessageBox.StandardButton.Discard:
            print('Discard!')
        elif button == QMessageBox.StandardButton.NoToAll:
            print('No to All!')
        else:
            print('Ignore!')


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()
