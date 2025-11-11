## Quick orientation for AI coding agents

This repository is a small Django-based personal portfolio site. The goal of this document is to give an AI code assistant the essential, actionable context to be productive immediately.

- Project root: `manage.py`, Django project package: `portfolio/` (settings, urls, wsgi/asgi)
- Main app: `main/` — contains models, forms, views, urls, templates and static assets

Key things to know (big picture)
- The app serves primarily static/content pages (home, about, experience, projects, qualifications, contact). See `main/urls.py` and `main/views.py` for routing and page logic.
- Contact submissions are persisted using the `ContactMessage` model in `main/models.py`. The contact page uses a `ModelForm` in `main/forms.py` and view logic in `main/views.py`.
- A PDF resume is generated on-the-fly in `main/views.py:download_resume` using ReportLab. That function builds a PDF and returns an HttpResponse with `application/pdf`.
- Email sending code is present but commented/disabled in `main/views.py`. Production email credentials are expected to come from environment (see `portfolio/settings.py` using `decouple.config`).

Developer workflows & commands (local / dev focus)
- Virtualenv: recommended. On Windows PowerShell:
  - `python -m venv venv`
  - `.\benv\\Scripts\\Activate.ps1` (adjust if you named it `venv`)
- Install deps: `pip install -r requirements.txt` (requirements include Django, python-decouple, reportlab)
- Migrations & DB:
  - `python manage.py makemigrations`
  - `python manage.py migrate`
- Create admin: `python manage.py createsuperuser`
- Run server (dev): `python manage.py runserver` (port can be changed with `runserver 8080`)
- Tests: `python manage.py test`
- Static files (production): `python manage.py collectstatic` — `STATIC_ROOT` is set to `BASE_DIR / 'staticfiles'` in `portfolio/settings.py`.

Project-specific conventions & patterns (important to reuse)
- Templates live under `main/templates/main/` and expect an `active_page` context variable to mark the active navbar item (see `main/views.py` where each view passes `"active_page"`).
- Navigation uses `url` names declared in `main/urls.py` (e.g., `home`, `contact`, `download_resume`) — prefer reversing by name when generating links.
- Contact form pattern: the `ContactForm` is a `ModelForm` for `ContactMessage`; the view saves via `form.save()` and redirects to `contact` with Django messages for feedback.
- PDF resume: complex but self-contained in `main/views.py`. If modifying layout, prefer editing styles/flowables there rather than re-implementing PDF generation elsewhere.
- Settings: `portfolio/settings.py` uses `decouple.config` for secrets — don't hard-code secrets when changing settings; follow the existing pattern.

Integration points & external dependencies
- ReportLab (PDF generation): `requirements.txt` includes `reportlab`. The code directly imports ReportLab classes in `main/views.py`.
- Email (SMTP): `portfolio/settings.py` is configured for Gmail SMTP with `EMAIL_HOST_PASSWORD` loaded via `decouple`. Email sending is disabled on the deployed site and the send-mail block in `main/views.py` is commented.
- Deployment notes: README contains a full PythonAnywhere deployment walkthrough (WSGI file, virtualenv path, static mappings). Use that as the canonical deployment steps.

Common pitfalls observed (from reading the code)
- `SECRET_KEY` and `DEBUG` are development-defaults in `portfolio/settings.py`. Treat `ALLOWED_HOSTS = ['*']` as insecure and avoid changing it in PRs without a clear migration plan.
- Email may fail locally if `EMAIL_HOST_PASSWORD` is missing; tests or local runs should not rely on outgoing email.
- `download_resume` uses fixed start dates (example: April 2025) to compute durations — be careful when changing logic that assumes those constants.

Files to open first when working on a feature or fix
- `main/views.py` — primary app logic (pages, contact handling, PDF generation)
- `main/models.py` / `main/forms.py` — contact persistence and form requirements
- `main/urls.py` — route names to use in templates and tests
- `main/templates/main/base.html` — base layout; uses `active_page` and loads `{% static 'css/style.css' %}`
- `portfolio/settings.py` — deployment, email, static root and installed apps
- `README.md` — has developer/setup and PythonAnywhere deploy notes; reflects repository-specific commands

If you change behavior, make these minimal CI-friendly checks
- Run `python manage.py makemigrations && python manage.py migrate` to ensure models are consistent
- Run `python manage.py test` (project has `main/tests.py`) — include a small unit test if you add page logic
- Smoke test the PDF endpoint: `GET /download-resume/` should return `Content-Type: application/pdf` (a small test can validate response headers)

When in doubt
- Follow existing patterns in `main/` rather than introducing parallel implementations (e.g., use the `ContactMessage` model rather than adding a new storage flow).
- Reference the README's deployment and environment sections before editing `settings.py` or deploy-related files.

If anything in this file is unclear or you'd like additional examples (unit test snippets, common refactor targets, or a short checklist for PDF formatting changes), tell me which area to expand.
