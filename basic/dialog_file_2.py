import sys

from PyQt6.QtWidgets import (
    QApplication,
    QFileDialog,
    QMainWindow,
    QPushButton,
)

FILE_FILTERS = [
    "Portable Network Graphic files (*.png)",
    "Text files (*.txt)",
    "Comma Separated Values (*.csv)",
    "All Files (*)"
]


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('My App')

        button1 = QPushButton('Open file')
        button1.clicked.connect(self.get_filename)
        self.setCentralWidget(button1)

    def get_filename(self):
        initial_filter = FILE_FILTERS[3]
        filters = ";;".join(FILE_FILTERS)
        print(f"Filters: {filters}")
        print(f"Initial Filter: {initial_filter}")

        filename, selected_filter = QFileDialog.getOpenFileName(
            self,
            filter=filters,
            initialFilter=initial_filter
        )
        print(f"Result: {filename}\nFilters: {selected_filter}")


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()
