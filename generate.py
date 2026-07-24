# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from build import *
from content_texts import *

# ============================================================
# PRAYER TOOLBAR (shared across all prayer pages)
# ============================================================
def prayer_toolbar():
    return '''<div class="prayer-toolbar">
  <div class="font-size-controls">
    <button class="icon-btn btn-sm" id="font-dec" aria-label="Decrease font size">A-</button>
    <button class="icon-btn btn-sm" id="font-inc" aria-label="Increase font size">A+</button>
  </div>
  <div class="btn-row" style="margin:0">
    <button class="btn btn-ghost btn-sm" id="copy-text"><span class="material-icons" style="font-size:1rem">content_copy</span> Copy</button>
    <button class="btn btn-ghost btn-sm" id="print-page"><span class="material-icons" style="font-size:1rem">print</span> Print</button>
    <button class="btn btn-ghost btn-sm" id="share-page"><span class="material-icons" style="font-size:1rem">share</span> Share</button>
    <button class="btn btn-ghost btn-sm" id="bookmark-page"><span class="material-icons" style="font-size:1rem">bookmark_border</span> Save</button>
    <a class="btn btn-outline btn-sm" href="#" onclick="window.print();return false;"><span class="material-icons" style="font-size:1rem">picture_as_pdf</span> Download PDF</a>
  </div>
</div>'''

def faq_block(qa_pairs, heading="अक्सर पूछे जाने वाले प्रश्न (FAQ)"):
    items = ""
    for q, a in qa_pairs:
        items += f'''<div class="faq-item">
  <button class="faq-q" aria-expanded="false">{q}<span class="material-icons" aria-hidden="true">expand_more</span></button>
  <div class="faq-a"><p>{a}</p></div>
</div>'''
    return f'<section class="section" id="faq"><div class="container"><div class="section-head"><h2>{heading}</h2></div><div style="max-width:820px;margin:0 auto">{items}</div></div></section>'

def related_articles(items):
    """items: list of (title, path, blurb)"""
    cards = "".join(f'''<a class="card" href="{BASE_PATH}{path}" data-search-item="{title}">
  <span class="material-icons" aria-hidden="true">auto_stories</span>
  <h3>{title}</h3><p>{blurb}</p>
</a>''' for title, path, blurb in items)
    return f'''<section class="section"><div class="container">
<div class="section-head"><h2>संबंधित लेख</h2></div>
<div class="grid grid-3">{cards}</div>
</div></section>'''

# ============================================================
# PRAYER PAGE BUILDER
# ============================================================
def prayer_page(slug, title_hi, title_en, meta_desc, keywords, prayer_html, intro_html,
                 benefits, how_to_read, best_time, importance, faqs, related, date="2026-01-10"):
    path = f"/{slug}/"
    body = f'''<section class="hero" style="padding:40px 0 30px">
  <div class="container" style="grid-template-columns:1fr;text-align:center">
    <div>
      {devotional_photo("hanuman-profile-crown", "भगवान हनुमान जी का मुकुट सहित चित्र", css_class="img-frame hero-avatar", width=736, height=1308)}
      <h1>{title_hi}<br><span style="font-size:.55em;color:var(--text-muted)">{title_en}</span></h1>
      <p class="lead" style="margin:0 auto">{intro_html}</p>
    </div>
  </div>
</section>
<div class="container">
{ad("wide")}
<div class="page-layout">
  <aside class="toc" aria-label="Table of contents">
    <h4>इस पेज में</h4>
    <ul>
      <li><a href="#prayer-body">पूर्ण पाठ</a></li>
      <li><a href="#benefits">लाभ</a></li>
      <li><a href="#how-to-read">पढ़ने की विधि</a></li>
      <li><a href="#best-time">सर्वोत्तम समय</a></li>
      <li><a href="#importance">महत्व</a></li>
      <li><a href="#faq">FAQ</a></li>
    </ul>
  </aside>
  <div>
    {prayer_toolbar()}
    <article class="prayer-text">
      <div id="prayer-body">{prayer_html}</div>
    </article>

    {gada()}
    <section id="benefits">
      <h2>लाभ (Benefits)</h2>
      {benefits}
    </section>

    {ad("wide")}

    <section id="how-to-read">
      <h2>पढ़ने की विधि (How to Read)</h2>
      {how_to_read}
    </section>

    <section id="best-time">
      <h2>पढ़ने का सर्वोत्तम समय (Best Time)</h2>
      {best_time}
    </section>

    <section id="importance">
      <h2>महत्व (Importance)</h2>
      {importance}
    </section>
  </div>
</div>
</div>
{faq_block(faqs)}
{related_articles(related)}
'''
    schema = faq_schema(faqs) + breadcrumb_schema([(title_hi, path)]) + article_schema(title_hi, meta_desc, path, date)
    html = page(
        title=f"{title_hi} — {title_en} | पूर्ण पाठ, अर्थ और लाभ",
        description=meta_desc,
        path=path,
        body=body,
        keywords=keywords,
        active=path,
        schema_extra=schema,
        breadcrumbs=[(title_hi, None)],
    )
    write(f"{slug}/index.html", html)

