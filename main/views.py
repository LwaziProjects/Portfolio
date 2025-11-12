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
from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer,
    Table,
    TableStyle,
    PageBreak,
)
from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_JUSTIFY
from io import BytesIO


def home(request):
    """Home page view"""
    context = {"page_title": "Home", "active_page": "home"}
    return render(request, "main/home.html", context)


def about(request):
    """About page view"""
    context = {"page_title": "About", "active_page": "about"}
    return render(request, "main/about.html", context)


def experience(request):
    """Experience page view"""
    # Calculate duration for current Transnet position
    start_date = datetime(2025, 4, 1)  # April 2025
    current_date = datetime.now()

    # Calculate months difference
    months_diff = (current_date.year - start_date.year) * 12 + (
        current_date.month - start_date.month
    )

    # Format duration string
    if months_diff < 1:
        duration_text = "Less than 1 month"
    elif months_diff == 1:
        duration_text = "1 month"
    else:
        duration_text = f"{months_diff} months"

    context = {
        "page_title": "Experience",
        "active_page": "experience",
        "current_position_duration": duration_text,
    }
    return render(request, "main/experience.html", context)


def projects(request):
    """Projects page view"""
    context = {"page_title": "Projects", "active_page": "projects"}
    return render(request, "main/projects.html", context)


def qualifications(request):
    """Qualifications page view"""
    context = {"page_title": "Qualifications", "active_page": "qualifications"}
    return render(request, "main/qualifications.html", context)


def contact(request):
    """Contact page view with form handling"""
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            # Save the contact message
            contact_message = form.save()

            # Email notification code (ENABLED)
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
                
                messages.success(
                    request,
                    "Thank you for your message! We've received your submission and sent you a confirmation email.",
                )
            except Exception as e:
                print(f"Email sending failed: {str(e)}")
                messages.success(
                    request,
                    "Thank you for your message! Your submission has been saved (email notification failed).",
                )

            return redirect("contact")
        else:
            messages.error(request, "Please correct the errors below.")
    else:
        form = ContactForm()

    context = {"page_title": "Contact", "active_page": "contact", "form": form}
    return render(request, "main/contact.html", context)


