# 🧭 Habit Tracker IU

A command-line **Habit Tracking Application** developed in Python as part of the IU course **Object-Oriented and Functional Programming with Python**.

The project demonstrates the practical use of:

- 🧠 Object-Oriented Programming
- λ Functional Programming
- 🗄️ SQLite persistence
- 🧪 Automated testing with pytest
- 💻 Command-line interaction
- 🌳 Git version control
- 🌐 GitHub repository management

**Repository:**  
https://github.com/lopillo/habit-tracker-iu

---

# 📌 Project Overview

The Habit Tracker allows users to define habits that should be completed periodically and to record when those habits are completed.

Users can:

- ➕ Create new habits
- 📋 View currently tracked habits
- ✅ Mark habits as completed
- 🗑️ Delete habits
- 📊 Analyse habit data
- 🔥 Calculate habit streaks
- 🕒 Store creation and completion timestamps
- 💾 Persist data between application sessions

The application is operated through a simple interactive command-line interface.

---

# 🎯 Project Requirements

The application was developed according to the requirements of the IU Habit Tracker portfolio assignment.

The implementation includes:

- Python 3.8 or later
- A `Habit` class using Object-Oriented Programming
- Daily habits
- Weekly habits
- Five predefined habits
- Four weeks of example tracking data
- Habit creation timestamps
- Completion timestamps
- Persistent storage
- Functional analytics
- Command-line interface
- Automated unit tests
- Python docstrings
- Installation and usage documentation

The application additionally supports **monthly habits** as an extension beyond the required daily and weekly periodicities.

---

# ✨ Main Features

## ➕ Create Habits

Users can create habits by specifying:

- a habit name
- a periodicity

Supported periodicities are:

| Periodicity | Description                           |
| ----------- | ------------------------------------- |
| `daily`     | Habit should be completed every day   |
| `weekly`    | Habit should be completed every week  |
| `monthly`   | Habit should be completed every month |

Daily and weekly habits satisfy the required project periodicities.

Monthly support was implemented as additional functionality.

---

# ✅ Habit Completion

Users can mark a habit as completed at any time.

For every completion, the application stores:

- Habit ID
- Completion date
- Completion time

The completion timestamps are used by the analytics module to determine habit streaks.

---

# 🔥 Streak Calculation

A streak represents the number of consecutive periods in which a habit was completed successfully.

Example for a daily habit:

```text
Monday      ✓
Tuesday     ✓
Wednesday   ✓
Thursday    ✗
Friday      ✓
```

The longest streak is:

```text
3 consecutive days
```

The application calculates streaks according to habit periodicity:

- Daily → consecutive calendar days
- Weekly → consecutive ISO weeks
- Monthly → consecutive calendar months

If a habit is completed more than once within the same period, that period is counted only once for streak calculation.

---

# 📊 Analytics

The analytics functionality is implemented in:

```text
analytics.py
```

The analytics module provides functionality to:

1. Return all currently tracked habits
2. Return habits with the same periodicity
3. Calculate the longest streak across all habits
4. Calculate the longest streak for a selected habit

The module uses functional-programming techniques including:

```python
filter()
map()
lambda
sorted()
max()
```

The analytics functions receive habit and completion data, process the data and return results without unnecessarily modifying the original objects.

---

# 🧠 Object-Oriented Programming

The central domain object of the application is the `Habit` class.

Each habit contains:

```text
id
name
periodicity
created_at
```

The `Habit` class validates:

- that the habit name is not empty
- that the selected periodicity is supported

Other responsibilities such as database access and analytics are intentionally separated from the `Habit` class.

This improves:

- maintainability
- modularity
- testability
- separation of concerns

---

# 🏗️ Application Architecture

The application follows a modular structure:

```text
                 ┌────────────────────┐
                 │        User        │
                 └─────────┬──────────┘
                           │
                           ▼
                 ┌────────────────────┐
                 │        CLI         │
                 │      main.py       │
                 └─────────┬──────────┘
                           │
                           ▼
                 ┌────────────────────┐
                 │   HabitManager     │
                 │ habit_manager.py   │
                 └──────┬──────┬──────┘
                        │      │
              ┌─────────┘      └─────────┐
              ▼                          ▼
       ┌─────────────┐            ┌─────────────┐
       │    Habit    │            │  Analytics  │
       │  habit.py   │            │ analytics.py│
       └─────────────┘            └─────────────┘
              │
              ▼
       ┌─────────────────┐
       │ DatabaseManager │
       │   database.py   │
       └────────┬────────┘
                │
                ▼
            🗄️ SQLite
```

