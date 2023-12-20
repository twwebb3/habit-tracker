

from PyQt5.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QComboBox
from .habit_form import HabitForm
from .habit_list import HabitList

class HabitTracker(QMainWindow):
    def __init__(self):
        super().__init__()

        # Set the title and size of the window
        self.setWindowTitle("Habit Tracker")
        self.setGeometry(100, 100, 600, 400)

        # Central widget and layout
        self.central_widget = QWidget(self)
        self.setCentralWidget(self.central_widget)
        self.main_layout = QVBoxLayout(self.central_widget)

        # Create menu within the window
        self.create_dropdown_menu()

        # Add habit form and list to the layout
        self.habit_list = HabitList(self)
        self.habit_form = HabitForm(self)
        self.main_layout.addWidget(self.habit_list)
        self.main_layout.addWidget(self.habit_form)

    def create_dropdown_menu(self):
        # Dropdown menu for habit frequency selection
        self.menu_dropdown = QComboBox(self)
        self.menu_dropdown.addItems(["All Habits", "Daily Habits", "Weekly Habits", "Monthly Habits", "Quarterly Habits"])
        self.main_layout.addWidget(self.menu_dropdown)

        # Connect dropdown selection change to a function
        self.menu_dropdown.currentIndexChanged.connect(self.filter_habits)

    def filter_habits(self, index):
        # Logic to filter and display habits based on the selected frequency
        frequency = self.menu_dropdown.currentText()
        print("Selected frequency:", frequency)
        # Implement the filtering logic here
