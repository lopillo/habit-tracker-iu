from datetime import datetime

from database import DatabaseManager
from habit import Habit


def test_save_and_load_habit(tmp_path):
    database_file = tmp_path / "test_habit_tracker.db"
    database = DatabaseManager(str(database_file))

    habit = Habit("Exercise", "daily")
    database.save_habit(habit)

    habits = database.load_habits()

    assert len(habits) == 1
    assert habits[0].name == "Exercise"
    assert habits[0].periodicity == "daily"


def test_delete_habit(tmp_path):
    database_file = tmp_path / "test_habit_tracker.db"
    database = DatabaseManager(str(database_file))

    habit = Habit("Read", "daily")
    database.save_habit(habit)

    database.delete_habit(habit.id)

    habits = database.load_habits()

    assert len(habits) == 0


def test_save_and_load_completion(tmp_path):
    database_file = tmp_path / "test_habit_tracker.db"
    database = DatabaseManager(str(database_file))

    habit = Habit("Call family", "weekly")
    database.save_habit(habit)

    completion_time = datetime(2026, 11, 14, 18, 0)

    database.save_completion(
        habit.id,
        completion_time
    )

    completions = database.load_completions(habit.id)

    assert len(completions) == 1
    assert completions[0]["habit_id"] == habit.id
    assert completions[0]["completed_at"] == completion_time


def test_delete_habit_also_deletes_completions(tmp_path):
    database_file = tmp_path / "test_habit_tracker.db"
    database = DatabaseManager(str(database_file))

    habit = Habit("Clean apartment", "weekly")
    database.save_habit(habit)

    database.save_completion(habit.id)

    database.delete_habit(habit.id)

    completions = database.load_completions(habit.id)

    assert len(completions) == 0


def test_load_all_completions(tmp_path):
    database_file = tmp_path / "test_habit_tracker.db"
    database = DatabaseManager(str(database_file))

    habit1 = Habit("Exercise", "daily")
    habit2 = Habit("Pay bills", "monthly")

    database.save_habit(habit1)
    database.save_habit(habit2)

    database.save_completion(habit1.id)
    database.save_completion(habit2.id)

    completions = database.load_completions()

    assert len(completions) == 2