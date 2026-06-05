# Personal Academic Website Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Build Yaomin Zhao's personal academic website (About + Publications + Research + CV download) on the al-folio Jekyll theme, previewable locally, committed to local git. GitHub deployment is deferred.

**Architecture:** Scaffold the al-folio theme into the existing repo, install a local Ruby 3.x toolchain (rbenv) so the site builds and previews via `jekyll serve`, then customize `_config.yml`, the About page, a `papers.bib` BibTeX file driving the Publications page, and a Research page. Unused al-folio pages/features (news, blog, teaching, repositories, projects portfolio) are disabled to keep the navbar to **About · Publications · Research · CV**.

**Tech Stack:** al-folio (Jekyll + jekyll-scholar), Ruby 3.x via rbenv, BibTeX, GitHub Pages (deferred).

**Spec:** `docs/superpowers/specs/2026-06-05-personal-website-design.md`

---

## Notes / deviations from spec (read first)

- **Corresponding author** is marked with a literal `*` after the name in the BibTeX author field, plus a one-line legend on the Publications page. **Own name** (Yaomin Zhao) is auto-bolded via al-folio's `scholar` config.
- **Student-underlining** in the author list is NOT implemented in this release: jekyll-scholar reformats author names and strips inline markup, so per-author underlining requires a custom bib template. Deferred as a later enhancement (logged in spec §9). The legend mentions only the `*` convention.
- **Honor badges** (cover, Editor's Pick, Review, ESI Highly Cited, In press) are carried in the bib `additional_info` field; if a given al-folio version ignores it, it degrades harmlessly. Flagship papers also get `selected={true}`.
- GitHub push deferred per user decision; al-folio's bundled `.github/workflows` is left in place for a future deploy.

## File structure

```
PersonalWebsite/
├── _config.yml                 # site identity, scholar bolding, nav, disabled features
├── _pages/about.md             # home/About (bio, photo, contact, honors, CV link, group note)
├── _pages/publications.md      # Publications page (renders papers.bib)
├── _pages/research.md          # Research directions (topic cards)
├── _bibliography/papers.bib    # all 45 papers (the data source)
├── assets/img/prof_pic.jpg     # processed profile photo
├── assets/pdf/cv.pdf           # bundled CV download
├── Gemfile / Gemfile.lock      # al-folio dependencies
├── .ruby-version               # pins Ruby 3.x for rbenv
├── cv_zhao_yaomin-v3.pdf       # original asset (kept; copied into assets/pdf)
├── 履历照-1-灰色.jpg            # original asset (kept; processed into assets/img)
└── docs/superpowers/...        # spec + this plan (already committed)
```

---

## Task 1: Install local Ruby 3.x toolchain

**Files:** none (environment setup)

- [ ] **Step 1: Install rbenv + ruby-build**

Run:
```bash
brew install rbenv ruby-build
```
Expected: brew installs `rbenv` and `ruby-build` successfully.

- [ ] **Step 2: Initialize rbenv for this shell and install Ruby 3.3.5**

Run:
```bash
eval "$(rbenv init - zsh)"
rbenv install 3.3.5 --skip-existing
```
Expected: Ruby 3.3.5 compiles and installs (takes several minutes). On success `rbenv versions` lists `3.3.5`.

- [ ] **Step 3: Pin the version in the project**

Run from the project root:
```bash
cd /Users/yaomin/WORK/PROJECTS/PersonalWebsite
rbenv local 3.3.5
eval "$(rbenv init - zsh)"
ruby -v
```
Expected: creates `.ruby-version` containing `3.3.5`; `ruby -v` prints `ruby 3.3.5`.

- [ ] **Step 4: Install bundler**

Run:
```bash
gem install bundler
bundler -v
```
Expected: a modern bundler (2.x) is installed under the rbenv shim.

> **IMPORTANT for all later tasks:** every new shell must first run `eval "$(rbenv init - zsh)"` (or restart the terminal) so `ruby`/`bundle` resolve to rbenv's 3.3.5, not system 2.6.

---

## Task 2: Scaffold the al-folio theme into the repo

**Files:** many (al-folio theme files added to repo root)

- [ ] **Step 1: Clone al-folio into a temp directory**

Run:
```bash
git clone --depth 1 https://github.com/alshedivat/al-folio.git /tmp/al-folio-src
```
Expected: shallow clone succeeds.

- [ ] **Step 2: Copy al-folio contents into the project (excluding its git history)**

Run:
```bash
cd /Users/yaomin/WORK/PROJECTS/PersonalWebsite
rsync -a --exclude='.git' /tmp/al-folio-src/ ./
```
Expected: `_config.yml`, `_pages/`, `_bibliography/`, `Gemfile`, `assets/`, `.github/`, etc. now exist in the project root alongside the existing `docs/` and original asset files.

- [ ] **Step 3: Verify key files landed and nothing clobbered docs/**

Run:
```bash
ls _config.yml Gemfile _pages/about.md _bibliography/papers.bib && ls docs/superpowers/specs/
```
Expected: all al-folio files listed AND the spec file still present.

- [ ] **Step 4: Commit the raw scaffold**

Run:
```bash
git add -A
git commit -m "Scaffold al-folio theme into repo"
```
Expected: large commit adding the theme.

---

## Task 3: Establish a baseline local build (before customizing)

**Files:** `Gemfile.lock` (generated)

- [ ] **Step 1: Install Ruby dependencies**

Run:
```bash
eval "$(rbenv init - zsh)"
cd /Users/yaomin/WORK/PROJECTS/PersonalWebsite
bundle install
```
Expected: gems install, `Gemfile.lock` is created. If a native gem fails, re-run after `brew install imagemagick` (al-folio uses it for responsive images).

- [ ] **Step 2: Build the unmodified site to confirm the toolchain works**

Run:
```bash
bundle exec jekyll build
```
Expected: build completes with `done in N seconds`, producing a `_site/` directory. Warnings are acceptable; errors are not.

- [ ] **Step 3: Commit the lockfile**

Run:
```bash
git add Gemfile.lock
git commit -m "Add Gemfile.lock from baseline al-folio build"
```
Expected: commit succeeds.

---

## Task 4: Configure `_config.yml` (identity, bolding, nav, disabled features)

**Files:**
- Modify: `_config.yml`

- [ ] **Step 1: Set site identity and URL**

In `_config.yml`, set these keys (replace the al-folio demo values):
```yaml
title: Yaomin Zhao
first_name: Yaomin
middle_name: ""
last_name: Zhao

email: yaomin.zhao@pku.edu.cn
description: Yaomin Zhao — Assistant Professor, Peking University. Turbulence simulation and machine-learning turbulence modeling.
footer_fixed: false

url: https://ymgroup-pku.github.io
baseurl: ""
```

- [ ] **Step 2: Configure author bolding for jekyll-scholar**

In `_config.yml`, set the `scholar` section so the author's name renders bold in the bibliography:
```yaml
scholar:
  last_name: [Zhao]
  first_name: [Yaomin, Y.]
```
(Other authors named `Zhang`/`Yang`/`W. Zhao` will not match and stay unbolded.)

- [ ] **Step 3: Disable unused features**

In `_config.yml`, turn off features not used in this release (set to false / disable):
```yaml
news: false
social: true
enable_google_analytics: false
enable_math: true
enable_tooltips: false
```
Leave `display_tags` / blog settings alone for now (the blog page is removed in Task 9).

- [ ] **Step 4: Add the Google Scholar handle for the social icon**

In `_config.yml` under the social/identity keys, set:
```yaml
scholar_userid: XS5AREoAAAAJ
orcid_id: ""
```
(al-folio renders a Scholar icon from `scholar_userid`; empty `orcid_id` hides ORCID.)

- [ ] **Step 5: Build and verify config parses**

Run:
```bash
eval "$(rbenv init - zsh)"
bundle exec jekyll build
grep -q "Yaomin Zhao" _site/index.html && echo "OK: name rendered"
```
Expected: build succeeds and the grep prints `OK: name rendered`.

- [ ] **Step 6: Commit**

Run:
```bash
git add _config.yml
git commit -m "Configure site identity, author bolding, and Scholar handle"
```

---

## Task 5: Add profile photo and CV assets

**Files:**
- Create: `assets/img/prof_pic.jpg`
- Create: `assets/pdf/cv.pdf`

- [ ] **Step 1: Resize/convert the profile photo (8 MB original is too large)**

Run:
```bash
cd /Users/yaomin/WORK/PROJECTS/PersonalWebsite
sips -Z 1000 --setProperty formatOptions 80 "履历照-1-灰色.jpg" --out assets/img/prof_pic.jpg
ls -lh assets/img/prof_pic.jpg
```
Expected: a JPEG ≤ ~1000 px on its long edge, a few hundred KB.

- [ ] **Step 2: Copy the CV PDF into assets**

Run:
```bash
mkdir -p assets/pdf
cp cv_zhao_yaomin-v3.pdf assets/pdf/cv.pdf
ls -lh assets/pdf/cv.pdf
```
Expected: `assets/pdf/cv.pdf` exists.

- [ ] **Step 3: Commit**

Run:
```bash
git add assets/img/prof_pic.jpg assets/pdf/cv.pdf
git commit -m "Add processed profile photo and CV PDF"
```

---

## Task 6: Write the About page

**Files:**
- Modify: `_pages/about.md`

- [ ] **Step 1: Replace `_pages/about.md` with the real content**

Set the file to exactly:
```markdown
---
layout: about
title: about
permalink: /
subtitle: Assistant Professor, <a href='https://www.pku.edu.cn/'>Peking University</a>. yaomin.zhao [at] pku.edu.cn

profile:
  align: right
  image: prof_pic.jpg
  image_circular: false
  more_info: >
    <p>Room 3013, Xin'ao Engineering Building</p>
    <p>No. 5 Yiheyuan Road, Haidian District</p>
    <p>Beijing 100871, China</p>

selected_papers: true
social: true

announcements:
  enabled: false
latest_posts:
  enabled: false
---

I am an Assistant Professor at the [School of Mechanics and Engineering Science](http://www.coe.pku.edu.cn/) and the Center for Applied Physics and Technology, Peking University, and a member of the State Key Laboratory for Turbulence and Complex Systems.

My research centers on **high-fidelity numerical simulation of turbulence** and **machine-learning / data-driven turbulence modeling**, including wall-bounded turbulence, laminar–turbulent transition, turbomachinery and aero-engine internal flows, and interfacial instability and mixing.

I received my B.S. in Physics (Yuanpei College) and my Ph.D. in Fluid Mechanics from Peking University, advised by Prof. Shiyi Chen and Prof. Yue Yang. Before joining Peking University in 2020, I was a Postdoctoral Research Fellow at the University of Melbourne with Prof. Richard D. Sandberg.

**Selected honors:** Young Elite Scientists Sponsorship Program, China Association for Science and Technology (2021); NSFC Excellent Young Scientists Fund (Overseas) (2022).

I lead an active research group of graduate students working on turbulence simulation and modeling. <a href="{{ '/assets/pdf/cv.pdf' | relative_url }}">Download my CV (PDF)</a>.
```

- [ ] **Step 2: Build and verify the About page renders the bio and CV link**

Run:
```bash
eval "$(rbenv init - zsh)"
bundle exec jekyll build
grep -q "assets/pdf/cv.pdf" _site/index.html && echo "OK: CV link present"
grep -q "Richard D. Sandberg" _site/index.html && echo "OK: bio present"
```
Expected: both `OK:` lines print.

- [ ] **Step 3: Commit**

Run:
```bash
git add _pages/about.md
git commit -m "Write About page content"
```

---

## Task 7: Build the publications bibliography and page

**Files:**
- Create/replace: `_bibliography/papers.bib`
- Modify: `_pages/publications.md`

- [ ] **Step 1: Replace `_bibliography/papers.bib` with all 45 papers**

Write the file to exactly the following (newest first; `*` = corresponding author; flagship papers flagged `selected`):

```bibtex
---
---

@string{jfm = {Journal of Fluid Mechanics}}
@string{jcp = {Journal of Computational Physics}}
@string{jot = {Journal of Turbomachinery}}
@string{prf = {Physical Review Fluids}}
@string{pof = {Physics of Fluids}}

% ===== Corresponding/first-author papers (after joining PKU) =====

@article{zhao2026lowwave,
  author  = {Yaomin Zhao and T. Wang and B. Lyu*},
  title   = {Low-wavenumber wall pressure fluctuations in turbulent flows within concentric annular ducts},
  journal = jfm,
  year    = {2026},
  additional_info = {in press},
  arxiv   = {2601.04590},
  bibtex_show = {true}
}

@article{wang2026asymmetric,
  author  = {T. Wang and C. Zhang and Yaomin Zhao*},
  title   = {Asymmetric particle transport in turbulent flows within concentric annular ducts},
  journal = jfm,
  year    = {2026},
  additional_info = {in press},
  arxiv   = {2605.26981},
  bibtex_show = {true}
}

@article{ji2026moe,
  author  = {H. Ji and Y. Luo and H. Zhou and Yaomin Zhao*},
  title   = {Progressive mixture-of-experts with autoencoder routing for continual RANS turbulence modelling},
  journal = jfm,
  year    = {2026},
  additional_info = {in press},
  arxiv   = {2601.09305},
  bibtex_show = {true}
}

@article{zhu2026roughness,
  author  = {X. Zhu and Y. Ge and Yaomin Zhao* and Z. Xiao and R. D. Sandberg},
  title   = {Boundary layer transition induced by surface roughness distributed over a low-pressure turbine blade},
  journal = jot,
  year    = {2026},
  additional_info = {in press},
  doi     = {10.1115/1.4072013},
  html    = {https://doi.org/10.1115/1.4072013},
  bibtex_show = {true}
}

@article{shen2026hairpin,
  author  = {W. Shen and Y. Ge and Z. Han and Yaomin Zhao* and Y. Yang*},
  title   = {Constructing wall turbulence using hierarchical hairpin vortices},
  journal = prf,
  volume  = {11},
  pages   = {044604},
  year    = {2026},
  bibtex_show = {true}
}

@article{wang2026compressor,
  author  = {T. Wang and B. Lyu and Yaomin Zhao*},
  title   = {Frequency response of the unsteady separating boundary layer in a compressor cascade},
  journal = {Acta Mechanica Sinica},
  year    = {2026},
  additional_info = {in press},
  bibtex_show = {true}
}

@article{ge2026fourequation,
  author  = {Y. Ge and X. Zhu and Y. Fang and Yaomin Zhao*},
  title   = {A machine-learning-enhanced four-equation model for predicting roughness induced transition},
  journal = {AIAA Journal},
  year    = {2026},
  additional_info = {in press},
  bibtex_show = {true}
}

@article{wang2026overset,
  author  = {T. Wang and B. Meng and B. Tian and Yaomin Zhao*},
  title   = {A high-fidelity and efficient framework for point-particle direct numerical simulation based on multi-block overset grids},
  journal = {Computer Physics Communications},
  volume  = {322},
  pages   = {110059},
  year    = {2026},
  bibtex_show = {true}
}

@article{xie2025compressiblemixing,
  author  = {H. Xie and T. Luo and Yaomin Zhao* and Y. Zhang* and J. Wang},
  title   = {A compressible Reynolds-averaged mixing model considering turbulent composition and heat fluxes},
  journal = jfm,
  volume  = {1019},
  pages   = {A56},
  year    = {2025},
  bibtex_show = {true}
}

@article{xie2025des,
  author  = {H. Xie and M. Xiao and Yaomin Zhao* and Y. Zhang* and J. Wang and Y. Shi},
  title   = {A detached-eddy simulation methodology for interfacial mixing flows},
  journal = {Physica D: Nonlinear Phenomena},
  volume  = {482},
  pages   = {134892},
  year    = {2025},
  bibtex_show = {true}
}

@article{xie2025intermittency,
  author  = {H. Xie and H. Qi and M. Xiao and Y. Zhang* and Yaomin Zhao*},
  title   = {An intermittency based Reynolds-averaged transition model for mixing flows induced by interfacial instabilities},
  journal = jfm,
  volume  = {1002},
  pages   = {A31},
  year    = {2025},
  bibtex_show = {true}
}

@article{li2025transformer,
  author  = {H. Li and J. Xie and C. Zhang and Y. Zhang and Yaomin Zhao*},
  title   = {A transformer-based convolutional method to model inverse cascade in forced two-dimensional turbulence},
  journal = jcp,
  volume  = {520},
  pages   = {113475},
  year    = {2025},
  bibtex_show = {true}
}

@article{li2024genets,
  author  = {H. Li and Yaomin Zhao* and F. Waschkowski and R. D. Sandberg},
  title   = {Evolutionary neural networks for learning turbulence closure models with explicit expressions},
  journal = pof,
  volume  = {36},
  pages   = {055126},
  year    = {2024},
  selected = {true},
  bibtex_show = {true}
}

@article{zhou2024pde,
  author  = {H. Zhou and H. Li and Yaomin Zhao*},
  title   = {Identification of partial differential equations from noisy data with integrated knowledge discovery and embedding using evolutionary neural networks},
  journal = {Theoretical and Applied Mechanics Letters},
  volume  = {14},
  number  = {2},
  pages   = {100511},
  year    = {2024},
  bibtex_show = {true}
}

@article{wang2023hptstage,
  author  = {T. Wang and Yaomin Zhao* and J. Leggett and R. D. Sandberg},
  title   = {Direct numerical simulation of a high-pressure turbine stage: unsteady boundary layer transition and the resulting flow structures},
  journal = jot,
  volume  = {145},
  number  = {12},
  pages   = {121009},
  year    = {2023},
  bibtex_show = {true}
}

@article{xie2023kl,
  author  = {H. Xie and Yaomin Zhao* and Y. Zhang*},
  title   = {Data-driven nonlinear K-L turbulent mixing model via gene expression programming method},
  journal = {Acta Mechanica Sinica},
  volume  = {39},
  pages   = {322315},
  year    = {2023},
  bibtex_show = {true}
}

@article{leggett2023unsteady,
  author  = {J. Leggett and Yaomin Zhao* and R. D. Sandberg},
  title   = {High-fidelity simulation study of the unsteady flow effects on high-pressure turbine blade performance},
  journal = jot,
  volume  = {145},
  number  = {1},
  pages   = {011002},
  year    = {2023},
  bibtex_show = {true}
}

@article{wu2022les,
  author  = {Q. Wu and Yaomin Zhao* and Y. Shi and S. Chen},
  title   = {Large eddy simulation of particle-laden isotropic turbulence using machine-learned subgrid scale model},
  journal = pof,
  volume  = {34},
  pages   = {065129},
  year    = {2022},
  additional_info = {Editor's Pick},
  selected = {true},
  bibtex_show = {true}
}

@article{li2021lesgep,
  author  = {H. Li and Yaomin Zhao* and J. Wang and R. D. Sandberg},
  title   = {Data-driven model development for large-eddy simulation of turbulence using gene-expression programming},
  journal = pof,
  volume  = {33},
  pages   = {125127},
  year    = {2021},
  bibtex_show = {true}
}

@article{zhao2021gep,
  author  = {Yaomin Zhao* and X. Xu},
  title   = {Data-driven turbulence modelling based on gene-expression programming},
  journal = {Chinese Journal of Theoretical and Applied Mechanics},
  volume  = {53},
  number  = {10},
  pages   = {1--16},
  year    = {2021},
  additional_info = {in Chinese},
  bibtex_show = {true}
}

% ===== Co-authored papers (after joining PKU) =====

@article{wang2026quantumvortex,
  author  = {Z. Wang and J. Zhong and K. Wang and Z. Zhu and Z. Bao and C. Zhu and W. Zhao and Yaomin Zhao and Y. Yang and C. Song* and S. Xiong*},
  title   = {Simulating fluid vortex interactions on a superconducting quantum processor},
  journal = {Nature Communications},
  volume  = {17},
  pages   = {2602},
  year    = {2026},
  selected = {true},
  bibtex_show = {true}
}

@article{fang2026oneshot,
  author  = {Y. Fang* and M. Reissmann and R. Pacciani and Yaomin Zhao and A. S. H. Ooi and M. Marconcini and H. D. Akolekar and R. D. Sandberg},
  title   = {Accelerating CFD-driven training of transition and turbulence models for turbine flows by one-shot and real-time transformer integration},
  journal = {Computers \& Fluids},
  volume  = {306},
  pages   = {106927},
  year    = {2026},
  bibtex_show = {true}
}

@article{wang2025qlbm,
  author  = {B. Wang and Z. Meng and Yaomin Zhao and Y. Yang*},
  title   = {Quantum lattice Boltzmann method for simulating nonlinear fluid dynamics},
  journal = {npj Quantum Information},
  volume  = {11},
  pages   = {196},
  year    = {2025},
  bibtex_show = {true}
}

@article{meng2025qcreview,
  author  = {Z. Meng and Z. Lu and S. Xiong and Yaomin Zhao and Y. Yang*},
  title   = {Advances in quantum computing for fluid dynamics},
  journal = {Advances in Mechanics},
  volume  = {55},
  number  = {3},
  pages   = {541--566},
  year    = {2025},
  additional_info = {in Chinese},
  bibtex_show = {true}
}

@article{zhu2025qvortex,
  author  = {C. Zhu and Z. Wang and S. Xiong* and Yaomin Zhao and Y. Yang},
  title   = {Quantum implicit representation of vortex filaments in turbulence},
  journal = jfm,
  volume  = {1014},
  pages   = {A31},
  year    = {2025},
  bibtex_show = {true}
}

@article{waschkowski2024gradient,
  author  = {F. Waschkowski* and H. Li and A. Deshmukh and T. Grenga and Yaomin Zhao and H. Pitsch and J. Klewicki and R. D. Sandberg},
  title   = {Gradient information and regularization for gene expression programming to develop data-driven physics closure models},
  journal = {Flow, Turbulence and Combustion},
  year    = {2024},
  bibtex_show = {true}
}

@article{fang2024lke,
  author  = {Y. Fang* and Yaomin Zhao and H. D. Akolekar and A. S. H. Ooi and R. D. Sandberg and R. Pacciani and M. Marconcini},
  title   = {A data-driven approach for generalizing the laminar kinetic energy model for separation and bypass transition in low- and high-pressure turbines},
  journal = jot,
  volume  = {146},
  number  = {9},
  pages   = {091005},
  year    = {2024},
  bibtex_show = {true}
}

@article{fang2023multicase,
  author  = {Y. Fang* and Yaomin Zhao and F. Waschkowski and A. S. H. Ooi and R. D. Sandberg},
  title   = {Toward more general turbulence models via multicase computational-fluid-dynamics-driven training},
  journal = {AIAA Journal},
  volume  = {65},
  number  = {5},
  year    = {2023},
  bibtex_show = {true}
}

@article{xu2023taylorcouette,
  author  = {B. Xu and H. Li and X. Liu and Y. Xiang and P. Lv and X. Tan and Yaomin Zhao and C. Sun and H. Duan*},
  title   = {Effect of micro-grooves on drag reduction in Taylor--Couette flow},
  journal = pof,
  volume  = {35},
  pages   = {063608},
  year    = {2023},
  bibtex_show = {true}
}

@article{lav2023coupled,
  author  = {C. Lav* and A. J. Banko and F. Waschkowski and Yaomin Zhao and C. J. Elkins and J. K. Eaton and R. D. Sandberg},
  title   = {A coupled framework for symbolic turbulence models from deep-learning},
  journal = {International Journal of Heat and Fluid Flow},
  volume  = {101},
  pages   = {109140},
  year    = {2023},
  bibtex_show = {true}
}

@article{sandberg2022review,
  author  = {R. D. Sandberg* and Yaomin Zhao},
  title   = {Machine-learning for turbulence and heat-flux model development: a review of challenges associated with distinct physical phenomena and progress to date},
  journal = {International Journal of Heat and Fluid Flow},
  volume  = {95},
  pages   = {108983},
  year    = {2022},
  additional_info = {Review},
  selected = {true},
  bibtex_show = {true}
}

@article{waschkowski2022multiobjective,
  author  = {F. Waschkowski* and Yaomin Zhao and R. D. Sandberg and J. Klewicki},
  title   = {Multi-objective CFD-driven development of coupled turbulence closure models},
  journal = jcp,
  volume  = {452},
  pages   = {110922},
  year    = {2022},
  bibtex_show = {true}
}

% ===== Papers before joining PKU =====

@article{akolekar2021integration,
  author  = {H. D. Akolekar* and Yaomin Zhao and R. D. Sandberg and R. Pacciani},
  title   = {Integration of machine learning and computational fluid dynamics to develop turbulence models for improved low-pressure turbine wake mixing prediction},
  journal = jot,
  volume  = {143},
  pages   = {121001},
  year    = {2021},
  bibtex_show = {true}
}

@article{zhao2021hptvane,
  author  = {Yaomin Zhao* and R. D. Sandberg},
  title   = {High fidelity simulations of a high-pressure turbine vane subject to large disturbances: effect of exit Mach number on losses},
  journal = jot,
  volume  = {143},
  pages   = {091002},
  year    = {2021},
  bibtex_show = {true}
}

@article{zhao2020bypass,
  author  = {Yaomin Zhao* and R. D. Sandberg},
  title   = {Bypass transition in boundary layers subject to strong pressure gradient and curvature effects},
  journal = jfm,
  volume  = {888},
  pages   = {A4},
  year    = {2020},
  additional_info = {Featured on cover},
  selected = {true},
  bibtex_show = {true}
}

@article{zhao2020ransml,
  author  = {Yaomin Zhao* and H. D. Akolekar and J. Weatheritt and V. Michelassi and R. D. Sandberg},
  title   = {RANS turbulence model development using CFD-driven machine learning},
  journal = jcp,
  volume  = {411},
  pages   = {109413},
  year    = {2020},
  selected = {true},
  bibtex_show = {true}
}

@article{zhao2020entropy,
  author  = {Yaomin Zhao* and R. D. Sandberg},
  title   = {Using a new entropy loss analysis to assess the accuracy of RANS predictions of a high-pressure turbine vane},
  journal = jot,
  volume  = {142},
  pages   = {081008},
  year    = {2020},
  bibtex_show = {true}
}

@article{weatheritt2020scalarflux,
  author  = {J. Weatheritt and Yaomin Zhao and R. D. Sandberg* and S. Mizukami and K. Tanimoto},
  title   = {Data-driven scalar-flux model development with application to jet in cross flow},
  journal = {International Journal of Heat and Mass Transfer},
  volume  = {147},
  pages   = {118931},
  year    = {2020},
  bibtex_show = {true}
}

@article{pichler2019endwall1,
  author  = {R. Pichler and Yaomin Zhao and R. D. Sandberg* and V. Michelassi and R. Pacciani and M. Marconcini and A. Arnone},
  title   = {Large-eddy simulation and RANS analysis of the end-wall flow in a linear low-pressure turbine cascade, part I: flow and secondary vorticity fields under varying inlet condition},
  journal = jot,
  volume  = {141},
  pages   = {121005},
  year    = {2019},
  bibtex_show = {true}
}

@article{marconcini2019endwall2,
  author  = {M. Marconcini* and R. Pacciani and A. Arnone and V. Michelassi and R. Pichler and Yaomin Zhao and R. D. Sandberg},
  title   = {Large-eddy simulation and RANS analysis of the end-wall flow in a linear low-pressure turbine cascade, part II: loss generation},
  journal = jot,
  volume  = {141},
  pages   = {051004},
  year    = {2019},
  bibtex_show = {true}
}

@article{zhao2018sinuous,
  author  = {Yaomin Zhao and S. Xiong and Y. Yang* and S. Chen},
  title   = {Sinuous distortion of vortex surfaces in the lateral growth of turbulent spots},
  journal = prf,
  volume  = {3},
  pages   = {074701},
  year    = {2018},
  bibtex_show = {true}
}

@article{zhao2016reconnection,
  author  = {Yaomin Zhao and Y. Yang* and S. Chen},
  title   = {Vortex reconnection in the late transition in channel flow},
  journal = jfm,
  volume  = {802},
  pages   = {R4},
  year    = {2016},
  bibtex_show = {true}
}

@article{zhao2016material,
  author  = {Yaomin Zhao and Y. Yang* and S. Chen},
  title   = {Evolution of material surfaces in the temporal transition in channel flow},
  journal = jfm,
  volume  = {793},
  pages   = {840--876},
  year    = {2016},
  bibtex_show = {true}
}

@article{xia2015sis,
  author  = {Z. Xia* and Y. Shi and Yaomin Zhao},
  title   = {Assessment of the shear-improved Smagorinsky model in laminar-turbulent transitional channel flow},
  journal = {Journal of Turbulence},
  volume  = {16},
  number  = {10},
  pages   = {925--936},
  year    = {2015},
  bibtex_show = {true}
}

@article{zhao2014cles,
  author  = {Yaomin Zhao and Z. Xia* and Y. Shi and Z. Xiao and S. Chen},
  title   = {Constrained large-eddy simulation of laminar-turbulent transition in channel flow},
  journal = pof,
  volume  = {26},
  pages   = {095103},
  year    = {2014},
  bibtex_show = {true}
}
```

- [ ] **Step 2: Replace `_pages/publications.md` with a configured page**

Set the file to exactly:
```markdown
---
layout: page
permalink: /publications/
title: publications
description: 45 journal papers; 1400+ citations. An asterisk (*) marks the corresponding author. See also my <a href="https://scholar.google.com/citations?user=XS5AREoAAAAJ&hl=en">Google Scholar</a> profile.
nav: true
nav_order: 2
---

<!-- _pages/publications.md -->

<div class="publications">

{% bibliography %}

</div>
```

- [ ] **Step 3: Build and verify the bibliography renders**

Run:
```bash
eval "$(rbenv init - zsh)"
bundle exec jekyll build
grep -c "bibtex_show\|bibliography" _site/publications/index.html >/dev/null && echo "page built"
grep -q "Bypass transition in boundary layers" _site/publications/index.html && echo "OK: papers rendered"
grep -q "<strong>" _site/publications/index.html && echo "OK: author bolding active"
```
Expected: `page built`, `OK: papers rendered`, and `OK: author bolding active` all print.

- [ ] **Step 4: Commit**

Run:
```bash
git add _bibliography/papers.bib _pages/publications.md
git commit -m "Add full publication list (45 papers) and configure Publications page"
```

---

## Task 8: Write the Research page

**Files:**
- Create: `_pages/research.md`

- [ ] **Step 1: Create `_pages/research.md`**

Set the file to exactly:
```markdown
---
layout: page
permalink: /research/
title: research
description: Research directions in turbulence simulation and modeling.
nav: true
nav_order: 3
---

## High-fidelity turbulence simulation (DNS/LES)

I develop and apply high-fidelity direct numerical simulation (DNS) and large-eddy simulation (LES) for complex turbulent flows, leveraging GPU heterogeneous computing to push the resolution and geometric complexity that can be simulated faithfully.

## Machine-learning and data-driven turbulence modeling

A central theme of my group is data-driven and interpretable turbulence modeling — using gene-expression programming, evolutionary neural networks, and modern deep-learning architectures to build RANS and subgrid-scale closures with explicit, generalizable expressions.

## Laminar–turbulent transition and wall turbulence

I study the mechanisms of laminar–turbulent transition and the structure of wall-bounded turbulence, including vortex-surface evolution, transitional spots, and the construction of wall turbulence from hierarchical hairpin vortices.

## Turbomachinery and aero-engine internal flows

Working closely with high-fidelity simulation and modeling, I investigate boundary-layer transition, separation, and loss generation in high- and low-pressure turbines and compressors relevant to aero-engine internal flows.

## Interfacial instability, mixing, and frontier directions

I also work on the modeling of compressible interfacial-instability-induced mixing, and on frontier directions such as quantum computing for fluid dynamics.
```

- [ ] **Step 2: Build and verify the Research page renders**

Run:
```bash
eval "$(rbenv init - zsh)"
bundle exec jekyll build
grep -q "data-driven and interpretable turbulence modeling" _site/research/index.html && echo "OK: research rendered"
```
Expected: `OK: research rendered` prints.

- [ ] **Step 3: Commit**

Run:
```bash
git add _pages/research.md
git commit -m "Add Research page"
```

---

## Task 9: Trim navigation — remove unused pages

**Files:**
- Delete: unused `_pages/*.md` (news/blog/teaching/repositories/projects/cv/etc.)
- Possibly modify: `_pages/dropdown.md` removal

- [ ] **Step 1: List the al-folio pages present**

Run:
```bash
ls _pages/
```
Expected: shows al-folio defaults such as `about.md`, `publications.md`, `blog.md`/posts, `news`, `teaching.md`, `repositories.md`, `projects.md`, `cv.md`, `dropdown.md`, `research.md`, `404.md`.

- [ ] **Step 2: Delete the pages not in scope**

Run (keep `about.md`, `publications.md`, `research.md`, `404.md`):
```bash
cd /Users/yaomin/WORK/PROJECTS/PersonalWebsite
rm -f _pages/blog.md _pages/teaching.md _pages/repositories.md _pages/projects.md _pages/cv.md _pages/dropdown.md _pages/people.md
rm -rf _news _projects _books _posts _pages/news.md
```
Expected: those files are removed. (Some may not exist; `-f`/`-rf` make that harmless.)

- [ ] **Step 3: Build and confirm the navbar shows only the four target items**

Run:
```bash
eval "$(rbenv init - zsh)"
bundle exec jekyll build 2>&1 | tail -5
grep -o 'href="[^"]*"[^>]*>\s*\(about\|publications\|research\)' _site/index.html | head
```
Expected: build succeeds; navbar links resolve to about / publications / research only (plus the CV link lives on the About page body).

- [ ] **Step 4: Verify no broken references to deleted collections**

Run:
```bash
eval "$(rbenv init - zsh)"
bundle exec jekyll build 2>&1 | grep -i "error" || echo "no errors"
```
Expected: `no errors`. If an error references a deleted collection (e.g. `_news`), remove the corresponding include from `_pages/about.md` front matter (the `announcements`/`latest_posts` blocks are already disabled in Task 6).

- [ ] **Step 5: Commit**

Run:
```bash
git add -A
git commit -m "Trim navbar to About, Publications, Research"
```

---

## Task 10: Final preview, full verification, and handoff

**Files:** none (verification + optional `.gitignore` touch-up)

- [ ] **Step 1: Ensure build artifacts are ignored**

Run:
```bash
grep -q "_site" .gitignore && grep -q "vendor" .gitignore && echo "gitignore OK" || echo "check .gitignore"
```
Expected: al-folio's `.gitignore` already lists `_site`, `.jekyll-cache`, `vendor`. If not, add them and commit.

- [ ] **Step 2: Serve the site locally for visual review**

Run:
```bash
eval "$(rbenv init - zsh)"
bundle exec jekyll serve --livereload
```
Expected: server starts at `http://127.0.0.1:4000`. Open it and visually confirm:
- About page: photo on the right, bio, selected honors, working CV download link, contact info, Google Scholar icon.
- Publications page: all 45 papers, newest first, own name bold, `*` legend visible, badges (cover / Editor's Pick / Review / in press) shown.
- Research page: five topic sections render.
- Navbar shows only About · Publications · Research.
- Dark-mode toggle works; mobile width looks reasonable.

- [ ] **Step 3: Stop the server and do a clean production build**

Run (Ctrl-C to stop serve, then):
```bash
eval "$(rbenv init - zsh)"
JEKYLL_ENV=production bundle exec jekyll build
echo "exit code: $?"
```
Expected: `exit code: 0`.

- [ ] **Step 4: Final commit**

Run:
```bash
git add -A
git commit -m "Finalize personal academic website (local)" --allow-empty
git log --oneline | head -12
```
Expected: clean history of the build.

- [ ] **Step 5: Report deferred GitHub deployment**

The site is complete and previewable locally. GitHub deployment was deferred by user choice. When ready, the remaining work is: create the `YMGroup-PKU.github.io` repo on GitHub, add it as a remote, push, and set Pages to build from the al-folio GitHub Actions workflow (already present in `.github/workflows/`). Confirm `url`/`baseurl` in `_config.yml` before the first deploy.

---

## Self-review (performed against the spec)

- **About page** (spec §4.1): Task 6 — photo, name/title/affiliations, address, email, Scholar icon (Task 4 §4), bio, selected honors, CV download, group sentence. ✓
- **Publications** (spec §4.2): Task 7 — all 45 papers from `.bib`, newest first, own-name bold, `*` corresponding legend, DOI/arXiv links, honor badges via `additional_info`, stats + Scholar link in page description. Student-underline deferred (documented). ✓ (with noted deviation)
- **Research** (spec §4.3): Task 8 — five topic sections matching the spec's listed themes. ✓
- **CV download** (spec §4 "additional"): Task 5 + Task 6. ✓
- **Privacy boundaries** (spec §3): no funding amounts, no roster — Research page is descriptive only; About has a single group sentence. ✓
- **Deferred** (spec §7): News page not created (Task 9 removes it); Group page not created; custom domain not set. ✓
- **Tech/deploy** (spec §5): al-folio, local Ruby 3.x toolchain (Tasks 1–3), navbar trimmed (Task 9); GitHub Actions deploy left in place but deferred per user. ✓
- **Social links** (spec §8): Scholar id `XS5AREoAAAAJ` wired (Task 4); ORCID omitted. ✓

No placeholder steps; types/paths/keys are consistent across tasks (`prof_pic.jpg`, `assets/pdf/cv.pdf`, `scholar_userid`, page permalinks).
