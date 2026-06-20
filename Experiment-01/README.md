# Experiment-01: Installation of Python, Django and Visual Studio Code

---

## Aim

To demonstrate the installation of Python, Django, and Visual Studio Code — the essential tools required for Full Stack Web Development using Django.

---

## Overview / Theory

### What is Full Stack Development?

Full Stack Development refers to building both the **front-end** (client-side) and **back-end** (server-side) of a web application. It involves working with databases, server logic, APIs, and user interfaces.

### What is Django?

Django is a high-level Python web framework that encourages rapid development and clean, pragmatic design. It follows the **Model-View-Template (MVT)** architecture and includes built-in features like an ORM, authentication, admin panel, and more.

### Why Django?

- **Batteries included** — comes with authentication, admin, ORM, and more out of the box
- **Secure** — built-in protection against SQL injection, XSS, CSRF, and other attacks
- **Scalable** — used by large production sites (Instagram, Pinterest, Mozilla)
- **Great documentation** — extensive and beginner-friendly official docs

### What is a Python Virtual Environment?

A virtual environment is an isolated Python environment that allows you to install project-specific dependencies without interfering with system-wide packages. It is considered a **best practice** for all Python/Django projects and is used throughout this lab.

---

## Software Required

- Python 3.x
- pip (Python package manager)
- Visual Studio Code (or any code editor)
- Django
- Command Prompt / Terminal
- Web browser

---

## Steps to Install Python

1. Visit the official Python download page: [python.org/downloads](https://www.python.org/downloads/)
2. Download the latest **Python 3.x** installer for your operating system
3. Run the installer
4. **Important:** Check the box **"Add Python to PATH"** at the bottom of the installer window
5. Click **Install Now** and wait for the installation to complete
6. Verify the installation by opening a terminal and running:

```bash
python --version
```

You should see output similar to: `Python 3.x.x`

---

## Steps to Open Python IDLE

1. After Python is installed, search for **IDLE** in the Start Menu (Windows) or launch it from the terminal
2. IDLE (Integrated Development and Learning Environment) is Python's built-in IDE
3. You can type Python commands directly in the IDLE shell window and see instant output
4. To exit IDLE, press `Ctrl + Z` then `Enter` (Windows) or `Ctrl + D` (Linux/macOS)

---

## Steps to Install Visual Studio Code

1. Visit the VS Code download page: [code.visualstudio.com/download](https://code.visualstudio.com/download)
2. Download the installer for your operating system
3. Run the installer and follow the default setup
4. Optional: Check **"Add to PATH"** during installation to open VS Code from the terminal
5. Launch VS Code after installation
6. Recommended: Install the **Python extension** from the Extensions marketplace (`Ctrl + Shift + X`)

---

## Steps to Install Django

It is recommended to install Django inside a **virtual environment**.

### Step 1: Create a Virtual Environment

```bash
python -m venv venv
```

### Step 2: Activate the Virtual Environment

**Windows:**

```bash
venv\Scripts\activate
```

**Linux / macOS:**

```bash
source venv/bin/activate
```

Once activated, you will see `(venv)` in your terminal prompt.

### Step 3: Install Django

```bash
pip install django
```

### Step 4: Verify Django Installation

```bash
python -m django --version
```

Expected output: `4.2.x` (or the installed version number)

---

## Expected Outcome

After completing this experiment:

- Python 3.x is installed and verified on the system
- Python IDLE is accessible
- Visual Studio Code is installed and ready for development
- Django is installed inside a virtual environment
- The development environment is fully prepared for all subsequent FSD lab experiments

---

## Conclusion

This experiment prepares the environment required for the remaining Django lab experiments (Experiments 02 through 12). All future experiments assume that Python, VS Code, and Django are installed and the virtual environment workflow is understood.

---

## Notes

- Always activate the virtual environment (`venv`) before working on any Django experiment
- If `python` is not recognized, try `python3` (Linux/macOS) or reinstall Python with **"Add to PATH"** checked (Windows)
- Keep your packages updated: `pip install --upgrade pip`
- Screenshots of the installation steps can be placed in the `assets/` folder for reference
- Refer to [`setup_guide.md`](../setup_guide.md) and [`run_commands.md`](../run_commands.md) at the repository root for quick reference
