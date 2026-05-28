# 🌍 Travela — Travel & Tour Booking Platform

A full-stack travel booking website built with **Django** (backend) and **HTML/CSS/JS** (frontend), ready for deployment on **Render**.

---

## 📁 Project Structure

```
travela-project/
├── backend/                    # Django Backend
│   ├── MiProject/              # Django project settings
│   │   ├── settings.py         # Main configuration
│   │   ├── urls.py             # Root URL routing
│   │   ├── wsgi.py             # WSGI entry point
│   │   └── asgi.py             # ASGI entry point
│   ├── App2/                   # Main Django app
│   │   ├── models.py           # Database models
│   │   ├── views.py            # View functions
│   │   ├── urls.py             # App URL routing
│   │   ├── forms.py            # Form definitions
│   │   ├── admin.py            # Admin panel config
│   │   └── migrations/         # Database migrations
│   ├── manage.py               # Django CLI
│   ├── requirements.txt        # Python dependencies
│   ├── build.sh                # Render build script
│   └── .env.example            # Environment variable template
├── frontend/                   # Frontend Assets
│   ├── static/                 # Static files
│   │   ├── css/                # Stylesheets
│   │   ├── js/                 # JavaScript
│   │   ├── img/                # Images
│   │   ├── lib/                # Third-party libraries
│   │   └── scss/               # SCSS source files
│   └── template/               # Django HTML templates
│       ├── base.html           # Base template
│       ├── index.html          # Homepage
│       ├── about.html          # About page
│       ├── booking.html        # Booking form
│       ├── contact.html        # Contact form
│       ├── destination.html    # Destinations listing
│       ├── packages.html       # Tour packages
│       └── ...                 # Other pages
├── render.yaml                 # Render deployment blueprint
├── .gitignore
└── README.md
```

---

## 🚀 Quick Start (Local Development)

### Prerequisites
- Python 3.10+
- pip

### 1. Clone the repository
```bash
git clone https://github.com/MohitBharambe01/travela-project.git
cd travela-project
```

### 2. Create a virtual environment
```bash
python -m venv venv

# Windows
venv\Scripts\activate

# macOS/Linux
source venv/bin/activate
```

### 3. Install dependencies
```bash
cd backend
pip install -r requirements.txt
```

### 4. Set up environment variables
```bash
cp .env.example .env
# Edit .env with your settings (optional for local dev)
```

### 5. Run migrations
```bash
python manage.py migrate
```

### 6. Create a superuser (for admin panel)
```bash
python manage.py createsuperuser
```

### 7. Run the development server
```bash
python manage.py runserver
```

Visit [http://localhost:8000](http://localhost:8000) to see the app.  
Admin panel: [http://localhost:8000/admin/](http://localhost:8000/admin/)

---

## 🌐 Deploy to Render

### Option 1: Blueprint (Recommended)

1. Push your code to GitHub
2. Go to [Render Dashboard](https://dashboard.render.com/)
3. Click **"New"** → **"Blueprint"**
4. Connect your GitHub repository
5. Render will auto-detect `render.yaml` and set up:
   - ✅ Django Web Service (with Gunicorn)
   - ✅ PostgreSQL Database (free tier)
   - ✅ Auto-generated SECRET_KEY
   - ✅ Static files via WhiteNoise

### Option 2: Manual Setup

1. Create a **Web Service** on Render
2. Set these values:
   - **Root Directory**: `backend`
   - **Build Command**: `./build.sh`
   - **Start Command**: `gunicorn MiProject.wsgi:application --bind 0.0.0.0:$PORT`
3. Add environment variables:
   - `SECRET_KEY` — generate a random key
   - `DEBUG` — `False`
   - `DATABASE_URL` — your PostgreSQL connection string
   - `ALLOWED_HOSTS` — `.onrender.com`

---

## 🔑 Environment Variables

| Variable | Description | Default |
|----------|-------------|---------|
| `SECRET_KEY` | Django secret key | Insecure default (dev only) |
| `DEBUG` | Enable debug mode | `True` |
| `ALLOWED_HOSTS` | Comma-separated hostnames | `localhost,127.0.0.1` |
| `DATABASE_URL` | PostgreSQL connection URL | SQLite (local) |

---

## 🛠️ Tech Stack

- **Backend**: Django 5.2, Gunicorn, WhiteNoise
- **Database**: SQLite (dev) / PostgreSQL (production)
- **Frontend**: HTML5, CSS3, Bootstrap 5, JavaScript
- **Deployment**: Render (Blueprint)

---

## 📄 License

This project is for educational purposes.
