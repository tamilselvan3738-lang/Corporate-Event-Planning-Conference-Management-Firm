
    // 1. Framer Motion Scroll Trigger Observers
    document.addEventListener('DOMContentLoaded', function () {
      var motionClasses = [
        '.framer-folio-glide',
        '.framer-countdown-snap',
        '.framer-capex-reveal',
        '.framer-blueprint-draft',
        '.framer-dual-hemisphere',
        '.framer-editorial-rise',
        '.framer-vault-open'
      ];

      var motionObserver = new IntersectionObserver(function (entries, obs) {
        entries.forEach(function (entry) {
          if (entry.isIntersecting) {
            entry.target.classList.add('framer-in-view');
            var children = entry.target.querySelectorAll('.framer-folio-glide, .framer-countdown-snap, .framer-capex-reveal, .framer-blueprint-draft, .framer-dual-hemisphere, .framer-editorial-rise, .framer-vault-open');
            children.forEach(function (c, idx) {
              setTimeout(function () {
                c.classList.add('framer-in-view');
              }, idx * 80);
            });
            obs.unobserve(entry.target);
          }
        });
      }, {
        threshold: 0.15,
        rootMargin: '0px 0px -50px 0px'
      });

      motionClasses.forEach(function (selector) {
        document.querySelectorAll(selector).forEach(function (el) {
          motionObserver.observe(el);
        });
      });
    });

    // 2. Section 1: Folio Chapter Selector
    var folioChaptersData = [
      {
        title: "The Sovereign Summit Master Playbook (240 Pages)",
        desc: "Comprehensive blueprint detailing executive sponsor alignment, multi-track agenda design, crisis communication escalation trees, and real-time incident dispatching.",
        audience: "C-Suite & Directors",
        scale: "500 – 15,000 Pax",
        format: "PDF + Excel Toolkit"
      },
      {
        title: "Technical Production & Redundancy Protocol (180 Pages)",
        desc: "Touring-grade broadcast audio/video specifications, dual-homed optical fiber ring deployment, and backup uninterruptible generator load calculations.",
        audience: "Technical Producers",
        scale: "Keynote & Hybrid",
        format: "CAD + Tech Spec PDF"
      },
      {
        title: "Post-Event Analytics & Executive ROI Synthesis (95 Pages)",
        desc: "Statistical methodologies for measuring sponsor brand equity attribution, attendee retention metrics, and post-conference feedback survey synthesis.",
        audience: "CMOs & Stakeholders",
        scale: "Enterprise Global",
        format: "Dashboard + Slide Deck"
      }
    ];

    function selectFolioChapter(index) {
      var cards = document.querySelectorAll('.rc-chapter-card');
      cards.forEach(function (c, idx) {
        if (idx === index) c.classList.add('active');
        else c.classList.remove('active');
      });

      var data = folioChaptersData[index];
      var titleEl = document.getElementById('currentFolioTitle');
      var descEl = document.getElementById('currentFolioDesc');
      var audEl = document.getElementById('folioAudienceVal');
      var scaEl = document.getElementById('folioScaleVal');
      var fmtEl = document.getElementById('folioFormatVal');

      if (titleEl) {
        titleEl.style.opacity = '0';
        setTimeout(function () {
          titleEl.textContent = data.title;
          if (descEl) descEl.textContent = data.desc;
          if (audEl) audEl.textContent = data.audience;
          if (scaEl) scaEl.textContent = data.scale;
          if (fmtEl) fmtEl.textContent = data.format;
          titleEl.style.opacity = '1';
        }, 180);
      }
    }

    // 3. Section 2: Readiness Checklist Meter
    var currentReadiness = 100;
    function updateReadinessScore(cb, weight) {
      if (cb.checked) {
        currentReadiness += weight;
      } else {
        currentReadiness -= weight;
      }
      currentReadiness = Math.max(0, Math.min(100, currentReadiness));

      var fillEl = document.getElementById('readinessBarFill');
      var textEl = document.getElementById('readinessScoreText');

      if (fillEl) fillEl.style.width = currentReadiness + '%';
      if (textEl) {
        textEl.textContent = currentReadiness + '% Prepared';
        if (currentReadiness >= 85) textEl.style.color = '#10b981';
        else if (currentReadiness >= 60) textEl.style.color = '#f59e0b';
        else textEl.style.color = '#ef4444';
      }
    }

    // 4. Section 3: CapEx Budget Simulator
    function simulateBudget(pax, btn) {
      ['btnCap500', 'btnCap1500', 'btnCap5000'].forEach(function (id) {
        var b = document.getElementById(id);
        if (b) {
          b.className = 'rc-btn rc-btn-outline';
          b.style.padding = '0.5rem 1rem';
          b.style.fontSize = '0.85rem';
        }
      });
      btn.className = 'rc-btn rc-btn-primary';
      btn.style.padding = '0.5rem 1rem';
      btn.style.fontSize = '0.85rem';

      var costPerPax = 485;
      var total = pax * costPerPax;

      var venue = Math.round(total * 0.35);
      var av = Math.round(total * 0.28);
      var speaker = Math.round(total * 0.18);
      var scenic = Math.round(total * 0.12);
      var cont = Math.round(total * 0.07);

      document.getElementById('simTotalBudget').textContent = '$' + total.toLocaleString();
      document.getElementById('allocVenueText').textContent = '$' + venue.toLocaleString();
      document.getElementById('allocAvText').textContent = '$' + av.toLocaleString();
      document.getElementById('allocSpeakerText').textContent = '$' + speaker.toLocaleString();
      document.getElementById('allocScenicText').textContent = '$' + scenic.toLocaleString();
      document.getElementById('allocContingencyText').textContent = '$' + cont.toLocaleString();
    }

    // 5. Section 7: FAQ Accordion Toggle & Live Keyword Search
    function toggleAccordion(header) {
      var item = header.closest('.rc-accordion-item');
      var body = item.querySelector('.rc-accordion-body');
      var isActive = item.classList.contains('active');

      document.querySelectorAll('.rc-accordion-item').forEach(function (i) {
        i.classList.remove('active');
        var b = i.querySelector('.rc-accordion-body');
        if (b) b.style.maxHeight = '0px';
      });

      if (!isActive) {
        item.classList.add('active');
        if (body) body.style.maxHeight = body.scrollHeight + 30 + 'px';
      }
    }

    function filterFaqQuestions(query) {
      var q = query.toLowerCase().trim();
      var items = document.querySelectorAll('.rc-accordion-item');
      items.forEach(function (item) {
        var text = item.textContent.toLowerCase();
        var keywords = item.getAttribute('data-keywords') || '';
        if (text.includes(q) || keywords.includes(q)) {
          item.style.display = 'block';
        } else {
          item.style.display = 'none';
        }
      });
    }
  