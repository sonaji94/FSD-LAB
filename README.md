# Full Stack Web Development Laboratory – Django Stack

**Course Code:** 22CSL67

---

## About the Repository

This repository contains all experiments from the **Full Stack Web Development Laboratory (22CSL67)** manual, organized experiment-wise under a single repository. Each experiment folder is self-contained with its own README explaining the aim, prerequisites, setup, and execution steps.

The lab is based on the **Django stack** (Python + Django + SQLite) and covers full stack web development concepts including models, views, templates, forms, admin interface, class-based views, and AJAX.

---

## Technologies Used

* Python 3.x
* Django
* HTML5, CSS3, JavaScript
* SQLite
* Bootstrap (as needed)
* jQuery (as needed)

---

## Software Requirements

* Python 3.x
* pip (Python package manager)
* Visual Studio Code (or any code editor)
* Git
* Modern web browser (Chrome, Firefox, Edge)

---

## Repository Structure

```text
FSD-Django-Lab/
│
├── README.md                  # Master README (this file)
├── requirements.txt           # Shared Python dependencies
├── .gitignore                 # Git ignore rules
├── setup_guide.md             # Step-by-step setup for fresh systems
├── run_commands.md            # Quick command reference for exams
│
├── Experiment-01/             # Installation of Python, Django and VS Code
│   ├── README.md
│   └── assets/
│
├── Experiment-02/             # Creation of virtual environment, Django project and App
├── Experiment-03/             # Django app displaying current date and time in server
├── Experiment-04/             # Django app displaying date and time four hours ahead and four hours before as an offset of current date and time in server
├── Experiment-05/             # Simple Django app with unordered fruit list and ordered student list
├── Experiment-06/             # Layout template with navigation, footer, Home, About Us, and Contact Us pages
├── Experiment-07/             # Student registration to a course using ManyToMany relationship
├── Experiment-08/             # Admin interface for student-course registration models and data entry through admin forms
├── Experiment-09/             # Project model and ModelForm integrated with student-course registration app
├── Experiment-10/             # Generic class-based views for student list and student detail
├── Experiment-11/             # CSV and PDF generation for Book model using csv module and xhtml2pdf
└── Experiment-12/             # AJAX-based student registration without page refresh
```

---

## One-Time Setup (on any system)

Follow these steps to set up the lab environment on a fresh machine.

### 1. Clone the Repository

```bash
git clone <your-repository-url>
cd FSD-Django-Lab
```

### 2. Create a Virtual Environment

```bash
python -m venv venv
```

### 3. Activate the Virtual Environment

**Windows**

```bash
venv\Scripts\activate
```

**Linux / macOS**

```bash
source venv/bin/activate
```

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

### 5. Verify Django Installation

```bash
python -m django --version
```

---

## Experiment List

| #  | Experiment Name                                                                                                                                                                                                                          |
| -- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 01 | Installation of Python, Django and Visual Studio Code                                                                                                                                                                                    |
| 02 | Creation of virtual environment, Django project and App                                                                                                                                                                                  |
| 03 | Develop a Django app that displays current date and time in server                                                                                                                                                                       |
| 04 | Develop a Django app that displays date and time four hours ahead and four hours before as an offset of current date and time in server                                                                                                  |
| 05 | Develop a simple Django app that displays an unordered list of fruits and ordered list of selected students for an event                                                                                                                 |
| 06 | Develop a layout.html with a suitable header (containing navigation menu) and footer with copyright and developer information. Inherit this layout.html and create 3 additional pages: Contact Us, About Us and Home page of any website |
| 07 | Develop a Django app that performs student registration to a course and displays students registered for a selected course                                                                                                               |
| 08 | Register admin interfaces for student and course models, perform migrations, and illustrate data entry through admin forms                                                                                                               |
| 09 | Develop a Model form for student project details using a Project model with topic, languages used and duration                                                                                                                           |
| 10 | Create generic class views to display student list and student detail for the student enrolment app                                                                                                                                      |
| 11 | Develop a Django app that performs CSV and PDF generation for models                                                                                                                                                                     |
| 12 | Develop a registration page for student enrolment without page refresh using AJAX                                                                                                                                                        |

---

## How to Run an Experiment

1. Navigate to the required experiment folder (for example, `Experiment-02/`)
2. Read that experiment’s `README.md` for experiment-specific instructions
3. If the experiment contains a Django project snapshot, enter the `project_files/` directory
4. Ensure the virtual environment is activated
5. Run migrations if needed:

   ```bash
   python manage.py migrate
   ```
6. Start the development server:

   ```bash
   python manage.py runserver
   ```
7. Open `http://127.0.0.1:8000/` in your browser

---

## Notes for Lab Exam / Viva

* Every experiment is kept in a separate folder with its own README
* Each experiment README includes aim, prerequisites, run instructions, and expected output
* Later experiments may build on earlier ones; standalone snapshots are provided where needed
* The repository is organized so that an examiner can open a single experiment folder and understand it independently
* For lab PCs missing packages, run `pip install -r requirements.txt` from the repo root
* See `setup_guide.md` for fresh system setup
* See `run_commands.md` for a quick command reference

---

## Current Status

* **Experiment-01** – Added (environment setup and installation guide)
* **Experiment-02** – Added (virtual environment, Django project and app creation)
* **Experiment-03** – Added (Django app displaying current date and time)
* **Experiment-04** – Added (Django app displaying date/time offsets of four hours ahead and before)
* **Experiment-05** – Added (Django app displaying unordered fruit list and ordered student list)
* **Experiment-06** – Added (Django app using a base layout template with navigation and footer, plus Home, About Us, and Contact Us pages)
* **Experiment-07** – Added (Django app for student registration to courses using ManyToMany relationship and displaying registered students per course)
* **Experiment-08** – Added (Django admin interface for Course and Student models, with migrations and data entry through admin forms)
* **Experiment-09** – Added (Project model, ProjectForm, and project registration integrated with the student-course registration app)
* **Experiment-10** – Added (Generic class-based views for student list and student detail in the student enrolment app)
* **Experiment-11** – Added (CSV and PDF generation for Book model using csv module and xhtml2pdf)
* **Experiment-12** – Added (AJAX-based student registration without page refresh)

---

## License

This repository is maintained for academic purposes under the **22CSL67** course curriculum.
