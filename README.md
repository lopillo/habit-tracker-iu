# 🧭 Habit Tracker IU

A command-line **Habit Tracking Application** developed in Python as part of the IU course **Object-Oriented and Functional Programming with Python**.

The project demonstrates the practical use of **object-oriented programming**, **functional programming**, **SQLite persistence**, automated testing with **pytest**, and a modular command-line application architecture.

Repository:  
https://github.com/lopillo/habit-tracker-iu

---

## 📌 Project Overview

The Habit Tracker allows users to define habits that should be completed periodically and to record when those habits are completed.

Users can:

- ➕ Create new habits
- 📋 View currently tracked habits
- ✅ Mark habits as completed
- 🗑️ Delete habits
- 📊 Analyse habit data
- 🔥 Calculate habit streaks
- 🕒 Store creation and completion timestamps
- 💾 Keep data between application sessions

The application is operated through a simple interactive command-line interface.

---

## 🎯 Project Requirements

The implementation was developed according to the main requirements of the IU Habit Tracker portfolio assignment.

The project includes:

- Python 3.7 or later
- A `Habit` class using object-oriented programming
- Daily and weekly habit periodicities
- Five predefined habits
- Persistent storage between application sessions
- Habit creation timestamps
- Completion timestamps
- Functional-programming-based analytics
- A command-line interface
- Automated unit tests
- Python docstrings
- Installation and usage documentation

The application additionally supports **monthly habits** as an extension beyond the minimum daily and weekly periodicities.

---

## ✨ Main Features

### ➕ Habit Creation

Users can create new habits by specifying:

- a habit name
- a periodicity

Supported periodicities are:

| Periodicity | Description                               |
| ----------- | ----------------------------------------- |
| `daily`     | The habit should be completed every day   |
| `weekly`    | The habit should be completed every week  |
| `monthly`   | The habit should be completed every month |

Daily and weekly habits satisfy the required project periodicities. Monthly support was added as an additional feature.

---

## ✅ Habit Completion

A habit can be marked as completed at any time.

For every completion, the application stores:

- the related habit ID
- the exact completion date
- the exact completion time

These timestamps are used by the analytics module to calculate streaks.

---

## 🔥 Streak Calculation

A streak represents the number of consecutive periods in which a habit has been completed successfully.

Example for a daily habit:

```text
Monday      ✓
Tuesday     ✓
Wednesday   ✓
Thursday    ✗
Friday      ✓
```

The longest streak in this example is:

```text
3 consecutive days
```

The application evaluates streaks according to the habit periodicity:

- Daily habits → consecutive calendar days
- Weekly habits → consecutive ISO weeks
- Monthly habits → consecutive calendar months

If a habit is completed more than once during the same period, that period is counted only once for streak calculation.

---

# 📊 Analytics

The analytics functionality is implemented in `analytics.py`.

The module provides the required functionality to:

1. Return all currently tracked habits
2. Return habits with the same periodicity
3. Calculate the longest streak across all habits
4. Calculate the longest streak for a selected habit

The analytics layer follows a functional-programming approach and uses Python functionality such as:

```python
filter()
map()
lambda
sorted()
max()
```

The functions receive data, process it and return results without unnecessarily modifying the original habit objects.

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

The class also validates that:

- the habit name is not empty
- the selected periodicity is supported

Database access and analytics are intentionally separated from the `Habit` class to maintain a clear separation of responsibilities.

---

# 🏗️ Application Architecture

The project follows a modular architecture.

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

This separation makes the application easier to understand, maintain and test.

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
│   └── Coordinates habit operations
│
├── database.py
│   └── SQLite persistence
│
├── analytics.py
│   └── Functional analytics and streak calculations
│
├── fixtures.py
│   └── Predefined habits and deterministic sample data
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

The local SQLite database file is excluded from Git using `.gitignore`.

This prevents personal runtime data from being published in the repository.

---

# 💾 Persistent Storage

The application uses **SQLite** through Python's built-in `sqlite3` module.

No external database server is required.

The database contains two main tables.

## `habits`

Stores the definition of each habit.

| Field         | Purpose                  |
| ------------- | ------------------------ |
| `id`          | Unique habit identifier  |
| `name`        | Habit name               |
| `periodicity` | Daily, weekly or monthly |
| `created_at`  | Habit creation timestamp |

