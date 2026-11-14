from datetime import datetime


class Habit:
    """
    Represents a habit tracked by the application.

    A habit has a name, a periodicity, a creation timestamp,
    and optionally a database identifier.
    """

    VALID_PERIODICITIES = ("daily", "weekly", "monthly")

    def __init__(
        self,
        name,
        periodicity,
        created_at=None,
        habit_id=None
    ):
        """
        Initialize a Habit instance.

        Args:
            name: Name or task description of the habit.
            periodicity: Frequency of the habit. Supported values
                are 'daily', 'weekly', and 'monthly'.
            created_at: Optional creation datetime. If omitted,
                the current date and time are used.
            habit_id: Optional database identifier for the habit.

        Raises:
            ValueError: If the habit name is empty or the
                periodicity is not supported.
        """
        self.id = habit_id
        self.name = name
        self.periodicity = periodicity.lower()
        self.created_at = created_at or datetime.now()

        self.validate()

    def validate(self):
        """
        Validate the habit name and periodicity.

        Raises:
            ValueError: If the habit name is empty or the
                periodicity is not one of the supported values.
        """
        if not self.name.strip():
            raise ValueError("Habit name cannot be empty.")

        if self.periodicity not in self.VALID_PERIODICITIES:
            raise ValueError(
                "Periodicity must be 'daily', 'weekly', or 'monthly'."
            )

    def __str__(self):
        """
        Return a human-readable representation of the habit.

        Returns:
            A string containing the habit name and periodicity.
        """
        return f"{self.name} ({self.periodicity})"