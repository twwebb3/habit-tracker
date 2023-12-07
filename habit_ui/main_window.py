

from PyQt5.QtWidgets import QMainWindow, QWidget, QVBoxLayout
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
        self.layout = QVBoxLayout(self.central_widget)

        # Add habit form and list to the layout
        self.habit_list = HabitList(self)
        self.habit_form = HabitForm(self)
        self.layout.addWidget(self.habit_list)
        self.layout.addWidget(self.habit_form)
