import os
import sys

from PyQt6.QtCore import Qt, QSize, QCoreApplication
from PyQt6.QtSql import QSqlDatabase, QSqlTableModel
from PyQt6.QtWidgets import QApplication, QMainWindow, QTableView

basedir = os.path.dirname(__file__)


def create_connection():
    # Create a connection to the database
    _db = QSqlDatabase.addDatabase('QSQLITE')
    _db.setDatabaseName(os.path.join(basedir, "chinook.sqlite"))

    if not _db.open():
        print("Unable to establish a database connection.")
        return False
    return _db


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Create a database connection
        db = create_connection()

        self.table = QTableView()
        self.model = QSqlTableModel(db=db)
        self.table.setModel(self.model)

        self.model.setTable("Track")
        column_titles = {
            "Name": "Name",
            "AlbumId": "Album (ID)",
            "MediaTypeId": "Media Type (ID)",
            "GenreId": "Genre (ID)",
            "Composer": "Composer",
        }

        for n, t in column_titles.items():
            idx = self.model.fieldIndex(n)
            self.model.setHeaderData(idx, Qt.Orientation.Horizontal, t)

        self.model.select()

        self.setMinimumSize(QSize(1024, 600))
        self.setCentralWidget(self.table)


if __name__ == '__main__':
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()
    app.exec()
