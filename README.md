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
* **`practice_exercises.py`**: Focuses on complex password validation, dynamic error feedback, and data clamping (enforcing numeric boundaries).

---

## 🛠️ Architecture & Core Features

### 1. Test Data Initialization & Mutation
Initialization and management of variables across various data types. Demonstrates the ability to override and update system variables dynamically, which is crucial for simulating changes in a System Under Test (SUT).

### 2. Advanced String Manipulation
Utilizes indexing and slicing to extract specific data points from strings. Employs **f-strings** (String Interpolation) to dynamically inject variables into text, a Python best practice for readable execution logs.

### 3. Control Flow & Boundary Validation
Implements conditional flow control (`if-elif-else`) to evaluate states. Analyzes current states to output formal execution statuses, forming the foundational infrastructure for Assertion mechanisms in test automation. Includes **Data Clamping** to enforce numeric boundaries (e.g., constraining variables between 0 and 120).

### 4. Dynamic Error Feedback (Password Validation)
Simulates real-world authentication testing by evaluating passwords against multiple constraints (length, starting characters, ending symbols) and providing specific, dynamic feedback based on the exact failure point.

---

## 💻 Prerequisites

Before running the scripts, ensure you have the following installed:
* **Python 3.8 or higher**
* An IDE or text editor (e.g., **VS Code**, PyCharm)

---

## 🚀 Execution Instructions

To execute the scripts in your local environment, open your terminal in the project's root directory and run the desired file:

```bash
# Run String Exercises
python string_exercises.py

# Run Conditions & Error Handling
python conditions_exercises.py

# Run Length Validation
python length_validation.py

# Run Advanced Practice (Passwords & Clamping)
python practice_exercises.py

```

---

## 📚 Stack & Core Concepts

* **Environment:** Visual Studio Code (VS Code)
* **Technologies:** Python 3 (Standard Library)
* **Flow Control:** `If-Elif-Else` logic, Multiple constraint checking
* **Techniques:** Data Clamping, String Indexing (`[0]`, `[-1]`), Logic Operators (`and`, `or`, `!=`)

---

## 🖥️ Example Output

Below is an example of what you will see in the terminal when running the **`practice_exercises.py`** script:

```text
--- Age Check ---
Please enter your age: -5
teenager

--- Password Validation ---
Please enter a password: Hello1234
Error: Password must start with 'C' or 'Z'.

```
