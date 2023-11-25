

from PyQt5.QtWidgets import QMainWindow, QAction, QLabel, QListWidget, QCheckBox, QListWidgetItem
class HabitTracker(QMainWindow):
    def __init__(self):
        super().__init__()

        # Set the title and size of the window
        self.setWindowTitle("Habit Tracker")
        self.setGeometry(300, 300, 400, 300)

        # Setup UI elements
        self.setupUI()

    def setupUI(self):
        # Create a menu bar
        self.menuBar = self.menuBar()

        # Create 'File' menu
        fileMenu = self.menuBar.addMenu('File')

        # Add 'New' action
        newAction = QAction('New', self)
        fileMenu.addAction(newAction)

        # Add 'Open' action
        openAction = QAction('Open', self)
        fileMenu.addAction(openAction)

        # Add 'Exit' action
        exitAction = QAction('Exit', self)
        exitAction.triggered.connect(self.close)  # Connect the action to close the window
        fileMenu.addAction(exitAction)

        # Add a label
        self.label = QLabel("Welcome to the Habit Tracker", self)
        self.label.adjustSize()
        self.label.move(50, 130)

        self.checklist = QListWidget(self)
        self.checklist.setGeometry(50, 50, 400, 300)

        # Add items to the checklist
        self.addChecklistItems(["Habit 1", "Habit 2", "Habit 3"])

    def addChecklistItems(self, items):
        for item_text in items:
            # Create a QListWidgetItem
            item = QListWidgetItem(self.checklist)

            # Create a QCheckBox for the item
            chkBox = QCheckBox(item_text)

            # Add the QCheckBox to the list
            self.checklist.setItemWidget(item, chkBox)