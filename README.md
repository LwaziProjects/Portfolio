# Lwazi Knowledge Gumede - Personal Portfolio Website

A personal portfolio website for Lwazi Knowledge Gumede, an ECSA Candidate Engineer with a BSc (Honours) in Computer Engineering. The site is a static HTML/CSS/JavaScript application hosted on GitHub Pages.

🌐 **Live Site**: [lwaziprojects.github.io/Portfolio](https://lwaziprojects.github.io/Portfolio/)  
📦 **GitHub**: [github.com/LwaziProjects/Portfolio](https://github.com/LwaziProjects/Portfolio)

## Overview

This is a fully static site: every page is plain HTML served directly by GitHub Pages, with no backend or database. Styling comes from Bootstrap (via CDN) plus a small custom stylesheet, and the interactive pieces (theme toggle, contact form, PDF export) run entirely in the browser.

## Features

- **Home**: Introduction with a professional summary and quick links
- **About**: Bio, areas of expertise, and technical skills
- **Experience**: Work history at Transnet and UKZN with impact-focused highlights
- **Projects**: A showcase of academic and professional projects, including the IoT Smart Meter System, Blockchain Invoice Verification, Multi-Factor Authentication System, and Transnet rail dashboards
- **Qualifications**: Educational background and academic achievements
- **Contact**: Contact details and a working message form (see below)
- **Resume / CV**: A print-ready CV page ([resume.html](resume.html)) that exports to PDF straight from the browser
- **Light / dark theme**: Toggle in the navigation bar, remembered per browser via `localStorage`
- **Responsive design**: Bootstrap 5 layout that adapts to phones, tablets, and desktops

## Technology Stack

- **Markup**: HTML5
- **Styling**: CSS3 with Bootstrap 5.3 (loaded from CDN)
- **Icons**: Bootstrap Icons
- **Scripting**: Vanilla JavaScript (no framework, no build step)
- **Contact form**: [EmailJS](https://www.emailjs.com/) (client-side email delivery)
- **Hosting**: GitHub Pages

## Project Structure

```
Portfolio/
│
├── index.html            # Home page
├── about.html            # About page
├── experience.html       # Experience page
├── projects.html         # Projects page
├── qualifications.html   # Qualifications page
├── contact.html          # Contact page (EmailJS form)
├── resume.html           # Print-to-PDF CV page
│
├── main/
│   └── static/
│       └── css/
│           └── style.css # Custom styles shared across pages
│
├── .nojekyll             # Tells GitHub Pages to skip Jekyll processing
└── README.md             # This file
```

> **Note:** The repository also contains an earlier Django version of this portfolio (the `main/` app, `portfolio/` config, and `requirements.txt`). That version is no longer deployed - the live site is the static HTML above. The Django files are kept only for reference.

## Running Locally

Because the site is static, you can open it without any build tools.

**Quickest way:** double-click `index.html` (or open it in your browser).

**With a local server** (recommended, mirrors how GitHub Pages serves the files):

```powershell
# From the project folder
python -m http.server 8000
```

Then visit **http://localhost:8000/** in your browser.

## Deployment (GitHub Pages)

The site deploys automatically from GitHub Pages. To publish changes:

1. Commit and push to the `main` branch:
   ```powershell
   git add .
   git commit -m "Your update message"
   git push origin main
   ```
2. GitHub Pages rebuilds the site within a minute or two, and the changes appear at the live URL.

**One-time Pages setup** (already configured for this repo):

- In the GitHub repository, go to **Settings → Pages**.
- Under **Build and deployment**, set **Source** to *Deploy from a branch*.
- Choose the `main` branch and the `/ (root)` folder, then save.
- The `.nojekyll` file ensures the files are served exactly as-is (no Jekyll processing).

## Contact Form

The contact form on [contact.html](contact.html) is powered by **EmailJS**, which sends submissions straight to `lwazig28@gmail.com` from the browser - no server required. If a message fails to send, the form shows a fallback prompting the visitor to email directly.

To point the form at a different account, update the EmailJS `publicKey`, `serviceID`, and `templateID` values in the `<script>` block near the bottom of `contact.html`.

## Resume / PDF Export

The CV lives at [resume.html](resume.html) and is styled for both screen and print. Clicking **Download / Save as PDF** opens the browser's print dialog with print-optimised styles applied. For a clean PDF, set the destination to *Save as PDF*, paper size to *A4*, and untick *Headers and footers*.

## Contact

**Lwazi Knowledge Gumede**

- **Location**: UMlazi, Durban, South Africa
- **Email**: lwazig28@gmail.com
- **Status**: ECSA Candidate Engineer
- **Education**: BSc (Honours) Computer Engineering, University of KwaZulu-Natal

## License

This is a personal portfolio website. All rights reserved by Lwazi Knowledge Gumede.

---

**Built with HTML5, CSS3, JavaScript, and Bootstrap 5.3 | Hosted on GitHub Pages**

**Last Updated**: July 2026
