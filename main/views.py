from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from .forms import ContactForm
from datetime import datetime


def home(request):
    """Home page view"""
    context = {
        'page_title': 'Home',
        'active_page': 'home'
    }
    return render(request, 'main/home.html', context)


def about(request):
    """About page view"""
    context = {
        'page_title': 'About',
        'active_page': 'about'
    }
    return render(request, 'main/about.html', context)


def experience(request):
    """Experience page view"""
    # Calculate duration for current Transnet position
    start_date = datetime(2025, 4, 1)  # April 2025
    current_date = datetime.now()
    
    # Calculate months difference
    months_diff = (current_date.year - start_date.year) * 12 + (current_date.month - start_date.month)
    
    # Format duration string
    if months_diff < 1:
        duration_text = "Less than 1 month"
    elif months_diff == 1:
        duration_text = "1 month"
    else:
        duration_text = f"{months_diff} months"
    
    context = {
        'page_title': 'Experience',
        'active_page': 'experience',
        'current_position_duration': duration_text
    }
    return render(request, 'main/experience.html', context)


def projects(request):
    """Projects page view"""
    context = {
        'page_title': 'Projects',
        'active_page': 'projects'
    }
    return render(request, 'main/projects.html', context)


def qualifications(request):
    """Qualifications page view"""
    context = {
        'page_title': 'Qualifications',
        'active_page': 'qualifications'
    }
    return render(request, 'main/qualifications.html', context)


def contact(request):
    """Contact page view with form handling"""
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Save the contact message
            contact_message = form.save()
            
            # Send email notification to you
            try:
                subject = f"New Contact Form Submission: {contact_message.subject}"
                message = f"""
You have received a new message from your portfolio website!

From: {contact_message.name}
Email: {contact_message.email}
Phone: {contact_message.phone or 'Not provided'}
Subject: {contact_message.subject}

Message:
{contact_message.message}

---
Submitted on: {contact_message.created_at.strftime('%B %d, %Y at %I:%M %p')}
"""
                
                send_mail(
                    subject=subject,
                    message=message,
                    from_email=settings.DEFAULT_FROM_EMAIL,
                    recipient_list=[settings.ADMIN_EMAIL],
                    fail_silently=False,
                )
                messages.success(request, 'Thank you for your message! I will get back to you soon.')
            except Exception as e:
                # Still save the message even if email fails
                messages.success(request, 'Thank you for your message! I will get back to you soon.')
                print(f"Email sending failed: {str(e)}")
            
            return redirect('contact')
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = ContactForm()
    
    context = {
        'page_title': 'Contact',
        'active_page': 'contact',
        'form': form
    }
    return render(request, 'main/contact.html', context)
