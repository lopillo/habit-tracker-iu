import pytest

from habit import Habit


def test_create_daily_habit():
    habit = Habit("Exercise", "daily")

    assert habit.name == "Exercise"
    assert habit.periodicity == "daily"


def test_create_weekly_habit():
    habit = Habit("Call family", "weekly")

    assert habit.name == "Call family"
    assert habit.periodicity == "weekly"


def test_create_monthly_habit():
    habit = Habit("Pay taxes", "monthly")

    assert habit.name == "Pay taxes"
    assert habit.periodicity == "monthly"


def test_created_at_is_generated():
    habit = Habit("Read", "daily")

    assert habit.created_at is not None


def test_empty_name_raises_error():
    with pytest.raises(ValueError):
        Habit("", "daily")


def test_invalid_periodicity_raises_error():
    with pytest.raises(ValueError):
        Habit("Exercise", "yearly")