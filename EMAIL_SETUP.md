# Email Setup Guide for Portfolio Contact Form

## Overview
Your portfolio website now sends email notifications when someone submits the contact form. You'll receive an email at **lwazig28@gmail.com** with all the details.

---

## Setup Steps

### Step 1: Create a Gmail App Password

Since Google doesn't allow direct password use for security, you need to create an "App Password":

1. **Go to your Google Account**: https://myaccount.google.com/
2. **Enable 2-Step Verification** (if not already enabled):
   - Click on "Security" in the left menu
   - Under "How you sign in to Google", click "2-Step Verification"
   - Follow the prompts to enable it

3. **Create App Password**:
   - Go to: https://myaccount.google.com/apppasswords
   - Or: Google Account → Security → 2-Step Verification → App passwords
   - Select "Mail" as the app
   - Select "Other (Custom name)" as the device
   - Enter: "Portfolio Website"
   - Click "Generate"
   - **Copy the 16-character password** (looks like: xxxx xxxx xxxx xxxx)

### Step 2: Create .env File

1. In your project folder, create a file named `.env` (note the dot at the start):
   ```
   c:\Users\0174988\Documents\usefulstuff\MyResume\portfolio_website\.env
   ```

2. Add this content (replace with your actual app password):
   ```
   EMAIL_HOST_PASSWORD=your_16_character_app_password_here
   ```
   
   Example:
   ```
   EMAIL_HOST_PASSWORD=abcd efgh ijkl mnop
   ```

3. Save the file

### Step 3: Restart Django Server

Stop the current server (CTRL+C) and restart it:
```powershell
Set-Location "c:\Users\0174988\Documents\usefulstuff\MyResume\portfolio_website"
C:/Users/0174988/Documents/usefulstuff/MyResume/.venv/Scripts/python.exe manage.py runserver
```

---

## What You'll Receive

When someone submits the contact form, you'll get an email like this:

**Subject:** New Contact Form Submission: [Their Subject]

**Body:**
```
You have received a new message from your portfolio website!

From: John Doe
Email: john@example.com
Phone: +27 12 345 6789
Subject: Job Opportunity

Message:
Hi Lwazi, I'd like to discuss a potential opportunity...

---
Submitted on: November 11, 2025 at 02:30 PM
```

---

## Testing

After setup, test the contact form:

1. Go to: http://127.0.0.1:8000/contact/
2. Fill in the form
3. Submit
4. Check your email at **lwazig28@gmail.com**

If you don't receive an email:
- Check your spam folder
- Verify the App Password is correct in `.env`
- Make sure you restarted the server
- Check the terminal for error messages

---

## Alternative Free Email Services

If you prefer not to use Gmail, here are alternatives:

### SendGrid (Free tier: 100 emails/day)
```python
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.sendgrid.net'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'apikey'
EMAIL_HOST_PASSWORD = 'your_sendgrid_api_key'
```

### Mailgun (Free tier: 100 emails/day for 3 months)
```python
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.mailgun.org'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'postmaster@your-domain.mailgun.org'
EMAIL_HOST_PASSWORD = 'your_mailgun_password'
```

---

## Security Notes

- ✅ The `.env` file is already added to `.gitignore`
- ✅ Never commit your App Password to version control
- ✅ Keep your `.env` file private
- ✅ The password is stored separately from your code

---

## Troubleshooting

### "SMTPAuthenticationError"
- App Password is incorrect or not set
- Check your `.env` file

### "Connection refused"
- Check your internet connection
- Verify Gmail SMTP settings

### No email received
- Check spam folder
- Verify EMAIL_HOST_USER matches your Gmail
- Check terminal for error messages

### "App Passwords unavailable"
- Make sure 2-Step Verification is enabled first
- Some accounts may need additional verification

---

## Current Configuration

**Email Settings:**
- SMTP Server: Gmail (smtp.gmail.com)
- Port: 587 (TLS)
- Your Email: lwazig28@gmail.com
- Notifications go to: lwazig28@gmail.com

**Features:**
- ✅ Email notification on every form submission
- ✅ Full contact details included
- ✅ Message still saved to database even if email fails
- ✅ User sees success message regardless

---

For questions, refer to the main README.md or Django email documentation:
https://docs.djangoproject.com/en/4.2/topics/email/