## `completions`

Stores completed occurrences of habits.

| Field          | Purpose                      |
| -------------- | ---------------------------- |
| `id`           | Unique completion identifier |
| `habit_id`     | Related habit                |
| `completed_at` | Completion timestamp         |

The relationship can be represented as:

```text
Habit
  │
  ├── Completion
  ├── Completion
  ├── Completion
  └── ...
```

Because the information is stored in SQLite, habits remain available after the application is closed and started again.

---

# 🧪 Predefined Habits and Fixture Data

The project contains five predefined habits for demonstration and testing.

| Habit                | Periodicity |
| -------------------- | ----------- |
| 💧 Drink Water       | Daily       |
| 🏃 Exercise          | Daily       |
| 📚 Read 20 Minutes   | Daily       |
| 📞 Call Family       | Weekly      |
| 💳 Pay Monthly Bills | Monthly     |

The predefined data is implemented in:

```text
fixtures.py
```

The fixture module contains deterministic historical completion timestamps that allow the streak calculations and analytics functions to be tested against predictable data.

The fixture loader is designed to be **idempotent**.

This means that executing the fixture-loading process repeatedly does not create duplicate predefined habits or identical fixture completion records.

---

# 🚀 Installation

## 1. Requirements

The application requires:

- Python 3.7 or later
- `pip`
- `pytest` for running the automated tests

The project was developed using Python 3.11.

SQLite is included in Python's standard library and therefore does not require a separate installation.

---

## 2. Clone the Repository

Open a terminal and run:

```bash
git clone https://github.com/lopillo/habit-tracker-iu.git
```

Enter the project directory:

```bash
cd habit-tracker-iu
```

---

## 3. Create a Virtual Environment

Creating a virtual environment is recommended.

### Windows

```bash
py -m venv .venv
```

### Activate in Git Bash

```bash
source .venv/Scripts/activate
```

### Activate in Windows Command Prompt

```cmd
.venv\Scripts\activate
```

### Linux / macOS

```bash
python3 -m venv .venv
source .venv/bin/activate
```

---

## 4. Install pytest

With the virtual environment activated:

```bash
python -m pip install pytest
```

On Windows, the Python launcher can also be used:

```bash
py -m pip install pytest
```

Verify the installation:

```bash
python -m pytest --version
```

---

# ▶️ Running the Application

From the root directory of the project:

```bash
python main.py
```

On Windows:

```bash
py main.py
```

The main menu is displayed:

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

## ➕ 1. Create a Habit

Select:

```text
1. Create habit
```

Enter the habit name:

```text
Enter habit name: Exercise
```

Select the periodicity:

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

The new habit is stored in SQLite.

---

## 📋 2. View Habits

Select:

```text
2. View habits
```

Example:

```text
Current habits:

1. Exercise (daily)
2. Drink Water (daily)
3. Read 20 Minutes (daily)
4. Call Family (weekly)
5. Pay Monthly Bills (monthly)
```

---

## ✅ 3. Complete a Habit

Select:

```text
3. Complete habit
```

The application displays the available habits.

Enter the ID of the habit:

```text
Enter the ID of the habit to complete: 1
```

The application stores the current completion timestamp.

```text
Habit completed successfully.
```

---

## 🗑️ 4. Delete a Habit

Select:

```text
4. Delete habit
```

Then enter the habit ID.

Example:

```text
Enter the ID of the habit to delete: 3
```

The habit and its related completion records are removed from the database.

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

## View All Habits

Returns all currently tracked habits.

## Filter by Periodicity

Users can filter habits by:

```text
Daily
Weekly
Monthly
```

## Longest Streak Overall

The program compares the streaks of all tracked habits and returns the habit with the longest streak.

Example:

```text
Longest streak overall:
Read 20 Minutes: 8 consecutive period(s)
```

## Longest Streak for a Habit

The user selects one habit and the application calculates its longest historical streak.

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

This history demonstrates that completion dates and times are stored persistently.

---

# 🧪 Automated Testing

Automated tests are implemented using **pytest**.

The test suite covers the main components of the application.

