# PythonTaskManager

Self-made project to master Python.

---

## Features

| FR | Description | Status |
|----|-------------|--------|
| 1 | Create a `Task` class with attributes: title, description, priority, status, and due date. | ⬜ |
| 2 | Create a `Project` class that holds a list of `Task` objects. | ⬜ |
| 3 | Implement inheritance: `BugTask` and `FeatureTask` derived from `Task`. | ⬜ |
| 4 | Use `@dataclass` decorator to simplify the `Task` class definition. | ⬜ |
| 5 | Use `enum.Enum` for `Priority` (LOW, MEDIUM, HIGH) and `Status` (TODO, IN_PROGRESS, DONE). | ⬜ |
| 6 | Store all projects in a `dict[str, Project]` indexed by project ID. | ⬜ |
| 7 | Implement custom exceptions: `TaskNotFoundException`, `DuplicateTaskException`. | ⬜ |
| 8 | Save and load data from JSON files (`projects.json`, `tasks.json`) using the `json` module. | ⬜ |
| 9 | Use list comprehensions and `filter()` to search tasks by priority or status. | ⬜ |
| 10 | Use `sorted()` with `lambda` functions to sort tasks by due date or priority. | ⬜ |
| 11 | Use `*args` and `**kwargs` in a generic `search()` function for flexible filtering. | ⬜ |
| 12 | Use `@property` and `@setter` decorators to validate task attributes on assignment. | ⬜ |
| 13 | Separate code into modules: `models.py`, `storage.py`, `cli.py`, `exceptions.py`. | ⬜ |
| 14 | Use `argparse` to build a CLI: add, list, update, delete, and filter tasks. | ⬜ |
| 15 | Write unit tests with `unittest` or `pytest` for all core functions. | ⬜ |
| 16 | Add type hints (`int`, `str`, `list[Task]`, `Optional`) to all functions and classes. | ⬜ |
| 17 | Document code with docstrings (Google style) for all classes and public methods. | ⬜ |
| 18 | Implement reporting: tasks per project, overdue tasks, completion rate per priority. | ⬜ |
| 19 | Export reports to `.csv` using the `csv` module. | ⬜ |
| 20 | Use a `requirements.txt` and a `README.md` with installation and usage instructions. | ⬜ |

---

## Roadmap

- **Week 1** — Classes + enums + exceptions (FR 1–7)
- **Week 2** — JSON files + search + sorting (FR 8–11)
- **Week 3** — Modules + CLI + type hints (FR 12–16)
- **Week 4** — Tests + documentation + reports (FR 17–20)
