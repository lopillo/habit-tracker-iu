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

- Python 3.7 or later
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

- Python 3.7 or later
- `pip`
- `pytest`

The project was developed and tested using Python 3.11.

SQLite is part of the Python standard library and does not require a separate installation.

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

Example:

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