---

# 📂 Project Structure

```text
HabitTracker/
│
├── main.py
│   └── Command-line interface and application entry point
│
├── habit.py
│   └── Habit class and validation
│
├── habit_manager.py
│   └── Coordinates application operations
│
├── database.py
│   └── SQLite persistence
│
├── analytics.py
│   └── Functional analytics and streak calculations
│
├── fixtures.py
│   └── Five predefined habits and four weeks of sample data
│
├── README.md
│   └── Project documentation
│
├── data/
│   └── habit_tracker.db
│
└── tests/
    ├── test_habit.py
    ├── test_habit_manager.py
    ├── test_database.py
    ├── test_analytics.py
    └── test_fixtures.py
```

The SQLite runtime database is excluded from Git using `.gitignore`.

This prevents local application data from being published in the GitHub repository.

---

# 💾 Persistent Storage

The application uses **SQLite** through Python's built-in `sqlite3` module.

No external database server is required.

The database contains two main tables.

## `habits`

| Field         | Description                  |
| ------------- | ---------------------------- |
| `id`          | Unique habit identifier      |
| `name`        | Habit name                   |
| `periodicity` | Daily, weekly or monthly     |
| `created_at`  | Habit creation date and time |

## `completions`

| Field          | Description                  |
| -------------- | ---------------------------- |
| `id`           | Unique completion identifier |
| `habit_id`     | ID of the related habit      |
| `completed_at` | Completion date and time     |

The logical relationship is:

```text
Habit
  │
  ├── Completion
  ├── Completion
  ├── Completion
  └── ...
```

Because the application uses persistent storage, habits remain available after the program is closed and restarted.

---

# 🧪 Predefined Habits

The application contains five predefined habits.

| Habit              | Periodicity |
| ------------------ | ----------- |
| 💧 Drink Water     | Daily       |
| 🏃 Exercise        | Daily       |
| 📚 Read 20 Minutes | Daily       |
| 📞 Call Family     | Weekly      |
| 🧹 Clean Apartment | Weekly      |

This provides:

```text
3 daily habits
2 weekly habits
5 predefined habits in total
```

---

# 🚀 First Run Behaviour

When the application is started for the first time, the SQLite database does not yet exist.

The application detects this situation and automatically loads:

- the five predefined habits
- four weeks of example completion data

The first-run flow is:

```text
Application starts
        ↓
Database does not exist
        ↓
Database is created
        ↓
Five predefined habits are loaded
        ↓
Four weeks of fixture data are inserted
        ↓
Main menu is displayed
```

On later runs, the existing database is reused.

This means that user changes are preserved and the predefined habits are not automatically recreated every time the program starts.

---

# 📅 Four Weeks of Example Tracking Data

The predefined habits include deterministic sample completion data covering a four-week period.

The fixture period is:

```text
1 October 2026
        ↓
28 October 2026
```

This corresponds to:

```text
28 days
=
4 weeks
```

The data deliberately contains both successful completions and missed periods.

This allows the application to demonstrate:

- successful streaks
- broken streaks
- daily streak calculations
- weekly streak calculations
- analytics across multiple habits

The fixture data is implemented in:

```text
fixtures.py
```

---

# 🔁 Idempotent Fixture Loading

The fixture loader is designed to be **idempotent**.

This means that loading the predefined data multiple times does not create:

- duplicate habits
- duplicate completion records

For example:

```text
Load fixtures
      ↓
5 predefined habits

Load fixtures again
      ↓
Still 5 predefined habits
```

This behaviour is verified automatically by the test suite.

---

# 🚀 Installation

## 1. Requirements

The project requires:

- Python 3.8 or later
- `pip`
- `pytest`

The project was developed and tested using:

```text
Python 3.11
pytest 9.2
```

SQLite is included in Python's standard library and does not require a separate installation.

---

# 📥 Clone the Repository

Open a terminal and execute:

```bash
git clone https://github.com/lopillo/habit-tracker-iu.git
```

Then enter the project directory:

```bash
cd habit-tracker-iu
```

---

# 🐍 Create a Virtual Environment

Using a virtual environment is recommended.

## Windows

