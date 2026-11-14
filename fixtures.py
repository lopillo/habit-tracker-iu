from datetime import datetime, timedelta


PREDEFINED_HABITS = [
    {
        "name": "Drink Water",
        "periodicity": "daily",
    },
    {
        "name": "Exercise",
        "periodicity": "daily",
    },
    {
        "name": "Read 20 Minutes",
        "periodicity": "daily",
    },
    {
        "name": "Call Family",
        "periodicity": "weekly",
    },
    {
        "name": "Clean Apartment",
        "periodicity": "weekly",
    },
]

def create_sample_data(manager):
    """
    Create the predefined habits and four weeks of example tracking data.

    The function can be executed multiple times without creating
    duplicate habits or duplicate completion records.
    """
    habits = _get_or_create_habits(manager)

    completion_data = _build_completion_data(habits)

    _insert_missing_completions(
        manager,
        completion_data
    )


def _get_or_create_habits(manager):
    """
    Return the five predefined habits.

    Existing habits are reused instead of being duplicated.
    """
    existing_habits = manager.get_habits()

    habits_by_name = {
        habit.name.lower(): habit
        for habit in existing_habits
    }

    predefined_habits = {}

    for habit_data in PREDEFINED_HABITS:
        name = habit_data["name"]
        periodicity = habit_data["periodicity"]

        existing_habit = habits_by_name.get(
            name.lower()
        )

        if existing_habit is not None:
            habit = existing_habit
        else:
            habit = manager.create_habit(
                name,
                periodicity
            )

        predefined_habits[name] = habit

    return predefined_habits


def _build_completion_data(habits):
    """
    Build deterministic sample completion data covering
    a full four-week period.

    The dates are fixed so that analytics and unit tests
    produce predictable results.
    """
    start_date = datetime(
        2026,
        10,
        1,
        18,
        0
    )

    completion_data = []

    # Drink Water:
    # Data distributed across the full 4-week period.
    # Includes several streaks and missed days.
    drink_water_days = [
        0, 1, 2, 3,
        5, 6, 7,
        9, 10, 11, 12,
        14, 15,
        17, 18, 19, 20, 21,
        23, 24,
        26, 27
    ]

    for day in drink_water_days:
        completion_data.append(
            (
                habits["Drink Water"].id,
                start_date + timedelta(days=day)
            )
        )

    # Exercise:
    # Data distributed across all four weeks with
    # several broken and consecutive streaks.
    exercise_days = [
        0, 1, 2,
        4, 5, 6, 7,
        10, 11,
        14, 15, 16,
        20, 21, 22, 23,
        26, 27
    ]

    for day in exercise_days:
        completion_data.append(
            (
                habits["Exercise"].id,
                start_date + timedelta(days=day)
            )
        )

    # Read 20 Minutes:
    # Data covers the complete four-week period and
    # contains a longer daily streak.
    read_days = [
        0, 1,
        3, 4, 5, 6,
        8, 9, 10, 11, 12, 13,
        15, 16, 17, 18, 19, 20, 21,
        23, 24, 25,
        27
    ]

    for day in read_days:
        completion_data.append(
            (
                habits["Read 20 Minutes"].id,
                start_date + timedelta(days=day)
            )
        )

    # Call Family:
    # One completion in each of four consecutive weeks.
    call_family_days = [
        0,
        7,
        14,
        21
    ]

    for day in call_family_days:
        completion_data.append(
            (
                habits["Call Family"].id,
                start_date + timedelta(days=day)
            )
        )

    # Clean Apartment:
    # Four weeks of example data with one missed week
    # to demonstrate a broken weekly streak.
    clean_apartment_days = [
        2,
        16,
        23
    ]

    for day in clean_apartment_days:
        completion_data.append(
            (
                habits["Clean Apartment"].id,
                start_date + timedelta(days=day)
            )
        )

    return completion_data


def _insert_missing_completions(
    manager,
    completion_data
):
    """
    Insert only completion records that do not already exist.
    """
    existing_completions = manager.get_completions()

    existing_records = {
        (
            completion["habit_id"],
            completion["completed_at"]
        )
        for completion in existing_completions
    }

    for habit_id, completed_at in completion_data:
        record = (
            habit_id,
            completed_at
        )

        if record not in existing_records:
            manager.complete_habit(
                habit_id,
                completed_at
            )

            existing_records.add(record)