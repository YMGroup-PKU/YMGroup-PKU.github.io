# Personal Academic Website — Design Spec

**Date:** 2026-06-05
**Owner:** Yaomin Zhao (赵耀民), Assistant Professor, Peking University
**Goal:** A clean, professional academic homepage hosted on GitHub Pages for scholarly self-promotion (international audience).

## 1. Summary

Build a personal academic website using the **al-folio** Jekyll theme, deployed to GitHub Pages via GitHub Actions. Repository: `YMGroup-PKU.github.io` → live at `https://ymgroup-pku.github.io`. Primary language: **English**.

Scope (first release): **three pages + CV download** — About, Publications, Research. News page is explicitly deferred.

## 2. Decisions (locked)

| Topic | Decision |
|---|---|
| Framework | al-folio (Jekyll) |
| Hosting | GitHub Pages, built by GitHub Actions |
| Repo name | `YMGroup-PKU.github.io` (user-site) |
| URL | `https://ymgroup-pku.github.io` (no custom domain for now) |
| Language | English-primary |
| Pages | About, Publications, Research |
| Deferred | News page, Group/People page |
| Assets on hand | `cv_zhao_yaomin-v3.pdf`, `履历照-1-灰色.jpg` |

## 3. Privacy / content boundaries (confirmed)

- **Exclude** research-project funding amounts (e.g. CNY figures) from the public site. Research page describes directions and representative project *titles* only.
- **Exclude** full student roster and scholarship details. No Group page in this release. About may note the group exists in one sentence.
- **Include** publicly: position, affiliations, bio, education, work experience, full publication list, selected honors, academic service (editorial/review), contact info, CV PDF download.

## 4. Pages

### 4.1 About (home)
- Profile photo (`履历照-1-灰色.jpg`, processed/cropped) on the left; right column: name (Yaomin Zhao / 赵耀民), title (Assistant Professor), affiliations (School of Mechanics and Engineering Science; Center for Applied Physics and Technology; State Key Laboratory for Turbulence and Complex Systems, Peking University), address (Room 3013, Xin'ao Engineering Building), email `yaomin.zhao@pku.edu.cn`, phone, social icons (Google Scholar, ORCID, email).
- Short bio (3–4 sentences): B.S. Physics (PKU, Yuanpei) → Ph.D. Fluid Mechanics (PKU; advisors Shiyi Chen, Yue Yang) → Postdoc (U. Melbourne; R. D. Sandberg) → Assistant Professor (PKU, 2020–).
- One-sentence research overview + "Selected Honors" (2–3 items, e.g. Young Elite Scientists Sponsorship Program 2021).
- **CV PDF download** button linking to the bundled PDF.
- One sentence acknowledging the research group (no roster).

### 4.2 Publications
- Generated from a `papers.bib` BibTeX file containing **all 45 journal papers** from the CV, newest first.
- Rendering: bold the author's own name; `*` marks corresponding author; underline marks supervised students.
- Badges where applicable: cover feature, Editor's Pick, Review, ESI Highly Cited, In press.
- Each entry links to DOI / arXiv where available.
- Header line with summary stats (45 papers, 1400+ citations) + Google Scholar link.

### 4.3 Research
- 4–5 topic cards (image placeholders), covering:
  1. High-fidelity turbulence simulation (DNS/LES)
  2. Machine-learning / data-driven turbulence modeling
  3. Laminar–turbulent transition & wall turbulence
  4. Turbomachinery / aero-engine internal flows
  5. Interfacial instability & mixing; quantum computing for fluids (frontier)
- Each card: short paragraph in English, optional representative-paper links (no funding figures).

## 5. Architecture & data flow

- al-folio standard layout. Site config in `_config.yml` (name, affiliation, social handles, scholar id).
- Content lives in: `_pages/about.md`, `_pages/publications.md` (+ `_bibliography/papers.bib`), `_pages/research.md` (or a projects-style page), `assets/img/prof_pic.jpg`, `assets/pdf/cv.pdf`.
- Navbar trimmed to: About · Publications · Research · CV.
- Unused al-folio pages/features (blog, news, projects-as-portfolio, teaching, repositories, etc.) removed or disabled in config so the navbar stays clean.
- Deployment: al-folio's bundled GitHub Actions workflow builds and publishes to the `gh-pages` branch / Pages.

## 6. Testing / verification

- Local build with `bundle exec jekyll serve` renders all three pages without errors.
- Publications page renders the full `.bib` with correct author highlighting and badges.
- Links (DOI/arXiv, Scholar, CV PDF, email) resolve.
- After push: GitHub Actions build succeeds and `https://ymgroup-pku.github.io` serves the site.
- Visual check on desktop + mobile widths; dark-mode toggle works (al-folio default).

## 7. Out of scope (this release)

- News/announcements page
- Group/People page and student roster
- Custom domain
- Teaching, talks, service as dedicated pages (selected items may appear inline on About; full lists deferred)
- Funding/grant amounts

## 8. Open follow-ups (later phases)

- Add News timeline once content cadence is decided.
- Optionally add Group page when ready to publish roster.
- Confirm ORCID id and exact Google Scholar URL to wire social links.
