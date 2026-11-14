from datetime import datetime, timedelta

from database import DatabaseManager
from habit_manager import HabitManager
from fixtures import create_sample_data, PREDEFINED_HABITS


def test_create_sample_data_is_idempotent(tmp_path):
    """
    Running the fixture loader multiple times must not
    duplicate habits or completion records.
    """
    database_file = tmp_path / "test_habit_tracker.db"

    database = DatabaseManager(database_file)
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


def test_predefined_habits_include_daily_and_weekly():
    """
    The five predefined habits must include at least
    one daily and one weekly habit.
    """
    periodicities = {
        habit["periodicity"]
        for habit in PREDEFINED_HABITS
    }

    assert len(PREDEFINED_HABITS) == 5
    assert "daily" in periodicities
    assert "weekly" in periodicities


def test_each_predefined_habit_has_completion_data(tmp_path):
    """
    Every predefined habit must have example
    completion data.
    """
    database_file = tmp_path / "test_habit_tracker.db"

    database = DatabaseManager(database_file)
    manager = HabitManager(database)

    create_sample_data(manager)

    habits = manager.get_habits()

    for habit in habits:
        completions = manager.get_completions(habit.id)

        assert len(completions) > 0


def test_fixture_data_covers_four_week_period(tmp_path):
    """
    The fixture data must cover the four-week period
    from 1 October 2026 through 28 October 2026.
    """
    database_file = tmp_path / "test_habit_tracker.db"

    database = DatabaseManager(database_file)
    manager = HabitManager(database)

    create_sample_data(manager)

    habits = manager.get_habits()

    period_start = datetime(
        2026,
        10,
        1,
        18,
        0
    )

    period_end = period_start + timedelta(days=27)

    for habit in habits:
        completions = manager.get_completions(habit.id)

        completion_dates = [
            completion["completed_at"]
            for completion in completions
        ]

        assert completion_dates

        assert min(completion_dates) >= period_start
        assert max(completion_dates) <= period_end