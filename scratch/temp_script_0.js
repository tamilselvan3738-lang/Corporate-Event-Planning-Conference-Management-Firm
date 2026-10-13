
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
  