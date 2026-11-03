/**
 * EventSphere - Brand Theme & Navigation Controller
 * Corporate Event Planning & Conference Management Firm
 */

(function () {
  'use strict';

  // Apply saved theme immediately before render to avoid flash
  const savedTheme = localStorage.getItem('eventsphere_theme');
  if (savedTheme === 'dark') {
    document.body.classList.add('dark');
  } else if (savedTheme === 'light') {
    document.body.classList.remove('dark');
  }

  const savedRTL = localStorage.getItem('eventsphere_rtl');
  if (savedRTL === 'true') {
    document.body.classList.add('rtl');
  }

  document.addEventListener('DOMContentLoaded', function () {
    // Theme toggle buttons
    const darkToggle = document.getElementById('darkModeToggle');
    const darkToggleMobile = document.getElementById('darkModeToggleMobile');
    const themeSwitches = document.querySelectorAll('.theme-switch');

    function updateIcons(isDark) {
      const iconClass = isDark ? 'fa-sun' : 'fa-moon';
      if (darkToggle) darkToggle.innerHTML = `<i class="fas ${iconClass}"></i>`;
      if (darkToggleMobile) darkToggleMobile.innerHTML = `<i class="fas ${iconClass}"></i>`;
      themeSwitches.forEach(btn => {
        const icon = btn.querySelector('i');
        if (icon) {
          icon.className = `fas ${iconClass}`;
        }
      });
    }

    // Set initial icon state
    updateIcons(document.body.classList.contains('dark'));

    function toggleTheme() {
      const isDark = document.body.classList.toggle('dark');
      localStorage.setItem('eventsphere_theme', isDark ? 'dark' : 'light');
      updateIcons(isDark);
    }

    if (darkToggle) darkToggle.addEventListener('click', toggleTheme);
    if (darkToggleMobile) darkToggleMobile.addEventListener('click', toggleTheme);
    themeSwitches.forEach(btn => btn.addEventListener('click', toggleTheme));

    // RTL Toggle
    const rtlToggle = document.getElementById('rtlToggle');
    const rtlToggleMobile = document.getElementById('rtlToggleMobile');
    const rtlSwitches = document.querySelectorAll('.rtl-switch');

    function toggleRTL() {
      const isRTL = document.body.classList.toggle('rtl');
      localStorage.setItem('eventsphere_rtl', isRTL ? 'true' : 'false');
    }

    if (rtlToggle) rtlToggle.addEventListener('click', toggleRTL);
    if (rtlToggleMobile) rtlToggleMobile.addEventListener('click', toggleRTL);
    rtlSwitches.forEach(btn => btn.addEventListener('click', toggleRTL));

    // Mobile Hamburger Menu
    const hamburger = document.getElementById('hamburgerBtn');
    const mobileMenu = document.getElementById('mobileMenu');

    if (hamburger && mobileMenu) {
      hamburger.addEventListener('click', function (e) {
        e.stopPropagation();
        mobileMenu.classList.toggle('active');
        hamburger.classList.toggle('open');
      });

      document.addEventListener('click', function (e) {
        if (!mobileMenu.contains(e.target) && !hamburger.contains(e.target) && mobileMenu.classList.contains('active')) {
          mobileMenu.classList.remove('active');
          hamburger.classList.remove('open');
        }
      });
    }

    // Mobile submenus toggle
    const mobileDropdownToggles = document.querySelectorAll('.mobile-dropdown-toggle');
    mobileDropdownToggles.forEach(toggle => {
      toggle.addEventListener('click', function (e) {
        e.preventDefault();
        const parent = this.closest('.mobile-dropdown');
        if (parent) {
          parent.classList.toggle('active');
        }
      });
    });

    // Back to top button
    const backToTopBtn = document.getElementById('backToTopBtn');
    if (backToTopBtn) {
      window.addEventListener('scroll', function () {
        if (window.scrollY > 400) {
          backToTopBtn.style.opacity = '1';
          backToTopBtn.style.pointerEvents = 'auto';
        } else {
          backToTopBtn.style.opacity = '0';
          backToTopBtn.style.pointerEvents = 'none';
        }
      });
      backToTopBtn.addEventListener('click', function () {
        window.scrollTo({ top: 0, behavior: 'smooth' });
      });
    }
  });
})();
