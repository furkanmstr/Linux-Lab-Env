# Linux Lab Environment

A hands-on lab environment for practicing Linux commands. Complete tasks and get instant feedback.

## Setup

> Requires **Python 3** and **pip**.

```bash
git clone <repo-url>
cd Linux-Lab-Env
pip install -r requirements.txt
```

## Usage

**See available labs:**

```bash
python lab list
```

**Start a lab** — sets up the environment and shows your tasks:

```bash
python lab start lab-1
```

**Finish a lab** — checks your work and shows your score:

```bash
python lab finish lab-1
```

## Example

```
$ python lab start lab-1
Lab 1 is ready.

Task:
Create the following:
  /tmp/linux-lab/project/
  /tmp/linux-lab/project/hello.txt
```

Complete the tasks using Linux commands, then check your results:

```
$ python lab finish lab-1
==================================================
  Lab 1 — Filesystem Basics
==================================================

  [+]  Directory exists: /tmp/linux-lab/project        PASS
  [+]  File exists: /tmp/linux-lab/project/hello.txt   PASS

--------------------------------------------------
  Result
--------------------------------------------------
  Passed  :  2
  Failed  :  0
  Score   :  2/2  (100%)
--------------------------------------------------
```

## Creating Your Own Labs

### 1. Create the lab folder

```
labs/
└── lab-2/
    ├── start.py
    └── finish.py
```

### 2. Write `start.py`

Sets up the environment and prints the tasks for the student.

```python
from pathlib import Path

LAB_ROOT = Path("/tmp/linux-lab")

if not LAB_ROOT.exists():
    LAB_ROOT.mkdir()

print("Lab 2 is ready.")
print()
print("Task:")
print("  Create a user called 'student'")
```

### 3. Write `finish.py`

Uses the built-in utilities to check the student's work.

```python
from utilities.checks import check_user, check_file, check_directory, check_group, check_exact_permission, check_owner, check_file_content, check_group_membership
from utilities.output import print_header, finish

print_header("Lab 2 — User Management")

check_user("student")

finish()
```

### Available Check Functions

| Function | Description |
|---|---|
| `check_file(path)` | File exists |
| `check_directory(path)` | Directory exists |
| `check_user(username)` | User exists |
| `check_group(groupname)` | Group exists |
| `check_group_membership(user, group)` | User is in group |
| `check_exact_permission(path, "755")` | Permission matches |
| `check_owner(path, username)` | Owner matches |
| `check_file_content(path, text)` | File contains text |

## License

MIT
