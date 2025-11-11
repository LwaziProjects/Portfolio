from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from django.http import HttpResponse
from .forms import ContactForm
from datetime import datetime
from reportlab.lib.pagesizes import letter, A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak
from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_JUSTIFY
from io import BytesIO


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
            
            # NOTE: Email sending is disabled on PythonAnywhere free tier
            # PythonAnywhere free accounts block Gmail SMTP for security reasons.
            # To enable email notifications, upgrade to paid account or use SendGrid/Mailgun.
            # See PYTHONANYWHERE_EMAIL_FIX.md for detailed setup instructions.
            
            # Email notification code (DISABLED)
            # try:
            #     subject = f"New Contact Form Submission: {contact_message.subject}"
            #     message = f"""
            # You have received a new message from your portfolio website!
            # 
            # From: {contact_message.name}
            # Email: {contact_message.email}
            # Phone: {contact_message.phone or 'Not provided'}
            # Subject: {contact_message.subject}
            # 
            # Message:
            # {contact_message.message}
            # 
            # ---
            # Submitted on: {contact_message.created_at.strftime('%B %d, %Y at %I:%M %p')}
            # """
            #     
            #     send_mail(
            #         subject=subject,
            #         message=message,
            #         from_email=settings.DEFAULT_FROM_EMAIL,
            #         recipient_list=[settings.ADMIN_EMAIL],
            #         fail_silently=False,
            #     )
            # except Exception as e:
            #     print(f"Email sending failed: {str(e)}")
            
            messages.success(request, 'Thank you for your message! Your submission has been saved and I will review it in the admin panel.')
            
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