# ------------------------------------------------------------
# Hanuman Chalisa
# ------------------------------------------------------------
prayer_page(
    slug="hanuman-chalisa",
    title_hi="हनुमान चालीसा",
    title_en="Hanuman Chalisa",
    meta_desc="हनुमान चालीसा हिंदी में शुद्ध पाठ, अर्थ सहित। जानें हनुमान चालीसा पढ़ने के लाभ, सही विधि और सर्वोत्तम समय। मुफ्त PDF डाउनलोड करें।",
    keywords="hanuman chalisa, hanuman chalisa hindi, हनुमान चालीसा, हनुमान चालीसा पाठ, hanuman chalisa lyrics hindi, hanuman chalisa pdf",
    prayer_html=HANUMAN_CHALISA_DOHA1 + HANUMAN_CHALISA_CHAUPAI + HANUMAN_CHALISA_DOHA2,
    intro_html="गोस्वामी तुलसीदास द्वारा रचित हनुमान चालीसा भगवान हनुमान जी की स्तुति में लिखी गई सबसे लोकप्रिय चालीसा है। इसका नियमित पाठ भय, संकट और नकारात्मक शक्तियों से रक्षा करता है।",
    benefits="""<p>हनुमान चालीसा का नियमित पाठ करने से मानसिक शांति मिलती है, आत्मविश्वास बढ़ता है और जीवन के संकटों से मुक्ति मिलती है। यह भय, चिंता और नकारात्मक ऊर्जा को दूर करने में सहायक माना जाता है।</p>
    <div class="grid grid-4">
      <div class="card"><span class="material-icons">shield</span><h3>संकट से रक्षा</h3><p>बाधाओं और भय से सुरक्षा मिलती है।</p></div>
      <div class="card"><span class="material-icons">self_improvement</span><h3>मानसिक शांति</h3><p>तनाव कम होकर मन शांत रहता है।</p></div>
      <div class="card"><span class="material-icons">bolt</span><h3>शक्ति व साहस</h3><p>आत्मबल और साहस में वृद्धि होती है।</p></div>
      <div class="card"><span class="material-icons">health_and_safety</span><h3>स्वास्थ्य लाभ</h3><p>रोग व पीड़ा दूर होने में सहायक।</p></div>
    </div>""",
    how_to_read="""<p>स्नान कर स्वच्छ वस्त्र धारण करें, पूर्व या उत्तर दिशा की ओर मुख करके बैठें। हनुमान जी और श्रीराम का ध्यान करते हुए दीपक व अगरबत्ती जलाएं। शांत मन से, स्पष्ट उच्चारण के साथ पूरा पाठ करें। मंगलवार और शनिवार को पाठ करना विशेष फलदायी माना जाता है।</p>""",
    best_time="""<p>ब्रह्म मुहूर्त (सुबह 4-6 बजे) या संध्या समय सूर्यास्त के बाद हनुमान चालीसा पढ़ना सर्वोत्तम माना जाता है। मंगलवार और शनिवार इसके लिए विशेष रूप से शुभ दिन हैं।</p>""",
    importance="""<p>हनुमान चालीसा केवल एक स्तुति नहीं बल्कि भक्त और भगवान के बीच गहरे विश्वास का प्रतीक है। यह चालीसा सदियों से करोड़ों भक्तों के जीवन में साहस, शक्ति और शांति का स्रोत रही है।</p>""",
    faqs=[
        ("हनुमान चालीसा किसने लिखी थी?", "हनुमान चालीसा की रचना गोस्वामी तुलसीदास जी ने की थी, जो अवधी भाषा में लिखी गई है।"),
        ("हनुमान चालीसा पढ़ने का सही समय क्या है?", "ब्रह्म मुहूर्त या संध्या समय, विशेषकर मंगलवार और शनिवार को पढ़ना शुभ माना जाता है।"),
        ("हनुमान चालीसा में कितने दोहे और चौपाई हैं?", "इसमें 2 दोहे, 40 चौपाई और अंत में 1 समापन दोहा है।"),
        ("क्या रोज़ हनुमान चालीसा पढ़ी जा सकती है?", "हां, प्रतिदिन श्रद्धा और नियम से हनुमान चालीसा का पाठ करना अत्यंत लाभकारी माना जाता है।"),
    ],
    related=[
        ("बजरंग बाण", "/bajrang-baan/", "संकट से तुरंत मुक्ति के लिए पढ़ें बजरंग बाण।"),
        ("हनुमान आरती", "/hanuman-aarti/", "आरती कीजै हनुमान लला की — पूर्ण आरती पढ़ें।"),
        ("हनुमान चालीसा के लाभ", "/blog/benefits-of-hanuman-chalisa/", "जानें रोज़ाना पाठ के वैज्ञानिक व आध्यात्मिक लाभ।"),
    ],
)

