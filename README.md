# Python — From Zero to Solid Intermediate

> A 26-lesson self-study track, organised into 5 blocks.
> One domain throughout: cars, garage and fleet management (the same as the C++ track).
> Every lesson is a `.py` file that runs cleanly. One commit per lesson.

**Mandatory checks for every lesson (Python 3.12 or newer):**

```bash
python3 -X dev lessonNN.py
ruff check lessonNN.py && ruff format lessonNN.py
```

From Lesson 14 onwards, also run `mypy --strict lessonNN.py`.
From Lesson 25 onwards, every change runs `pytest` before the commit.

> `-X dev` turns on development mode: extra runtime warnings, resource-leak
> detection, and stricter checks. It is Python's closest equivalent to
> `-Wall -Wextra`.

---

## BLOCK I — Foundations

*You write terminal programs that work. If you already know some Python, go fast — but do Lesson 6 properly.*

| # | Lesson | What you learn | Deliverable |
|:--:|---|---|---|
| 1 | First program and variables | `print`, `input`, the basic types (`int`, `float`, `bool`, `str`, `None`), dynamic typing, f-strings, `/` vs `//` vs `%` | `lesson01.py` |
| 2 | Operators and expressions | arithmetic, comparison, logical, truthiness, `==` vs `is`, conversions (`int()`, `float()`, `str()`) | `lesson02.py` |
| 3 | Conditionals | `if` / `elif` / `else`, chained comparisons, conditional expressions, `match` basics | `lesson03.py` |
| 4 | Loops | `for` over any iterable, `range`, `while`, `break`, `continue`, loop `else`, `enumerate`, `zip` | `lesson04.py` |
| 5 | Functions I | `def`, `return`, scope and the LEGB rule, docstrings, first type hints | `lesson05.py` |
| 6 | **Names, objects and mutability** | variables are labels not boxes, mutable vs immutable, aliasing, `copy` vs `deepcopy`, how arguments are really passed, the mutable-default trap | `lesson06.py` |

> **Lesson 6 is the most important of this block.** "Everything is a reference
> to an object" explains 80% of the bugs beginners cannot explain. It is the
> Python equivalent of by-value vs by-reference in C++. Do not rush it.

**Block I checkpoint:** you can write a looping terminal menu, built from
functions, that never crashes on bad input.

---

## BLOCK II — Data and structure

*You stop juggling loose variables and start modelling the problem.*

| # | Lesson | What you learn | Deliverable |
|:--:|---|---|---|
| 7 | Strings | methods, slicing, immutability, format specs, `str` vs `bytes`, encodings | `lesson07.py` |
| 8 | Lists and tuples | slicing, `sort` vs `sorted`, unpacking, list comprehensions, when a tuple beats a list | `lesson08.py` |
| 9 | Dicts and sets | hashing, `get` / `setdefault`, dict and set comprehensions, `Counter`, `defaultdict` | `lesson09.py` |
| 10 | Files and I/O | `with`, `pathlib`, text vs binary, `csv`, `json`, input validation | `lesson10.py` |
| 11 | Errors and exceptions | `try` / `except` / `else` / `finally`, `raise`, custom exception hierarchies, EAFP vs LBYL | `lesson11.py` |
| 12 | Modules, packages and environments | the import system, `if __name__ == "__main__"`, `src/` layout, `venv` or `uv`, `pyproject.toml` | `lesson12/` |

**Block II checkpoint — Mini-Garage project:**
cars stored as dicts in a list, a full menu, JSON and CSV persistence,
custom exceptions for invalid input, code split into a proper package
under `src/`, installable with `pip install -e .`, zero `ruff` findings.

> **End of the beginner level.** If you stopped here, you can program in Python.
> What follows is what makes Python *Python* — and what separates scripts from software.

---

## BLOCK III — Objects and the Python data model

*The heart of the language. This block is why Python code can be both short and correct.*

| # | Lesson | What you learn | Deliverable |
|:--:|---|---|---|
| 13 | Your first class | `__init__`, instance vs class attributes, methods, `__repr__` / `__str__`, invariants, `@property` | `lesson13.py` |
| 14 | Dataclasses and serious type hints | `@dataclass`, `frozen`, `field`, `Enum`, `Optional`, unions, `mypy --strict` | `lesson14.py` |
| 15 | **The data model (dunder methods)** | `__eq__`, `__hash__`, `__lt__`, `__len__`, `__contains__`, `__getitem__`, operator overloading, why `__eq__` removes `__hash__` | `lesson15.py` |
| 16 | Inheritance, composition and Protocols | `super()`, overriding, composition over inheritance, ABCs, duck typing, `typing.Protocol` | `lesson16.py` |
| 17 | **Iterators and generators** | the iteration protocol, `iter` / `next`, `yield`, generator expressions, lazy pipelines, `itertools` | `lesson17.py` |
| 18 | Closures, decorators and context managers | first-class functions, closures, `@decorator` desugared, `functools.wraps`, `lru_cache`, `contextlib.contextmanager` | `lesson18.py` |

> **Lessons 15 and 17 are the watershed.** Someone who understands the data model
> and the iteration protocol knows Python. Someone who does not writes Java with
> Python syntax.

