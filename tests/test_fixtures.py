from database import DatabaseManager
from fixtures import create_sample_data
from habit_manager import HabitManager


def test_create_sample_data_is_idempotent(tmp_path):
    database_file = tmp_path / "test_habit_tracker.db"

    database = DatabaseManager(str(database_file))
    manager = HabitManager(database)

    create_sample_data(manager)

    habits_first_run = manager.get_habits()
    completions_first_run = manager.get_completions()

    create_sample_data(manager)

    habits_second_run = manager.get_habits()
    completions_second_run = manager.get_completions()

    assert len(habits_first_run) == 5
    assert len(habits_second_run) == 5

    assert len(completions_first_run) == len(
        completions_second_run
    )