# ------------------------------------------------------------
# Bajrang Baan
# ------------------------------------------------------------
prayer_page(
    slug="bajrang-baan",
    title_hi="बजरंग बाण",
    title_en="Bajrang Baan",
    meta_desc="बजरंग बाण हिंदी में पूर्ण पाठ, अर्थ और लाभ सहित पढ़ें। संकट, भय और शत्रु बाधा से तुरंत मुक्ति के लिए बजरंग बाण का पाठ करें।",
    keywords="bajrang baan, bajrang baan hindi, बजरंग बाण, बजरंग बाण पाठ, bajrang baan lyrics",
    prayer_html=BAJRANG_BAAN,
    intro_html="बजरंग बाण हनुमान जी की स्तुति में रचित एक अत्यंत प्रभावशाली स्तोत्र है, जिसे संकट और शत्रु बाधा से तत्काल मुक्ति पाने के लिए पढ़ा जाता है।",
    benefits="""<p>बजरंग बाण का पाठ शत्रु बाधा, भय और अकारण संकटों से रक्षा करता है। इसे विशेष रूप से कठिन समय में तुरंत राहत पाने के लिए पढ़ा जाता है।</p>""",
    how_to_read="""<p>शुद्ध मन और स्वच्छ स्थान पर बैठकर, दीपक जलाकर श्रद्धा भाव से बजरंग बाण का पाठ करें। इसे सामान्यतः हनुमान चालीसा के बाद पढ़ा जाता है।</p>""",
    best_time="""<p>मंगलवार व शनिवार, विशेषकर संकट के समय या किसी महत्वपूर्ण कार्य से पूर्व बजरंग बाण पढ़ना शुभ माना जाता है।</p>""",
    importance="""<p>बजरंग बाण को अत्यंत शक्तिशाली स्तोत्र माना गया है, जो साहस बढ़ाकर मन के भय को दूर करता है और सुरक्षा प्रदान करता है।</p>""",
    faqs=[
        ("बजरंग बाण कब पढ़ना चाहिए?", "संकट के समय, यात्रा से पहले या मंगलवार-शनिवार को बजरंग बाण पढ़ना शुभ माना जाता है।"),
        ("क्या बजरंग बाण रोज़ पढ़ सकते हैं?", "हां, श्रद्धा और नियमपूर्वक प्रतिदिन पाठ किया जा सकता है।"),
    ],
    related=[
        ("हनुमान चालीसा", "/hanuman-chalisa/", "संपूर्ण हनुमान चालीसा हिंदी में पढ़ें।"),
        ("संकट मोचन स्तोत्र", "/sankat-mochan/", "संकट से मुक्ति के लिए संस्कृत स्तोत्र।"),
        ("हनुमान मंत्र", "/hanuman-mantras/", "शक्तिशाली हनुमान मंत्र जानें।"),
    ],
)

