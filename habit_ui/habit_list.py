
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QCheckBox

class HabitList(QWidget):
    def __init__(self, parent=None, database=None):
        super().__init__(parent)
        self.database = database
        self.layout = QVBoxLayout(self)

        self.load_habits()

    def load_habits(self):
        # Retrieve all habits from the database
        habits = self.database.get_all_habits()
        for habit in habits:
            # Create a checkbox for each habit
            checkbox = QCheckBox(habit[1], self)
            self.layout.addWidget(checkbox)
            # Retrieve all completion records for the habit
            completions = self.database.get_completions(habit[0])
            for completion in completions:
                # Add a checkmark to the checkbox for each completion
                checkbox.setCheckState(2)
