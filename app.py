
import sys
from PyQt5.QtWidgets import QApplication
from habit_ui.main_window import HabitTracker
from database.habit_database import HabitDatabase


def main():
    app = QApplication(sys.argv)

    database = HabitDatabase("habits.db")

    mainWin = HabitTracker(database)
    mainWin.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
