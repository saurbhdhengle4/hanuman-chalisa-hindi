# Hanuman Chalisa Hindi — Static Website

A fast, SEO-optimized, AdSense-ready static website for Hanuman Chalisa, Bajrang Baan,
Hanuman Ashtak, Sankat Mochan Stotra, Hanuman Aarti, and Hanuman Mantras — built with
plain HTML5, CSS3, and vanilla JavaScript. No build tools, no backend, no database required.

## 📁 Structure
```
index.html                  Home page
hanuman-chalisa/index.html
bajrang-baan/index.html
hanuman-ashtak/index.html
hanuman-aarti/index.html
sankat-mochan/index.html
hanuman-mantras/index.html
about/index.html
contact/index.html
privacy-policy/index.html
disclaimer/index.html
terms/index.html
blog/index.html + 4 article pages
404.html
assets/css/style.css        All styles (light + dark mode)
assets/js/main.js           Theme toggle, progress bar, prayer tools, FAQ, forms
assets/favicon/             Favicon PNGs
robots.txt
sitemap.xml
manifest.json
build.py / generate.py / generate2.py / content_texts.py   ← the Python page generator (dev tool, not needed to host the site)
```

## ✅ Features included
- Sticky header with dark/light mode toggle (saved in localStorage)
- Reading progress bar + Back-to-top button
- Copy text / Print / Share / Bookmark / Font size +– on every prayer page
- FAQ accordions, breadcrumbs, related-articles sections
- SEO: unique titles/descriptions, canonical tags, Open Graph, Twitter cards,
  JSON-LD (Organization, WebSite, BreadcrumbList, Article, FAQPage)
- robots.txt + sitemap.xml + manifest.json
- Google AdSense placeholder slots (`<div class="ad-slot">`) — no publisher ID included;
  add your own `<script>`/`<ins>` AdSense tags once your account is approved
- Fully responsive, mobile-first, keyboard accessible, `prefers-reduced-motion` respected

## 🚀 Deploy for free — pick any one

### Option A: GitHub Pages
1. Create a new GitHub repo and push everything **inside this `site` folder** to the repo root.
2. Repo → Settings → Pages → Source: `main` branch, `/ (root)` → Save.
3. Your site goes live at `https://<username>.github.io/<repo>/`.
   (If you use a custom domain, add a `CNAME` file with your domain name.)

### Option B: Cloudflare Pages
1. Push the folder to a GitHub/GitLab repo (see above).
2. Cloudflare dashboard → Workers & Pages → Create → Pages → Connect to Git.
3. Build command: *(leave blank)*, Build output directory: `/` (root).
4. Deploy — you get a free `*.pages.dev` URL instantly, plus custom domain support.

### Option C: Netlify
1. Netlify dashboard → Add new site → Deploy manually (drag-and-drop) **or** connect Git repo.
2. If drag-and-drop: zip the contents of this folder (not the folder itself) and drop it in.
3. Netlify auto-detects it as a static site — no build command needed.

### Option D: Vercel
1. `npm i -g vercel` (or use the Vercel dashboard → New Project → Import Git repo).
2. Framework preset: **Other** (static site). Output directory: `/`.
3. Run `vercel --prod` from inside this folder, or deploy via the dashboard.

### Option E: Render (Static Site)
1. Render dashboard → New → Static Site → connect your repo.
2. Build command: *(leave blank)*, Publish directory: `/`.

## 🔧 Before going live — 3 things to update
1. **Domain**: open `build.py`, change the `SITE` variable at the top from
   `https://hanumanchalisahindi.com` to your real domain, then re-run
   `python3 build.py && python3 generate.py && python3 generate2.py` to regenerate
   every page's canonical URL, sitemap references, and JSON-LD.
2. **sitemap.xml**: it already lists every page — just make sure the domain matches step 1.
3. **AdSense**: once approved, replace the `<!-- AdSense: ... Placeholder -->` comments
   inside `assets/css/style.css`-styled `.ad-slot` `<div>`s (search each HTML file for
   `ad-slot`) with your real `<ins class="adsbygoogle">` snippet and add the AdSense
   loader `<script>` tag (with your publisher ID) once, right before `</head>` in each page,
   or better: add it to a shared include if you switch to a templating build later.

## 🖼️ About images/assets
The hero illustration and the small "gada" (mace) divider icon are original inline SVGs
defined right inside the generated HTML — there is nothing to download separately, so the
site works completely offline / immediately after deploy with zero missing assets.
Fonts (Poppins, Noto Sans Devanagari) and Material Icons are loaded from Google Fonts CDN
over HTTPS — no local font files needed, but you can self-host them later for slightly
faster loading if you want a 100/100 Lighthouse score.

## 🧑‍💻 Editing content
All page content lives in `generate.py`, `generate2.py`, and `content_texts.py` as plain
Python strings — edit the text there and re-run the three build scripts, or simply hand-edit
the generated `.html` files directly (they're plain static HTML, so either approach works).
# hanuman-chalisa-hindi
