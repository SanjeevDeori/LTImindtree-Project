# 📝 Student Grading System – Python Project

## 📌 Project Description



The **Student Grading System** is a modular, well-structured Python application designed to read student records from a CSV file, process their scores through customizable grading strategies, and generate insightful reports.

This project was developed as part of the LTIMindtree training program, demonstrating practical application of Python programming concepts learned during the online session training.

It follows **clean architecture principles** by separating models, services, and utilities, making the code easy to understand, extend, and maintain.

### This project showcases:

- ✔ **Proper Python project structure** (models, services, utils, data)
- ✔ **Object-Oriented Programming** with polymorphic grading strategies
- ✔ **CSV data validation** and safe loading
- ✔ **Customizable command-line interface** using `argparse`
- ✔ **Automatic JSON export** of final graded results
- ✔ **Useful report generation** (grade distribution, pass rate, toppers)
- ✔ **GitHub-ready layout** with README, `.gitignore`, and clean folder organization

---

## 📂 Project Structure

```
Project2/
│
├─ app.py
├─ README.md
│
├─ data/
│   ├─ students.csv
│   └─ results.json          (auto-created after running)
│
├─ models/
│   ├─ __init__.py
│   └─ student.py
│
├─ services/
│   ├─ __init__.py
│   ├─ loader.py
│   ├─ analyzer.py
│   └─ reporter.py
│
└─ utils/
    ├─ __init__.py
    └─ grade_utils.py
```

---

## 🚀 How to Run the Project

Make sure you have **Python 3.8+** installed.

### Default run
```bash
python app.py
```

### Choose grading strategy
```bash
python app.py -s weighted
```

### Choose custom CSV input and JSON output
```bash
python app.py -i data/custom.csv -o output/results.json
```

### See all CLI options
```bash
python app.py --help
```

---

## 🎯 Features

### ✔ Load & validate CSV
- Ensures required columns exist
- Skips rows with invalid values
- Catches wrong paths (file vs directory)

### ✔ Grading strategies using OOP
- **SimpleAverageStrategy**: Equal weight for assignment, quiz, exam
- **WeightedExamHeavyStrategy**: Exam = 60%, Assignment = 20%, Quiz = 20%

### ✔ Summary reporting
Displays:
- Grade counts (A/B/C/D/F)
- Average final score
- Pass rate
- Failed student count
- Top performers

### ✔ Save final results to JSON
All final results (scores + grades) are stored in clean JSON format.

---

## 🧩 Modules & Responsibilities

### 📘 `models/student.py`
Defines the `Student` dataclass:
- ID
- Name
- Assignment/quiz/exam scores
- Computed final score
- Letter grade

### ⚙️ `services/loader.py`
Handles CSV loading:
- Validates columns
- Converts rows → `Student` objects
- Checks file existence
- Handles wrong paths (directory instead of file)

### 🧠 `services/analyzer.py`
Contains:
- `GradingStrategy` (abstract base class)
- `SimpleAverageStrategy`
- `WeightedExamHeavyStrategy`
- `apply_grading()` to compute final score & letter grade

### 📊 `services/reporter.py`
Provides reporting functions:
- `save_results_as_json()`
- `print_summary()`
- `print_top_students()`

Outputs include:
- Grade distribution
- Average final score
- Pass rate
- Failed students
- Top N students

### 🔧 `utils/grade_utils.py`
Utility to convert numeric score → letter grade:
- **A** (90+)
- **B** (80+)
- **C** (70+)
- **D** (60+)
- **F** (<60)

---

## 📑 Sample CSV

Create this inside `data/students.csv`:

```csv
id,name,assignment,quiz,exam
1,Alice,85,90,88
2,Bob,70,65,72
3,Charlie,92,95,94
4,Drake,60,58,62
5,Edward,78,80,76
```

---

## 🖥 Example Console Output

```
===== Grade Summary =====
Grade A: 2 student(s)
Grade B: 2 student(s)
Grade C: 1 student(s)

Average final score: 81.25
Pass rate: 100.0% (5 / 5)
Failed students: 0

Top 3 students:
  1. Charlie - 93.67 [A]
  2. Alice - 87.67 [B]
  3. Edward - 78.00 [C]
```

---

## 📦 `requirements.txt`

```txt
# Standard library only project
# Tested with Python 3.8+
```

---

## 🚫 `.gitignore`

```gitignore
# Byte-compiled / optimized / DLL files
__pycache__/
*.py[cod]
*$py.class

# Virtual environments
venv/
.env/

# VS Code settings
.vscode/

# System files
.DS_Store
Thumbs.db
```

## 👤 Author

**Sanjeev Deori**  
GitHub: [@SanjeevDeori](https://github.com/SanjeevDeori)  
Repository: [LTImindtree-Project](https://github.com/SanjeevDeori/LTImindtree-Project)

---

## 🎓 Acknowledgments

This project was developed as part of the **LTIMindtree Python Training Program**. Special thanks to the instructors for their guidance throughout the online session training course.

---
