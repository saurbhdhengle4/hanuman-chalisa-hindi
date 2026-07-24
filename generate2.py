# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from build import *
from generate import faq_block, related_articles, gada

def simple_page(path, title, meta_desc, heading, body_html, keywords="", active="", schema_extra=""):
    body = f'''<section class="section" style="padding-top:32px">
  <div class="container" style="max-width:820px">
    <h1>{heading}</h1>
    {body_html}
  </div>
</section>'''
    html = page(title=title, description=meta_desc, path=path, body=body, keywords=keywords,
                active=active, schema_extra=schema_extra + breadcrumb_schema([(heading, None)]),
                breadcrumbs=[(heading, None)])
    write((path.strip("/") + "/index.html") if path != "/" else "index.html", html)

# ---------------- About ----------------
simple_page(
    "/about/", "About Us | Hanuman Chalisa Hindi",
    "जानें Hanuman Chalisa Hindi वेबसाइट के बारे में — हमारा उद्देश्य हर भक्त तक शुद्ध हनुमान भक्ति सामग्री पहुंचाना है।",
    "About Us",
    f'''<p><strong>Hanuman Chalisa Hindi</strong> एक भक्ति-केंद्रित वेबसाइट है, जिसका उद्देश्य हनुमान चालीसा, बजरंग बाण, हनुमान अष्टक, संकट मोचन स्तोत्र, हनुमान आरती और हनुमान मंत्रों को शुद्ध, स्पष्ट और सरल हिंदी में हर भक्त तक पहुंचाना है।</p>
    <p>हम मानते हैं कि आस्था और तकनीक साथ मिलकर भक्तों के अनुभव को और सरल बना सकते हैं। इसी सोच के साथ हमने यह वेबसाइट बनाई है — बड़े अक्षर, डार्क मोड, प्रिंट व डाउनलोड सुविधा, और मोबाइल-फ्रेंडली डिज़ाइन के साथ।</p>
    <figure style="margin:32px 0;text-align:center">
      {devotional_photo("hanuman-ram-shila-lekhan", "भगवान हनुमान जी शिला पर श्रद्धा से 'राम' नाम लिखते हुए", css_class="img-frame about-feature", width=735, height=917)}
      <figcaption class="muted" style="margin-top:12px;font-size:.9rem">श्रद्धा और समर्पण — भगवान हनुमान जी सदैव श्रीराम के नाम-स्मरण में लीन रहते हैं</figcaption>
    </figure>
    <h2>हमारा उद्देश्य</h2>
    <ul>
      <li>शुद्ध और प्रामाणिक पाठ उपलब्ध कराना</li>
      <li>हर उम्र के भक्तों के लिए सुलभ पठन अनुभव</li>
      <li>निःशुल्क, बिना किसी शुल्क के सामग्री प्रदान करना</li>
    </ul>
    <p>यदि आपके पास कोई सुझाव है, तो कृपया हमारे <a href="{BASE_PATH}/contact/">संपर्क पृष्ठ</a> के माध्यम से हमसे जुड़ें।</p>''',
    keywords="about hanuman chalisa hindi, about us", active="/about/"
)

# ---------------- Contact ----------------
contact_body = '''<p>आपके सुझाव और प्रश्नों का स्वागत है। नीचे दिए गए फॉर्म को भरें, हम जल्द ही आपसे संपर्क करेंगे।</p>
<form class="contact-form" id="contact-form">
  <div><label for="c-name">नाम</label><input id="c-name" type="text" required placeholder="आपका नाम"></div>
  <div><label for="c-email">ईमेल</label><input id="c-email" type="email" required placeholder="आपका ईमेल"></div>
  <div><label for="c-msg">संदेश</label><textarea id="c-msg" required placeholder="अपना संदेश लिखें..."></textarea></div>
  <button class="btn btn-primary" type="submit" style="width:fit-content">संदेश भेजें</button>
  <p class="form-msg" style="color:var(--secondary);font-weight:600"></p>
</form>
<p style="margin-top:24px">ईमेल: <a href="mailto:contact@hanumanchalisahindi.com">contact@hanumanchalisahindi.com</a></p>'''
simple_page("/contact/", "Contact Us | Hanuman Chalisa Hindi",
    "Hanuman Chalisa Hindi वेबसाइट से संपर्क करें — प्रश्न, सुझाव या फीडबैक भेजें।",
    "Contact Us", contact_body, keywords="contact hanuman chalisa hindi", active="/contact/")

