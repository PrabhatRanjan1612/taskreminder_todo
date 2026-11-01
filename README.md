# 📌 Task Reminder & Scheduler Web Application

A clean, responsive, and lightweight web application built with **Python**, **Django**, and **SQLite** to help users schedule daily tasks, monitor deadlines, track task completion statuses, and stay productive.

---

## 🚀 Features

- **User Authentication & Session Management**:
  - Secure user registration with input validation.
  - Login system backed by Django sessions to keep individual user data private.
  - Password recovery / reset functionality.
- **Task Management (Full CRUD)**:
  - **Create**: Add new tasks with title, description, and due date.
  - **Read**: View all tasks belonging to the logged-in user in a clean tabular view.
  - **Update**: Edit task details, deadlines, or toggle task completion status (Pending/Completed) with one click.
  - **Delete**: Remove completed or obsolete tasks instantly.
- **Task Detail Inspection**: Deep-dive view for full descriptions and scheduled deadlines.
- **Interactive UI**:
  - Responsive layout designed with modern HTML5, CSS3, and Font Awesome 6.7 icons.
  - Instant client-side alerts for operations (Task added, updated, login errors, etc.).

---

## 🛠️ Tech Stack

| Layer | Technology |
|---|---|
| **Backend** | Python 3.11+ / 3.14, Django 5.1 |
| **Frontend** | HTML5, CSS3, Font Awesome 6.7, Django Template Language (DTL) |
| **Database** | SQLite3 (`db.sqlite3`) |
| **Architecture** | Model-View-Template (MVT) |

---

## 📁 Project Structure

```text
taskreminder/
│
├── manage.py                   # Django CLI management script
├── db.sqlite3                  # SQLite relational database
│
├── taskreminder/               # Main project configuration
│   ├── settings.py             # App settings, DB config, installed apps
│   ├── urls.py                 # Root URL router
│   ├── wsgi.py                 # WSGI web server gateway
│   └── asgi.py                 # ASGI configuration
│
└── todo/                       # Application module
    ├── models.py               # Database models ('user' and 'Taskadd')
    ├── views.py                # Business logic, auth & CRUD controllers
    ├── urls.py                 # App-specific URL routes
    ├── admin.py                # Django Admin registration
    ├── migrations/             # Database migrations
    ├── static/todo/            # CSS files, styles, icons, and logo
    └── templates/todo/         # HTML templates (Login, Register, Tasks, etc.)
```

---

## ⚙️ Installation & Setup

### Prerequisites
Make sure you have **Python (3.10+)** and **pip** installed on your system.

### 1. Clone the Repository
```bash
git clone https://github.com/PrabhatRanjan1612/taskreminder.git
cd taskreminder
```

### 2. Install Dependencies
Install Django (if not already installed):
```bash
pip install django
```

### 3. Run Migrations
Apply database migrations to set up the SQLite schema:
```bash
python manage.py makemigrations
python manage.py migrate
```

### 4. Start Development Server
```bash
python manage.py runserver
```

### 5. Open in Browser
Visit the app at:
```text
http://127.0.0.1:8000/puproject/
```

> **Note**: The application routes are mapped under the `/puproject/` prefix in `taskreminder/urls.py`.

---

## 🗄️ Database Schema

The database consists of two core relational entities:

### 1. `user` Table
| Column | Type | Details |
|---|---|---|
| `id` | Integer | Primary Key (Auto-increment) |
| `name` | CharField(50) | Full name |
| `username` | CharField(50) | Unique username |
| `password` | CharField(50) | Account password |

### 2. `Taskadd` Table
| Column | Type | Details |
|---|---|---|
| `id` | Integer | Primary Key (Auto-increment) |
| `title` | CharField(150) | Task headline |
| `description` | TextField | Detailed notes/instructions |
| `due_date` | DateField | Deadline |
| `completed` | BooleanField | Status flag (`False` = Pending, `True` = Done) |
| `created_at` | DateTimeField | Timestamp of creation |
| `user_task` | ForeignKey (`user`) | Associated user account (CASCADE on delete) |

---

## 📊 Application Data Flow

```text
User Input (Form/Click)
       │
       ▼
Django URL Dispatcher (urls.py)
       │
       ▼
View Controller (views.py) ◄──► Session Verification (request.session)
       │
       ▼
Django ORM Queries (INSERT, FILTER, UPDATE, DELETE)
       │
       ▼
SQLite Database (db.sqlite3)
       │
       ▼
Rendered HTML Template + Client Alert
```

---

## 🔮 Future Roadmap

- [ ] Automated Email and SMS push reminders using Celery and Redis.
- [ ] Priority tags (High, Medium, Low) and custom category labels.
- [ ] Drag-and-drop Kanban view (To-Do, In-Progress, Completed).
- [ ] Progressive Web App (PWA) support for offline usage.

---

## 👨‍💻 Author

- **Prabhat Ranjan**
- GitHub: [@PrabhatRanjan1612](https://github.com/PrabhatRanjan1612)

---

## 📄 License

This project is licensed under the MIT License - feel free to use and modify it for academic or personal projects.
