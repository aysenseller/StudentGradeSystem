# Student Grade System

A Python-based student grade management system that runs in the terminal.

The application allows users to manage students, add and update grades, calculate averages, search for students, and store data using JSON.

## Features

- Add students
- Show all students
- Find students by ID
- Search students by name
- Edit student information
- Delete students
- Add grades
- Calculate student averages
- Show statistics
- Save data as JSON
- Load data from JSON
- Input validation
- Automated tests with pytest
- GitHub Actions CI

## Technologies

- Python 3
- JSON
- Pytest
- Git
- GitHub
- GitHub Actions

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

macOS / Linux:

```bash
source .venv/bin/activate
```

Windows:

```bash
.venv\Scripts\activate
```

### 5. Install dependencies

```bash
pip install -r requirements.txt
```