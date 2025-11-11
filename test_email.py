# Test Email Configuration
# Run this to test if email sending works

import os
import sys
import django

# Setup Django

django.setup()

from django.core.mail import send_mail
from django.conf import settings

print("=" * 60)
print("TESTING EMAIL CONFIGURATION")
print("=" * 60)
print(f"\nEmail Settings:")
print(f"  Backend: {settings.EMAIL_BACKEND}")
print(f"  Host: {settings.EMAIL_HOST}")
print(f"  Port: {settings.EMAIL_PORT}")
print(f"  TLS: {settings.EMAIL_USE_TLS}")
print(f"  From: {settings.EMAIL_HOST_USER}")
print(f"  Password Set: {'Yes' if settings.EMAIL_HOST_PASSWORD else 'No (REQUIRED!)'}")
print(f"  Admin Email: {settings.ADMIN_EMAIL}")

if not settings.EMAIL_HOST_PASSWORD:
    print("\n❌ ERROR: EMAIL_HOST_PASSWORD is not set!")
    print("\nPlease:")
    print("1. Create a .env file in the project root")
    print("2. Add: EMAIL_HOST_PASSWORD=your_app_password_here")
    print("3. See EMAIL_SETUP.md for instructions")
    sys.exit(1)

print("\n" + "=" * 60)
print("SENDING TEST EMAIL...")
print("=" * 60)

try:
    send_mail(
        subject='Test Email from Portfolio Website',
        message='This is a test email. If you receive this, your email configuration is working correctly!',
        from_email=settings.DEFAULT_FROM_EMAIL,
        recipient_list=[settings.ADMIN_EMAIL],
        fail_silently=False,
    )
    print("\n✅ SUCCESS! Test email sent!")
    print(f"   Check your inbox at: {settings.ADMIN_EMAIL}")
    print("   (Don't forget to check spam folder)")
    
except Exception as e:
    print(f"\n❌ ERROR: Failed to send email")
    print(f"   Error: {str(e)}")
    print("\nCommon issues:")
    print("  - Incorrect App Password")
    print("  - 2-Step Verification not enabled on Gmail")
    print("  - Internet connection issues")
    print("\nSee EMAIL_SETUP.md for detailed setup instructions")
    sys.exit(1)

print("\n" + "=" * 60)
