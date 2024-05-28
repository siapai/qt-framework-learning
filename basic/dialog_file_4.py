import os.path
import sys

from PyQt6.QtWidgets import (
    QApplication,
    QFileDialog,
    QMainWindow,
    QPushButton, QVBoxLayout, QWidget, QMessageBox,
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

        layout = QVBoxLayout()
        button1 = QPushButton('Open file')
        button1.clicked.connect(self.get_filename)
        layout.addWidget(button1)

        button2 = QPushButton('Open files')
        button2.clicked.connect(self.get_filenames)
        layout.addWidget(button2)

        button3 = QPushButton('Save file')
        button3.clicked.connect(self.get_save_filename)
        layout.addWidget(button3)

        button4 = QPushButton('Select folder')
        button4.clicked.connect(self.get_folder)
        layout.addWidget(button4)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def get_filename(self):
        caption = ""
        initial_dir = ""
        initial_filter = FILE_FILTERS[3]
        filters = ";;".join(FILE_FILTERS)
        print(f"Filters: {filters}")
        print(f"Initial Filter: {initial_filter}")

        filename, selected_filter = QFileDialog.getOpenFileName(
            self,
            caption=caption,
            directory=initial_dir,
            filter=filters,
            initialFilter=initial_filter
        )
        print(f"Result: {filename}\nFilters: {selected_filter}")

        if filename:
            with open(filename, "r") as f:
                file_contents = f.read()

    def get_filenames(self):
        caption = ""
        initial_dir = ""
        initial_filter = FILE_FILTERS[1]
        filters = ";;".join(FILE_FILTERS)
        print(f"Filters: {filters}")
        print(f"Initial Filter: {initial_filter}")

        filenames, selected_filter = QFileDialog.getOpenFileNames(
            self,
            caption=caption,
            directory=initial_dir,
            filter=filters,
            initialFilter=initial_filter
        )
        print(f"Result: {filenames}\nFilters: {selected_filter}")

        for filename in filenames:
            with open(filename, "r") as f:
                file_contents = f.read()

    def get_save_filename(self):
        caption = ""
        initial_dir = ""
        initial_filter = FILE_FILTERS[2]
        filters = ";;".join(FILE_FILTERS)
        print(f"Filters: {filters}")
        print(f"Initial Filter: {initial_filter}")

        filename, selected_filter = QFileDialog.getSaveFileName(
            self,
            caption=caption,
            directory=initial_dir,
            filter=filters,
            initialFilter=initial_filter
        )
        print(f"Result: {filename}\nFilters: {selected_filter}")

        if filename:
            if os.path.exists(filename):
                write_confirmed = QMessageBox.question(
                    self,
                    "Overwrite file?",
                    f"The file {filename} exists. Do you want to overwrite it?"
                )
            else:
                write_confirmed = True

            if write_confirmed:
                with open(filename, "w") as f:
                    file_contents = "MY FILE CONTENTS"
                    f.write(file_contents)

    def get_folder(self):
        caption = ""
        initial_dir = ""
        folder_path = QFileDialog.getExistingDirectory(
            self,
            caption=caption,
            directory=initial_dir
        )
        print("Result:", folder_path)


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()
