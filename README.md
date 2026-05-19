# Python Data Handling & Validation 🚀

![Python Version](https://img.shields.io/badge/python-3.8%2B-blue?style=for-the-badge&logo=python)
![QA Focus](https://img.shields.io/badge/Focus-QA_%26_Automation-green?style=for-the-badge)
![Learning](https://img.shields.io/badge/Level-Beginner-orange?style=for-the-badge)

> A foundational Python repository demonstrating core principles in development, data management, string manipulation, and validation for software testing.

This repository showcases test data handling, run-time state management, interactive I/O mechanisms, and validation logic. It serves as an essential stepping stone for building robust infrastructure in test automation and advanced Python scripting.

---

## 📋 Table of Contents
- [Repository Structure](#-repository-structure)
- [Architecture & Core Features](#-architecture--core-features)
- [Prerequisites](#-prerequisites)
- [Execution Instructions](#-execution-instructions)
- [Stack & Core Concepts](#-stack--core-concepts)
- [Example Output](#️-example-output)

---

## 📂 Repository Structure

* **`string_exercises.py`**: Focuses on string indexing, slicing, length calculation, and character replacement.
* **`conditions_exercises.py`**: Focuses on control flow (`if-elif-else`), type casting, error handling, and basic input validation (e.g., email format checks).
* **`length_validation.py`**: Focuses on boundary testing, evaluating string lengths, and grouping states into distinct ranges.

---

## 🛠️ Architecture & Core Features

### 1. Test Data Initialization & Mutation
Initialization and management of variables across various data types. Demonstrates the ability to override and update system variables dynamically, which is crucial for simulating changes in a System Under Test (SUT).

### 2. Interactive I/O Processing
Captures dynamic parameters in real-time using the `input()` function, processing user data to generate custom, context-aware outputs.

### 3. Advanced String Manipulation
Utilizes indexing and slicing to extract specific data points from strings. Employs **f-strings** (String Interpolation) to dynamically inject variables into text, a Python best practice for readable execution logs.

### 4. Control Flow & Validation Logic
Implements conditional flow control (`if-elif-else`) to evaluate states. Analyzes current states to output formal execution statuses, forming the foundational infrastructure for Assertion mechanisms in test automation.

### 5. Type Casting & Error Handling
Demonstrates safe data conversion (e.g., `String` to `Float`) using `try-except` blocks. This ensures the script handles invalid inputs gracefully without crashing, mimicking robust backend validation.

### 6. Boundary Testing & Range Validation
Implements logic to test data against defined boundaries (e.g., less than 4, greater than 9). This mimics real-world form validation (like checking if a password is long enough but not too long).

---

## 💻 Prerequisites

Before running the scripts, ensure you have the following installed:
* **Python 3.8 or higher**
* An IDE or text editor (e.g., **VS Code**, PyCharm)

---

## 🚀 Execution Instructions

To execute the scripts in your local environment, open your terminal in the project's root directory and run the desired file:

**Run String Exercises:**
```bash
python string_exercises.py

```

**Run Conditions & Error Handling:**

```bash
python conditions_exercises.py

```

**Run Length Validation (Boundary Testing):**

```bash
python length_validation.py

```

*(**Note:** For specific environments such as macOS or Linux, you may need to use `python3` instead of `python`)*

---

## 📚 Stack & Core Concepts

* **Environment:** Visual Studio Code (VS Code)
* **Technologies:** Python 3 (Standard Library)
* **Data Types:** `String`, `Integer`, `Float`, `Boolean`
* **Flow Control:** `If-Elif-Else` logic, `Try-Except` error handling
* **Syntax & Utilities:** `f-strings` (Interpolation), I/O handling, `len()` function, Type Casting (`float()`)

---

## 🖥️ Example Output

Below is an example of what you will see in the terminal when running the **`length_validation.py`** script:

```text
--- String Length Validation ---
Please enter a string: automation
too long
(The actual length was: 10)

--- String Length Validation ---
Please enter a string: test
OK
(The actual length was: 4)

```