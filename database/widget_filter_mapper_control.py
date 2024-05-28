import os
import sys

from PyQt6.QtCore import QSize, Qt, QSortFilterProxyModel
from PyQt6.QtSql import QSqlDatabase, QSqlTableModel
from PyQt6.QtWidgets import (
    QApplication,
    QComboBox,
    QDataWidgetMapper,
    QDoubleSpinBox,
    QFormLayout,
    QHBoxLayout,
    QLabel,
    QLineEdit,
    QMainWindow,
    QPushButton,
    QSpinBox,
    QVBoxLayout,
    QWidget,
    QTableView,
)

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

        layout = QVBoxLayout()

        self.filter = QLineEdit()
        self.filter.setPlaceholderText("Search...")
        self.table = QTableView()

        v_layout = QVBoxLayout()
        v_layout.addWidget(self.filter)
        v_layout.addWidget(self.table)

        # Left / Right pane
        h_layout = QHBoxLayout()
        h_layout.addLayout(v_layout)
        h_layout.addLayout(layout)

        form = QFormLayout()

        self.track_id = QSpinBox()
        self.track_id.setRange(0, 2147483647)
        self.track_id.setDisabled(True)
        self.name = QLineEdit()
        self.album = QComboBox()
        self.media_type = QComboBox()
        self.genre = QComboBox()
        self.composer = QLineEdit()

        self.milliseconds = QSpinBox()
        self.milliseconds.setRange(0, 2147483647)

        self.bytes = QSpinBox()
        self.bytes.setRange(0, 2147483647)
        self.bytes.setSingleStep(1)

        self.unit_price = QDoubleSpinBox()
        self.unit_price.setRange(0, 999)
        self.unit_price.setSingleStep(0.1)
        self.unit_price.setPrefix("$")

        form.addRow(QLabel("Track ID"), self.track_id)
        form.addRow(QLabel("Track name"), self.name)
        form.addRow(QLabel("Composer"), self.composer)
        form.addRow(QLabel("Milliseconds"), self.milliseconds)
        form.addRow(QLabel("Bytes"), self.bytes)
        form.addRow(QLabel("Unit Price"), self.unit_price)

        self.model = QSqlTableModel(db=db)

        self.proxy_model = QSortFilterProxyModel()
        self.proxy_model.setSourceModel(self.model)
        self.proxy_model.sort(1, Qt.SortOrder.AscendingOrder)
        self.proxy_model.setFilterKeyColumn(-1)
        self.table.setModel(self.proxy_model)

        self.filter.textChanged.connect(
            self.proxy_model.setFilterFixedString
        )

        self.mapper = QDataWidgetMapper()
        self.mapper.setModel(self.proxy_model)

        self.mapper.addMapping(self.track_id, 0)
        self.mapper.addMapping(self.name, 1)
        self.mapper.addMapping(self.composer, 5)
        self.mapper.addMapping(self.milliseconds, 6)
        self.mapper.addMapping(self.bytes, 7)
        self.mapper.addMapping(self.unit_price, 8)

        self.model.setTable("Track")
        self.model.select()

        # Change the mapper selection using the table
        self.table.selectionModel().currentRowChanged.connect(
            self.mapper.setCurrentModelIndex
        )

        self.mapper.toFirst()

        self.setMinimumSize(QSize(800, 400))

        controls = QHBoxLayout()

        prev_rec = QPushButton("Previous")
        prev_rec.clicked.connect(self.mapper.toPrevious)

        next_rec = QPushButton("Next")
        next_rec.clicked.connect(self.mapper.toNext)

        save_rec = QPushButton("Save Changes")
        save_rec.clicked.connect(self.mapper.submit)

        controls.addWidget(prev_rec)
        controls.addWidget(next_rec)
        controls.addWidget(save_rec)

        layout.addLayout(form)
        layout.addLayout(controls)

        widget = QWidget()
        widget.setLayout(h_layout)
        self.setCentralWidget(widget)


if __name__ == '__main__':
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()
    app.exec()
