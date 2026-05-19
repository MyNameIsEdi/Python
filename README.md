
# Python Data Handling & Validation 🚀

![Python Version](https://img.shields.io/badge/python-3.8%2B-blue?style=for-the-badge&logo=python)
![QA Focus](https://img.shields.io/badge/Focus-QA_%26_Automation-green?style=for-the-badge)
![Learning](https://img.shields.io/badge/Level-Beginner-orange?style=for-the-badge)

> A foundational Python script demonstrating core principles in development, data management, and validation for software testing.

This repository showcases test data handling, run-time state management, interactive I/O mechanisms, and validation logic. It serves as an essential stepping stone for building robust infrastructure in test automation and advanced Python scripting.

---

## 📋 Table of Contents
- [Architecture & Core Features](#-architecture--core-features)
- [Prerequisites](#-prerequisites)
- [Execution Instructions](#-execution-instructions)
- [Stack & Core Concepts](#-stack--core-concepts)
- [Example Output](#️-example-output)

---

## 🛠️ Architecture & Core Features

### 1. Test Data Initialization
Initialization and management of variables across various data types (`String`, `Integer`, `Float`, `Boolean`). This represents core testing entities, such as tester credentials, session connectivity status, and execution scores.

### 2. Run-time Data Mutation (State Management)
Demonstrates the ability to override and update system variables dynamically during script execution. This capability is crucial for simulating changes in the System Under Test (SUT) or updating authentication tokens during live automation runs.

### 3. Interactive I/O Processing
Captures dynamic parameters in real-time using the `input()` function. The system receives data directly from the end-user (or an external system) and processes it to generate custom, context-aware outputs.

### 4. Advanced String Formatting (Smart Logging)
Utilizes **f-strings** (String Interpolation) to dynamically inject variables—such as the tester's name and the number of tests executed—into live text strings. This mechanism is a Python best practice for generating readable, efficient, and clear execution logs.

### 5. Conditional Logic & Validation
Implements conditional flow control (`if-else`) to evaluate boolean statuses (e.g., `test_passed`). The script analyzes the current state and outputs a formal execution status (`TEST PASSED` or `TEST FAILED`). This logic forms the foundational infrastructure for Assertion mechanisms in test automation.

---

## 💻 Prerequisites

Before running the script, ensure you have the following installed:
* **Python 3.8 or higher**
* An IDE or text editor (e.g., **VS Code**, PyCharm)

---

## 🚀 Execution Instructions

To execute the script in your local environment, open your terminal in the project's root directory and run the following command:

```bash
python main.py

```

*(**Note:** For specific environments such as macOS or Linux, you may need to use `python3 main.py`)*

---

## 📚 Stack & Core Concepts

* **Environment:** Visual Studio Code (VS Code)
* **Technologies:** Python 3 (Standard Library)
* **Data Types:** `String`, `Integer`, `Float`, `Boolean`
* **Flow Control:** `If-Else` conditional logic
* **Syntax & Utilities:** `f-strings` (Interpolation), I/O handling, Variable instantiation

---

## 🖥️ Example Output

Below is an example of what you will see in the terminal when running the script and interacting with the prompts:

```text
--- Exercise 1 ---
Please enter a string (e.g., an email address): hello@world.com
First character: h
Middle character: o
Last character: m

--- Exercise 2 ---
Please enter a string of at least 5 characters: user name 123
a. Sliced string (3rd char to end): er name 123
b. String length: 13
c. String without spaces: user-name-123

```
