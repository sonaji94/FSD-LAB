# Quick Run Commands – FSD Django Lab

Quick reference for lab exam / viva / daily use.

---

## One-Time Setup

```bash
python -m venv venv
venv\Scripts\activate          # Windows
source venv/bin/activate       # Linux / macOS
pip install -r requirements.txt
```

---

## Verify Installation

```bash
python --version
python -m django --version
```

---

## Run a Django Experiment

```bash
cd Experiment-NN/project_files
python manage.py migrate
python manage.py runserver
```

Open `http://127.0.0.1:8000` in browser.

---

## Common Django Commands

| Action | Command |
|--------|---------|
| Create project | `django-admin startproject project_name` |
| Create app | `python manage.py startapp app_name` |
| Make migrations | `python manage.py makemigrations` |
| Apply migrations | `python manage.py migrate` |
| Create superuser | `python manage.py createsuperuser` |
| Run development server | `python manage.py runserver` |
| Open Django shell | `python manage.py shell` |
| Collect static files | `python manage.py collectstatic` |

---

## Deactivate Virtual Environment

```bash
deactivate
```

---

> For experiment-specific run instructions, see the README inside each experiment folder.
