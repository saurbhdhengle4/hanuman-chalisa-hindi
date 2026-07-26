#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Static site generator for HanumanChalisaHindi.com
Generates every HTML page from shared header/footer templates so all
pages stay consistent. Run: python3 build.py
"""
import os, re

BASE_PATH = ""                              # <-- served from a domain root (Netlify); set to a "/repo-name" prefix only for a GitHub Pages project site
SITE = "https://boisterous-lollipop-a076ad.netlify.app"   # <-- update to your real custom domain once one is pointed at Netlify
SITE_NAME = "Hanuman Chalisa Hindi"
ADSENSE_CLIENT = "ca-pub-1782498878685450"
ROOT = os.path.dirname(os.path.abspath(__file__))

NAV = [
    ("/", "होम"),
    ("/hanuman-chalisa/", "हनुमान चालीसा"),
    ("/bajrang-baan/", "बजरंग बाण"),
    ("/hanuman-ashtak/", "हनुमान अष्टक"),
    ("/hanuman-aarti/", "हनुमान आरती"),
    ("/about/", "About"),
]

FOOTER_COLS = {
    "प्रार्थनाएं": [
        ("/hanuman-chalisa/", "हनुमान चालीसा"),
        ("/bajrang-baan/", "बजरंग बाण"),
        ("/hanuman-ashtak/", "हनुमान अष्टक"),
        ("/hanuman-aarti/", "हनुमान आरती"),
        ("/sankat-mochan/", "संकट मोचन स्तोत्र"),
        ("/hanuman-mantras/", "हनुमान मंत्र"),
    ],
    "जानकारी": [
        ("/about/", "About Us"),
        ("/blog/", "Blog"),
        ("/contact/", "Contact Us"),
    ],
    "कानूनी": [
        ("/privacy-policy/", "Privacy Policy"),
        ("/disclaimer/", "Disclaimer"),
        ("/terms/", "Terms & Conditions"),
    ],
}

def gada_svg():
    return '''<svg viewBox="0 0 48 48" fill="none" xmlns="http://www.w3.org/2000/svg" aria-hidden="true">
<circle cx="24" cy="14" r="10" fill="currentColor" opacity="0.15"/>
<circle cx="24" cy="14" r="6" fill="currentColor"/>
<rect x="21" y="20" width="6" height="22" rx="3" fill="currentColor"/>
<rect x="14" y="40" width="20" height="4" rx="2" fill="currentColor"/>
</svg>'''

def hero_illustration_svg():
    """Original CSS/SVG illustration (no external image downloads needed) —
    a stylised flame + diya + om motif representing Hanuman's devotion/strength."""
    return '''<svg viewBox="0 0 340 340" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Hanuman ji illustration — divine flame and om symbol">
<defs>
  <linearGradient id="flame" x1="0" y1="1" x2="0" y2="0">
    <stop offset="0%" stop-color="#E65100"/>
    <stop offset="55%" stop-color="#FF6F00"/>
    <stop offset="100%" stop-color="#FFD54F"/>
  </linearGradient>
  <radialGradient id="glow" cx="50%" cy="45%" r="60%">
    <stop offset="0%" stop-color="#FFD54F" stop-opacity="0.55"/>
    <stop offset="100%" stop-color="#FFD54F" stop-opacity="0"/>
  </radialGradient>
</defs>
<circle cx="170" cy="150" r="140" fill="url(#glow)"/>
<circle cx="170" cy="150" r="120" fill="none" stroke="#FFD54F" stroke-width="2" stroke-dasharray="6 10" opacity="0.6"/>
<path d="M170 60 C 205 100 210 140 185 165 C 205 155 225 130 220 100 C 245 130 245 175 210 205 C 175 230 130 225 110 195 C 90 165 100 125 130 100 C 115 130 120 155 140 165 C 120 135 130 90 170 60 Z" fill="url(#flame)"/>
<ellipse cx="170" cy="255" rx="92" ry="18" fill="#E65100" opacity="0.18"/>
<text x="170" y="150" text-anchor="middle" font-size="46" fill="#FFFFFF" font-family="Noto Sans Devanagari, sans-serif" opacity="0.9" dy="16">ॐ</text>
</svg>'''

def devotional_photo(name, alt, css_class="img-frame", width=800, height=None, loading="lazy", fetchpriority=None):
    """<picture> for a hand-illustrated Hanuman ji artwork in /assets/images/
    (webp with jpg fallback), wrapped in the shared framed-portrait card style."""
    dims = f' width="{width}"' + (f' height="{height}"' if height else "")
    fp = f' fetchpriority="{fetchpriority}"' if fetchpriority else ""
    return f'''<picture class="{css_class}">
  <source srcset="{BASE_PATH}/assets/images/{name}.webp" type="image/webp">
  <img src="{BASE_PATH}/assets/images/{name}.jpg" alt="{alt}"{dims} loading="{loading}"{fp}>
</picture>'''