# ------------------------------------------------------------
# Hanuman Ashtak
# ------------------------------------------------------------
prayer_page(
    slug="hanuman-ashtak",
    title_hi="हनुमान अष्टक (संकटमोचन)",
    title_en="Hanuman Ashtak",
    meta_desc="हनुमान अष्टक हिंदी में पूर्ण पाठ पढ़ें — तुलसीदास रचित संकटमोचन हनुमान अष्टक, अर्थ और लाभ सहित।",
    keywords="hanuman ashtak, hanuman ashtak hindi, हनुमान अष्टक, sankat mochan hanuman ashtak",
    prayer_html=HANUMAN_ASHTAK,
    intro_html="हनुमान अष्टक तुलसीदास जी द्वारा रचित 8 छंदों का स्तोत्र है, जिसमें हनुमान जी की विभिन्न लीलाओं का वर्णन कर संकट से मुक्ति की प्रार्थना की गई है।",
    benefits="""<p>हनुमान अष्टक का पाठ जीवन के हर प्रकार के संकट — शारीरिक, मानसिक व आर्थिक — से मुक्ति दिलाने में सहायक माना जाता है।</p>""",
    how_to_read="""<p>प्रातःकाल स्नान के बाद स्वच्छ आसन पर बैठकर श्रद्धापूर्वक आठों छंदों का क्रमशः पाठ करें।</p>""",
    best_time="""<p>प्रातः या सायं, विशेषकर मंगलवार को हनुमान अष्टक पढ़ना उत्तम माना जाता है।</p>""",
    importance="""<p>यह अष्टक हनुमान जी की भक्ति और शक्ति की महिमा का वर्णन करता है और भक्तों में अटूट विश्वास जगाता है।</p>""",
    faqs=[
        ("हनुमान अष्टक किसने लिखा?", "हनुमान अष्टक की रचना गोस्वामी तुलसीदास जी ने की थी।"),
        ("हनुमान अष्टक में कितने छंद हैं?", "इसमें कुल 8 छंद (श्लोक) हैं, जो हनुमान जी की विभिन्न लीलाओं का वर्णन करते हैं।"),
    ],
    related=[
        ("संकट मोचन स्तोत्र", "/sankat-mochan/", "संस्कृत में संकट मोचन हनुमान स्तोत्र पढ़ें।"),
        ("हनुमान चालीसा", "/hanuman-chalisa/", "संपूर्ण हनुमान चालीसा हिंदी में पढ़ें।"),
        ("बजरंग बाण", "/bajrang-baan/", "शत्रु बाधा से मुक्ति के लिए बजरंग बाण पढ़ें।"),
    ],
)

