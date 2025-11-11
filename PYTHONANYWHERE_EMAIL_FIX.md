# Fix Email Sending on PythonAnywhere

## Problem
PythonAnywhere free accounts have email restrictions. Gmail SMTP may not work directly.

---

## ✅ Solution 1: Use PythonAnywhere's Email Allowlist (Recommended)

### Step 1: Add Gmail to Allowlist (Paid Accounts Only)

If you have a paid PythonAnywhere account:
1. Go to **Account** tab
2. Click **Email** section
3. Add `smtp.gmail.com` to the allowlist

**Note:** Free accounts cannot add custom SMTP servers!

---

## ✅ Solution 2: Use SendGrid (Free - Recommended for Free Accounts)

SendGrid offers a free tier (100 emails/day) that works with PythonAnywhere free accounts.

### Step 1: Sign up for SendGrid

1. Go to https://sendgrid.com
2. Sign up for free account (100 emails/day free)
3. Verify your email address

### Step 2: Create API Key

1. Go to **Settings** → **API Keys**
2. Click **Create API Key**
3. Name it: "PythonAnywhere Portfolio"
4. Select **Full Access** or **Restricted Access** (Mail Send)
5. **Copy the API key** (you'll only see it once!)

### Step 3: Update Django Settings

On PythonAnywhere, edit `portfolio/settings.py`:

```bash
cd ~/Portfolio
nano portfolio/settings.py
```

Replace the email configuration with:

```python
# Email Configuration for SendGrid
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.sendgrid.net'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'apikey'  # This is literal 'apikey', not your username
EMAIL_HOST_PASSWORD = config('SENDGRID_API_KEY', default='')  # Your SendGrid API key
DEFAULT_FROM_EMAIL = 'lwazig28@gmail.com'
ADMIN_EMAIL = 'lwazig28@gmail.com'
```

### Step 4: Create .env File on PythonAnywhere

```bash
cd ~/Portfolio
nano .env
```

Add this line (replace with YOUR actual API key):
```
SENDGRID_API_KEY=SG.your_actual_api_key_here
```

Save: `CTRL+X`, `Y`, `ENTER`

### Step 5: Install python-decouple (if not already)

```bash
cd ~/Portfolio
workon portfolio-env
pip install python-decouple
```

### Step 6: Reload Web App

Go to **Web tab** → Click **Reload**

---

## ✅ Solution 3: Use Mailgun (Alternative)

Mailgun also offers free tier that works with PythonAnywhere.

### Setup:
1. Sign up at https://www.mailgun.com (5,000 emails/month free)
2. Verify your domain or use sandbox domain
3. Get SMTP credentials
4. Update settings.py:

```python
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.mailgun.org'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = config('MAILGUN_SMTP_LOGIN', default='')
EMAIL_HOST_PASSWORD = config('MAILGUN_SMTP_PASSWORD', default='')
DEFAULT_FROM_EMAIL = 'your-email@your-domain.com'
ADMIN_EMAIL = 'lwazig28@gmail.com'
```

---

## ✅ Solution 4: Console Email Backend (Testing Only)

For testing without actual email sending:

```python
# In settings.py - TESTING ONLY
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
```

This prints emails to console instead of sending them.

---

## 🔍 Testing Email Configuration

### Test in PythonAnywhere Bash Console:

```bash
cd ~/Portfolio
workon portfolio-env
python manage.py shell
```

Then run:

```python
from django.core.mail import send_mail

send_mail(
    'Test Email from Portfolio',
    'This is a test email from your portfolio website.',
    'lwazig28@gmail.com',
    ['lwazig28@gmail.com'],
    fail_silently=False,
)
```

If successful, you'll see: `1` (meaning 1 email sent)

If there's an error, it will show you the error message.

---

## 📋 Quick Setup Commands for SendGrid (Recommended)

```bash
# 1. Navigate to project
cd ~/Portfolio

# 2. Activate virtual environment
workon portfolio-env

# 3. Install python-decouple
pip install python-decouple

# 4. Create .env file
nano .env
# Add: SENDGRID_API_KEY=your_key_here
# Save: CTRL+X, Y, ENTER

# 5. Update settings.py
nano portfolio/settings.py
# Update email configuration (see above)
# Save: CTRL+X, Y, ENTER

# 6. Test email
python manage.py shell
# Run test code above

# 7. If test works, reload web app in Web tab
```

---

## 🚫 Why Gmail Doesn't Work on PythonAnywhere Free

PythonAnywhere free accounts can only send emails to:
- Whitelisted servers (none by default on free accounts)
- Services that are pre-approved (SendGrid, Mailgun, etc.)

Gmail's SMTP (`smtp.gmail.com`) is **blocked** on free accounts for security reasons.

---

## ✅ Best Solution Summary

**For PythonAnywhere Free Account:**
1. ✅ **Use SendGrid** (100 emails/day free)
2. ✅ **Use Mailgun** (5,000 emails/month free)

**For PythonAnywhere Paid Account:**
- Add `smtp.gmail.com` to allowlist
- Keep Gmail configuration

---

## 📧 Expected Behavior After Fix

When someone submits your contact form:
1. Form data saves to database
2. Email notification sent to `lwazig28@gmail.com`
3. Success message shown to user
4. You receive email with contact details

---

**Recommended:** Use SendGrid - it's free, reliable, and works perfectly with PythonAnywhere free accounts! 🚀
