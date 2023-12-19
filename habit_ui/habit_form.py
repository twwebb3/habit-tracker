
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QComboBox

class HabitForm(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.layout = QVBoxLayout(self)

        # Add form elements
        self.layout.addWidget(QLabel("Enter a new habit:"))
        self.habit_input = QLineEdit(self)
        self.layout.addWidget(self.habit_input)

        # Frequency selection
        self.layout.addWidget(QLabel("Select a frequency:"))
        self.frequency_combo = QComboBox(self)
        self.frequency_combo.addItems(["Daily", "Weekly", "Monthly", "Quarterly"])
        self.layout.addWidget(self.frequency_combo)

        self.add_button = QPushButton("Add Habit", self)
        self.layout.addWidget(self.add_button)
        self.add_button.clicked.connect(self.add_habit)

    def add_habit(self):
        habit_name = self.habit_input.text()
        habit_frequency = self.frequency_combo.currentText()
        # Logic to add the habit to the list and storage
        print("Habit to add:", habit_name, "Frequency:", habit_frequency)
        # Clear the input field
        self.habit_input.clear()
        self.frequency_combo.setCurrentIndex(0)

