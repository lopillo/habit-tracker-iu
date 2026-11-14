from datetime import datetime


class Habit:
    """
    Represents a habit tracked by the application.
    """

    VALID_PERIODICITIES = ("daily", "weekly", "monthly")

    def __init__(self, name, periodicity, created_at=None, habit_id=None):
        self.id = habit_id
        self.name = name
        self.periodicity = periodicity.lower()
        self.created_at = created_at or datetime.now()

        self.validate()

    def validate(self):
        """
        Validate the habit name and periodicity.
        """
        if not self.name.strip():
            raise ValueError("Habit name cannot be empty.")

        if self.periodicity not in self.VALID_PERIODICITIES:
            raise ValueError(
                "Periodicity must be 'daily', 'weekly', or 'monthly'."
            )

    def __str__(self):
        return f"{self.name} ({self.periodicity})"