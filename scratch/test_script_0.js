
    // ===== DARK MODE TOGGLE =====
    const darkToggle = document.getElementById('darkModeToggle');
    const darkToggleMobile = document.getElementById('darkModeToggleMobile');
    const rtlToggle = document.getElementById('rtlToggle');
    const rtlToggleMobile = document.getElementById('rtlToggleMobile');
    const hamburger = document.getElementById('hamburgerBtn');
    const mobileMenu = document.getElementById('mobileMenu');
    const body = document.body;

    function toggleDark() {
      body.classList.toggle('dark');
      const icon = body.classList.contains('dark') ? 'fa-sun' : 'fa-moon';
      darkToggle.innerHTML = `<i class="fas ${icon}"></i>`;
      if (darkToggleMobile) darkToggleMobile.innerHTML = `<i class="fas ${icon}"></i>`;
    }

    darkToggle.addEventListener('click', toggleDark);
    if (darkToggleMobile) darkToggleMobile.addEventListener('click', toggleDark);

    function toggleRTL() {
      body.classList.toggle('rtl');
    }

    rtlToggle.addEventListener('click', toggleRTL);
    if (rtlToggleMobile) rtlToggleMobile.addEventListener('click', toggleRTL);

    // ===== HAMBURGER MENU WITH SMOOTH MOTION =====
    hamburger.addEventListener('click', (e) => {
      e.stopPropagation();
      mobileMenu.classList.toggle('active');
      hamburger.classList.toggle('open');
      
      // Framer Motion style spring animation on menu
      if (mobileMenu.classList.contains('active')) {
        mobileMenu.style.transform = 'scale(0.92) translateY(-12px)';
        mobileMenu.style.opacity = '0';
        requestAnimationFrame(() => {
          mobileMenu.style.transition = 'transform 0.5s cubic-bezier(0.34, 1.56, 0.64, 1), opacity 0.3s ease';
          mobileMenu.style.transform = 'scale(1) translateY(0)';
          mobileMenu.style.opacity = '1';
        });
      }
    });

    // Close menu on outside click
    document.addEventListener('click', (e) => {
      if (!mobileMenu.contains(e.target) && !hamburger.contains(e.target) && mobileMenu.classList.contains('active')) {
        mobileMenu.classList.remove('active');
        hamburger.classList.remove('open');
        mobileMenu.style.transform = 'scale(0.92) translateY(-12px)';
        mobileMenu.style.opacity = '0';
      }
    });

    // ===== EXTREME HOVER EFFECTS (Framer Motion style) =====
    const allButtons = document.querySelectorAll('.icon-btn, .login-btn, .hamburger, .footer-form button, .back-to-top-btn, .footer-social-btn');
    allButtons.forEach(btn => {
      btn.addEventListener('mouseenter', () => {
        btn.style.transition = 'transform 0.4s cubic-bezier(0.34, 1.56, 0.64, 1), box-shadow 0.4s ease, background 0.3s ease';
      });
      btn.addEventListener('mouseleave', () => {
        btn.style.transition = 'transform 0.3s cubic-bezier(0.23, 1, 0.32, 1), box-shadow 0.4s ease, background 0.3s ease';
      });
    });

    // ===== MOBILE SUBMENU ACCORDION =====
    const mobileDropdownHeaders = document.querySelectorAll('.mobile-dropdown-header');
    mobileDropdownHeaders.forEach(header => {
      header.addEventListener('click', (e) => {
        const parent = header.closest('.mobile-dropdown');
        if (parent) {
          parent.classList.toggle('open');
        }
      });
    });

    // ===== NAV LINK STAGGER ANIMATION =====
    const navLinks = document.querySelectorAll('.nav-links > li');
    navLinks.forEach((link, index) => {
      link.style.opacity = '0';
      link.style.transform = 'translateY(-8px)';
      link.style.transition = `opacity 0.5s ease ${0.05 * index + 0.1}s, transform 0.5s cubic-bezier(0.23, 1, 0.32, 1) ${0.05 * index + 0.1}s`;
      setTimeout(() => {
        link.style.opacity = '1';
        link.style.transform = 'translateY(0)';
      }, 50);
      setTimeout(() => {
        link.style.removeProperty('opacity');
        link.style.removeProperty('transform');
        link.style.removeProperty('transition');
      }, 800);
    });

    // ===== INITIAL DARK ICON CHECK =====
    if (body.classList.contains('dark')) {
      darkToggle.innerHTML = '<i class="fas fa-sun"></i>';
      if (darkToggleMobile) darkToggleMobile.innerHTML = '<i class="fas fa-sun"></i>';
    }

    // ===== BACK TO TOP SMOOTH SCROLL =====
    const backToTopBtn = document.getElementById('backToTopBtn');
    if (backToTopBtn) {
      backToTopBtn.addEventListener('click', () => {
        window.scrollTo({ top: 0, behavior: 'smooth' });
      });
    }

    // ===== NEWSLETTER INTERACTION =====
    function handleNewsletterSubmit() {
      const form = document.getElementById('newsletterForm');
      const emailInput = document.getElementById('newsletterEmail');
      if (form && emailInput && emailInput.value) {
        form.innerHTML = '<div style="display:flex;align-items:center;gap:0.6rem;color:#16a34a;font-weight:600;font-size:0.9rem;padding:0.6rem 1rem;"><i class="fas fa-check-circle"></i> Thank you! You are subscribed to EventSphere Executive Briefings.</div>';
      }
    }

    <!-- =====================================================================
         INTERACTIVE CLIENT CONTROLS & FRAMER MOTION OBSERVERS
         ===================================================================== -->
    <script>
    // 1. Framer Motion Scroll Trigger Observers
    document.addEventListener('DOMContentLoaded', () => {
      const motionClasses = [
        '.framer-folio-glide',
        '.framer-countdown-snap',
        '.framer-capex-reveal',
        '.framer-blueprint-draft',
        '.framer-dual-hemisphere',
        '.framer-editorial-rise',
        '.framer-vault-open'
      ];

      const motionObserver = new IntersectionObserver((entries, obs) => {
        entries.forEach(entry => {
          if (entry.isIntersecting) {
            entry.target.classList.add('framer-in-view');
            // Stagger child elements if any
            const children = entry.target.querySelectorAll('.framer-folio-glide, .framer-countdown-snap, .framer-capex-reveal, .framer-blueprint-draft, .framer-dual-hemisphere, .framer-editorial-rise, .framer-vault-open');
            children.forEach((c, idx) => {
              setTimeout(() => c.classList.add('framer-in-view'), idx * 80);
            });
            obs.unobserve(entry.target);
          }
        });
      }, {
        threshold: 0.15,
        rootMargin: '0px 0px -50px 0px'
      });

      motionClasses.forEach(selector => {
        document.querySelectorAll(selector).forEach(el => motionObserver.observe(el));
      });
    });

    // 2. Section 1: Folio Chapter Selector
    const folioChaptersData = [
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
      const cards = document.querySelectorAll('.rc-chapter-card');
      cards.forEach((c, idx) => {
        if (idx === index) c.classList.add('active');
        else c.classList.remove('active');
      });

      const data = folioChaptersData[index];
      const titleEl = document.getElementById('currentFolioTitle');
      const descEl = document.getElementById('currentFolioDesc');
      const audEl = document.getElementById('folioAudienceVal');
      const scaEl = document.getElementById('folioScaleVal');
      const fmtEl = document.getElementById('folioFormatVal');

      if (titleEl) {
        titleEl.style.opacity = '0';
        setTimeout(() => {
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
    let currentReadiness = 100;
    function updateReadinessScore(cb, weight) {
      if (cb.checked) {
        currentReadiness += weight;
      } else {
        currentReadiness -= weight;
      }
      currentReadiness = Math.max(0, Math.min(100, currentReadiness));

      const fillEl = document.getElementById('readinessBarFill');
      const textEl = document.getElementById('readinessScoreText');

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
      ['btnCap500', 'btnCap1500', 'btnCap5000'].forEach(id => {
        const b = document.getElementById(id);
        if (b) {
          b.className = 'rc-btn rc-btn-outline';
          b.style.padding = '0.5rem 1rem';
          b.style.fontSize = '0.85rem';
        }
      });
      btn.className = 'rc-btn rc-btn-primary';
      btn.style.padding = '0.5rem 1rem';
      btn.style.fontSize = '0.85rem';

      const costPerPax = 485;
      const total = pax * costPerPax;

      const venue = Math.round(total * 0.35);
      const av = Math.round(total * 0.28);
      const speaker = Math.round(total * 0.18);
      const scenic = Math.round(total * 0.12);
      const cont = Math.round(total * 0.07);

      document.getElementById('simTotalBudget').textContent = '$' + total.toLocaleString();
      document.getElementById('allocVenueText').textContent = '$' + venue.toLocaleString();
      document.getElementById('allocAvText').textContent = '$' + av.toLocaleString();
      document.getElementById('allocSpeakerText').textContent = '$' + speaker.toLocaleString();
      document.getElementById('allocScenicText').textContent = '$' + scenic.toLocaleString();
      document.getElementById('allocContingencyText').textContent = '$' + cont.toLocaleString();
    }

    // 5. Section 7: FAQ Accordion Toggle & Live Keyword Search
    function toggleAccordion(header) {
      const item = header.closest('.rc-accordion-item');
      const body = item.querySelector('.rc-accordion-body');
      const isActive = item.classList.contains('active');

      // Close other accordion items
      document.querySelectorAll('.rc-accordion-item').forEach(i => {
        i.classList.remove('active');
        const b = i.querySelector('.rc-accordion-body');
        if (b) b.style.maxHeight = '0px';
      });

      if (!isActive) {
        item.classList.add('active');
        if (body) body.style.maxHeight = body.scrollHeight + 30 + 'px';
      }
    }

    function filterFaqQuestions(query) {
      const q = query.toLowerCase().trim();
      const items = document.querySelectorAll('.rc-accordion-item');
      items.forEach(item => {
        const text = item.textContent.toLowerCase();
        const keywords = item.getAttribute('data-keywords') || '';
        if (text.includes(q) || keywords.includes(q)) {
          item.style.display = 'block';
        } else {
          item.style.display = 'none';
        }
      });
    }
    