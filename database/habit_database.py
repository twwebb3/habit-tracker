

import sqlite3
from datetime import datetime

class HabitDatabase:
    def __init__(self, db_path):
        self.conn = sqlite3.connect(db_path)
        self.create_tables()

    def create_tables(self):
        # Create a table for habits
        self.conn.execute('''
            CREATE TABLE IF NOT EXISTS habits (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                frequency TEXT NOT NULL
            )
        ''')
        # Create a table for tracking habit completions
        self.conn.execute('''
            CREATE TABLE IF NOT EXISTS tracker (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                habit_id INTEGER NOT NULL,
                completion_date DATE NOT NULL,
                FOREIGN KEY (habit_id) REFERENCES habits(id)
            )
        ''')
        self.conn.commit()

    def add_habit(self, name, frequency):
        # Add a new habit to the database
        self.conn.execute('INSERT INTO habits (name, frequency) VALUES (?, ?)', (name, frequency))
        self.conn.commit()

    def add_completion(self, habit_id, completion_date=None):
        # Add a completion record for a habit
        if completion_date is None:
            completion_date = datetime.now().strftime("%Y-%m-%d")
        self.conn.execute('INSERT INTO tracker (habit_id, completion_date) VALUES (?, ?)', (habit_id, completion_date))
        self.conn.commit()

    def get_all_habits(self):
        # Retrieve all habits from the database
        cursor = self.conn.execute('SELECT id, name, frequency FROM habits')
        return cursor.fetchall()

    def get_completions(self, habit_id):
        # Retrieve all completion records for a specific habit
        cursor = self.conn.execute('SELECT completion_date FROM tracker WHERE habit_id = ?', (habit_id,))
        return cursor.fetchall()

    def close(self):
        # Close the database connection
        self.conn.close()