def download_resume(request):
    """Generate and download resume as PDF"""
    # Create a buffer to receive PDF data
    buffer = BytesIO()
    
    # Create the PDF object using the buffer as its "file"
    doc = SimpleDocTemplate(buffer, pagesize=A4, topMargin=0.5*inch, bottomMargin=0.5*inch)
    
    # Container for the 'Flowable' objects
    elements = []
    
    # Define styles
    styles = getSampleStyleSheet()
    
    # Custom styles
    title_style = ParagraphStyle(
        'CustomTitle',
        parent=styles['Heading1'],
        fontSize=24,
        textColor=colors.HexColor('#0d6efd'),
        spaceAfter=6,
        alignment=TA_CENTER,
        fontName='Helvetica-Bold'
    )
    
    subtitle_style = ParagraphStyle(
        'CustomSubtitle',
        parent=styles['Normal'],
        fontSize=12,
        textColor=colors.grey,
        spaceAfter=12,
        alignment=TA_CENTER
    )
    
    heading_style = ParagraphStyle(
        'CustomHeading',
        parent=styles['Heading2'],
        fontSize=14,
        textColor=colors.HexColor('#0d6efd'),
        spaceAfter=10,
        spaceBefore=12,
        fontName='Helvetica-Bold'
    )
    
    body_style = ParagraphStyle(
        'CustomBody',
        parent=styles['Normal'],
        fontSize=10,
        spaceAfter=6,
        alignment=TA_JUSTIFY
    )
    
    # Header
    elements.append(Paragraph("LWAZI KNOWLEDGE GUMEDE", title_style))
    elements.append(Paragraph("ECSA Candidate Engineer | BSc (Honours) Computer Engineering", subtitle_style))
    
    # Contact Information
    contact_info = [
        ["Email:", "lwazig28@gmail.com", "Phone:", "+27 76 935 2103"],
        ["Location:", "Johannesburg, South Africa", "Phone:", "+27 65 711 1226"]
    ]
    contact_table = Table(contact_info, colWidths=[1*inch, 2.2*inch, 1*inch, 1.5*inch])
    contact_table.setStyle(TableStyle([
        ('FONTSIZE', (0, 0), (-1, -1), 9),
        ('TEXTCOLOR', (0, 0), (0, -1), colors.grey),
        ('TEXTCOLOR', (2, 0), (2, -1), colors.grey),
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
    ]))
    elements.append(contact_table)
    elements.append(Spacer(1, 0.2*inch))
    
    # Professional Summary
    elements.append(Paragraph("PROFESSIONAL SUMMARY", heading_style))
    summary_text = """Results-driven ECSA Candidate Engineer with a BSc (Honours) in Computer Engineering, 
    specializing in software development, system automation, and hardware integration. Proficient in Python, 
    C++, Java, JavaScript, and modern frameworks including React, Django, and Flask. Experienced in developing 
    innovative solutions for rail transport systems, with expertise in IoT, blockchain technology, and embedded systems."""
    elements.append(Paragraph(summary_text, body_style))
    elements.append(Spacer(1, 0.15*inch))
    
    # Technical Skills
    elements.append(Paragraph("TECHNICAL SKILLS", heading_style))
    skills_data = [
        ["Programming Languages:", "Python, C++, Java, JavaScript, C#, Assembly Language"],
        ["Web Development:", "React, Django, Flask, HTML5, CSS3, Bootstrap, RESTful APIs"],
        ["Databases:", "MySQL, PostgreSQL, SQLite, MongoDB"],
        ["Tools & Technologies:", "Git, Docker, Linux, Arduino, Raspberry Pi, MATLAB, Simulink"],
        ["Specialized Skills:", "IoT Systems, Blockchain Development, Embedded Systems, System Automation"]
    ]
    skills_table = Table(skills_data, colWidths=[1.8*inch, 4.8*inch])
    skills_table.setStyle(TableStyle([
        ('FONTSIZE', (0, 0), (-1, -1), 9),
        ('TEXTCOLOR', (0, 0), (0, -1), colors.grey),
        ('VALIGN', (0, 0), (-1, -1), 'TOP'),
        ('LEFTPADDING', (0, 0), (-1, -1), 0),
        ('RIGHTPADDING', (0, 0), (-1, -1), 6),
    ]))
    elements.append(skills_table)
    elements.append(Spacer(1, 0.15*inch))
    
    # Professional Experience
    elements.append(Paragraph("PROFESSIONAL EXPERIENCE", heading_style))
    
    # Calculate duration for Transnet position
    start_date = datetime(2025, 4, 1)
    current_date = datetime.now()
    months_diff = (current_date.year - start_date.year) * 12 + (current_date.month - start_date.month)
    if months_diff < 1:
        duration_text = "Less than 1 month"
    elif months_diff == 1:
        duration_text = "1 month"
    else:
        duration_text = f"{months_diff} months"
    
    elements.append(Paragraph("<b>Junior Engineer - IT Solutions</b>", body_style))
    elements.append(Paragraph("Transnet SOC Ltd | April 2025 - Present ({})".format(duration_text), body_style))
    transnet_duties = """
    • Developed Rail Monitor Dashboard for real-time train tracking and operational efficiency<br/>
    • Created Trunking Highsite Dashboard for communication systems monitoring<br/>
    • Built VIS Master system for vehicle inspection and safety compliance<br/>
    • Designed Procurement for R&D platform for streamlined research procurement<br/>
    • Redesigned CAS Dashboard for enhanced collision avoidance system monitoring<br/>
    • Developed Train Movement Segmenting tool for route optimization and efficiency
    """
    elements.append(Paragraph(transnet_duties, body_style))
    elements.append(Spacer(1, 0.1*inch))
    
    # Academic Experience
    elements.append(Paragraph("<b>Tutor - Computer Engineering Department</b>", body_style))
    elements.append(Paragraph("University of Johannesburg | 2022 - 2023", body_style))
    tutor_duties = """
    • Tutored undergraduate students in Computer Architecture, Digital Systems, and Programming<br/>
    • Supervised by Prof. S. Xulu and Prof. O. A. Amodu<br/>
    • Conducted lab sessions and provided academic support for 50+ students
    """
    elements.append(Paragraph(tutor_duties, body_style))
    elements.append(Spacer(1, 0.15*inch))
    
    # Education
    elements.append(Paragraph("EDUCATION", heading_style))
    elements.append(Paragraph("<b>BSc (Honours) Computer Engineering</b>", body_style))
    elements.append(Paragraph("University of Johannesburg | 2022 - 2023", body_style))
    elements.append(Spacer(1, 0.05*inch))
    elements.append(Paragraph("<b>BSc Computer Engineering</b>", body_style))
    elements.append(Paragraph("University of Johannesburg | 2018 - 2021", body_style))
    elements.append(Spacer(1, 0.15*inch))
    
    # Key Projects
    elements.append(Paragraph("KEY PROJECTS", heading_style))
    
    projects = [
        ("IoT Smart Meter System", "Developed Arduino-based smart meter with web interface for real-time monitoring"),
        ("Blockchain Invoice Verification", "Created blockchain system for secure invoice management and fraud prevention"),
        ("Multi-Factor Authentication", "Built face and fingerprint recognition system with 95%+ accuracy"),
        ("Embedded Game System", "Designed PIC16 microcontroller-based game with custom hardware"),
        ("Image Compression System", "Implemented JPEG compression algorithm with 60% file size reduction"),
    ]
    
    for project_name, project_desc in projects:
        elements.append(Paragraph(f"<b>{project_name}:</b> {project_desc}", body_style))
    
    elements.append(Spacer(1, 0.15*inch))
    
    # Certifications
    elements.append(Paragraph("PROFESSIONAL DEVELOPMENT", heading_style))
    certs = """
    • ECSA Candidate Engineer Registration<br/>
    • Git & GitHub Training<br/>
    • Agile Development Methodologies<br/>
    • Database Management Systems
    """
    elements.append(Paragraph(certs, body_style))
    
    # Build PDF
    doc.build(elements)
    
    # Get the value of the BytesIO buffer and return it
    pdf = buffer.getvalue()
    buffer.close()
    
    # Create the HTTP response with PDF
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="Lwazi_Gumede_Resume.pdf"'
    response.write(pdf)
    
    return response
