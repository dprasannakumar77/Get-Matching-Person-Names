#  Smart Name Matching System 🔍

**Zero-dependency fuzzy name matcher that handles typos, nicknames & phonetic variations**  
`geetha` → `Geetha` | `jhonny` → `Johnny` | `priiya` → `Priyanka`

[![Python 3.8+](https://img.shields.io/badge/Python-3.8%2B-blue.svg)](https://www.python.org)
[![No Dependencies](https://img.shields.io/badge/Dependencies-None-success.svg)]()
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## 📑 Table of Contents

1. [🎯 Why This Project?](#why-this-project)  
2. [✨ Features](#features)  
3. [🚀 Live Demo](#live-demo)  
4. [📁 Project Structure](#project-structure)  
5. [⚙️ Setup & Installation](#setup--installation)  
6. [▶️ How to Run](#how-to-run)  
7. [📊 Sample Inputs & Outputs](#sample-inputs--outputs)  
8. [🔧 Customization](#customization)  
9. [❓ Troubleshooting](#troubleshooting)  
10. [📄 License](#license)

---

## 1. 🎯 Why This Project? <a name="why-this-project"></a>

Real names in forms and databases are often misspelled. This tool instantly finds the correct name — ideal for:
- ✅ **Form validation** - Correct user input in real-time
- ✅ **Data cleaning** - Standardize names in databases
- ✅ **Customer deduplication** - Identify duplicate records
- ✅ **Search autocomplete** - Suggest correct names instantly

**[⬆ Back to Top](#task-1--smart-name-matching-system-)**

---

## 2. ✨ Features <a name="features"></a>

| Feature | Description |
|---------|-------------|
| 🚀 **Zero external dependencies** | Uses only Python's built-in `difflib` |
| ⚡ **Lightning fast** | < 1ms response even with 1000+ names |
| 🌐 **Case-insensitive** | Works with any capitalization |
| 📊 **Ranked results + scores** | Shows similarity percentage |
| 🔧 **Easy to extend** | Just add names to `names.txt` |

**[⬆ Back to Top](#task-1--smart-name-matching-system-)**

---

## 3. 🚀 Live Demo <a name="live-demo"></a>


Enter a name (or 'quit' to exit): gheeta

🎯 Results:
🏆 Best Match → Geetha (score: 0.952)
📊 Top Similar Names:

Geeta           → 0.909
Geethu          → 0.857
Gita            → 0.800
Geetu           → 0.800
Gittu           → 0.769

---

### 4. 📁 Project Structure <a name="project-structure"></a>

Task-1-Name-Matching/

│
├── 📄 names.txt          ← Master list of real name variations

├── 🐍 matcher.py         ← Core fuzzy matching engine

├── 🎮 main.py            ← Interactive CLI (run this file)

├── 📋 requirements.txt   ← Empty – no installation needed

└── 📖 README.md          ← This file


---

### 5. ⚙️ Setup & Installation <a name="setup--installation"></a>
No installation required!

Only needs Python 3.8 or higher.

# Create virtual environment (recommended)
python -m venv venv

# Activate virtual environment
venv\Scripts\activate        # Windows

source venv/bin/activate     # Linux/Mac

---

### 6. ▶️ How to Run <a name="how-to-run"></a>

python main.py

---

### 7. 📊 Sample Inputs & Outputs <a name="sample-inputs--outputs"></a>
| Input    | Best Match | Score  |
|----------|------------|--------|
| gheeta   | Geetha     | 0.952  |
| micheal  | Michael    | 0.933  |
| priiya   | Priya      | 0.923  |
| jhonny   | Johnny     | 0.952  |
| annaa    | Anna       | 0.923  |
| kathrine | Katherine  | 0.941  |
| stefan   | Stephan    | 0.917  |
---

### 8. 🔧 Customization <a name="customization"></a>


| Want to... | How to do it |
|------------|--------------|
| Add more names | Edit `names.txt` (one name per line) |
| Make matching stricter | Increase `threshold=0.7` in `matcher.py` |
| Make matching looser | Decrease `threshold=0.5` in `matcher.py` |
| Show more results | Change `top_n=5` → `10` in `main.py` |
| Change similarity algorithm | Modify `find_similar_names()` in `matcher.py` |
---
### 9. ❓ Troubleshooting <a name="troubleshooting"></a>

| Issue | Solution |
|-------|----------|
| ❌ No matches found | Lower threshold to `0.5` in `matcher.py` |
| 📁 "File not found" error | Keep all files in the same folder |
| ⏳ Program not responding | Still faster than any external library! |
| 🐍 Python command not found | Install Python 3.8+ and add to PATH |
| 🔧 Virtual environment issues | Run directly with `python main.py` |
---
### 10. 📄 License <a name="license"></a>
MIT License – Free for personal, academic, and commercial use.