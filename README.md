# Rock Paper Scissors

A simple terminal-based Rock, Paper, Scissors game written in Python.

## What is `.venv`?

`.venv` is a **Python virtual environment** folder.

- It contains a local Python interpreter and packages for this project only.
- It keeps project dependencies separate from your system Python.
- It helps avoid version conflicts between projects.

## Create `.venv` on your computer

1. Install Python 3 (from [python.org](https://www.python.org/downloads/)).
2. Open a terminal in the project folder.
3. Create the virtual environment:

```powershell
python -m venv .venv
```

4. Activate it:

For PowerShell:

```powershell
.venv/Scripts/Activate.ps1
```

For Command Prompt (`cmd`):

```cmd
.venv\Scripts\activate.bat
```

After activation, you can run commands with `python` directly.

## About the game

- You choose: `rock`, `paper`, or `scissors`
- The computer randomly chooses one option
- The winner is decided by classic rules:
	- Rock beats Scissors
	- Scissors beats Paper
	- Paper beats Rock

## Run the game

From the project root (`rock-paper-sissors`), run:

```powershell
.venv/Scripts/python.exe game.py
```

If the virtual environment is activated:

```powershell
python game.py
```

## Run the tests

From the project root (`rock-paper-sissors`), run:

```powershell
.venv/Scripts/python.exe -m unittest -v
```

This runs all unit tests (currently in `test_game.py`).

## Run one test file

```powershell
.venv/Scripts/python.exe -m unittest -v test_game.py
```

## Optional: activate the virtual environment first

If you activate the virtual environment, you can use `python` directly:

```powershell
.venv/Scripts/Activate.ps1
python -m unittest -v
```

For Command Prompt (`cmd`):

```cmd
.venv\Scripts\activate.bat
python -m unittest -v
```
