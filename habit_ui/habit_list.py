
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QCheckBox

class HabitList(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.layout = QVBoxLayout(self)

        # Example checkbox (you will dynamically add checkboxes based on stored habits)
        self.example_checkbox = QCheckBox("Example Habit", self)
        self.layout.addWidget(self.example_checkbox)

