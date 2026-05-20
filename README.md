# Python Data Handling & Validation 🚀

![Python Version](https://img.shields.io/badge/python-3.8%2B-blue?style=for-the-badge&logo=python)
![QA Focus](https://img.shields.io/badge/Focus-QA_%26_Automation-green?style=for-the-badge)
![Learning](https://img.shields.io/badge/Level-Beginner-orange?style=for-the-badge)

A beginner-friendly collection of small Python exercises that demonstrate core programming concepts useful for QA and test automation: variables and state, user input, string manipulation, conditionals, length validation, clamping, and simple password checks.

## Quick summary
- **Purpose:** Teach and demonstrate basic Python patterns useful for testers and automation engineers through short, interactive scripts.
- **Audience:** Beginners learning Python for QA, manual testers learning scripting, or anyone practicing control flow and string handling.

## Repository Structure
- [main.py](main.py) — Simple interactive script demonstrating variables, updates, and basic input usage.
- [practice_1/string_exercises.py](practice_1/string_exercises.py) — String indexing, slicing, length and replacement exercises.
- [practice_1/conditions_exercises.py](practice_1/conditions_exercises.py) — Control flow exercises and small validations (number sign, modify leading 'A', basic email checks).
- [practice_1/length_validation.py](practice_1/length_validation.py) — Boundary checking for string length with user-friendly output.
- [practice_1/practice_exercises.py](practice_1/practice_exercises.py) — Age clamping/categorization and password validation with specific error messages.

## Features & Teaching Points
- Interactive I/O and `input()` usage for hands-on practice.
- String operations: indexing, slicing, replacement, and length measurement.
- Conditional logic: `if/elif/else` patterns and clear, early-return style validations.
- Data clamping and boundary handling for robust input processing.

## Prerequisites
- Python 3.8 or higher

## Run the examples
Open a terminal in the project root and run any script directly. Examples:

```bash
python main.py
python practice_1/string_exercises.py
python practice_1/conditions_exercises.py
python practice_1/length_validation.py
python practice_1/practice_exercises.py
```

## Example output (excerpt)
Running `practice_1/practice_exercises.py` shows an age check and password validation, for example:

--- Age Check ---
Please enter your age: -5
teenager

--- Password Validation ---
Please enter a password: Hello1234
Error: Password must start with 'C' or 'Z'.

## Next steps
- Try the scripts and modify inputs to explore how clamping and validations respond.
- Use these exercises as small building blocks to create test helpers or simple validators in larger projects.

---
License: See repository root for terms.
