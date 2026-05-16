
# QA Automation: Python Data Handling & Validation 🚀
![Python Version](https://img.shields.io/badge/python-3.8%2B-blue?style=for-the-badge&logo=python)
![QA Focus](https://img.shields.io/badge/Focus-QA_%26_Automation-green?style=for-the-badge)
![Learning](https://img.shields.io/badge/Level-Beginner-orange?style=for-the-badge)


This repository contains a Python script demonstrating core principles in development and data management for software testing. The project showcases test data handling, run-time state management, interactive I/O mechanisms, and validation logic, serving as a foundational infrastructure for test automation and advanced scripting.

* **Environment:** VS Code
* **Technologies:** Python 3 (Standard Library)

---

## 🛠️ Architecture & Core Features

### 1. Test Data Initialization
Initialization and management of variables across various data types (`String`, `Integer`, `Float`, `Boolean`) to represent core testing entities, such as tester credentials, session connectivity status, and execution scores.

### 2. Run-time Data Mutation (State Management)
Demonstrates the ability to override and update system variables dynamically during script execution. This capability is crucial for simulating changes in the System Under Test (SUT) or updating authentication tokens during live automation runs.

### 3. Interactive I/O Processing
Capturing dynamic parameters in real-time using the `input()` function. The system receives data directly from the end-user (or an external system) and processes it to generate custom, context-aware outputs.

### 4. Advanced String Formatting (Smart Logging)
Utilizing **f-strings** (String Interpolation) to dynamically inject variables—such as the tester's name and the number of tests executed—into live text strings. This mechanism is a Python Best Practice for generating readable, efficient, and clear execution logs.

### 5. Conditional Logic & Validation
Implementing conditional flow control (`if-else`) to evaluate boolean statuses (e.g., `test_passed`). The script analyzes the current state and outputs a formal execution status (`TEST PASSED` or `TEST FAILED`). This logic forms the foundational infrastructure for Assertion mechanisms in test automation.

---

## 🚀 Execution Instructions

To execute the script in your local environment, open the Terminal in the project's root directory and run the following command:

```bash
python main.py

```

*(For specific environments such as macOS or Linux, use `python3 main.py`)*

---

## 📚 Stack & Core Concepts

* **Data Types:** `String`, `Integer`, `Float`, `Boolean`
* **Flow Control:** `If-Else` conditional logic
* **Syntax & Utilities:** `f-strings` (Interpolation), I/O handling, Variable instantiation

```

```