# ---------------- Privacy Policy ----------------
simple_page("/privacy-policy/", "Privacy Policy | Hanuman Chalisa Hindi",
    "Hanuman Chalisa Hindi की गोपनीयता नीति पढ़ें — जानें हम आपकी जानकारी का उपयोग और सुरक्षा कैसे करते हैं.",
    "Privacy Policy",
    f'''<p><em>अंतिम अद्यतन: जनवरी 2026</em></p>
    <p>Hanuman Chalisa Hindi (यह वेबसाइट) आपकी गोपनीयता का सम्मान करती है। यह नीति बताती है कि हम किस प्रकार की जानकारी एकत्र करते हैं और उसका उपयोग कैसे करते हैं।</p>
    <h2>1. एकत्रित जानकारी</h2>
    <p>हम केवल वही जानकारी एकत्र करते हैं जो आप संपर्क फॉर्म या न्यूज़लेटर सब्सक्रिप्शन के माध्यम से स्वेच्छा से प्रदान करते हैं, जैसे नाम और ईमेल पता।</p>
    <h2>2. कुकीज़ और विज्ञापन</h2>
    <p>यह वेबसाइट थर्ड-पार्टी विज्ञापन सेवाओं (जैसे Google AdSense) का उपयोग कर सकती है, जो कुकीज़ के माध्यम से प्रासंगिक विज्ञापन दिखाने हेतु जानकारी एकत्र कर सकती हैं। आप अपने ब्राउज़र सेटिंग्स से कुकीज़ को नियंत्रित कर सकते हैं।</p>
    <h2>3. डेटा सुरक्षा</h2>
    <p>हम आपकी जानकारी को सुरक्षित रखने के लिए उचित तकनीकी उपाय अपनाते हैं। हालांकि, इंटरनेट पर किसी भी डेटा ट्रांसमिशन की 100% सुरक्षा की गारंटी नहीं दी जा सकती।</p>
    <h2>4. तृतीय-पक्ष लिंक</h2>
    <p>हमारी वेबसाइट पर अन्य वेबसाइटों के लिंक हो सकते हैं। हम उन वेबसाइटों की गोपनीयता प्रथाओं के लिए जिम्मेदार नहीं हैं।</p>
    <h2>5. नीति में बदलाव</h2>
    <p>हम समय-समय पर इस नीति को अपडेट कर सकते हैं। किसी भी बदलाव की जानकारी इसी पृष्ठ पर दी जाएगी।</p>
    <h2>संपर्क करें</h2>
    <p>प्रश्नों के लिए <a href="{BASE_PATH}/contact/">Contact Us</a> पृष्ठ पर जाएं।</p>''',
    keywords="privacy policy hanuman chalisa hindi", active="/privacy-policy/")

# ---------------- Disclaimer ----------------
simple_page("/disclaimer/", "Disclaimer | Hanuman Chalisa Hindi",
    "Hanuman Chalisa Hindi वेबसाइट का डिस्क्लेमर पढ़ें।",
    "Disclaimer",
    '''<p>इस वेबसाइट पर उपलब्ध सभी सामग्री (हनुमान चालीसा, बजरंग बाण, हनुमान अष्टक, आरती, स्तोत्र, मंत्र व ब्लॉग लेख) केवल सामान्य जानकारी और धार्मिक/आध्यात्मिक उद्देश्यों के लिए प्रदान की गई है।</p>
    <p>यह सामग्री पारंपरिक ग्रंथों और लोक-प्रचलित पाठों पर आधारित है। पाठों के शब्दों में क्षेत्रीय भिन्नता हो सकती है। हम किसी भी प्रकार की चिकित्सीय, कानूनी या वित्तीय सलाह प्रदान नहीं करते।</p>
    <p>वेबसाइट पर दी गई जानकारी का उपयोग स्वयं के विवेक से करें। किसी भी हानि या नुकसान के लिए वेबसाइट उत्तरदायी नहीं होगी।</p>''',
    keywords="disclaimer hanuman chalisa hindi", active="/disclaimer/")