**Block III checkpoint:** you can explain to a colleague, without notes, what a
`for` loop actually calls under the hood, and why a class with `__eq__` but no
`__hash__` cannot go into a `set`.

---

## BLOCK IV — The standard library and modern Python

*You stop reinventing the wheel and start using the batteries that are included.*

| # | Lesson | What you learn | Deliverable |
|:--:|---|---|---|
| 19 | Choosing data structures | `list`, `dict`, `set`, `deque`, `heapq`, `bisect` — complexity and how to choose | `lesson19.py` |
| 20 | Functional tools | `lambda`, `key=` functions, `map` / `filter` vs comprehensions, `functools`, `operator`, `itertools.groupby` | `lesson20.py` |
| 21 | Advanced typing and pattern matching | generics (PEP 695 syntax), `TypeVar`, `Literal`, `TypedDict`, structural `match` on objects | `lesson21.py` |
| 22 | Practical standard library | `datetime` and time zones, `logging`, `argparse`, `subprocess`, `sqlite3` | `lesson22.py` |
| 23 | Concurrency | threads vs processes vs `asyncio`, the GIL, `concurrent.futures`, I/O-bound vs CPU-bound | `lesson23.py` |
| 24 | Performance and NumPy | `timeit`, `cProfile`, why pure Python loops are slow, vectorisation with NumPy arrays | `lesson24.py` |

**Block IV checkpoint:** you pick the right data structure for a problem and
justify it with its complexity, and you can tell whether a slow program needs
threads, processes, async, or NumPy.

---

## BLOCK V — Going professional

*The difference between a script that works and code you ship.*

| # | Lesson | What you learn | Deliverable |
|:--:|---|---|---|
| 25 | Tooling | `pytest` (fixtures, `parametrize`), `ruff`, `mypy`, `pdb` / `breakpoint()`, `pre-commit`, GitHub Actions CI | `lesson25/` |
| 26 | **Capstone project** | full FleetManager: CLI + SQLite persistence + trip-log analysis, with tests, CI, type-checked, documented | repository |

> Optional capstone extension: expose the FleetManager through a small FastAPI
> REST API. It is the natural bridge to backend work.

---

## How you know you have reached solid intermediate

You can answer all of these without looking anything up:

- [ ] What does `a = b` do when `b` is a list — and why does changing `b` change `a`?
- [ ] Why is `def f(cars=[]):` a bug, and what is the idiomatic fix?
- [ ] Why can a tuple be a dict key but a list cannot?
- [ ] What exactly does a `for` loop call under the hood?
- [ ] When is a generator better than a list — and when is it worse?
- [ ] Why is `x in my_list` O(n) and `x in my_set` O(1) on average?
- [ ] What does `@my_decorator` above a function actually translate to?
- [ ] What is the GIL, and when do threads still help?
- [ ] EAFP vs LBYL: what are they, and which does Python favour?
- [ ] Why do you write `x is None` and not `x == None`?

And you can do all of these:

- [ ] Read a long traceback and find the actual cause
- [ ] Use `breakpoint()` / `pdb` to track down a bug instead of adding `print`s
- [ ] Set up a project from scratch with `pyproject.toml`, tests, linting, type checking and CI
- [ ] Get a non-trivial module to pass `mypy --strict`
- [ ] Read someone else's Python without getting lost

---

## What this track deliberately does **not** cover

Advanced topics, intentionally out of scope. They are not worth the time yet:

- Metaclasses and descriptors in depth
- Multiple inheritance and MRO edge cases
- `asyncio` internals and writing your own event loop
- C extensions, Cython, ctypes
- Import hooks and runtime code generation
- Publishing packages to PyPI
- The free-threaded (no-GIL) build

Domain libraries are also left out of the core track. They are separate tracks,
to be taken after Lesson 26:

- **Scientific Python:** NumPy in depth, Matplotlib, pandas, SciPy
- **Computer vision and ML:** OpenCV, PyTorch
- **Robotics:** ROS 2 with `rclpy`
- **Backend:** FastAPI, SQLAlchemy, Docker

---

## Pace

| Block | Lessons | Realistic time |
|---|---|---|
| I — Foundations | 1–6 | 3–5 days (faster if you already know some Python) |
| II — Data and structure | 7–12 + project | 1.5 weeks |
| III — Objects and data model | 13–18 | 2 weeks |
| IV — Standard library | 19–24 | 1.5 weeks |
| V — Going professional | 25–26 | 1.5 weeks |

**Total: roughly 7 weeks** at 1–2 hours per day. With coursework alongside,
count on 2 to 2.5 months. It is not a race — Block III is what matters.

---

## Ground rules

1. Never copy code you cannot explain line by line.
2. Always run `ruff check`. A lint warning is a deferred bug.
3. From Lesson 14 onwards, always pass `mypy --strict`. Type hints are documentation the machine checks.
4. A long traceback? Read **the last line** first (what went wrong), then the frame just above it that points into *your* code (where). The rest is the path that led there.
5. One commit per lesson. The history is the proof of the journey.
