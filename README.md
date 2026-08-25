# Student Grade System

A Python-based student grade management system that runs in the terminal.

The application allows users to manage students, add and update grades, calculate averages, search for students, and store data using JSON.

## Features

* Add students
* Show all students
* Find students by ID
* Search students by name
* Edit student information
* Delete students
* Add grades
* Calculate student averages
* Show statistics
* Save data as JSON
* Load data from JSON
* Input validation
* Automated tests with pytest
* GitHub Actions CI

## Technologies

* Python 3
* JSON
* Pytest
* Git
* GitHub
* GitHub Actions

## Project Structure

```text
StudentGradeSystem/

│
├── src/
│   ├── student.py
│   └── student_manager.py
│
├── tests/
│   ├── test_student.py
│   └── test_student_manager.py
│
├── main.py
├── data.json
├── requirements.txt
├── pytest.ini
├── .gitignore
└── README.md
```

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/aysenseller/StudentGradeSystem.git
```

### 2. Enter the project directory

```bash
cd StudentGradeSystem
```

### 3. Create a virtual environment

```bash
python3 -m venv .venv
```

### 4. Activate the virtual environment

**macOS / Linux:**

```bash
source .venv/bin/activate
```

**Windows:**

```bash
.venv\Scripts\activate
```

### 5. Install dependencies

```bash
pip install -r requirements.txt
```

## Usage

Run the application:

```bash
python3 main.py
```

The application provides a terminal-based menu for managing students, grades, searches, and statistics.

## Testing

Run all tests with:

```bash
pytest
```

The project currently contains 21 automated tests covering:

* Student creation
* Grade management
* Average calculation
* Student validation
* Student management
* Student search
* Statistics
* JSON save/load
* Student display

## Continuous Integration

GitHub Actions automatically runs the test suite when changes are pushed or a pull request is created.

All tests must pass before changes are merged into the `main` branch.