# ---------------- Terms ----------------
simple_page("/terms/", "Terms & Conditions | Hanuman Chalisa Hindi",
    "Hanuman Chalisa Hindi वेबसाइट की नियम व शर्तें पढ़ें।",
    "Terms & Conditions",
    '''<p>इस वेबसाइट का उपयोग करके, आप निम्नलिखित नियमों और शर्तों से सहमत होते हैं:</p>
    <h2>1. सामग्री का उपयोग</h2>
    <p>इस वेबसाइट की सामग्री केवल व्यक्तिगत और गैर-व्यावसायिक उपयोग के लिए है। सामग्री के पुनर्प्रकाशन के लिए हमसे अनुमति लें।</p>
    <h2>2. उपयोगकर्ता आचरण</h2>
    <p>आप वेबसाइट का उपयोग किसी भी गैरकानूनी उद्देश्य के लिए नहीं करेंगे।</p>
    <h2>3. दायित्व की सीमा</h2>
    <p>वेबसाइट "जैसा है" के आधार पर प्रदान की जाती है। हम किसी भी प्रकार की स्पष्ट या अंतर्निहित गारंटी नहीं देते।</p>
    <h2>4. परिवर्तन</h2>
    <p>हम बिना पूर्व सूचना के इन शर्तों को कभी भी संशोधित करने का अधिकार सुरक्षित रखते हैं।</p>''',
    keywords="terms and conditions hanuman chalisa hindi", active="/terms/")

# ---------------- Blog Index ----------------
POSTS = [
    ("benefits-of-hanuman-chalisa", "हनुमान चालीसा पढ़ने के 10 अद्भुत लाभ",
     "हनुमान चालीसा के नियमित पाठ के मानसिक, आध्यात्मिक और शारीरिक लाभों की पूरी जानकारी।",
     "पूजा-पाठ"),
    ("best-time-to-read-hanuman-chalisa", "हनुमान चालीसा पढ़ने का सही समय क्या है?",
     "जानें ब्रह्म मुहूर्त, संध्या और विशेष दिनों में हनुमान चालीसा पढ़ने का महत्व।",
     "मार्गदर्शन"),
    ("who-wrote-hanuman-chalisa", "हनुमान चालीसा किसने लिखी? पूरा इतिहास",
     "गोस्वामी तुलसीदास द्वारा हनुमान चालीसा की रचना की संपूर्ण कहानी और पृष्ठभूमि।",
     "इतिहास"),
    ("tuesday-hanuman-puja-vidhi", "मंगलवार हनुमान पूजा विधि — पूरी जानकारी",
     "मंगलवार को हनुमान जी की पूजा कैसे करें — सामग्री, विधि और मंत्रों की पूरी सूची।",
     "पूजा विधि"),
]

def blog_index():
    cards = "".join(f'''<a class="card blog-card" href="{BASE_PATH}/blog/{slug}/" data-search-item="{title}">
  <span class="tag">{tag}</span>
  <h3>{title}</h3><p>{desc}</p>
  <span class="blog-meta">5 मिनट पढ़ें</span>
</a>''' for slug, title, desc, tag in POSTS)
    body = f'''<section class="hero" style="padding:40px 0 30px"><div class="container" style="grid-template-columns:1fr;text-align:center">
<div><span class="hero-eyebrow"><span class="material-icons" style="font-size:1rem">rss_feed</span> ब्लॉग</span>
<h1>हनुमान भक्ति ब्लॉग</h1>
<p class="lead" style="margin:0 auto">पूजा विधि, महत्व, इतिहास और हनुमान भक्ति से जुड़े लेख पढ़ें।</p></div>
</div></section>
<div class="container">
{ad("wide")}
<div class="grid grid-3">{cards}</div>
</div>'''
    html = page(title="Blog | Hanuman Chalisa Hindi", description="हनुमान भक्ति, पूजा विधि, त्योहार और इतिहास से जुड़े SEO लेख पढ़ें।",
                path="/blog/", body=body, active="/blog/", keywords="hanuman blog, hanuman chalisa articles",
                schema_extra=breadcrumb_schema([("Blog", None)]), breadcrumbs=[("Blog", None)])
    write("blog/index.html", html)

blog_index()

def blog_post(slug, title, desc, tag, content_html, faqs, related):
    path = f"/blog/{slug}/"
    body = f'''<article class="section" style="padding-top:24px">
  <div class="container" style="max-width:820px">
    <span class="tag-pill">{tag}</span>
    <h1 style="margin-top:14px">{title}</h1>
    <p class="muted">5 मिनट पढ़ें &middot; अद्यतन: जनवरी 2026</p>
    {ad("wide")}
    {content_html}
    {gada()}
  </div>
</article>
{faq_block(faqs)}
{related_articles(related)}'''
    schema = article_schema(title, desc, path) + faq_schema(faqs) + breadcrumb_schema([("Blog", "/blog/"), (title, None)])
    html = page(title=f"{title} | Hanuman Chalisa Hindi Blog", description=desc, path=path, body=body,
                active="/blog/", keywords=title, schema_extra=schema, breadcrumbs=[("Blog", "/blog/"), (title, None)])
    write(f"blog/{slug}/index.html", html)

