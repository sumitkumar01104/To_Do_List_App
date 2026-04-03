# 📚 StudyTask — Students Task Manager

A full-stack web app that helps students manage their tasks and subtasks efficiently. Built with a Django REST API backend and a vanilla HTML/CSS/JS frontend.

---

## 🛠️ Tech Stack

| Part | Technology |
|------|-----------|
| Frontend | HTML, CSS, Vanilla JavaScript |
| Backend | Django + Django REST Framework |
| Authentication | Token Authentication |
| Fonts | Google Fonts (Syne, DM Sans) |

---

## ✨ Features

- 🔐 User Registration & Login (Token-based auth)
- ✅ Add, delete, and toggle tasks complete/incomplete
- 📋 Subtasks — create subtasks inside each task
- 📊 Progress bar — tracks subtask completion
- 🔍 Filter tasks — All / Pending / Done
- 📈 Stats panel — Total, Pending, Done count
- 🔔 Toast notifications for all actions
- 💾 Token saved in LocalStorage (stays logged in on reload)

---

## 📁 Project Structure

```
project/
│
├── backend/                  # Django project
│   ├── api/
│   │   ├── models.py         # Task, Subtask models
│   │   ├── serializers.py    # DRF Serializers
│   │   ├── views.py          # API Views
│   │   └── urls.py           # API URL routes
│   ├── settings.py
│   └── urls.py
│
└── frontend/
    └── index.html            # Complete frontend (single file)
```

---

## ⚙️ Backend Setup

### 1. Create a Virtual Environment

```bash
python -m venv venv
source venv/bin/activate        # Linux/Mac
venv\Scripts\activate           # Windows
```

### 2. Install Dependencies

```bash
pip install django djangorestframework
```

### 3. Add to `settings.py`

```python
INSTALLED_APPS = [
    ...
    'rest_framework',
    'rest_framework.authtoken',
    'api',
]

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.TokenAuthentication',
    ],
}
```

### 4. Run Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 5. Start the Server

```bash
python manage.py runserver
```

---

## 🔗 API Endpoints

| Method | URL | Description |
|--------|-----|-------------|
| POST | `/api/auth/register/` | Create a new account |
| POST | `/api/auth/login/` | Login and receive token |
| POST | `/api/auth/logout/` | Logout (deletes token) |
| GET | `/api/tasks/` | Get all tasks |
| POST | `/api/tasks/` | Create a new task |
| PATCH | `/api/tasks/{id}/` | Update a task |
| DELETE | `/api/tasks/{id}/` | Delete a task |
| GET | `/api/tasks/{id}/subtasks/` | Get subtasks |
| POST | `/api/tasks/{id}/subtasks/` | Create a subtask |
| PATCH | `/api/tasks/{id}/subtasks/{sid}/` | Update a subtask |
| DELETE | `/api/tasks/{id}/subtasks/{sid}/` | Delete a subtask |

---

## 🚨 Important — CSRF Fix

`LoginView` and `RegisterView` must have these two lines, otherwise you will get a **403 Forbidden** error on every login attempt:

```python
from rest_framework.permissions import AllowAny

class LoginView(APIView):
    authentication_classes = []       # Removes CSRF enforcement
    permission_classes = [AllowAny]   # Allows public access

class RegisterView(APIView):
    authentication_classes = []       # Removes CSRF enforcement
    permission_classes = [AllowAny]   # Allows public access
```

**Why?** Django REST Framework's default `SessionAuthentication` enforces CSRF on every POST request. Since login and register endpoints are public and use Token auth, they don't need CSRF protection.

---

## 🌐 Frontend Setup

Open `index.html` and update the API base URL to match your backend:

```javascript
const API       = 'http://127.0.0.1:8000/api';
const URL_LOGIN = `${API}/auth/login/`;
const URL_REG   = `${API}/auth/register/`;
const URL_TASKS = `${API}/tasks/`;
```

Just open `index.html` in your browser — no build step required!

---

## 🐛 Common Errors & Fixes

| Error | Cause | Fix |
|-------|-------|-----|
| `403 Forbidden` on login | CSRF enforcement | Add `authentication_classes = []` to Login/Register views |
| `401 Unauthorized` on tasks | Missing token | Log in first — token is saved automatically |
| `404 Not Found` on favicon | No favicon file | Already handled with `<link rel="icon" href="data:,">` ✅ |
| Tracking Prevention (Bootstrap) | Browser privacy feature | Harmless — the app uses custom CSS, not Bootstrap |
| `ERR_NETWORK_CHANGED` (Fonts) | Network interruption | Reload the page |

---

## 👨‍💻 Developer Notes

- Bootstrap CSS is linked in the HTML but not actually used — it can safely be removed
- The auth token is stored in `localStorage` so users remain logged in after page reload
- Pressing `Enter` on the login/register form submits it
- Pressing `Enter` in the subtask input adds a chip

---

## 📄 License

MIT — Free to use and modify.
## 📸 Screenshots

### Register Page
![Register](screenshots/Register.png)

### Login Page
![Login](screenshots/Login.png)


### Dashboard
![Dashboard](screenshots/Dashboard.png)