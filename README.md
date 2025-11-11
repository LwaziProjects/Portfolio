# Lwazi Knowledge Gumede - Personal Portfolio Website

A professional portfolio website built with Django showcasing the qualifications, experience, projects, and skills of Lwazi Knowledge Gumede, an ECSA Candidate Engineer with a BSc (Honours) in Computer Engineering.

## Features

- **Home Page**: Welcome page with professional summary and quick links
- **About Page**: Detailed bio with areas of expertise and technical skills
- **Experience Page**: Professional work history at Transnet with detailed achievements
- **Projects Page**: Showcase of key projects including:
  - Authentication and Key Management System
  - IoT Smart Meter System
  - Blockchain Invoice Discounting Platform
- **Qualifications Page**: Educational background and academic achievements
- **Contact Page**: Contact information and functional message form with email notifications
- **Email Notifications**: Automatic email alerts when contact form is submitted
- **Responsive Design**: Bootstrap-based responsive layout for all devices
- **Modern UI**: Professional styling with smooth animations and transitions

## Technology Stack

- **Backend**: Django 4.2+
- **Frontend**: HTML5, CSS3, JavaScript
- **Styling**: Bootstrap 5.3
- **Icons**: Bootstrap Icons
- **Database**: SQLite (development)
- **Python**: 3.8+

## Project Structure

```
portfolio_website/
│
├── portfolio/                  # Main project configuration
│   ├── __init__.py
│   ├── settings.py            # Django settings
│   ├── urls.py                # Root URL configuration
│   ├── wsgi.py               # WSGI configuration
│   └── asgi.py               # ASGI configuration
│
├── main/                      # Main application
│   ├── migrations/           # Database migrations
│   ├── static/               # Static files
│   │   └── css/
│   │       └── style.css     # Custom CSS
│   ├── templates/            # HTML templates
│   │   └── main/
│   │       ├── base.html     # Base template
│   │       ├── home.html     # Home page
│   │       ├── about.html    # About page
│   │       ├── experience.html  # Experience page
│   │       ├── projects.html    # Projects page
│   │       ├── qualifications.html  # Qualifications page
│   │       └── contact.html     # Contact page
│   ├── __init__.py
│   ├── admin.py              # Admin configuration
│   ├── apps.py               # App configuration
│   ├── models.py             # Database models
│   ├── views.py              # View functions
│   ├── urls.py               # App URL patterns
│   ├── forms.py              # Django forms
│   └── tests.py              # Test cases
│
├── manage.py                 # Django management script
├── requirements.txt          # Python dependencies
├── README.md                 # This file
└── db.sqlite3               # SQLite database (created after setup)
```

## Installation & Setup

### Prerequisites

- Python 3.8 or higher
- pip (Python package installer)
- Virtual environment (recommended)

### Step 1: Clone or Navigate to the Project Directory

```powershell
cd c:\Users\0174988\Documents\usefulstuff\MyResume\portfolio_website
```

### Step 2: Create a Virtual Environment (Recommended)

```powershell
python -m venv venv
```

### Step 3: Activate the Virtual Environment

**Windows PowerShell:**
```powershell
.\venv\Scripts\Activate.ps1
```

**Windows Command Prompt:**
```cmd
venv\Scripts\activate.bat
```

### Step 4: Install Dependencies

```powershell
pip install -r requirements.txt
```

### Step 5: Run Database Migrations

```powershell
python manage.py makemigrations
python manage.py migrate
```

### Step 6: Create a Superuser (Optional - for Admin Access)

```powershell
python manage.py createsuperuser
```

Follow the prompts to create an admin account.

### Step 7: Collect Static Files (Production)

For production deployment:
```powershell
python manage.py collectstatic
```

### Step 8: Set Up Email Notifications (Optional but Recommended)

To receive email notifications when someone submits the contact form:

**Quick Setup:**
```powershell
.\setup_email.ps1
```

**Manual Setup:**
1. See detailed instructions in `EMAIL_SETUP.md`
2. Create `.env` file with your Gmail App Password
3. Test with: `python test_email.py`

### Step 9: Run the Development Server

```powershell
python manage.py runserver
```

The website will be available at: **http://127.0.0.1:8000/**

### Step 10: Access the Admin Panel (Optional)

If you created a superuser, access the admin panel at: **http://127.0.0.1:8000/admin/**

## Usage

### Viewing the Website

1. Start the development server (Step 8 above)
2. Open your web browser
3. Navigate to `http://127.0.0.1:8000/`
4. Use the navigation bar to explore different sections

### Managing Contact Messages

1. Access the admin panel at `http://127.0.0.1:8000/admin/`
2. Log in with your superuser credentials
3. Navigate to "Contact Messages" to view submissions from the contact form

## Configuration

### Security Settings

The current configuration is set for **development use**. For production deployment, update the following in `portfolio/settings.py`:

```python
# SECURITY WARNING: change this in production!
SECRET_KEY = 'your-secure-secret-key-here'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['your-domain.com', 'www.your-domain.com']

# Enable HTTPS security
CSRF_COOKIE_SECURE = True
SESSION_COOKIE_SECURE = True
```

### Database Configuration

For production, consider using PostgreSQL or MySQL instead of SQLite. Update the `DATABASES` setting in `portfolio/settings.py`:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'your_database_name',
        'USER': 'your_database_user',
        'PASSWORD': 'your_password',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```

## Contact Information

**Lwazi Knowledge Gumede**

- **Location**: Johannesburg, Braamfontein, South Africa
- **Phone**: +27 76 935 2103 / +27 65 711 1226
- **Email**: lwazig28@gmail.com
- **Status**: ECSA Candidate Engineer
- **Education**: BSc (Honours) Computer Engineering, University of KwaZulu-Natal

## Features Overview

### Contact Form
- Secure form submission with CSRF protection
- Email validation
- Success/error message feedback
- Data stored in database for easy management

### Responsive Design
- Mobile-first approach
- Optimized for all screen sizes
- Touch-friendly navigation

### Professional Presentation
- Clean, modern design
- Intuitive navigation
- Fast loading times
- Accessibility considerations

## Troubleshooting

### Port Already in Use
If port 8000 is already in use, run the server on a different port:
```powershell
python manage.py runserver 8080
```

### Static Files Not Loading
Make sure you're in development mode (DEBUG=True) or run:
```powershell
python manage.py collectstatic
```

### Database Errors
Delete `db.sqlite3` and run migrations again:
```powershell
python manage.py migrate
```

## Development

### Running Tests
```powershell
python manage.py test
```

### Creating New Migrations
After modifying models:
```powershell
python manage.py makemigrations
python manage.py migrate
```

## License

This is a personal portfolio website. All rights reserved by Lwazi Knowledge Gumede.

## Support

For questions or support, please contact via email: lwazig28@gmail.com

---

**Built with Django 4.2 | Bootstrap 5.3 | Python 3.8+**

**Last Updated**: November 2025