blog_post(
    "benefits-of-hanuman-chalisa", "हनुमान चालीसा पढ़ने के 10 अद्भुत लाभ",
    "हनुमान चालीसा के नियमित पाठ के मानसिक, आध्यात्मिक और शारीरिक लाभों की पूरी जानकारी।", "पूजा-पाठ",
    f'''<p>हनुमान चालीसा केवल एक धार्मिक पाठ नहीं, बल्कि आत्मबल और मानसिक शांति पाने का एक सरल साधन है। आइए जानते हैं इसके प्रमुख लाभ।</p>
    <h2>1. मानसिक शांति</h2><p>नियमित पाठ से मन शांत होता है और तनाव में कमी आती है।</p>
    <h2>2. भय से मुक्ति</h2><p>अज्ञात भय और नकारात्मक विचारों को दूर करने में सहायक माना जाता है।</p>
    <h2>3. आत्मविश्वास में वृद्धि</h2><p>कठिन समय में साहस और आत्मबल बढ़ता है।</p>
    <h2>4. एकाग्रता में सुधार</h2><p>नियमित पाठ से ध्यान और एकाग्रता क्षमता में सुधार होता है।</p>
    <h2>5. सकारात्मक ऊर्जा</h2><p>घर में सकारात्मक वातावरण बनाए रखने में सहायक।</p>
    <p>पूरा पाठ पढ़ने के लिए हमारा <a href="{BASE_PATH}/hanuman-chalisa/">हनुमान चालीसा पृष्ठ</a> देखें।</p>''',
    faqs=[("क्या हनुमान चालीसा के वैज्ञानिक लाभ भी हैं?", "पाठ के दौरान गहरी सांस व एकाग्रता से मानसिक शांति मिलती है, जो तनाव कम करने में सहायक मानी जाती है।")],
    related=[("हनुमान चालीसा", "/hanuman-chalisa/", "पूर्ण पाठ पढ़ें।"),
             ("पढ़ने का सही समय", "/blog/best-time-to-read-hanuman-chalisa/", "कब पढ़ें, जानें।"),
             ("बजरंग बाण", "/bajrang-baan/", "संकट से मुक्ति के लिए पढ़ें।")]
)

blog_post(
    "best-time-to-read-hanuman-chalisa", "हनुमान चालीसा पढ़ने का सही समय क्या है?",
    "जानें ब्रह्म मुहूर्त, संध्या और विशेष दिनों में हनुमान चालीसा पढ़ने का महत्व।", "मार्गदर्शन",
    '''<p>हनुमान चालीसा पढ़ने के लिए समय का विशेष महत्व है। सही समय पर पाठ करने से इसका प्रभाव और भी अधिक शुभ माना जाता है।</p>
    <h2>ब्रह्म मुहूर्त (सुबह 4-6 बजे)</h2><p>यह समय सबसे शुद्ध और शांत माना जाता है, जो पाठ के लिए सर्वोत्तम है।</p>
    <h2>संध्या काल</h2><p>सूर्यास्त के बाद संध्या पूजा के समय भी पाठ करना शुभ माना जाता है।</p>
    <h2>मंगलवार और शनिवार</h2><p>यह दोनों दिन हनुमान जी को समर्पित माने जाते हैं और इन दिनों पाठ करना विशेष फलदायी है।</p>''',
    faqs=[("क्या रात में हनुमान चालीसा पढ़ सकते हैं?", "हां, परंतु परंपरागत रूप से सुबह या संध्या का समय अधिक शुभ माना जाता है।")],
    related=[("हनुमान चालीसा", "/hanuman-chalisa/", "पूर्ण पाठ पढ़ें।"),
             ("मंगलवार पूजा विधि", "/blog/tuesday-hanuman-puja-vidhi/", "पूरी विधि जानें।"),
             ("हनुमान मंत्र", "/hanuman-mantras/", "शक्तिशाली मंत्र पढ़ें।")]
)

