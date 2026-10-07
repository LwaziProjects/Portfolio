# Portfolio

Source for [lwaziprojects.github.io/Portfolio](https://lwaziprojects.github.io/Portfolio/), the personal site of Lwazi Knowledge Gumede, systems engineer at Transnet Rail Infrastructure Manager.

It's one static page: plain HTML, one CSS file, self-hosted fonts and two photos. No framework, no build step, no JavaScript, and nothing loaded from third-party servers. First load is about 210 KB.

## Run it locally

```powershell
cd Portfolio
python -m http.server 8000 --directory docs
```

Then open http://localhost:8000. Double-clicking `docs/index.html` also works.

## Where things are

| Path | What it is |
|---|---|
| `docs/index.html` | The whole site, in order: masthead, introduction, Work, Tools, Qualifications, Contact |
| `docs/styles.css` | All styling. Colours, type sizes and spacing are tokens at the top in `:root` |
| `docs/fonts/` | Besley and IBM Plex Mono as Latin WOFF2 subsets, with their OFL licences |
| `docs/images/` | `portrait.webp` (introduction) and `site-visit.webp` (beside the RailBAM entry) |
| `docs/Lwazi_Knowledge_Gumede_CV.pdf` | The CV every download link points to |
| `docs/og-image.png` | The preview card LinkedIn and WhatsApp show when the link is shared |
| `docs/404.html` | Shown for any address that doesn't exist |
| `docs/about.html`, `experience.html`, `projects.html`, `qualifications.html`, `contact.html`, `resume.html` | Redirects from the old multi-page site, so existing links still land somewhere |
| `.github/workflows/pages.yml` | Publishes `docs/` to GitHub Pages when a push to `main` touches it |
| `main/`, `portfolio/`, `manage.py`, `Dockerfile` | The earlier Django version. Kept for reference, not published |

## Common edits

**Add a project.** In `docs/index.html`, find the role it belongs to (each `<article class="group">` is one role) and copy an existing `<li class="entry">` block into it. Newest goes first. Keep the summary to a short paragraph and put the longer detail in that entry's `<details class="notes">` block.

**Add a role.** Copy a whole `<article class="group">` block and place it in date order.

**Replace the CV.** Overwrite `docs/Lwazi_Knowledge_Gumede_CV.pdf` and keep the file name so every link keeps working.

**Bump the revision.** When the content changes, move the letter in the title block (bottom of `index.html`) to the next one, A to B to C, and update the date beside it. It's how a visitor can tell how current the page is.

**Change a colour or size.** Edit the tokens at the top of `docs/styles.css`. The hi-vis colour (`--hivis`) is only used on the title block. Keep it that way.

## Content rules for Transnet work

This site is public. Describe what a system does and what you did on it, and leave out:

- hostnames, IP addresses, ports, server or machine names, user IDs and file paths
- database, table, script and internal system names
- live data, availability figures, fault counts and dashboard screenshots
- specific sites, corridors, depots and incident details, derailments included
- supplier, tender and procurement details
- names of colleagues and managers

If you're unsure, write it the way you'd explain it to someone outside the company.

## Deployment

Pushing to `main` runs `.github/workflows/pages.yml`, which uploads `docs/` and deploys it. The live site updates within a couple of minutes.

One-time setting: **Settings > Pages > Build and deployment > Source: GitHub Actions**.

If you'd rather not use Actions, set Source to *Deploy from a branch*, choose `main` and `/docs`, and delete the workflow file.

`docs/404.html` contains `<base href="/Portfolio/">`. If the repo is renamed or a custom domain is added, change that one line.

## Fonts

Besley (Owen Earl) and IBM Plex Mono (IBM), both under the SIL Open Font License. The licences are in `docs/fonts/`. Source files come from the [google/fonts](https://github.com/google/fonts) repository and were cut down with fontTools:

```bash
fonttools varLib.instancer "Besley[wght].ttf" wght=400:700 -o besley-400-700.ttf
pyftsubset besley-400-700.ttf \
  --unicodes="U+0020-007E,U+00A0-00FF,U+0131,U+0152-0153,U+02C6,U+02DA,U+02DC,U+2013-2014,U+2018-201E,U+2022,U+2026,U+2032-2033,U+2039-203A,U+20AC,U+2122,U+2190-2193,U+2212" \
  --flavor=woff2 --output-file=besley-latin-var.woff2
```

The same `--unicodes` list was used for IBM Plex Mono Regular, Italic and Medium. If you add text with characters outside it, re-run the subset with the extra code points, or the browser will fall back to Georgia or Menlo for those characters.

## Licence

Content and photos © Lwazi Knowledge Gumede, all rights reserved. Fonts are under their own OFL licences.
