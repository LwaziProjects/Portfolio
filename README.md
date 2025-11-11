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
cd c:\\yourpath
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
3. Configure email settings in Django admin

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

## Deployment

### Deploying to PythonAnywhere

#### Quick Start

1. **Create a PythonAnywhere Account**
   - Go to [https://www.pythonanywhere.com](https://www.pythonanywhere.com)
   - Sign up for a free account
   - Verify your email address

2. **Open a Bash Console**
   - From PythonAnywhere dashboard, click "Consoles"
   - Start a new "Bash" console

3. **Clone Your Repository**
   ```bash
   git clone https://github.com/LwaziProjects/Portfolio.git
   cd Portfolio
   ```

4. **Create Virtual Environment**
   ```bash
   mkvirtualenv portfolio-env --python=/usr/bin/python3.10
   workon portfolio-env
   pip install -r requirements.txt
   ```

5. **Configure Django**
   ```bash
   python manage.py collectstatic --noinput
   python manage.py migrate
   python manage.py createsuperuser
   ```

#### Setting Up the Web App

1. **Create a New Web App**
   - Go to "Web" tab in PythonAnywhere dashboard
   - Click "Add a new web app"
   - Choose "Manual configuration"
   - Select Python 3.10

2. **Configure WSGI File**
   - In the "Web" tab, click on the WSGI configuration file link
   - Replace the contents with:
   ```python
   import os
   import sys

   # Add your project directory to the sys.path
   path = '/home/stephusband/Portfolio'
   if path not in sys.path:
       sys.path.append(path)

   # Set environment variable to tell Django where your settings module is
   os.environ['DJANGO_SETTINGS_MODULE'] = 'portfolio.settings'

   # Activate your virtual environment
   activate_this = '/home/stephusband/.virtualenvs/portfolio-env/bin/activate_this.py'
   with open(activate_this) as file_:
       exec(file_.read(), dict(__file__=activate_this))

   # Import Django's WSGI handler
   from django.core.wsgi import get_wsgi_application
   application = get_wsgi_application()
   ```
   - **Important**: Replace `stephusband` with your PythonAnywhere username

3. **Configure Virtual Environment**
   - In the "Web" tab, scroll to "Virtualenv" section
   - Enter the path: `/home/yourusername/.virtualenvs/portfolio-env`
   - Replace `yourusername` with your actual PythonAnywhere username

4. **Configure Static Files**
   - In the "Web" tab, scroll to "Static files" section
   - Add a new mapping:
     - URL: `/static/`
     - Directory: `/home/yourusername/Portfolio/staticfiles`
   - Add another mapping:
     - URL: `/media/`
     - Directory: `/home/yourusername/Portfolio/main/images`

5. **Update Django Settings**
   - Open `portfolio/settings.py` in the PythonAnywhere editor or bash console
   - Update `ALLOWED_HOSTS`:
   ```python
   ALLOWED_HOSTS = ['yourusername.pythonanywhere.com', 'localhost', '127.0.0.1']
   ```

6. **Reload Web App**
   - Go back to the "Web" tab
   - Click the green "Reload" button
   - Visit your site at: `https://yourusername.pythonanywhere.com`

#### Common Deployment Issues and Solutions

**Issue: "ModuleNotFoundError: No module named 'django'"**
- **Solution**: Activate your virtual environment:
  ```bash
  workon portfolio-env
  pip install -r requirements.txt
  ```

**Issue: "NameError: name 'os' is not defined"**
- **Solution**: Add `import os` at the top of `portfolio/settings.py`

**Issue: WSGI shows "yourusername" placeholder**
- **Solution**: Replace all instances of `yourusername` or `stephusband` with your actual PythonAnywhere username in:
  - WSGI configuration file
  - Virtualenv path
  - Static files paths

**Issue: Static files not loading**
- **Solution**: Run collectstatic and verify paths:
  ```bash
  python manage.py collectstatic --noinput
  ```
  - Check Static files configuration in Web tab

**Issue: Git merge conflicts during pull**
- **Solution**: Stash local changes before pulling:
  ```bash
  git stash
  git pull origin main
  git stash pop
  ```

#### Updating Your Deployed Site

When you make changes to your code:

1. **Commit and Push to GitHub**:
   ```powershell
   git add .
   git commit -m "Your update message"
   git push origin main
   ```

2. **Update on PythonAnywhere**:
   ```bash
   cd ~/Portfolio
   workon portfolio-env
   git pull origin main
   pip install -r requirements.txt
   python manage.py collectstatic --noinput
   python manage.py migrate
   ```

3. **Reload Web App**:
   - Go to "Web" tab
   - Click the green "Reload" button

#### Environment Variables (Optional)

For production, consider using environment variables for sensitive data:

1. Create a `.env` file (don't commit this to Git):
   ```
   SECRET_KEY=your-secret-key-here
   DEBUG=False
   DATABASE_URL=your-database-url
   ```

2. Update `settings.py`:
   ```python
   import os
   from pathlib import Path

   # Load environment variables
   SECRET_KEY = os.environ.get('SECRET_KEY', 'fallback-secret-key')
   DEBUG = os.environ.get('DEBUG', 'False') == 'True'
   ```

3. Set environment variables in PythonAnywhere:
   - Use the "Files" tab to create/edit `.env`
   - Or set in WSGI configuration file

### Deploying to Other Platforms

This Django application can also be deployed to:
- **Heroku**: Use `Procfile` and `gunicorn`
- **Railway**: Direct GitHub integration
- **DigitalOcean**: Using App Platform or Droplets
- **AWS**: Elastic Beanstalk or EC2
- **Azure**: App Service

Refer to each platform's Django deployment documentation for specific instructions.

## License

This is a personal portfolio website. All rights reserved by Lwazi Knowledge Gumede.

## Support

For questions or support, please contact via email: lwazig28@gmail.com

---

**Built with Django 4.2 | Bootstrap 5.3 | Python 3.8+**

**Last Updated**: November 2025
