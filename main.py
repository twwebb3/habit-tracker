
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel

class HabitTracker(QMainWindow):
    def __init__(self):
        super().__init__()

        # Set the title of the window
        self.setWindowTitle("Habit Tracker")

        # Set the size of the window
        self.setGeometry(300, 300, 400, 300)

        # Add a label as an example
        self.label = QLabel("Welcome to the Habit Tracker", self)
        self.label.adjustSize()
        self.label.move(10, 200)

    def setupUI(self):
        # This method can be used to set up UI elements
        pass

def main():
    app = QApplication(sys.argv)
    mainWin = HabitTracker()
    mainWin.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
