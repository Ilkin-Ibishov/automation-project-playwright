# Automation Portfolio Setup Guide

Welcome to your automation engineering journey! This guide will help you set up your environment for Python and Playwright automation.

## 1. Prerequisites

Before we start, ensure you have the following installed:
- **Python (3.8 or higher)**: [Download Python](https://www.python.org/downloads/)
  - *Tip*: During installation, check "Add Python to PATH".
- **VS Code**: [Download VS Code](https://code.visualstudio.com/)
- **Git**: [Download Git](https://git-scm.com/)

## 2. Project Initialization

1.  **Open your terminal** (Command Prompt or PowerShell) and navigate to your project folder:
    ```powershell
    cd c:\Programming\Playground\Folder01\automation-portfoilo-playwright
    ```

2.  **Create a Virtual Environment**:
    It's best practice to isolate your project dependencies.
    ```powershell
    python -m venv venv
    ```

3.  **Activate the Virtual Environment**:
    ```powershell
    .\venv\Scripts\activate
    ```
    *You should see `(venv)` at the start of your command line.*

## 3. Install Dependencies

Install Playwright and Pytest testing framework.

1.  **Install Packages**:
    ```powershell
    pip install playwright pytest pytest-playwright
    ```

2.  **Install Playwright Browsers**:
    ```powershell
    playwright install
    ```

## 4. Recommended Project Structure

We will use the **Page Object Model (POM)** design pattern. It keeps your tests clean and maintainable.

```text
automation-portfolio/
├── .gitignore
├── README.md
├── requirements.txt
├── tests/
│   ├── __init__.py
│   └── test_login.py
├── pages/
│   ├── __init__.py
│   └── login_page.py
└── utils/
    └── config.py
```

- **tests/**: Contains your actual test scripts.
- **pages/**: Contains classes representing web pages (POM).
- **utils/**: Helper functions and configurations.

## 5. VS Code Configuration

1.  Open VS Code in your project folder:
    ```powershell
    code .
    ```
2.  Install the **Python** extension by Microsoft from the Extensions view.
3.  Install the **Playwright Test for VSCode** extension for a better testing experience.
4.  Ensure your VS Code uses the virtual environment interpreter:
    - Press `Ctrl+Shift+P`
    - Type "Python: Select Interpreter"
    - Select the one inside `venv` (e.g., `.\venv\Scripts\python.exe`).

---
**Next Step**: Check `portfolio_log.md` to see your roadmap!
