from datetime import datetime

from habit import Habit


class HabitManager:
    """
    Coordinates habit-related operations between the application
    and the database layer.
    """

    def __init__(self, database):
        self.database = database

    def create_habit(self, name, periodicity):
        """
        Create a new habit and save it to the database.
        """
        habit = Habit(name, periodicity)
        self.database.save_habit(habit)

        return habit

    def get_habits(self):
        """
        Return all stored habits.
        """
        return self.database.load_habits()

    def complete_habit(self, habit_id, completed_at=None):
        """
        Mark a habit as completed.
        """
        completed_at = completed_at or datetime.now()

        return self.database.save_completion(
            habit_id,
            completed_at
        )

    def delete_habit(self, habit_id):
        """
        Delete a habit and its related completion records.
        """
        self.database.delete_habit(habit_id)

    def get_completions(self, habit_id=None):
        """
        Return completion records.
        """
        return self.database.load_completions(habit_id)