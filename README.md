# CarFleetManager
Self-made project to master Python.

---

## Features

| FR | Description | Status |
|----|-------------|--------|
| 1 | Create a `Car` class with attributes: plate, model, fuel, status, and inspection date. | ⬜ |
| 2 | Create a `Garage` class that holds a list of `Car` objects. | ⬜ |
| 3 | Implement inheritance: `ElectricCar` and `CombustionCar` derived from `Car`. | ⬜ |
| 4 | Use `@dataclass` decorator to simplify the `Car` class definition. | ⬜ |
| 5 | Use `enum.Enum` for `Fuel` (PETROL, DIESEL, ELECTRIC) and `Status` (AVAILABLE, IN_MAINTENANCE, SOLD). | ⬜ |
| 6 | Store all garages in a `dict[str, Garage]` indexed by garage ID. | ⬜ |
| 7 | Implement custom exceptions: `CarNotFoundException`, `DuplicateCarException`. | ⬜ |
| 8 | Save and load data from JSON files (`garages.json`, `cars.json`) using the `json` module. | ⬜ |
| 9 | Use list comprehensions and `filter()` to search cars by fuel or status. | ⬜ |
| 10 | Use `sorted()` with `lambda` functions to sort cars by inspection date or model. | ⬜ |
| 11 | Use `*args` and `**kwargs` in a generic `search()` function for flexible filtering. | ⬜ |
| 12 | Use `@property` and `@setter` decorators to validate car attributes on assignment. | ⬜ |
| 13 | Separate code into modules: `models.py`, `storage.py`, `cli.py`, `exceptions.py`. | ⬜ |
| 14 | Use `argparse` to build a CLI: add, list, update, delete, and filter cars. | ⬜ |
| 15 | Write unit tests with `unittest` or `pytest` for all core functions. | ⬜ |
| 16 | Add type hints (`int`, `str`, `list[Car]`, `Optional`) to all functions and classes. | ⬜ |
| 17 | Document code with docstrings (Google style) for all classes and public methods. | ⬜ |
| 18 | Implement reporting: cars per garage, overdue inspections, availability rate per fuel type. | ⬜ |
| 19 | Export reports to `.csv` using the `csv` module. | ⬜ |
| 20 | Use a `requirements.txt` and a `README.md` with installation and usage instructions. | ⬜ |

---

## Roadmap

- **Week 1** — Classes + enums + exceptions (FR 1–7)
- **Week 2** — JSON files + search + sorting (FR 8–11)
- **Week 3** — Modules + CLI + type hints (FR 12–16)
- **Week 4** — Tests + documentation + reports (FR 17–20)

---

## Mapping from the previous version

| Before | Now |
|--------|-----|
| `Task` | `Car` |
| `Project` | `Garage` |
| `BugTask` / `FeatureTask` | `ElectricCar` / `CombustionCar` |
| `Priority` (LOW/MEDIUM/HIGH) | `Fuel` (PETROL/DIESEL/ELECTRIC) |
| `Status` (TODO/IN_PROGRESS/DONE) | `Status` (AVAILABLE/IN_MAINTENANCE/SOLD) |
| `due_date` | `inspection_date` |