```bash
py -m venv .venv
```

Activate it in Git Bash:

```bash
source .venv/Scripts/activate
```

Or in Windows Command Prompt:

```cmd
.venv\Scripts\activate
```

## Linux / macOS

```bash
python3 -m venv .venv
source .venv/bin/activate
```

---

# 📦 Install pytest

With the virtual environment activated:

```bash
python -m pip install pytest
```

On Windows:

```bash
py -m pip install pytest
```

Verify the installation:

```bash
py -m pytest --version
```

---

# ▶️ Running the Application

From the root directory:

```bash
python main.py
```

On Windows:

```bash
py main.py
```

The application displays:

```text
===================================
          HABIT TRACKER
===================================
1. Create habit
2. View habits
3. Complete habit
4. Delete habit
5. Analyze habits
6. View completions
7. Exit
```

---

# 🧑‍💻 Using the Application

## ➕ 1. Create Habit

Select:

```text
1. Create habit
```

Enter a name:

```text
Enter habit name: Exercise
```

Select a periodicity:

```text
Choose periodicity:

1. Daily
2. Weekly
3. Monthly
```

Example:

```text
Select an option: 1

Habit created successfully: Exercise (daily)
```

The habit is stored in SQLite.

---

# 📋 2. View Habits

Select:

```text
2. View habits
```

On a new installation, the predefined habits are initially available:

```text
Current habits:

1. Drink Water (daily)
2. Exercise (daily)
3. Read 20 Minutes (daily)
4. Call Family (weekly)
5. Clean Apartment (weekly)
```

---

# ✅ 3. Complete Habit

Select:

```text
3. Complete habit
```

Enter the ID of the habit:

```text
Enter the ID of the habit to complete: 1
```

The application stores the current date and time.

Example result:

```text
Habit completed successfully.
```

---

# 🗑️ 4. Delete Habit

Select:

```text
4. Delete habit
```

Enter the habit ID:

```text
Enter the ID of the habit to delete: 3
```

The selected habit and its associated completion records are removed from the database.

---

# 📊 5. Analyse Habits

Select:

```text
5. Analyze habits
```

The analytics menu provides:

```text
-----------------------------------
          ANALYTICS
-----------------------------------
1. View all habits
2. Filter habits by periodicity
3. View longest streak overall
4. View longest streak for a habit
5. Back to main menu
```

---

## View All Habits

Returns all currently tracked habits.

---

## Filter Habits by Periodicity

Habits can be filtered according to periodicity.

Examples:

```text
daily
weekly
monthly
```

---

## Longest Streak Overall

The application calculates the longest streak among all currently tracked habits.

The result identifies:

- the habit
- the longest number of consecutive periods

---

## Longest Streak for a Habit

The user can select a specific habit and calculate its longest historical streak.

Example:

```text
Longest streak for Exercise:
4 consecutive period(s)
```

---

# 🕒 6. View Completion History

Select:

```text
6. View completions
```

Example:

```text
Completion history:

Habit ID: 1 | Completed: 2026-10-01 18:00:00
Habit ID: 1 | Completed: 2026-10-02 18:00:00
Habit ID: 1 | Completed: 2026-10-03 18:00:00
```

The completion history demonstrates that completion dates and times are stored persistently.

---

# 🧪 Automated Testing

The project uses **pytest** for automated testing.

The test suite covers the critical application components.

| Area            | Tested functionality                                            |
| --------------- | --------------------------------------------------------------- |
| Habit           | creation, validation, periodicity and timestamps                |
| DatabaseManager | saving, loading, deleting and persistence                       |
| HabitManager    | creation, completion, retrieval and deletion                    |
| Analytics       | filtering and streak calculations                               |
| Edge cases      | no completions, broken streaks and duplicate-period completions |
| Fixtures        | five predefined habits                                          |
| Fixtures        | daily and weekly requirements                                   |
| Fixtures        | four-week fixture period                                        |
| Fixtures        | duplicate prevention                                            |

---

# 📅 Fixture Requirement Tests

The fixture tests explicitly verify that:

```text
✓ Exactly 5 predefined habits exist

✓ Daily habits are included

✓ Weekly habits are included

✓ Every predefined habit has completion data

✓ Fixture completion data belongs to the
  four-week example period

✓ Loading the fixture multiple times
  does not create duplicate records
```

---

# 🗄️ Database Isolation During Testing