# ------------------------------------------------------------
# Hanuman Aarti
# ------------------------------------------------------------
prayer_page(
    slug="hanuman-aarti",
    title_hi="हनुमान आरती",
    title_en="Hanuman Aarti",
    meta_desc="आरती कीजै हनुमान लला की — हनुमान आरती हिंदी में पूर्ण पाठ, अर्थ और लाभ सहित पढ़ें।",
    keywords="hanuman aarti, hanuman aarti hindi, आरती कीजै हनुमान लला की, hanuman ji ki aarti",
    prayer_html=HANUMAN_AARTI,
    intro_html='"आरती कीजै हनुमान लला की" हनुमान जी की सबसे लोकप्रिय आरती है, जो हर मंदिर व घर में पूजा के अंत में गाई जाती है।',
    benefits="""<p>आरती गाने से भक्ति भाव जागृत होता है और घर में सकारात्मक ऊर्जा का संचार होता है। यह पूजा का समापन शुभ रूप से करने का माध्यम है।</p>""",
    how_to_read="""<p>घी या कपूर का दीपक जलाकर हनुमान जी की प्रतिमा या चित्र के समक्ष खड़े होकर, ताली बजाते हुए भक्तिभाव से आरती गाएं।</p>""",
    best_time="""<p>प्रतिदिन संध्या पूजा के समय, विशेषकर मंगलवार और शनिवार को आरती करना शुभ माना जाता है।</p>""",
    importance="""<p>आरती भक्त और भगवान के बीच सीधे संवाद व समर्पण का प्रतीक है, जो पूजा को पूर्णता प्रदान करती है।</p>""",
    faqs=[
        ("हनुमान आरती कब करनी चाहिए?", "प्रतिदिन पूजा के अंत में, विशेषकर संध्या समय आरती करना शुभ माना जाता है।"),
        ("आरती के समय क्या ध्यान रखें?", "स्वच्छता, श्रद्धा और दीपक जलाकर भक्तिभाव से आरती गाने का ध्यान रखें।"),
    ],
    related=[
        ("हनुमान चालीसा", "/hanuman-chalisa/", "पूजा से पूर्व हनुमान चालीसा पढ़ें।"),
        ("हनुमान मंत्र", "/hanuman-mantras/", "पूजा में उपयोग होने वाले शक्तिशाली मंत्र जानें।"),
        ("मंगलवार पूजा विधि", "/blog/tuesday-hanuman-puja-vidhi/", "मंगलवार को हनुमान पूजा कैसे करें, जानें पूरी विधि।"),
    ],
)

# ------------------------------------------------------------
# Sankat Mochan
# ------------------------------------------------------------
prayer_page(
    slug="sankat-mochan",
    title_hi="संकट मोचन हनुमान स्तोत्र",
    title_en="Sankat Mochan Stotra",
    meta_desc="संकट मोचन हनुमान स्तोत्र संस्कृत में पूर्ण पाठ, अर्थ और लाभ सहित पढ़ें। जीवन के हर संकट से मुक्ति के लिए इस स्तोत्र का पाठ करें।",
    keywords="sankat mochan hanuman stotra, संकट मोचन, sankat mochan hanuman ashtak hindi",
    prayer_html=SANKAT_MOCHAN_STOTRA,
    intro_html="संकट मोचन हनुमान स्तोत्र संस्कृत में रचित एक पवित्र स्तोत्र है, जो हनुमान जी के अतुलित बल और भक्तवत्सल स्वभाव का वर्णन करता है।",
    benefits="""<p>यह स्तोत्र मानसिक भय, बाधा और अनिश्चितता को दूर कर आत्मविश्वास व सुरक्षा की भावना प्रदान करता है।</p>""",
    how_to_read="""<p>शुद्ध उच्चारण के साथ, शांत मन से इस संस्कृत स्तोत्र का पाठ करें। संभव हो तो किसी विद्वान से सही उच्चारण सीखें।</p>""",
    best_time="""<p>प्रातःकाल या संकट के समय इस स्तोत्र का पाठ करना विशेष फलदायी माना जाता है।</p>""",
    importance="""<p>यह स्तोत्र हनुमान जी के दिव्य स्वरूप और उनकी असीम शक्ति का स्मरण कराता है, जो भक्तों को हर संकट से उबारने में सक्षम है।</p>""",
    faqs=[
        ("संकट मोचन स्तोत्र किस भाषा में है?", "यह स्तोत्र संस्कृत भाषा में रचित है।"),
        ("इसे कब पढ़ना चाहिए?", "जीवन में किसी भी प्रकार का संकट या भय होने पर इसका पाठ करना शुभ माना जाता है।"),
    ],
    related=[
        ("हनुमान अष्टक", "/hanuman-ashtak/", "संकटमोचन हनुमान अष्टक हिंदी में पढ़ें।"),
        ("बजरंग बाण", "/bajrang-baan/", "शत्रु बाधा से मुक्ति के लिए बजरंग बाण पढ़ें।"),
        ("हनुमान चालीसा", "/hanuman-chalisa/", "संपूर्ण हनुमान चालीसा हिंदी में पढ़ें।"),
    ],
)

print("Prayer pages generated.")

