from database import DatabaseManager
from habit_manager import HabitManager
from analytics import (
    get_all_habits,
    get_habits_by_periodicity,
    get_longest_streak,
    get_longest_streak_for_habit,
)


def show_menu():
    print("\n" + "=" * 35)
    print("          HABIT TRACKER")
    print("=" * 35)
    print("1. Create habit")
    print("2. View habits")
    print("3. Complete habit")
    print("4. Delete habit")
    print("5. Analyze habits")
    print("6. View completions")
    print("7. Exit")


def create_habit(manager):
    name = input("Enter habit name: ").strip()

    print("\nChoose periodicity:")
    print("1. Daily")
    print("2. Weekly")
    print("3. Monthly")

    choice = input("Select an option: ").strip()

    periodicities = {
        "1": "daily",
        "2": "weekly",
        "3": "monthly",
    }

    periodicity = periodicities.get(choice)

    if periodicity is None:
        print("Invalid periodicity.")
        return

    try:
        habit = manager.create_habit(name, periodicity)

        print(
            f"\nHabit created successfully: "
            f"{habit.name} ({habit.periodicity})"
        )

    except ValueError as error:
        print(f"Error: {error}")


def view_habits(manager):
    habits = manager.get_habits()

    if not habits:
        print("\nNo habits found.")
        return

    print("\nCurrent habits:")

    for habit in habits:
        print(
            f"{habit.id}. "
            f"{habit.name} "
            f"({habit.periodicity})"
        )


def complete_habit(manager):
    habits = manager.get_habits()

    if not habits:
        print("\nNo habits available.")
        return

    view_habits(manager)

    try:
        habit_id = int(
            input("\nEnter the ID of the habit to complete: ")
        )

        valid_ids = [habit.id for habit in habits]

        if habit_id not in valid_ids:
            print("Habit not found.")
            return

        manager.complete_habit(habit_id)

        print("Habit completed successfully.")

    except ValueError:
        print("Please enter a valid numeric ID.")


def delete_habit(manager):
    habits = manager.get_habits()

    if not habits:
        print("\nNo habits available.")
        return

    view_habits(manager)

    try:
        habit_id = int(
            input("\nEnter the ID of the habit to delete: ")
        )

        valid_ids = [habit.id for habit in habits]

        if habit_id not in valid_ids:
            print("Habit not found.")
            return

        manager.delete_habit(habit_id)

        print("Habit deleted successfully.")

    except ValueError:
        print("Please enter a valid numeric ID.")


def view_completions(manager):
    completions = manager.get_completions()

    if not completions:
        print("\nNo completions found.")
        return

    print("\nCompletion history:")

    for completion in completions:
        print(
            f"Habit ID: {completion['habit_id']} | "
            f"Completed: {completion['completed_at']}"
        )


def main():
    database = DatabaseManager()
    manager = HabitManager(database)

    
    while True:
        show_menu()

        choice = input("\nChoose an option: ").strip()

        if choice == "1":
            create_habit(manager)

        elif choice == "2":
            view_habits(manager)

        elif choice == "3":
            complete_habit(manager)

        elif choice == "4":
            delete_habit(manager)

        elif choice == "5":
            analyze_habits(manager)

        elif choice == "6":
            view_completions(manager)

        elif choice == "7":
            print("\nGoodbye!")
            break

        else:
            print("\nInvalid option. Please try again.")


def analyze_habits(manager):
    habits = manager.get_habits()
    completions = manager.get_completions()

    if not habits:
        print("\nNo habits available.")
        return

    while True:
        print("\n" + "-" * 35)
        print("          ANALYTICS")
        print("-" * 35)
        print("1. View all habits")
        print("2. Filter habits by periodicity")
        print("3. View longest streak overall")
        print("4. View longest streak for a habit")
        print("5. Back to main menu")

        choice = input("\nChoose an option: ").strip()

        if choice == "1":
            result = get_all_habits(habits)

            print("\nTracked habits:")

            for habit in result:
                print(
                    f"{habit.id}. "
                    f"{habit.name} "
                    f"({habit.periodicity})"
                )

        elif choice == "2":
            print("\nChoose periodicity:")
            print("1. Daily")
            print("2. Weekly")
            print("3. Monthly")

            period_choice = input(
                "Select an option: "
            ).strip()

            periodicities = {
                "1": "daily",
                "2": "weekly",
                "3": "monthly",
            }

            periodicity = periodicities.get(
                period_choice
            )

            if periodicity is None:
                print("Invalid periodicity.")
                continue

            result = get_habits_by_periodicity(
                habits,
                periodicity
            )

            if not result:
                print(
                    f"\nNo {periodicity} habits found."
                )
                continue

            print(
                f"\n{periodicity.capitalize()} habits:"
            )

            for habit in result:
                print(
                    f"{habit.id}. "
                    f"{habit.name}"
                )

        elif choice == "3":
            habit, streak = get_longest_streak(
                habits,
                completions
            )

            if habit is None:
                print("\nNo habits available.")
            else:
                print("\nLongest streak overall:")
                print(
                    f"{habit.name}: "
                    f"{streak} consecutive period(s)"
                )

        elif choice == "4":
            print("\nSelect a habit:")

            for habit in habits:
                print(
                    f"{habit.id}. "
                    f"{habit.name} "
                    f"({habit.periodicity})"
                )

            try:
                habit_id = int(
                    input("\nEnter habit ID: ")
                )
            except ValueError:
                print("Please enter a valid numeric ID.")
                continue

            selected_habit = next(
                (
                    habit
                    for habit in habits
                    if habit.id == habit_id
                ),
                None,
            )

            if selected_habit is None:
                print("Habit not found.")
                continue

            streak = get_longest_streak_for_habit(
                selected_habit,
                completions
            )

            print(
                f"\nLongest streak for "
                f"{selected_habit.name}: "
                f"{streak} consecutive period(s)"
            )

        elif choice == "5":
            break

        else:
            print("\nInvalid option. Please try again.")


if __name__ == "__main__":
    main()