Database tests use temporary SQLite databases.

Example:

```python
database_file = tmp_path / "test_habit_tracker.db"
```

This ensures that automated testing does not modify:

```text
data/habit_tracker.db
```

This makes the tests:

- repeatable
- isolated
- predictable

---

# ▶️ Running the Tests

Run the complete test suite:

```bash
py -m pytest -v
```

Current verified result:

```text
29 passed
```

Individual modules can also be executed.

Example:

```bash
py -m pytest tests/test_habit.py -v
```

```bash
py -m pytest tests/test_database.py -v
```

```bash
py -m pytest tests/test_analytics.py -v
```

```bash
py -m pytest tests/test_fixtures.py -v
```

---

# 🛡️ Input Validation

The application validates common invalid inputs.

Examples include:

- Empty habit names
- Unsupported periodicities
- Invalid menu selections
- Non-numeric habit IDs
- Unknown habit IDs

This prevents common user-input errors from unnecessarily terminating the application.

---

# 📝 Python Documentation

The application source code is documented using Python docstrings.

Docstrings are used in:

- `Habit`
- `HabitManager`
- `DatabaseManager`
- analytics functions
- fixture functions
- CLI functions

Example:

```python
def save_habit(self, habit):
    """
    Save a Habit object to the database.
    """
```

Another example:

```python
def analyze_habits(manager):
    """
    Display the analytics menu and process analysis requests.
    """
```

The docstrings complement the README and make the source code easier to understand and maintain.

---

# 🧰 Technologies Used

| Technology     | Purpose                   |
| -------------- | ------------------------- |
| 🐍 Python 3.11 | Main programming language |
| 🗄️ SQLite      | Persistent storage        |
| 🧪 pytest      | Automated testing         |
| 🌳 Git         | Version control           |
| 🌐 GitHub      | Repository hosting        |
| 💻 VS Code     | Development environment   |

The application mainly uses Python's standard library, keeping external dependencies minimal.

---

# 🔄 Typical Application Flow

```text
User
  ↓
CLI
  ↓
HabitManager
  ↓
Habit / DatabaseManager
  ↓
SQLite
```

Analytics flow:

```text
User
  ↓
CLI
  ↓
HabitManager
  ↓
Habit + Completion Data
  ↓
Analytics
  ↓
Result
  ↓
CLI
```

---

# 🌟 Additional Functionality

The IU project requires support for daily and weekly habits.

This implementation additionally supports:

```text
monthly
```

Monthly habits use the same general architecture as daily and weekly habits.

The monthly streak calculation is also covered by automated tests.

This functionality is an extension and does not replace the required daily and weekly predefined habits.

---

# ✅ Project Status

The current implementation includes:

- ✅ Object-oriented Habit model
- ✅ Daily habits
- ✅ Weekly habits
- ✅ Monthly habit support
- ✅ Five predefined habits
- ✅ Automatic first-run fixture loading
- ✅ Four weeks of sample tracking data
- ✅ Habit creation
- ✅ Habit deletion
- ✅ Habit completion
- ✅ Creation timestamps
- ✅ Completion timestamps
- ✅ SQLite persistence
- ✅ Functional analytics
- ✅ Periodicity filtering
- ✅ Longest streak for one habit
- ✅ Longest streak across all habits
- ✅ Deterministic fixtures
- ✅ Idempotent fixture loading
- ✅ Command-line interface
- ✅ Automated pytest suite
- ✅ Temporary test databases
- ✅ Python docstrings
- ✅ Git version control
- ✅ GitHub repository
- ✅ 29 automated tests passing

---

# 🎓 Academic Context

This application was developed as part of the IU portfolio assignment for:

**Object-Oriented and Functional Programming with Python**

The project demonstrates the practical application of:

- Object-Oriented Programming
- Functional Programming
- Persistent data storage
- Modular software architecture
- Automated testing
- Software documentation
- Version control

The application follows the technical architecture defined during the conception phase, with refinements made during implementation to improve correctness, usability and testability.

The focus of the project is on:

- correctness
- maintainability
- modularity
- testability
- clear separation of responsibilities

rather than graphical user-interface complexity.

---

# 📄 Academic Use

This repository represents an academic portfolio project.

The code and documentation are intended primarily for educational and assessment purposes.

---

## 🌐 Repository

https://github.com/lopillo/habit-tracker-iu
