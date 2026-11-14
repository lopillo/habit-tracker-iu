from datetime import datetime

from analytics import (
    get_all_habits,
    get_habits_by_periodicity,
    get_longest_streak,
    get_longest_streak_for_habit,
)
from habit import Habit


def test_get_all_habits():
    habits = [
        Habit("Exercise", "daily", habit_id=1),
        Habit("Call Family", "weekly", habit_id=2),
    ]

    result = get_all_habits(habits)

    assert len(result) == 2


def test_get_habits_by_periodicity():
    habits = [
        Habit("Exercise", "daily", habit_id=1),
        Habit("Read", "daily", habit_id=2),
        Habit("Call Family", "weekly", habit_id=3),
    ]

    daily_habits = get_habits_by_periodicity(
        habits,
        "daily"
    )

    assert len(daily_habits) == 2


def test_daily_longest_streak():
    habit = Habit(
        "Exercise",
        "daily",
        habit_id=1
    )

    completions = [
        {
            "habit_id": 1,
            "completed_at": datetime(2026, 10, 1)
        },
        {
            "habit_id": 1,
            "completed_at": datetime(2026, 10, 2)
        },
        {
            "habit_id": 1,
            "completed_at": datetime(2026, 10, 3)
        },
        {
            "habit_id": 1,
            "completed_at": datetime(2026, 10, 5)
        },
    ]

    result = get_longest_streak_for_habit(
        habit,
        completions
    )

    assert result == 3


def test_weekly_longest_streak():
    habit = Habit(
        "Call Family",
        "weekly",
        habit_id=1
    )

    completions = [
        {
            "habit_id": 1,
            "completed_at": datetime(2026, 10, 1)
        },
        {
            "habit_id": 1,
            "completed_at": datetime(2026, 10, 8)
        },
        {
            "habit_id": 1,
            "completed_at": datetime(2026, 10, 15)
        },
    ]

    result = get_longest_streak_for_habit(
        habit,
        completions
    )

    assert result == 3


def test_monthly_longest_streak():
    habit = Habit(
        "Pay Bills",
        "monthly",
        habit_id=1
    )

    completions = [
        {
            "habit_id": 1,
            "completed_at": datetime(2026, 9, 1)
        },
        {
            "habit_id": 1,
            "completed_at": datetime(2026, 10, 1)
        },
        {
            "habit_id": 1,
            "completed_at": datetime(2026, 11, 1)
        },
    ]

    result = get_longest_streak_for_habit(
        habit,
        completions
    )

    assert result == 3


def test_no_completions_returns_zero():
    habit = Habit(
        "Exercise",
        "daily",
        habit_id=1
    )

    result = get_longest_streak_for_habit(
        habit,
        []
    )

    assert result == 0


def test_single_completion_returns_one():
    habit = Habit(
        "Exercise",
        "daily",
        habit_id=1
    )

    completions = [
        {
            "habit_id": 1,
            "completed_at": datetime(2026, 10, 1)
        }
    ]

    result = get_longest_streak_for_habit(
        habit,
        completions
    )

    assert result == 1


def test_duplicate_completion_same_day_counts_once():
    habit = Habit(
        "Exercise",
        "daily",
        habit_id=1
    )

    completions = [
        {
            "habit_id": 1,
            "completed_at": datetime(2026, 10, 1, 10)
        },
        {
            "habit_id": 1,
            "completed_at": datetime(2026, 10, 1, 18)
        },
        {
            "habit_id": 1,
            "completed_at": datetime(2026, 10, 2, 18)
        },
    ]

    result = get_longest_streak_for_habit(
        habit,
        completions
    )

    assert result == 2


def test_longest_streak_overall():
    habit1 = Habit(
        "Exercise",
        "daily",
        habit_id=1
    )

    habit2 = Habit(
        "Read",
        "daily",
        habit_id=2
    )

    habits = [
        habit1,
        habit2
    ]

    completions = [
        {
            "habit_id": 1,
            "completed_at": datetime(2026, 10, 1)
        },
        {
            "habit_id": 1,
            "completed_at": datetime(2026, 10, 2)
        },
        {
            "habit_id": 2,
            "completed_at": datetime(2026, 10, 1)
        },
        {
            "habit_id": 2,
            "completed_at": datetime(2026, 10, 2)
        },
        {
            "habit_id": 2,
            "completed_at": datetime(2026, 10, 3)
        },
    ]

    habit, streak = get_longest_streak(
        habits,
        completions
    )

    assert habit.name == "Read"
    assert streak == 3