
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton

class HabitForm(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.layout = QVBoxLayout(self)

        # Add form elements
        self.layout.addWidget(QLabel("Enter a new habit:"))
        self.habit_input = QLineEdit(self)
        self.layout.addWidget(self.habit_input)

        self.add_button = QPushButton("Add Habit", self)
        self.layout.addWidget(self.add_button)
        self.add_button.clicked.connect(self.add_habit)

    def add_habit(self):
        habit = self.habit_input.text()
        # Logic to add the habit to the list and storage
        print("Habit to add:", habit)