def head(title, description, canonical_path, keywords="", schema_extra="", og_image="/assets/images/og-default.jpg"):
    canonical = SITE + canonical_path
    return f'''<script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client={ADSENSE_CLIENT}" crossorigin="anonymous"></script>
<meta name="google-adsense-account" content="{ADSENSE_CLIENT}">
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title}</title>
<meta name="description" content="{description}">
<meta name="keywords" content="{keywords}">
<meta name="robots" content="index, follow, max-image-preview:large">
<link rel="canonical" href="{canonical}">
<link rel="alternate" hreflang="hi" href="{canonical}">
<link rel="alternate" hreflang="x-default" href="{canonical}">
<link rel="icon" type="image/svg+xml" href="{BASE_PATH}/assets/favicon/favicon.svg">
<link rel="icon" type="image/png" sizes="96x96" href="{BASE_PATH}/assets/favicon/favicon-96x96.png">
<link rel="shortcut icon" href="{BASE_PATH}/assets/favicon/favicon.ico">
<link rel="apple-touch-icon" href="{BASE_PATH}/assets/favicon/apple-touch-icon.png">
<link rel="manifest" href="{BASE_PATH}/manifest.json">
<meta name="theme-color" content="#FF6F00">

<!-- Open Graph -->
<meta property="og:type" content="website">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{description}">
<meta property="og:url" content="{canonical}">
<meta property="og:site_name" content="{SITE_NAME}">
<meta property="og:image" content="{SITE}{og_image}">
<meta property="og:locale" content="hi_IN">

<!-- Twitter -->
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{title}">
<meta name="twitter:description" content="{description}">
<meta name="twitter:image" content="{SITE}{og_image}">

<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Noto+Sans+Devanagari:wght@400;500;600;700&family=Poppins:wght@400;500;600;700;800&display=swap" rel="stylesheet">
<link rel="stylesheet" href="https://fonts.googleapis.com/icon?family=Material+Icons">
<link rel="stylesheet" href="{BASE_PATH}/assets/css/style.css">
{schema_extra}'''

def org_schema():
    return f'''<script type="application/ld+json">
{{
  "@context": "https://schema.org",
  "@type": "Organization",
  "name": "{SITE_NAME}",
  "url": "{SITE}/",
  "logo": "{SITE}/assets/favicon/web-app-manifest-512x512.png",
  "sameAs": []
}}
</script>
<script type="application/ld+json">
{{
  "@context": "https://schema.org",
  "@type": "WebSite",
  "name": "{SITE_NAME}",
  "url": "{SITE}/",
  "potentialAction": {{
    "@type": "SearchAction",
    "target": "{SITE}/?s={{search_term_string}}",
    "query-input": "required name=search_term_string"
  }}
}}
</script>'''

def breadcrumb_schema(items):
    # items: list of (name, path)
    parts = []
    for i, (name, path) in enumerate(items, start=1):
        parts.append(f'{{"@type":"ListItem","position":{i},"name":"{name}","item":"{SITE}{path}"}}')
    return '''<script type="application/ld+json">
{"@context":"https://schema.org","@type":"BreadcrumbList","itemListElement":[''' + ",".join(parts) + ''']}
</script>'''

def faq_schema(qa_pairs):
    parts = []
    for q, a in qa_pairs:
        a_clean = a.replace('"', '\\"').replace("\n", " ")
        q_clean = q.replace('"', '\\"')
        parts.append(f'{{"@type":"Question","name":"{q_clean}","acceptedAnswer":{{"@type":"Answer","text":"{a_clean}"}}}}')
    return '''<script type="application/ld+json">
{"@context":"https://schema.org","@type":"FAQPage","mainEntity":[''' + ",".join(parts) + ''']}
</script>'''

def article_schema(headline, description, path, date="2026-01-15"):
    return f'''<script type="application/ld+json">
{{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "{headline}",
  "description": "{description}",
  "author": {{"@type":"Organization","name":"{SITE_NAME}"}},
  "publisher": {{"@type":"Organization","name":"{SITE_NAME}","logo":{{"@type":"ImageObject","url":"{SITE}/assets/favicon/web-app-manifest-512x512.png"}}}},
  "datePublished": "{date}",
  "dateModified": "{date}",
  "mainEntityOfPage": "{SITE}{path}"
}}
</script>'''

def header_html(active_path):
    links = []
    for href, label in NAV:
        cls = ' class="active"' if href == active_path else ''
        links.append(f'<li><a href="{BASE_PATH}{href}"{cls}>{label}</a></li>')
    return f'''<div class="progress-bar" id="progress-bar"></div>
<header class="site-header">
  <div class="container">
    <a href="{BASE_PATH}/" class="brand" aria-label="{SITE_NAME} home">
      <span class="brand-mark"><img src="{BASE_PATH}/assets/images/hanuman-profile-crown.webp" alt="" width="38" height="38"></span> {SITE_NAME}
    </a>
    <nav class="nav" aria-label="Primary">
      <ul class="nav-links" id="nav-links">
        {''.join(links)}
      </ul>
      <div class="header-actions">
        <button class="icon-btn" id="theme-toggle" aria-label="Toggle dark mode">
          <span class="material-icons" aria-hidden="true">dark_mode</span>
        </button>
        <button class="icon-btn menu-toggle" id="menu-toggle" aria-label="Toggle menu" aria-expanded="false">
          <span class="material-icons" aria-hidden="true">menu</span>
        </button>
      </div>
    </nav>
  </div>
</header>'''

