from datetime import datetime

from database import DatabaseManager
from habit_manager import HabitManager


def test_create_habit(tmp_path):
    database_file = tmp_path / "test_habit_tracker.db"

    database = DatabaseManager(str(database_file))
    manager = HabitManager(database)

    habit = manager.create_habit(
        "Exercise",
        "daily"
    )

    assert habit.id is not None
    assert habit.name == "Exercise"
    assert habit.periodicity == "daily"

    habits = manager.get_habits()

    assert len(habits) == 1


def test_create_monthly_habit(tmp_path):
    database_file = tmp_path / "test_habit_tracker.db"

    database = DatabaseManager(str(database_file))
    manager = HabitManager(database)

    habit = manager.create_habit(
        "Pay bills",
        "monthly"
    )

    assert habit.periodicity == "monthly"


def test_complete_habit(tmp_path):
    database_file = tmp_path / "test_habit_tracker.db"

    database = DatabaseManager(str(database_file))
    manager = HabitManager(database)

    habit = manager.create_habit(
        "Read",
        "daily"
    )

    completion_time = datetime(
        2026,
        11,
        14,
        19,
        30
    )

    manager.complete_habit(
        habit.id,
        completion_time
    )

    completions = manager.get_completions(
        habit.id
    )

    assert len(completions) == 1
    assert completions[0]["completed_at"] == completion_time


def test_delete_habit(tmp_path):
    database_file = tmp_path / "test_habit_tracker.db"

    database = DatabaseManager(str(database_file))
    manager = HabitManager(database)

    habit = manager.create_habit(
        "Clean apartment",
        "weekly"
    )

    manager.delete_habit(habit.id)

    habits = manager.get_habits()

    assert len(habits) == 0