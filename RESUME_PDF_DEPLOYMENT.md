# PDF Resume Download Feature - Deployment Guide

## What's New

✅ **PDF Resume Download** - Professional PDF resume generated on-the-fly
✅ **Download Button** - Added to navigation bar and home page hero section
✅ **ReportLab Integration** - Professional PDF generation library

---

## 🚀 Deploy to PythonAnywhere

### Step 1: Open PythonAnywhere Bash Console

Go to https://www.pythonanywhere.com and click **"Bash"**

### Step 2: Update Code from GitHub

```bash
# Navigate to project
cd ~/Portfolio

# Pull latest changes
git pull origin main
```

### Step 3: Install ReportLab

```bash
# Activate virtual environment
workon portfolio-env

# Install reportlab
pip install reportlab

# Verify installation
pip list | grep reportlab
```

### Step 4: Reload Web App

- Go to **"Web"** tab
- Click green **"Reload stephusband.pythonanywhere.com"** button

---

## ✨ Features Added

### 1. **Download Resume Button**
- **Navigation Bar**: "Resume" button with download icon
- **Home Page**: Prominent "Download Resume" button in hero section

### 2. **PDF Content Includes**:
- ✅ Contact Information (Email, Phone, Location)
- ✅ Professional Summary
- ✅ Technical Skills (Programming, Web Dev, Databases, Tools)
- ✅ Professional Experience (Transnet Junior Engineer with 6 projects)
- ✅ Academic Experience (UJ Tutor positions)
- ✅ Education (Honours & BSc degrees)
- ✅ Key Projects (5 highlighted projects)
- ✅ Professional Development & Certifications

### 3. **Professional Formatting**:
- Clean, modern design with blue headings
- Proper spacing and layout
- Contact information in table format
- Skills organized in structured tables
- A4 page size for international standard

---

## 🔗 URLs Added

- **Download URL**: `/download-resume/`
- **Direct Link**: `https://stephusband.pythonanywhere.com/download-resume/`

---

## 📦 Dependencies Updated

Added to `requirements.txt`:
```
reportlab>=4.0.0
```

This will automatically install:
- `reportlab` - PDF generation library
- `pillow` - Image processing (reportlab dependency)

---

## 🧪 Testing Locally

```bash
# Activate virtual environment
.venv\Scripts\activate

# Install reportlab (if not already)
pip install reportlab

# Run server
python manage.py runserver

# Test the download
# Visit: http://localhost:8000/
# Click "Download Resume" button
```

---

## 📱 How Users Access It

### Option 1: Navigation Bar
Click **"Resume"** in the top navigation (any page)

### Option 2: Home Page
Click **"Download Resume"** button in the hero section

### Option 3: Direct URL
Visit: `https://stephusband.pythonanywhere.com/download-resume/`

---

## 🎯 What Happens When Downloaded

1. User clicks "Download Resume" or "Resume" button
2. PDF is generated dynamically with latest information
3. Browser downloads file: `Lwazi_Gumede_Resume.pdf`
4. PDF opens in PDF viewer or saves to downloads folder

---

## 🔧 Customization

To update resume content, edit `main/views.py` in the `download_resume()` function:

- **Contact Info**: Lines with email, phone, location
- **Skills**: `skills_data` list
- **Experience**: `transnet_duties` and `tutor_duties` text
- **Projects**: `projects` list
- **Summary**: `summary_text` variable

After changes:
1. Commit and push to GitHub
2. Pull changes on PythonAnywhere
3. Reload web app

---

## ✅ Deployment Checklist

- [ ] Pull latest code from GitHub
- [ ] Install reportlab in virtual environment
- [ ] Reload web app
- [ ] Test download button on homepage
- [ ] Test download button in navigation
- [ ] Verify PDF opens correctly
- [ ] Check all content is accurate

---

## 🎉 Done!

Your resume is now downloadable in professional PDF format! 

**Live URLs:**
- Website: https://stephusband.pythonanywhere.com
- Direct Download: https://stephusband.pythonanywhere.com/download-resume/
