# Setup Guide – FSD Django Lab

Use this guide to set up the **FSD Django Lab** repository on any system — including college lab PCs where Python or Django may not be pre-installed.

---

## Purpose

This guide walks you through installing all required software and running any experiment from this repository on a fresh machine.

---

## 1. Install Python

1. Visit [python.org/downloads](https://www.python.org/downloads/)
2. Download the latest **Python 3.x** installer for your operating system
3. Run the installer
4. **Important:** Check the box **"Add Python to PATH"** at the bottom of the installer
5. Click **Install Now** and wait for the installation to complete
6. Verify the installation:

```bash
python --version
```

Expected output: `Python 3.x.x`

---

## 2. Install Visual Studio Code

1. Visit [code.visualstudio.com/download](https://code.visualstudio.com/download)
2. Download the installer for your OS
3. Run the installer (keep default settings)
4. Launch VS Code
5. Recommended: Install the **Python extension** from the Extensions marketplace

---

## 3. Clone the Repository

```bash
git clone <your-repo-url>
cd FSD-Django-Lab
```

> If Git is not installed, download it from [git-scm.com](https://git-scm.com/) or simply download the repo ZIP and extract it.

---

## 4. Create and Activate Virtual Environment

**Windows:**

```bash
python -m venv venv
venv\Scripts\activate
```

**Linux / macOS:**

```bash
python3 -m venv venv
source venv/bin/activate
```

After activation, you will see `(venv)` in your terminal prompt.

---

## 5. Install Dependencies

```bash
pip install -r requirements.txt
```

Verify Django installation:

```bash
python -m django --version
```

---

## 6. Run an Experiment

1. Navigate to the experiment folder:

```bash
cd Experiment-02
```

2. Read the experiment's `README.md` for specific instructions
3. If the experiment has a Django project, go inside `project_files/`:

```bash
cd project_files
```

4. Run migrations and start the server:

```bash
python manage.py migrate
python manage.py runserver
```

5. Open `http://127.0.0.1:8000` in your browser

---

## 7. Deactivate Virtual Environment

When done:

```bash
deactivate
```

---

## Common Troubleshooting

| Problem | Likely Fix |
|---------|-----------|
| `python` not recognized | Reinstall Python and check **"Add Python to PATH"** |
| `pip` not recognized | Ensure Python is installed correctly; try `python -m pip` |
| Virtual environment not activating on Windows | Run `Set-ExecutionPolicy Unrestricted -Scope Process` in PowerShell, then retry |
| `ModuleNotFoundError: No module named 'django'` | Activate the virtual environment first, then run `pip install -r requirements.txt` |
| `django-admin` not found | Install Django via `pip install django` inside the activated venv |
| Command not found on macOS/Linux | Use `python3` instead of `python` |
