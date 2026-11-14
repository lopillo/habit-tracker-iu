import sqlite3
from datetime import datetime
from pathlib import Path

from habit import Habit


class DatabaseManager:
    """
    Handles persistent storage using SQLite.
    """

    def __init__(self, database_path="data/habit_tracker.db"):
        self.database_path = database_path

        Path(database_path).parent.mkdir(
            parents=True,
            exist_ok=True
        )

        self.create_tables()

    def connect(self):
        """
        Open a connection to the SQLite database.
        """
        return sqlite3.connect(self.database_path)

    def create_tables(self):
        """
        Create the required database tables if they do not exist.
        """
        with self.connect() as connection:
            cursor = connection.cursor()

            cursor.execute(
                """
                CREATE TABLE IF NOT EXISTS habits (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    periodicity TEXT NOT NULL,
                    created_at TEXT NOT NULL
                )
                """
            )

            cursor.execute(
                """
                CREATE TABLE IF NOT EXISTS completions (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    habit_id INTEGER NOT NULL,
                    completed_at TEXT NOT NULL,
                    FOREIGN KEY (habit_id)
                    REFERENCES habits(id)
                )
                """
            )

            connection.commit()

    def save_habit(self, habit):
        """
        Save a Habit object to the database.
        """
        with self.connect() as connection:
            cursor = connection.cursor()

            cursor.execute(
                """
                INSERT INTO habits (
                    name,
                    periodicity,
                    created_at
                )
                VALUES (?, ?, ?)
                """,
                (
                    habit.name,
                    habit.periodicity,
                    habit.created_at.isoformat(),
                ),
            )

            connection.commit()

            habit.id = cursor.lastrowid
            return habit.id

    def load_habits(self):
        """
        Load all habits from the database.
        """
        with self.connect() as connection:
            cursor = connection.cursor()

            cursor.execute(
                """
                SELECT id, name, periodicity, created_at
                FROM habits
                ORDER BY id
                """
            )

            rows = cursor.fetchall()

        habits = []

        for row in rows:
            habit = Habit(
                habit_id=row[0],
                name=row[1],
                periodicity=row[2],
                created_at=datetime.fromisoformat(row[3]),
            )

            habits.append(habit)

        return habits

    def delete_habit(self, habit_id):
        """
        Delete a habit and its completion records.
        """
        with self.connect() as connection:
            cursor = connection.cursor()

            cursor.execute(
                """
                DELETE FROM completions
                WHERE habit_id = ?
                """,
                (habit_id,),
            )

            cursor.execute(
                """
                DELETE FROM habits
                WHERE id = ?
                """,
                (habit_id,),
            )

            connection.commit()

    def save_completion(self, habit_id, completed_at=None):
        """
        Save a completion timestamp for a habit.
        """
        completed_at = completed_at or datetime.now()

        with self.connect() as connection:
            cursor = connection.cursor()

            cursor.execute(
                """
                INSERT INTO completions (
                    habit_id,
                    completed_at
                )
                VALUES (?, ?)
                """,
                (
                    habit_id,
                    completed_at.isoformat(),
                ),
            )

            connection.commit()

            return cursor.lastrowid

    def load_completions(self, habit_id=None):
        """
        Load completion records.
        If habit_id is provided, only completions for that habit are returned.
        """
        with self.connect() as connection:
            cursor = connection.cursor()

            if habit_id is None:
                cursor.execute(
                    """
                    SELECT id, habit_id, completed_at
                    FROM completions
                    ORDER BY completed_at
                    """
                )
            else:
                cursor.execute(
                    """
                    SELECT id, habit_id, completed_at
                    FROM completions
                    WHERE habit_id = ?
                    ORDER BY completed_at
                    """,
                    (habit_id,),
                )

            rows = cursor.fetchall()

        return [
            {
                "id": row[0],
                "habit_id": row[1],
                "completed_at": datetime.fromisoformat(row[2]),
            }
            for row in rows
        ]