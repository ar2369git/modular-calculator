# Modular Calculator

[![CI](https://github.com/<YOUR_USERNAME>/modular-calculator/actions/workflows/python-app.yml/badge.svg)](https://github.com/<YOUR_USERNAME>/modular-calculator/actions)

A sophisticated, modular command-line calculator in Python featuring advanced design patterns, persistent history via pandas, dotenv-driven configuration, and full test automation with GitHub Actions.

---

## Features

- **REPL Interface**: Read–Eval–Print loop for interactive use  
- **Arithmetic Operations**: `+`, `-`, `*`, `/`, `^` (power), `root`  
- **Design Patterns**  
  - **Factory** for operation instantiation  
  - **Strategy** for interchangeable execution  
  - **Observer** (history auto-save)  
  - **Memento** for undo/redo  
  - **Facade** hiding subsystem complexity  
- **History Management** with pandas DataFrame → CSV  
- **Configuration** via `.env` (dotenv)  
- **Comprehensive Error Handling** (LBYL & EAFP)  
- **Test Suite**  
  - pytest with parameterized tests  
  - pytest-cov measuring coverage  
- **CI Pipeline** with GitHub Actions enforcing ≥ 95% coverage

---

## Requirements

- Python 3+  
- `pandas`  
- `python-dotenv`  
- `pytest`, `pytest-cov`

---

## Installation

```bash
# 1. Clone
git clone https://github.com/<YOUR_USERNAME>/modular-calculator.git
cd modular-calculator

# 2. Create & activate virtualenv
python -m venv .venv
source .venv/bin/activate      # macOS/Linux
.venv\Scripts\activate         # Windows

# 3. Install Python dependencies
pip install --upgrade pip
pip install -r requirements.txt

# 4. Copy configuration template
cp .env.example .env
# Edit `.env` if you wish to change HISTORY_PATH or AUTO_SAVE
