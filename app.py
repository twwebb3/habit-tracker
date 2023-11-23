
import sys
from PyQt5.QtWidgets import QApplication
from habit_ui.main_window import HabitTracker


def main():
    app = QApplication(sys.argv)
    mainWin = HabitTracker()
    mainWin.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
