# Linux Lab Environment

A hands-on lab environment for practicing Linux commands. Complete tasks and get instant feedback.

## Setup

> Requires **Python 3** and **pip**.

```bash
git clone <repo-url>
cd Linux-Lab-Env
pip install typer
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

## License

MIT