blog_post(
    "who-wrote-hanuman-chalisa", "हनुमान चालीसा किसने लिखी? पूरा इतिहास",
    "गोस्वामी तुलसीदास द्वारा हनुमान चालीसा की रचना की संपूर्ण कहानी और पृष्ठभूमि।", "इतिहास",
    '''<p>हनुमान चालीसा की रचना 16वीं शताब्दी में महान संत-कवि गोस्वामी तुलसीदास जी ने अवधी भाषा में की थी।</p>
    <h2>तुलसीदास जी कौन थे?</h2><p>तुलसीदास जी रामचरितमानस के रचयिता थे और उन्हें भगवान राम का परम भक्त माना जाता है।</p>
    <h2>चालीसा की रचना क्यों हुई?</h2><p>माना जाता है कि हनुमान जी के प्रति अपनी अटूट भक्ति व्यक्त करने के लिए तुलसीदास जी ने यह चालीसा रची, जिसमें 40 चौपाइयां और 2 दोहे हैं।</p>''',
    faqs=[("हनुमान चालीसा किस भाषा में लिखी गई है?", "यह अवधी भाषा में लिखी गई है, जो हिंदी की एक बोली है।")],
    related=[("हनुमान चालीसा", "/hanuman-chalisa/", "पूर्ण पाठ पढ़ें।"),
             ("हनुमान अष्टक", "/hanuman-ashtak/", "तुलसीदास रचित अष्टक पढ़ें।"),
             ("हनुमान चालीसा के लाभ", "/blog/benefits-of-hanuman-chalisa/", "लाभ जानें।")]
)

blog_post(
    "tuesday-hanuman-puja-vidhi", "मंगलवार हनुमान पूजा विधि — पूरी जानकारी",
    "मंगलवार को हनुमान जी की पूजा कैसे करें — सामग्री, विधि और मंत्रों की पूरी सूची।", "पूजा विधि",
    '''<p>मंगलवार का दिन हनुमान जी को समर्पित माना जाता है। इस दिन विधिपूर्वक पूजा करने से विशेष फल की प्राप्ति होती है।</p>
    <h2>पूजा सामग्री</h2><p>सिंदूर, चमेली का तेल, लाल फूल, चोला, प्रसाद (बूंदी या गुड़-चना), दीपक और अगरबत्ती।</p>
    <h2>पूजा विधि</h2><p>स्नान कर स्वच्छ वस्त्र पहनें। हनुमान जी को सिंदूर व चोला अर्पित करें, दीप जलाएं और हनुमान चालीसा व आरती का पाठ करें।</p>
    <h2>मंत्र जाप</h2><p>पूजा के दौरान "ॐ हं हनुमते नमः" मंत्र का 108 बार जाप करें।</p>''',
    faqs=[("मंगलवार को क्या नहीं करना चाहिए?", "इस दिन मांस-मदिरा का सेवन और नकारात्मक विचारों से दूर रहने की सलाह दी जाती है।")],
    related=[("हनुमान आरती", "/hanuman-aarti/", "पूजा के अंत में आरती पढ़ें।"),
             ("हनुमान मंत्र", "/hanuman-mantras/", "पूजा में उपयोग होने वाले मंत्र।"),
             ("हनुमान चालीसा", "/hanuman-chalisa/", "पूजा के दौरान पाठ करें।")]
)

# ---------------- 404 ----------------
def not_found_page():
    body = f'''<div class="error-page">
  <div class="code">404</div>
  <h1>पृष्ठ नहीं मिला</h1>
  <p class="muted" style="max-width:44ch">क्षमा करें, आप जिस पृष्ठ को खोज रहे हैं वह उपलब्ध नहीं है। हो सकता है यह हटा दिया गया हो या पता गलत हो।</p>
  <div class="btn-row">
    <a class="btn btn-primary" href="{BASE_PATH}/">होम पेज पर जाएं</a>
    <a class="btn btn-outline" href="{BASE_PATH}/hanuman-chalisa/">हनुमान चालीसा पढ़ें</a>
  </div>
</div>'''
    html = f'''<!DOCTYPE html>
<html lang="hi">
<head>
{head("पृष्ठ नहीं मिला (404) | Hanuman Chalisa Hindi", "यह पृष्ठ उपलब्ध नहीं है। होम पेज पर जाएं या हनुमान चालीसा पढ़ें।", "/404.html")}
</head>
<body>
{header_html("")}
<main>{body}</main>
{footer_html()}
</body>
</html>'''
    write("404.html", html)

not_found_page()
print("Static, blog, and 404 pages generated.")
