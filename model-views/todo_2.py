import sys

from PyQt6.QtCore import Qt, QAbstractListModel
from PyQt6.QtWidgets import QApplication, QMainWindow

from MainWindow import Ui_MainWindow


class TodoModel(QAbstractListModel):
    def __init__(self, todos=None):
        super().__init__()
        self.todos = todos or []

    def data(self, index, role):
        if role == Qt.ItemDataRole.DisplayRole:
            status, text = self.todos[index.row()]
            return text

    def rowCount(self, index):
        return len(self.todos)


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.model = TodoModel()
        self.todoView.setModel(self.model)
        self.addButton.pressed.connect(self.add)

    def add(self):
        """
        Add an item to our todo list
        """
        text = self.todoEdit.text()
        text = text.strip()
        if text:
            self.model.todos.append((False, text))
            # Trigger refresh
            self.model.layoutChanged.emit()
            self.todoEdit.setText("")


app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()
