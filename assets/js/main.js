/* Hanuman Chalisa Hindi — main.js
   Vanilla JS, no dependencies. Handles theme, nav, progress bar,
   back-to-top, FAQ accordions, prayer tools (copy/print/font-size/bookmark/share),
   and a lightweight client-side search across quick nav links. */
(function(){
  "use strict";

  /* ---------- Theme toggle ---------- */
  var root = document.documentElement;
  var THEME_KEY = "hcx-theme";
  function applyTheme(t, animateBtn){
    if(t === "dark"){ root.setAttribute("data-theme","dark"); }
    else { root.removeAttribute("data-theme"); }
    var btn = document.getElementById("theme-toggle");
    if(btn){
      btn.innerHTML = t === "dark" ? '<span class="material-icons" aria-hidden="true">light_mode</span>' : '<span class="material-icons" aria-hidden="true">dark_mode</span>';
      if(animateBtn){
        btn.classList.remove("spin");
        void btn.offsetWidth; /* restart animation */
        btn.classList.add("spin");
      }
    }
  }
  var savedTheme = null;
  try{ savedTheme = localStorage.getItem(THEME_KEY); }catch(e){}
  if(!savedTheme && window.matchMedia && window.matchMedia("(prefers-color-scheme: dark)").matches){ savedTheme = "dark"; }
  applyTheme(savedTheme, false);
  document.addEventListener("click", function(e){
    var btn = e.target.closest("#theme-toggle");
    if(!btn) return;
    var current = root.getAttribute("data-theme") === "dark" ? "dark" : "light";
    var next = current === "dark" ? "light" : "dark";
    applyTheme(next, true);
    try{ localStorage.setItem(THEME_KEY, next); }catch(err){}
  });

  /* ---------- Mobile nav ---------- */
  document.addEventListener("click", function(e){
    var toggle = e.target.closest("#menu-toggle");
    if(toggle){
      var nav = document.getElementById("nav-links");
      var expanded = toggle.getAttribute("aria-expanded") === "true";
      toggle.setAttribute("aria-expanded", String(!expanded));
      if(nav) nav.classList.toggle("open");
      return;
    }
    if(e.target.closest(".nav-links a")){
      var navEl = document.getElementById("nav-links");
      if(navEl) navEl.classList.remove("open");
    }
  });

  /* ---------- Reading progress bar ---------- */
  var progressBar = document.getElementById("progress-bar");
  function updateProgress(){
    if(!progressBar) return;
    var h = document.documentElement;
    var scrollTop = h.scrollTop || document.body.scrollTop;
    var scrollHeight = (h.scrollHeight || document.body.scrollHeight) - h.clientHeight;
    var pct = scrollHeight > 0 ? (scrollTop / scrollHeight) * 100 : 0;
    progressBar.style.width = pct + "%";
  }
  document.addEventListener("scroll", updateProgress, { passive: true });
  updateProgress();

  /* ---------- Back to top ---------- */
  var backToTop = document.getElementById("back-to-top");
  function toggleBackToTop(){
    if(!backToTop) return;
    if(window.scrollY > 400){ backToTop.classList.add("show"); }
    else { backToTop.classList.remove("show"); }
  }
  document.addEventListener("scroll", toggleBackToTop, { passive: true });
  toggleBackToTop();
  if(backToTop){
    backToTop.addEventListener("click", function(){
      window.scrollTo({ top: 0, behavior: "smooth" });
    });
  }

  /* ---------- FAQ accordion ---------- */
  document.addEventListener("click", function(e){
    var q = e.target.closest(".faq-q");
    if(!q) return;
    var item = q.closest(".faq-item");
    var wasOpen = item.classList.contains("open");
    item.parentElement.querySelectorAll(".faq-item.open").forEach(function(el){ if(el!==item) el.classList.remove("open"); });
    item.classList.toggle("open", !wasOpen);
    q.setAttribute("aria-expanded", String(!wasOpen));
  });

  /* ---------- Prayer toolbar: font size ---------- */
  var fontStep = 0;
  document.addEventListener("click", function(e){
    var body = document.getElementById("prayer-body");
    if(e.target.closest("#font-inc") && body){
      fontStep = Math.min(fontStep + 1, 5);
      body.style.fontSize = (1.15 + fontStep * 0.12) + "rem";
    }
    if(e.target.closest("#font-dec") && body){
      fontStep = Math.max(fontStep - 1, -3);
      body.style.fontSize = (1.15 + fontStep * 0.12) + "rem";
    }
  });

  /* ---------- Copy text ---------- */
  document.addEventListener("click", function(e){
    var btn = e.target.closest("#copy-text");
    if(!btn) return;
    var body = document.getElementById("prayer-body");
    if(!body) return;
    var text = body.innerText;
    if(navigator.clipboard){
      navigator.clipboard.writeText(text).then(function(){
        flashLabel(btn, "Copied!");
      }).catch(function(){ flashLabel(btn, "Copy failed"); });
    }
  });
  function flashLabel(btn, msg){
    var original = btn.getAttribute("data-label") || btn.textContent;
    btn.setAttribute("data-label", original);
    btn.textContent = msg;
    setTimeout(function(){ btn.textContent = original; }, 1600);
  }

  /* ---------- Print ---------- */
  document.addEventListener("click", function(e){
    if(e.target.closest("#print-page")){ window.print(); }
  });

  /* ---------- Share ---------- */
  document.addEventListener("click", function(e){
    var btn = e.target.closest("#share-page");
    if(!btn) return;
    var shareData = { title: document.title, url: window.location.href };
    if(navigator.share){
      navigator.share(shareData).catch(function(){});
    } else if(navigator.clipboard){
      navigator.clipboard.writeText(window.location.href);
      flashLabel(btn, "Link copied!");
    }
  });

  /* ---------- Bookmark (localStorage) ---------- */
  document.addEventListener("click", function(e){
    var btn = e.target.closest("#bookmark-page");
    if(!btn) return;
    var key = "hcx-bookmarks";
    var url = window.location.pathname;
    var list = [];
    try{ list = JSON.parse(localStorage.getItem(key)) || []; }catch(err){}
    if(list.indexOf(url) === -1){
      list.push(url);
      flashLabel(btn, "Saved!");
    } else {
      list = list.filter(function(u){ return u !== url; });
      flashLabel(btn, "Removed");
    }
    try{ localStorage.setItem(key, JSON.stringify(list)); }catch(err){}
  });

  /* ---------- Simple homepage search ---------- */
  document.addEventListener("input", function(e){
    if(e.target.id !== "site-search") return;
    var q = e.target.value.trim().toLowerCase();
    var anyVisible = false;
    document.querySelectorAll("[data-search-item]").forEach(function(card){
      var text = card.getAttribute("data-search-item").toLowerCase();
      var match = (q === "" || text.indexOf(q) !== -1);
      card.style.display = match ? "" : "none";
      if(match) anyVisible = true;
    });
    var noResults = document.getElementById("search-no-results");
    if(noResults) noResults.style.display = (q !== "" && !anyVisible) ? "" : "none";
    if(q !== ""){
      var target = document.getElementById("prayers");
      if(target && target.getBoundingClientRect().top > window.innerHeight * 0.6){
        target.scrollIntoView({behavior:"smooth", block:"start"});
      }
    }
  });

  /* ---------- Newsletter (static demo, no backend) ---------- */
  document.addEventListener("submit", function(e){
    var form = e.target.closest("#newsletter-form");
    if(!form) return;
    e.preventDefault();
    var msg = form.querySelector(".nl-msg");
    if(msg) msg.textContent = "धन्यवाद! आप सफलतापूर्वक सब्सक्राइब हो गए हैं।";
    form.reset();
  });

  /* ---------- Contact form (static demo, no backend) ---------- */
  document.addEventListener("submit", function(e){
    var form = e.target.closest("#contact-form");
    if(!form) return;
    e.preventDefault();
    var msg = form.querySelector(".form-msg");
    if(msg) msg.textContent = "धन्यवाद! आपका संदेश प्राप्त हो गया है। हम जल्द ही संपर्क करेंगे।";
    form.reset();
  });

  /* ---------- Scroll reveal (fade + slide-in) ----------
     .reveal is only ever added here, in JS — so if this never runs
     (no JS, older browser, reduced motion) content stays fully visible.
     Scoped to small decorative elements only (cards/testimonials/newsletter)
     — never whole .section blocks or .prayer-text, so a slow/failed
     IntersectionObserver callback (print, full-page screenshot/crawler
     capture before the browser fires it) can never blank out real content.
     A timed fallback also force-reveals everything as a safety net. */
  var reduceMotion = window.matchMedia && window.matchMedia("(prefers-reduced-motion: reduce)").matches;
  if(!reduceMotion && "IntersectionObserver" in window){
    var revealTargets = document.querySelectorAll(".card, .testimonial, .newsletter");
    if(revealTargets.length){
      var io = new IntersectionObserver(function(entries){
        entries.forEach(function(entry){
          if(entry.isIntersecting){
            entry.target.classList.add("in-view");
            io.unobserve(entry.target);
          }
        });
      }, { threshold: 0.12, rootMargin: "0px 0px -40px 0px" });
      revealTargets.forEach(function(el, i){
        el.classList.add("reveal");
        el.style.transitionDelay = Math.min((i % 6) * 60, 240) + "ms";
        io.observe(el);
      });
      setTimeout(function(){
        revealTargets.forEach(function(el){ el.classList.add("in-view"); });
      }, 1800);
    }
  }

  /* ---------- Mobile TOC bottom-sheet (long prayer pages) ---------- */
  document.addEventListener("click", function(e){
    var toc = document.getElementById("page-toc");
    if(!toc) return;
    var fab = e.target.closest("#toc-fab");
    var closeBtn = e.target.closest("#toc-close");
    var tocLink = e.target.closest("#page-toc a");
    if(fab){
      var isOpen = toc.classList.toggle("open");
      fab.setAttribute("aria-expanded", String(isOpen));
    } else if(closeBtn || tocLink){
      toc.classList.remove("open");
      var fabBtn = document.getElementById("toc-fab");
      if(fabBtn) fabBtn.setAttribute("aria-expanded", "false");
    }
  });

})();
