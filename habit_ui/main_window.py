

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

        self.show_home()

    def create_dropdown_menu(self):
        # Dropdown menu for habit frequency selection
        self.menu_dropdown = QComboBox(self)
        self.menu_dropdown.addItems(["Home", "Add Habit", "Analytics"])
        self.main_layout.addWidget(self.menu_dropdown)

        # Connect dropdown selection change to a function
        self.menu_dropdown.currentIndexChanged.connect(self.filter_habits)

    def filter_habits(self, index):
        selected_option = self.menu_dropdown.currentText()
        if selected_option == "Home":
            self.show_home()
        elif selected_option == "Add Habit":
            self.show_add_habit_form()
        elif selected_option == "Analytics":
            self.show_analytics()

    def show_home(self):
        self.habit_list.show()
        self.habit_form.hide()

    def show_add_habit_form(self):
        self.habit_list.hide()
        self.habit_form.show()

    def show_analytics(self):
        self.habit_list.hide()
        self.habit_form.hide()
