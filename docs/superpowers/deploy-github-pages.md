# Deploying the site to GitHub Pages

Theme: academicpages (Jekyll). Account/username: **YMGroup-PKU**.
For a *user/organization site*, the repository name MUST be exactly
`YMGroup-PKU.github.io`, and the site is served at `https://ymgroup-pku.github.io`.

The local repo is ready: branch `main`, content committed, `_config.yml` already has
`url: https://ymgroup-pku.github.io` and `baseurl: ""`.

---

## Step 1 — Create the empty repository on GitHub (web)

1. Log in to GitHub as **YMGroup-PKU**.
2. Top-right **＋ → New repository**.
3. Repository name: `YMGroup-PKU.github.io` (must match the username exactly).
4. Visibility: **Public**.
5. **Do NOT** add a README, .gitignore, or license (we already have content).
6. Click **Create repository**. Leave the page open — you'll need the URL.

## Step 2 — Make sure git can reach GitHub (China network)

Direct github.com fails here; route git through the local proxy:

```bash
cd /Users/yaomin/WORK/PROJECTS/PersonalWebsite
git config --local http.proxy  http://127.0.0.1:7897
git config --local https.proxy http://127.0.0.1:7897
```
(These are repo-local, so they won't affect your other projects.)

## Step 3 — Connect the remote and push

```bash
cd /Users/yaomin/WORK/PROJECTS/PersonalWebsite
git remote add origin https://github.com/YMGroup-PKU/YMGroup-PKU.github.io.git
git branch -M main
git push -u origin main
```

Authentication when prompted:
- **Username:** YMGroup-PKU
- **Password:** a **Personal Access Token** (NOT your account password).
  Create one at GitHub → Settings → Developer settings → Personal access tokens →
  *Tokens (classic)* → Generate new token → scope **repo** → copy it and paste as the password.
  (Tip: the token is shown only once; save it somewhere safe.)

## Step 4 — Turn on GitHub Pages

1. In the repo: **Settings → Pages**.
2. **Build and deployment → Source:** *Deploy from a branch*.
3. **Branch:** `main`, folder `/ (root)` → **Save**.
4. GitHub will build the Jekyll site automatically (academicpages uses only
   GitHub-Pages-supported plugins, so the classic build works — no Actions needed).

## Step 5 — Wait and verify

- First build takes ~1–5 minutes. Refresh **Settings → Pages**; it will show
  *"Your site is live at https://ymgroup-pku.github.io"*.
- Open **https://ymgroup-pku.github.io** and check About / Research / Publications /
  Group and the CV link.

---

## Updating the site later

Edit files locally, then:

```bash
cd /Users/yaomin/WORK/PROJECTS/PersonalWebsite
git add -A
git commit -m "Describe the change"
git push
```
GitHub rebuilds automatically within a minute or two.

## Notes / troubleshooting

- **Build status / errors:** repo → **Actions** tab (or Settings → Pages) shows the
  "pages build and deployment" run; click it to see logs if the site doesn't appear.
- **Gemfile.lock** is gitignored on purpose — GitHub Pages manages its own gem
  versions, so this is fine.
- **Local source originals** (`履历照-1-灰色.jpg`, `cv_zhao_yaomin-v3.pdf`) are
  gitignored; the served copies are `images/profile.jpg` and `files/cv.pdf`.
- **Custom domain** (optional, later): Settings → Pages → Custom domain; then add a
  `CNAME` DNS record. Not needed for the `ymgroup-pku.github.io` address.
- If a push hangs, confirm the proxy is running (port 7897) and that Step 2 was applied.