def download_resume(request):
    """Generate and download resume as PDF"""
    # Create a buffer to receive PDF data
    buffer = BytesIO()

    # Create the PDF object using the buffer as its "file"
    doc = SimpleDocTemplate(
        buffer,
        pagesize=A4,
        topMargin=0.5 * inch,
        bottomMargin=0.5 * inch,
        title="Lwazi Knowledge Gumede - Resume",
        author="Lwazi Knowledge Gumede",
        subject="Professional Resume - ECSA Candidate Engineer",
    )

    # Container for the 'Flowable' objects
    elements = []

    # Define styles
    styles = getSampleStyleSheet()

    # Custom styles
    title_style = ParagraphStyle(
        "CustomTitle",
        parent=styles["Heading1"],
        fontSize=24,
        textColor=colors.HexColor("#0d6efd"),
        spaceAfter=6,
        alignment=TA_CENTER,
        fontName="Helvetica-Bold",
    )

    subtitle_style = ParagraphStyle(
        "CustomSubtitle",
        parent=styles["Normal"],
        fontSize=12,
        textColor=colors.grey,
        spaceAfter=12,
        alignment=TA_CENTER,
    )

    heading_style = ParagraphStyle(
        "CustomHeading",
        parent=styles["Heading2"],
        fontSize=14,
        textColor=colors.HexColor("#0d6efd"),
        spaceAfter=10,
        spaceBefore=12,
        fontName="Helvetica-Bold",
    )

    body_style = ParagraphStyle(
        "CustomBody",
        parent=styles["Normal"],
        fontSize=10,
        spaceAfter=6,
        alignment=TA_JUSTIFY,
    )

    # Compact style for references (reduced line spacing)
    reference_style = ParagraphStyle(
        "ReferenceStyle",
        parent=styles["Normal"],
        fontSize=10,
        spaceAfter=0,
        alignment=TA_LEFT,
        leading=12,  # Reduced line spacing (default is usually 12-14)
    )

    # Header
    elements.append(Paragraph("LWAZI KNOWLEDGE GUMEDE", title_style))
    elements.append(
        Paragraph(
            "ECSA Candidate Engineer | BSc (Honours) Computer Engineering",
            subtitle_style,
        )
    )

    # Contact Information with clickable website link
    website_link = Paragraph(
        '<a href="https://stephusband.pythonanywhere.com" color="blue"><u>Portfolio Website</u></a>',
        body_style
    )
    
    contact_info = [
        ["Email:", "lwazig28@gmail.com", "Phone:", "+27 76 935 2103"],
        ["Location:", "Johannesburg, South Africa", "Phone:", "+27 65 711 1226"],
        ["Website:", website_link, "", ""],
    ]
    contact_table = Table(
        contact_info, colWidths=[1 * inch, 2.2 * inch, 1 * inch, 1.5 * inch]
    )
    contact_table.setStyle(
        TableStyle(
            [
                ("FONTSIZE", (0, 0), (-1, -1), 9),
                ("TEXTCOLOR", (0, 0), (0, -1), colors.grey),
                ("TEXTCOLOR", (2, 0), (2, -1), colors.grey),
                ("ALIGN", (0, 0), (-1, -1), "LEFT"),
            ]
        )
    )
    elements.append(contact_table)
    elements.append(Spacer(1, 0.2 * inch))

    # Professional Summary
    elements.append(Paragraph("PROFESSIONAL SUMMARY", heading_style))
    summary_text = """Results-driven ECSA Candidate Engineer with a BSc (Honours) in Computer Engineering, 
    specializing in software development, system automation, and hardware integration. Proficient in Python, 
    C++, Java, JavaScript, and modern frameworks including React, Django, and Flask. Experienced in developing 
    innovative solutions for rail transport systems, with expertise in IoT, blockchain technology, and embedded systems."""
    elements.append(Paragraph(summary_text, body_style))
    elements.append(Spacer(1, 0.15 * inch))

    # Technical Skills
    elements.append(Paragraph("TECHNICAL SKILLS", heading_style))
    tech_skills = """
    <b>Programming Languages:</b> Python, C++, Java, JavaScript, C#, Assembly Language<br/>
    <b>Web Development:</b> React, Django, Flask, Node.js, HTML5, CSS3, Bootstrap, RESTful APIs<br/>
    <b>Databases:</b> MySQL, PostgreSQL, SQLite, MongoDB, Database Design & Optimization<br/>
    <b>Tools & Technologies:</b> Git, GitHub, Docker, Linux, Visual Studio Code, Arduino, Raspberry Pi<br/>
    <b>Engineering Tools:</b> MATLAB, Simulink, Proteus, Altium Designer, Oscilloscope<br/>
    <b>Specialized Skills:</b> IoT Systems, Blockchain Development, Embedded Systems, System Automation, Microcontroller Programming
    """
    elements.append(Paragraph(tech_skills, body_style))
    elements.append(Spacer(1, 0.15 * inch))

    # Soft Skills
    elements.append(Paragraph("CORE COMPETENCIES", heading_style))
    soft_skills = """
    <b>Leadership & Teamwork:</b> Proven ability to work collaboratively in cross-functional teams and mentor junior developers<br/>
    <b>Problem-Solving:</b> Strong analytical skills with creative approach to complex technical challenges<br/>
    <b>Communication:</b> Excellent verbal and written communication skills; experience presenting technical concepts to diverse audiences<br/>
    <b>Project Management:</b> Skilled in Agile methodologies, time management, and delivering projects within deadlines<br/>
    <b>Adaptability:</b> Quick learner with ability to master new technologies and adapt to changing requirements<br/>
    <b>Attention to Detail:</b> Meticulous approach to code quality, testing, and documentation
    """
    elements.append(Paragraph(soft_skills, body_style))
    elements.append(Spacer(1, 0.15 * inch))

    # Professional Experience
    elements.append(Paragraph("PROFESSIONAL EXPERIENCE", heading_style))

    # Calculate duration for Transnet position
    start_date = datetime(2025, 4, 1)
    current_date = datetime.now()
    months_diff = (current_date.year - start_date.year) * 12 + (
        current_date.month - start_date.month
    )
    if months_diff < 1:
        duration_text = "Less than 1 month"
    elif months_diff == 1:
        duration_text = "1 month"
    else:
        duration_text = f"{months_diff} months"

    elements.append(Paragraph("<b>Engineer-in-Training</b>", body_style))
    elements.append(
        Paragraph(
            "Transnet SOC Ltd | April 2025 - Present ({})".format(duration_text),
            body_style,
        )
    )
    transnet_duties = """
    • Developed Rail Monitor Dashboard for real-time train tracking and operational efficiency<br/>
    • Created Trunking Highsite Dashboard for communication systems monitoring<br/>
    • Built VIS Master system for vehicle inspection and safety compliance<br/>
    • Designed Procurement for R&D platform for streamlined research procurement<br/>
    • Redesigned CAS Dashboard for enhanced collision avoidance system monitoring<br/>
    • Developed Train Movement Segmenting tool for route optimization and efficiency
    """
    elements.append(Paragraph(transnet_duties, body_style))
    elements.append(Spacer(1, 0.1 * inch))

    # Academic Experience
    elements.append(Paragraph("<b>Teaching & Demonstration Roles</b>", body_style))
    elements.append(Paragraph("University of KwaZulu-Natal | 2024 - 2025", body_style))
    teaching_duties = """
    <b>Technical Communication Tutor</b> (Feb - May 2025) | Lecturer: Wayne Nelson<br/>
    • Facilitated tutorials on technical writing, professional documentation, and presentation skills<br/>
    • Coached first-year engineering students in technical report writing and communication strategies<br/>
    <br/>
    <b>Computer Methods Demonstrator</b> (Jun - Nov 2024) | Lecturer: Dr. Jules-Raymond Tapamo<br/>
    • Conducted laboratory sessions on programming and computational methods<br/>
    • Demonstrated numerical analysis techniques and algorithm implementation<br/>
    <br/>
    <b>Electronic Engineering Design Tutor</b> (Feb - May 2024) | Lecturer: Adv. Dr. Ernest Bhero<br/>
    • Mentored students in circuit design, system analysis, and practical implementation<br/>
    <br/>
    <b>Electrical Principles Demonstrator</b> (Feb - May 2024) | Lecturer: Dr. Bhekisizwe Mthethwa<br/>
    • Demonstrated concepts across multiple modules: Electrical Principles, Field Theory, and Electronics<br/>
    • Supervised laboratory sessions ensuring student safety and proper equipment use
    """
    elements.append(Paragraph(teaching_duties, body_style))
    elements.append(Spacer(1, 0.15 * inch))

    # Education
    elements.append(Paragraph("EDUCATION", heading_style))
    elements.append(Paragraph("<b>BSc (Honours) Computer Engineering</b>", body_style))
    elements.append(Paragraph("University of KwaZulu-Natal| 2022 - 2023", body_style))
    elements.append(Spacer(1, 0.05 * inch))
    elements.append(
        Paragraph("<b>National Senior Certificate (Matric)</b>", body_style)
    )
    elements.append(Paragraph("Nombuso High School| 2018", body_style))
    elements.append(Spacer(1, 0.15 * inch))

    # Key Projects
    elements.append(Paragraph("KEY ACADEMIC & PROFESSIONAL PROJECTS", heading_style))

    # Professional Projects
    elements.append(
        Paragraph("<b>Professional Projects (Transnet SOC Ltd)</b>", body_style)
    )
    professional_projects = """
    <b>Rail Monitor Dashboard:</b> Developed real-time train tracking system with live location updates, 
    operational metrics, and automated alerts. Improved operational efficiency by providing actionable insights 
    to rail traffic controllers. Technologies: React, Python, Django, PostgreSQL, WebSocket.<br/>
    <br/>
    <b>Trunking Highsite Dashboard:</b> Built comprehensive monitoring system for communication infrastructure 
    across rail network. Features include site status tracking, equipment health monitoring, and maintenance 
    scheduling. Technologies: JavaScript, Flask, MySQL, Chart.js.<br/>
    <br/>
    <b>VIS Master (Vehicle Inspection System):</b> Created automated vehicle inspection platform for safety 
    compliance and maintenance tracking. Implemented image recognition for defect detection and automated 
    reporting system. Technologies: Python, OpenCV, Django REST Framework, PostgreSQL.<br/>
    <br/>
    <b>CAS Dashboard Redesign:</b> Redesigned Collision Avoidance System dashboard with improved UX/UI, 
    real-time alerts, and enhanced data visualization. Significantly reduced incident response time. 
    Technologies: React, TypeScript, D3.js, Node.js.
    """
    elements.append(Paragraph(professional_projects, body_style))
    elements.append(Spacer(1, 0.1 * inch))

    # Academic Projects
    elements.append(
        Paragraph("<b>Academic Projects (University of KwaZulu-Natal)</b>", body_style)
    )
    academic_projects = """
    <b>IoT Smart Meter System:</b> Designed and developed Arduino-based smart electricity meter with real-time 
    energy consumption monitoring via web interface. Implemented data logging, visualization charts, and 
    consumption alerts with high accuracy in power measurement.<br/>
    <br/>
    <b>Blockchain Invoice Verification System:</b> Created secure blockchain-based platform for invoice management 
    and fraud prevention. Implemented smart contracts for automated verification and immutable transaction records. 
    Significantly reduced processing time.<br/>
    <br/>
    <b>Multi-Factor Authentication System:</b> Built biometric authentication system combining facial recognition 
    and fingerprint scanning with high accuracy using machine learning algorithms. 
    Technologies: Python, OpenCV, TensorFlow, SQLite.<br/>
    <br/>
    <b>PIC16 Embedded Game System:</b> Designed custom hardware and firmware for microcontroller-based gaming 
    console. Implemented game logic, display drivers, and input handling in Assembly language. 
    Featured LCD display and button controls.<br/>
    <br/>
    <b>JPEG Image Compression System:</b> Implemented industry-standard JPEG compression algorithm from scratch. 
    Achieved significant file size reduction while maintaining image quality. Demonstrated understanding of 
    DCT, quantization, and Huffman encoding.
    """
    elements.append(Paragraph(academic_projects, body_style))
    elements.append(Spacer(1, 0.15 * inch))

    # Achievements & Recognition
    elements.append(Paragraph("ACHIEVEMENTS & RECOGNITION", heading_style))
    achievements = """
    • <b>ECSA Candidate Engineer Registration:</b> Successfully registered with Engineering Council of South Africa, 
    demonstrating commitment to professional engineering standards and continuous development<br/>
    <br/>
    • <b>Academic Excellence:</b> Completed BSc Honours in Computer Engineering with strong focus on embedded systems, 
    IoT, and software development. Maintained consistent academic performance throughout undergraduate and postgraduate studies<br/>
    <br/>
    • <b>Industry Impact:</b> Delivered 6 production-ready systems at Transnet SOC Ltd within 7 months, 
    directly improving operational efficiency and safety in rail transport infrastructure<br/>
    <br/>
    • <b>Teaching Excellence:</b> Successfully tutored numerous undergraduate students in complex engineering subjects, 
    receiving positive feedback for clear explanations and supportive teaching approach
    """
    elements.append(Paragraph(achievements, body_style))
    elements.append(Spacer(1, 0.15 * inch))

    # Professional Development & Training
    elements.append(Paragraph("PROFESSIONAL DEVELOPMENT & TRAINING", heading_style))
    certs = """
    <b>Certifications & Training:</b><br/>
    • ECSA Candidate Engineer Registration (Active)<br/>
    • Git & GitHub Version Control - Advanced Workflows<br/>
    • Agile & Scrum Development Methodologies<br/>
    • Database Management & Optimization<br/>
    • Software Testing & Quality Assurance<br/>
    • RESTful API Design & Development<br/>
    <br/>
    <b>Continuous Learning:</b><br/>
    • Active participation in online coding communities and open-source projects<br/>
    • Regular attendance at engineering webinars and technical workshops<br/>
    • Self-directed learning in emerging technologies including AI/ML and cloud computing<br/>
    • Contributing to technical documentation and knowledge sharing initiatives
    """
    elements.append(Paragraph(certs, body_style))
    elements.append(Spacer(1, 0.08 * inch))

    # References
    elements.append(Paragraph("REFERENCES", heading_style))

    # Create two-column layout for references with compact spacing
    ref1 = Paragraph(
        """
    <b>Professional Reference - Transnet SOC Ltd</b><br/>
    <b>Lungelihle Jafta</b> - Line Manager<br/>
    Engineer-in-Training Position<br/>
    Transnet Rail Infrastructure Manager, Johannesburg<br/>
    Email: Lungelihle.Jafta@transnet.net
    """,
        reference_style,
    )

    ref2 = Paragraph(
        """
    <b>Academic Reference 1 - University of KwaZulu-Natal</b><br/>
    <b>Dr. Jules-Raymond Tapamo</b> - Lecturer<br/>
    Computer Methods Module<br/>
    University of KwaZulu-Natal<br/>
    Email: tapamoj@ukzn.ac.za
    """,
        reference_style,
    )

    ref3 = Paragraph(
        """
    <b>Academic Reference 2 - University of KwaZulu-Natal</b><br/>
    <b>Wayne Nelson</b> - Lecturer<br/>
    Technical Communication Module<br/>
    University of KwaZulu-Natal<br/>
    Email: nelsonw@ukzn.ac.za
    """,
        reference_style,
    )

    ref4 = Paragraph(
        """
    <b>Academic Reference 3 - University of KwaZulu-Natal</b><br/>
    <b>Adv. Dr. Ernest Bhero</b> - Lecturer<br/>
    Electronic Engineering Design Module<br/>
    University of KwaZulu-Natal<br/>
    Email: bhero@ukzn.ac.za
    """,
        reference_style,
    )

    # Create table with 2 columns for references with gap between columns
    references_data = [[ref1, ref3], [ref2, ref4]]

    references_table = Table(references_data, colWidths=[3.2 * inch, 3.2 * inch])
    references_table.setStyle(
        TableStyle(
            [
                ("VALIGN", (0, 0), (-1, -1), "TOP"),
                ("LEFTPADDING", (0, 0), (-1, -1), 0),
                (
                    "RIGHTPADDING",
                    (0, 0),
                    (0, -1),
                    20,
                ),  # Add more space on right side of first column
                (
                    "RIGHTPADDING",
                    (1, 0),
                    (1, -1),
                    0,
                ),  # No extra padding on second column
                ("TOPPADDING", (0, 0), (-1, -1), 0),
                (
                    "BOTTOMPADDING",
                    (0, 0),
                    (0, 0),
                    12,
                ),  # Add space between ref1 and ref2
                (
                    "BOTTOMPADDING",
                    (1, 0),
                    (1, 0),
                    12,
                ),  # Add space between ref3 and ref4
                ("BOTTOMPADDING", (0, 1), (1, 1), 0),  # No space after last row
            ]
        )
    )
    elements.append(references_table)

    # Build PDF
    doc.build(elements)

    # Get the value of the BytesIO buffer and return it
    pdf = buffer.getvalue()
    buffer.close()

    # Create the HTTP response with PDF
    response = HttpResponse(content_type="application/pdf")
    response["Content-Disposition"] = 'attachment; filename="Lwazi_Gumede_Resume.pdf"'
    response.write(pdf)

    return response
