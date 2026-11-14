from datetime import date, timedelta


def get_all_habits(habits):
    """
    Return all currently tracked habits.
    """
    return list(habits)


def get_habits_by_periodicity(habits, periodicity):
    """
    Return habits matching the selected periodicity.
    """
    return list(
        filter(
            lambda habit: habit.periodicity == periodicity,
            habits
        )
    )


def _get_period_key(completed_at, periodicity):
    """
    Convert a completion datetime into a comparable period.
    """

    if periodicity == "daily":
        return completed_at.date()

    if periodicity == "weekly":
        iso_year, iso_week, _ = completed_at.isocalendar()
        return (iso_year, iso_week)

    if periodicity == "monthly":
        return (
            completed_at.year,
            completed_at.month
        )

    raise ValueError("Unsupported periodicity.")


def _are_consecutive(previous, current, periodicity):
    """
    Determine whether two periods are consecutive.
    """

    if periodicity == "daily":
        return current - previous == timedelta(days=1)

    if periodicity == "weekly":
        previous_year, previous_week = previous
        current_year, current_week = current

        # Simple comparison through ISO week dates.
        previous_date = date.fromisocalendar(
            previous_year,
            previous_week,
            1
        )

        current_date = date.fromisocalendar(
            current_year,
            current_week,
            1
        )

        return current_date - previous_date == timedelta(weeks=1)

    if periodicity == "monthly":
        previous_year, previous_month = previous
        current_year, current_month = current

        previous_index = (
            previous_year * 12
            + previous_month
        )

        current_index = (
            current_year * 12
            + current_month
        )

        return current_index - previous_index == 1

    return False


def get_longest_streak_for_habit(
    habit,
    completions
):
    """
    Calculate the longest streak for a specific habit.
    """

    habit_completions = list(
        filter(
            lambda completion:
            completion["habit_id"] == habit.id,
            completions
        )
    )

    if not habit_completions:
        return 0

    periods = sorted(
        {
            _get_period_key(
                completion["completed_at"],
                habit.periodicity
            )
            for completion in habit_completions
        }
    )

    if len(periods) == 1:
        return 1

    longest_streak = 1
    current_streak = 1

    for previous, current in zip(
        periods,
        periods[1:]
    ):
        if _are_consecutive(
            previous,
            current,
            habit.periodicity
        ):
            current_streak += 1
        else:
            current_streak = 1

        longest_streak = max(
            longest_streak,
            current_streak
        )

    return longest_streak


def get_longest_streak(
    habits,
    completions
):
    """
    Return the habit with the longest streak
    and the length of that streak.
    """

    if not habits:
        return None, 0

    results = list(
        map(
            lambda habit: (
                habit,
                get_longest_streak_for_habit(
                    habit,
                    completions
                )
            ),
            habits
        )
    )

    return max(
        results,
        key=lambda item: item[1]
    )