# ============================================================
# HOME PAGE
# ============================================================
def home_page():
    path = "/"
    quick_nav = [
        ("hanuman-chalisa/", "हनुमान चालीसा", "menu_book", "संपूर्ण पाठ, अर्थ और लाभ सहित"),
        ("bajrang-baan/", "बजरंग बाण", "flash_on", "संकट व शत्रु बाधा से मुक्ति"),
        ("hanuman-ashtak/", "हनुमान अष्टक", "auto_stories", "तुलसीदास रचित संकटमोचन अष्टक"),
        ("hanuman-aarti/", "हनुमान आरती", "local_fire_department", "आरती कीजै हनुमान लला की"),
        ("sankat-mochan/", "संकट मोचन स्तोत्र", "shield", "संस्कृत में पवित्र स्तोत्र"),
        ("hanuman-mantras/", "हनुमान मंत्र", "self_improvement", "शक्तिशाली बीज व रक्षा मंत्र"),
    ]
    cards = "".join(f'''<a class="card" href="{BASE_PATH}/{href}" data-search-item="{title} {desc}">
  <span class="material-icons" aria-hidden="true">{icon}</span>
  <h3>{title}</h3><p>{desc}</p>
  <span class="card-link">पढ़ें &rarr;</span>
</a>''' for href, title, icon, desc in quick_nav)

    benefits_cards = "".join(f'''<div class="card">
  <span class="material-icons">{icon}</span><h3>{t}</h3><p>{d}</p>
</div>''' for icon, t, d in [
        ("shield", "संकट से रक्षा", "भय, बाधा और नकारात्मक शक्तियों से सुरक्षा मिलती है।"),
        ("self_improvement", "मानसिक शांति", "मन शांत रहता है और तनाव कम होता है।"),
        ("bolt", "आत्मबल में वृद्धि", "साहस, आत्मविश्वास और शक्ति बढ़ती है।"),
        ("health_and_safety", "स्वास्थ्य लाभ", "रोग व पीड़ा को दूर करने में सहायक माना जाता है।"),
    ])

    testimonials = "".join(f'''<div class="testimonial">
  <div class="stars" aria-hidden="true">★★★★★</div>
  <p>"{q}"</p>
  <div class="who">— {who}</div>
</div>''' for q, who in [
        ("रोज़ सुबह हनुमान चालीसा पढ़ने से मन को बहुत शांति मिलती है। यह वेबसाइट पढ़ने में बहुत आसान है।", "रमेश शर्मा"),
        ("बजरंग बाण का टेक्स्ट बड़े अक्षरों में है जिससे पढ़ना आसान होता है। धन्यवाद!", "सुनीता देवी"),
        ("मंगलवार को पूरा परिवार मिलकर यहीं से आरती पढ़ता है। बहुत सुंदर वेबसाइट।", "अजय पटेल"),
    ])

    popular_posts = "".join(f'''<a class="card blog-card" href="{BASE_PATH}{href}" data-search-item="{t}">
  <span class="tag">ब्लॉग</span>
  <h3>{t}</h3><p>{d}</p>
  <span class="blog-meta">5 मिनट पढ़ें</span>
</a>''' for href, t, d in [
        ("/blog/benefits-of-hanuman-chalisa/", "हनुमान चालीसा पढ़ने के 10 अद्भुत लाभ", "जानें कैसे नियमित पाठ जीवन में सकारात्मक बदलाव लाता है।"),
        ("/blog/best-time-to-read-hanuman-chalisa/", "हनुमान चालीसा पढ़ने का सही समय क्या है?", "ब्रह्म मुहूर्त से लेकर संध्या तक — पूरी जानकारी।"),
        ("/blog/who-wrote-hanuman-chalisa/", "हनुमान चालीसा किसने लिखी? पूरा इतिहास", "गोस्वामी तुलसीदास और चालीसा की रचना की कहानी।"),
    ])

    body = f'''<section class="hero">
  <div class="container">
    <div>
      <span class="hero-eyebrow"><span class="material-icons" style="font-size:1rem">auto_awesome</span> जय श्री हनुमान</span>
      <h1>पढ़ें <span>हनुमान चालीसा</span><br>शुद्ध हिंदी में</h1>
      <p class="lead">हनुमान चालीसा, बजरंग बाण, हनुमान अष्टक, संकट मोचन, हनुमान आरती और हनुमान मंत्र — सब एक ही जगह, बड़े व स्पष्ट अक्षरों में।</p>
      <div class="search-box">
        <span class="material-icons" aria-hidden="true">search</span>
        <input type="text" id="site-search" placeholder="जैसे: बजरंग बाण, आरती..." aria-label="Search prayers">
      </div>
      <div class="btn-row">
        <a class="btn btn-primary" href="{BASE_PATH}/hanuman-chalisa/">हनुमान चालीसा पढ़ें</a>
        <a class="btn btn-outline" href="{BASE_PATH}/blog/">ब्लॉग पढ़ें</a>
      </div>
    </div>
    <div class="hero-illustration">{devotional_photo("hero-hanuman-blessing", "भगवान हनुमान जी आशीर्वाद मुद्रा में, चारों ओर राम-नाम की आभा", width=736, height=1104, loading="eager", fetchpriority="high")}</div>
  </div>
</section>

<div class="container">{ad("wide")}</div>

<section class="section" id="prayers">
  <div class="container">
    <div class="section-head"><h2>सभी पवित्र पाठ</h2><p>जिस भी प्रार्थना की आपको तलाश है, उसे नीचे से चुनें</p></div>
    <div class="grid grid-3">{cards}</div>
    <p id="search-no-results" style="display:none;text-align:center;color:var(--text-muted);margin-top:20px">कोई परिणाम नहीं मिला। कृपया कोई अन्य शब्द आज़माएं।</p>
  </div>
</section>

<section class="section" style="background:var(--bg-soft)">
  <div class="container">
    <div class="section-head"><h2>हनुमान चालीसा के लाभ</h2><p>नियमित पाठ से मिलने वाले मुख्य लाभ</p></div>
    <div class="grid grid-4">{benefits_cards}</div>
  </div>
</section>

<section class="section">
  <div class="container">
    <div class="section-head"><h2>रोज़ाना पाठ क्यों करें?</h2></div>
    <div style="max-width:760px;margin:0 auto" class="text-center">
      <p>हिंदू परंपरा में हनुमान जी को संकटमोचन कहा जाता है — यानी संकटों को हरने वाले। प्रतिदिन श्रद्धा से पाठ करने से मन में स्थिरता, साहस और सकारात्मकता आती है। यह न केवल एक धार्मिक अनुष्ठान है, बल्कि आत्मबल बढ़ाने का एक सरल माध्यम भी है।</p>
    </div>
  </div>
</section>

<div class="container">{ad("wide")}</div>

<section class="section" style="background:var(--bg-soft)">
  <div class="container">
    <div class="section-head"><h2>नवीनतम लेख</h2></div>
    <div class="grid grid-3">{popular_posts}</div>
  </div>
</section>

<section class="section">
  <div class="container">
    <div class="section-head"><h2>भक्तों के अनुभव</h2></div>
    <div class="grid grid-3">{testimonials}</div>
  </div>
</section>

{faq_block([
    ("क्या हनुमान चालीसा रोज़ पढ़ी जा सकती है?", "हां, प्रतिदिन श्रद्धा और नियम से हनुमान चालीसा पढ़ना अत्यंत शुभ माना जाता है।"),
    ("संकट के समय कौन सा पाठ करें?", "संकट के समय बजरंग बाण और संकट मोचन स्तोत्र पढ़ना विशेष रूप से लाभकारी माना जाता है।"),
    ("क्या यह वेबसाइट मुफ्त है?", "हां, इस वेबसाइट पर सभी पाठ, अर्थ और जानकारी पूरी तरह से निःशुल्क उपलब्ध हैं।"),
])}

<section class="section">
  <div class="container">
    <div class="newsletter">
      <h2>साप्ताहिक भक्ति न्यूज़लेटर पाएं</h2>
      <p>नए लेख, पूजा विधि और त्योहारों की जानकारी सीधे अपने ईमेल पर पाएं।</p>
      <form id="newsletter-form">
        <input type="email" required placeholder="आपका ईमेल पता" aria-label="Email address">
        <button class="btn btn-primary" type="submit">सब्सक्राइब करें</button>
      </form>
      <small class="nl-msg"></small>
    </div>
  </div>
</section>
'''
    html = page(
        title="हनुमान चालीसा हिंदी में | Hanuman Chalisa, Bajrang Baan, Aarti — पूर्ण पाठ",
        description="हनुमान चालीसा, बजरंग बाण, हनुमान अष्टक, संकट मोचन, हनुमान आरती और हनुमान मंत्र हिंदी में पढ़ें — शुद्ध पाठ, अर्थ और लाभ सहित, पूरी तरह मुफ्त।",
        path=path,
        body=body,
        keywords="hanuman chalisa, hanuman chalisa hindi, bajrang baan, hanuman aarti, hanuman ashtak, sankat mochan, हनुमान चालीसा हिंदी",
        active=path,
    )
    write("index.html", html)