def embers_html():
    """Lightweight CSS-only floating ember particles for the hero flame glow
    (opacity/transform keyframes only — cheap, no canvas/JS-per-frame cost)."""
    spans = "".join(f'<span class="ember e{i}"></span>' for i in range(1, 7))
    return f'<div class="embers" aria-hidden="true">{spans}</div>'

MOBILE_QUICK_LINKS = [
    ("/hanuman-chalisa/", "menu_book", "चालीसा"),
    ("/bajrang-baan/", "flash_on", "बजरंग बाण"),
    ("/hanuman-aarti/", "local_fire_department", "आरती"),
    ("/hanuman-mantras/", "self_improvement", "मंत्र"),
]

def mobile_quickbar_html():
    """Sticky bottom quick-access bar (mobile only, hidden via CSS on
    desktop) so the most-read prayers are always one tap away."""
    links = "".join(
        f'<a href="{BASE_PATH}{href}"><span class="material-icons" aria-hidden="true">{icon}</span><span>{label}</span></a>'
        for href, icon, label in MOBILE_QUICK_LINKS
    )
    return f'<nav class="mobile-quickbar" aria-label="त्वरित पाठ पहुंच">{links}</nav>'

def footer_html():
    cols = ""
    for title, links in FOOTER_COLS.items():
        items = "".join(f'<li><a href="{BASE_PATH}{href}">{label}</a></li>' for href, label in links)
        cols += f'<div><h4>{title}</h4><ul>{items}</ul></div>'
    return f'''<footer class="site-footer">
  <div class="container">
    <div class="footer-grid">
      <div>
        <div class="brand" style="margin-bottom:10px">
          <span class="brand-mark"><img src="{BASE_PATH}/assets/images/hanuman-profile-crown.webp" alt="" width="38" height="38"></span> {SITE_NAME}
        </div>
        <p class="muted" style="max-width:32ch">हनुमान चालीसा, बजरंग बाण, हनुमान अष्टक और संकट मोचन — शुद्ध हिंदी में, हर भक्त के लिए।</p>
      </div>
      {cols}
    </div>
    <div class="footer-bottom">
      <span>&copy; <span id="year">2026</span> {SITE_NAME}. जय श्री राम 🚩</span>
      <span>Made with devotion for Hanuman Bhakts</span>
    </div>
  </div>
</footer>
{mobile_quickbar_html()}
<button class="back-to-top" id="back-to-top" aria-label="Back to top">
  <span class="material-icons" aria-hidden="true">arrow_upward</span>
</button>
<script>document.getElementById('year').textContent = new Date().getFullYear();</script>
<script src="{BASE_PATH}/assets/js/main.js"></script>'''

def breadcrumb_html(items):
    # items list of (name, path) excluding home; home always first
    crumbs = [f'<a href="{BASE_PATH}/">होम</a>']
    for i, (name, path) in enumerate(items):
        crumbs.append('<span>/</span>')
        if path:
            crumbs.append(f'<a href="{BASE_PATH}{path}">{name}</a>')
        else:
            crumbs.append(f'<span aria-current="page">{name}</span>')
    return f'<nav class="breadcrumb container" aria-label="Breadcrumb">{"".join(crumbs)}</nav>'

def page(title, description, path, body, keywords="", active="", schema_extra="", breadcrumbs=None, og_image="/assets/images/og-default.jpg"):
    bc = breadcrumb_html(breadcrumbs) if breadcrumbs else ""
    return f'''<!DOCTYPE html>
<html lang="hi">
<head>
{head(title, description, path, keywords, org_schema() + schema_extra, og_image)}
</head>
<body>
{header_html(active)}
{bc}
<main id="main-content">
{body}
</main>
{footer_html()}
</body>
</html>'''

def write(rel_path, content):
    full = os.path.join(ROOT, rel_path)
    os.makedirs(os.path.dirname(full), exist_ok=True)
    with open(full, "w", encoding="utf-8") as f:
        f.write(content)
    print("wrote", rel_path)

def ad(kind="wide"):
    """Reserved AdSense container — real publisher ID, placeholder ad-unit
    slot ID (create real ad units in the AdSense dashboard and paste the
    resulting data-ad-slot value in below; nothing else needs to change)."""
    return f'''<div class="ad-slot {kind}">
  <span class="ad-slot-label">विज्ञापन · Advertisement</span>
  <!-- TODO: replace data-ad-slot with your real AdSense ad unit ID
       (AdSense dashboard → Ads → By ad unit → Display ads → Create) -->
  <ins class="adsbygoogle"
       style="display:block;width:100%"
       data-ad-client="{ADSENSE_CLIENT}"
       data-ad-slot="0000000000"
       data-ad-format="auto"
       data-full-width-responsive="true"></ins>
  <script>(adsbygoogle = window.adsbygoogle || []).push({{}});</script>
</div>'''

def gada():
    return f'<div class="gada-divider">{gada_svg()}</div>'

print("Templates loaded. Import page-content modules next.")
