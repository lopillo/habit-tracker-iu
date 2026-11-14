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
        "name": "Pay Monthly Bills",
        "periodicity": "monthly",
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
    Build deterministic sample completion data.

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
    # longest daily streak = 5 days
    for day in [
        0, 1, 2, 3,
        5, 6, 7, 8, 9
    ]:
        completion_data.append(
            (
                habits["Drink Water"].id,
                start_date + timedelta(days=day)
            )
        )

    # Exercise:
    # longest daily streak = 4 days
    for day in [
        0, 1, 2,
        4, 5, 6, 7
    ]:
        completion_data.append(
            (
                habits["Exercise"].id,
                start_date + timedelta(days=day)
            )
        )

    # Read 20 Minutes:
    # longest daily streak = 8 days
    for day in range(10, 18):
        completion_data.append(
            (
                habits["Read 20 Minutes"].id,
                start_date + timedelta(days=day)
            )
        )

    # Call Family:
    # four consecutive weekly periods
    for week in range(4):
        completion_data.append(
            (
                habits["Call Family"].id,
                start_date + timedelta(weeks=week)
            )
        )

    # Pay Monthly Bills:
    # example monthly data.
    # Four consecutive months are used so that monthly
    # streak calculation can also be demonstrated.
    for month in [
        datetime(2026, 8, 1, 18, 0),
        datetime(2026, 9, 1, 18, 0),
        datetime(2026, 10, 1, 18, 0),
        datetime(2026, 11, 1, 18, 0),
    ]:
        completion_data.append(
            (
                habits["Pay Monthly Bills"].id,
                month
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