home_page()

# ============================================================
# HANUMAN MANTRAS PAGE
# ============================================================
def mantras_page():
    path = "/hanuman-mantras/"
    cards = "".join(f'''<div class="card">
  <span class="material-icons">self_improvement</span>
  <h3>{name}</h3>
  <p class="prayer-text" style="padding:14px 16px;font-weight:600;color:var(--secondary);box-shadow:none;margin:10px 0">{mantra}</p>
  <p>{meaning}</p>
</div>''' for name, mantra, meaning in MANTRAS)
    body = f'''<section class="hero" style="padding:40px 0 30px"><div class="container" style="grid-template-columns:1fr;text-align:center">
<div>{devotional_photo("hanuman-namaskar-ram", "भगवान हनुमान जी राम-नाम जाप की मुद्रा में", css_class="img-frame hero-avatar", width=736, height=1308)}
<span class="hero-eyebrow"><span class="material-icons" style="font-size:1rem">self_improvement</span> मंत्र संग्रह</span>
<h1>हनुमान मंत्र</h1>
<p class="lead" style="margin:0 auto">शक्ति, सुरक्षा और संकट-निवारण के लिए हनुमान जी के प्रमुख मंत्र, अर्थ सहित।</p></div>
</div></section>
<div class="container">
{ad("wide")}
<div class="grid grid-2">{cards}</div>
{gada()}
<section><h2>मंत्र जाप विधि</h2><p>स्वच्छ स्थान पर बैठें, हनुमान जी का ध्यान करें और माला से 108 बार मंत्र का जाप करें। नियमित जाप से मन एकाग्र होता है और इच्छित फल की प्राप्ति होती है।</p></section>
</div>
{faq_block([
    ("हनुमान मंत्र जाप का सही समय क्या है?", "प्रातःकाल ब्रह्म मुहूर्त में मंत्र जाप करना सर्वोत्तम माना जाता है।"),
    ("क्या मंत्र जाप के लिए माला ज़रूरी है?", "माला से जाप करना पारंपरिक और सुविधाजनक तरीका है, परंतु बिना माला के भी श्रद्धा से जाप किया जा सकता है।"),
])}
{related_articles([
    ("हनुमान चालीसा", "/hanuman-chalisa/", "मंत्र जाप से पहले हनुमान चालीसा पढ़ें।"),
    ("बजरंग बाण", "/bajrang-baan/", "संकट से मुक्ति के लिए बजरंग बाण पढ़ें।"),
    ("पूजा विधि", "/blog/tuesday-hanuman-puja-vidhi/", "मंगलवार की पूजा विधि जानें।"),
])}
'''
    html = page(
        title="हनुमान मंत्र | Powerful Hanuman Mantras in Hindi with Meaning",
        description="हनुमान जी के शक्तिशाली बीज मंत्र, पंचमुखी मंत्र और संकटमोचन मंत्र हिंदी अर्थ सहित पढ़ें।",
        path=path, body=body, active=path,
        keywords="hanuman mantra, hanuman beej mantra, हनुमान मंत्र, panchmukhi hanuman mantra",
        schema_extra=breadcrumb_schema([("हनुमान मंत्र", None)]),
        breadcrumbs=[("हनुमान मंत्र", None)],
    )
    write("hanuman-mantras/index.html", html)

mantras_page()
print("Home + Mantras pages generated.")