| Test Area         | Examples                                                        |
| ----------------- | --------------------------------------------------------------- |
| `Habit`           | creation, validation, periodicity and timestamps                |
| `DatabaseManager` | saving, loading, deleting and persistence                       |
| `HabitManager`    | creating, completing, retrieving and deleting habits            |
| Analytics         | filtering and streak calculations                               |
| Edge cases        | no completions, broken streaks and duplicate-period completions |
| Fixtures          | prevention of duplicate fixture data                            |

Database tests use temporary databases provided through pytest's `tmp_path` fixture.

This prevents automated tests from modifying the normal application database.

---

## ▶️ Running All Tests

Run:

```bash
python -m pytest -v
```

On Windows:

```bash
py -m pytest -v
```

Current verified result:

```text
24 passed
```

Individual test modules can also be executed.

Example:

```bash
py -m pytest tests/test_analytics.py -v
```

or:

```bash
py -m pytest tests/test_database.py -v
```

---

# 🗄️ Database Isolation During Testing

The normal application database is located at:

```text
data/habit_tracker.db
```

Tests requiring database access use temporary databases.

Example:

```python
database_file = tmp_path / "test_habit_tracker.db"
```

This provides two important advantages:

- Tests do not change real user data
- Tests remain repeatable

---

# 🛡️ Input Validation

The application contains validation for common invalid inputs.

Examples include:

- Empty habit names
- Unsupported periodicities
- Invalid menu selections
- Non-numeric habit IDs
- Habit IDs that do not exist

Invalid input is handled without intentionally terminating the application.

---

# 📝 Code Documentation

Important classes and functions include Python docstrings describing their responsibilities.

Example:

```python
def save_habit(self, habit):
    """
    Save a Habit object to the database.
    """
```

The docstrings complement this README and make the source code easier to understand and maintain.

---

# 🧰 Technologies Used

| Technology | Purpose                   |
| ---------- | ------------------------- |
| 🐍 Python  | Main programming language |
| 🗄️ SQLite  | Persistent storage        |
| 🧪 pytest  | Automated testing         |
| 🌳 Git     | Version control           |
| 🌐 GitHub  | Repository hosting        |
| 💻 VS Code | Development environment   |

The core application mainly uses Python's standard library to keep the implementation lightweight.

---

# 🔄 Typical Application Flow

```text
User
  ↓
CLI
  ↓
HabitManager
  ↓
Habit / Database
  ↓
SQLite
```

For analytics:

```text
User
  ↓
CLI
  ↓
HabitManager
  ↓
Habits + Completion Data
  ↓
Analytics
  ↓
Result
  ↓
CLI
```

---

# 🌟 Additional Functionality

The project requirements specify daily and weekly habits as the required periodicities.

This implementation additionally supports:

```text
monthly
```

The monthly periodicity uses the same architecture and streak-calculation logic as the required periodicities.

This extension was implemented without changing the general modular structure of the application.

---

# ✅ Current Project Status

The current implementation includes:

- ✅ Habit object model
- ✅ Daily habits
- ✅ Weekly habits
- ✅ Monthly habits
- ✅ Habit creation
- ✅ Habit deletion
- ✅ Habit completion
- ✅ Habit creation timestamps
- ✅ Completion timestamps
- ✅ SQLite persistence
- ✅ Functional analytics
- ✅ Periodicity filtering
- ✅ Individual longest streak calculation
- ✅ Overall longest streak calculation
- ✅ Five predefined habits
- ✅ Deterministic fixture data
- ✅ Idempotent fixture loading
- ✅ Interactive CLI
- ✅ Automated pytest suite
- ✅ Temporary databases for database tests
- ✅ Python docstrings
- ✅ Git version control
- ✅ GitHub repository

---

# 🎓 Academic Context

This application was developed as part of the IU portfolio project for:

**Object-Oriented and Functional Programming with Python**

The project follows the modular architecture defined during the conception phase and demonstrates the practical application of:

- object-oriented programming
- functional programming
- persistent data storage
- modular software architecture
- automated testing
- documentation
- version control

The focus of the project is on correct functionality, clear separation of responsibilities, maintainability and testability rather than graphical interface complexity.

---

# 📄 Academic Use

This repository represents an academic portfolio project.

The code and documentation are intended primarily for educational and assessment purposes.

---

**Repository:**  
https://github.com/lopillo/habit-tracker-iu
