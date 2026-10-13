
    document.addEventListener('DOMContentLoaded', function() {
      // 1. Clone Navigation to Mobile Drawer
      const desktopList = document.getElementById('mainSidebarList');
      const drawerList = document.getElementById('drawerMenuList');
      if (desktopList && drawerList) {
        drawerList.innerHTML = desktopList.innerHTML;
      }

      // 2. Hamburger & Mobile Drawer Toggling
      const hamburgerBtn = document.getElementById('hamburgerBtn');
      const closeDrawerBtn = document.getElementById('closeDrawerBtn');
      const mobileDrawer = document.getElementById('mobileDrawer');
      const drawerBackdrop = document.getElementById('drawerBackdrop');

      function openDrawer() {
        mobileDrawer.classList.add('open');
        drawerBackdrop.classList.add('open');
        document.body.style.overflow = 'hidden';
      }

      function closeDrawer() {
        mobileDrawer.classList.remove('open');
        drawerBackdrop.classList.remove('open');
        document.body.style.overflow = '';
      }

      if (hamburgerBtn) hamburgerBtn.addEventListener('click', openDrawer);
      if (closeDrawerBtn) closeDrawerBtn.addEventListener('click', closeDrawer);
      if (drawerBackdrop) drawerBackdrop.addEventListener('click', closeDrawer);

      // 3. Module Tab Switching (Both Desktop & Drawer)
      function attachNavListeners() {
        const allNavItems = document.querySelectorAll('.nav-module-item');
        allNavItems.forEach(item => {
          item.addEventListener('click', function(e) {
            e.preventDefault();
            const mod = this.getAttribute('data-module');
            if (!mod) {
              if (this.classList.contains('logout-item') || this.id === 'sidebarLogoutBtn') {
                openModal('logoutModal');
              }
              return;
            }

            // Update active state in both desktop & drawer lists
            allNavItems.forEach(i => {
              if (i.getAttribute('data-module') === mod) {
                i.classList.add('active');
              } else {
                i.classList.remove('active');
              }
            });

            // Switch view
            const allViews = document.querySelectorAll('.module-view');
            allViews.forEach(v => v.classList.remove('active'));
            const targetView = document.getElementById('view-' + mod);
            if (targetView) {
              targetView.classList.add('active');
            }

            // Close mobile drawer if open
            closeDrawer();
            window.scrollTo({ top: 0, behavior: 'smooth' });
          });
        });
      }
      attachNavListeners();

      // 4. Dark / Light Theme Toggle
      const themeToggleBtn = document.getElementById('themeToggleBtn');
      const drawerThemeBtn = document.getElementById('drawerThemeBtn');

      function toggleTheme() {
        document.body.classList.toggle('light');
        const isLight = document.body.classList.contains('light');
        const icon = isLight ? '<i class="fas fa-sun" style="color: #f59e0b;"></i>' : '<i class="fas fa-moon"></i>';
        if (themeToggleBtn) themeToggleBtn.innerHTML = icon;
        if (drawerThemeBtn) drawerThemeBtn.innerHTML = icon + ' Theme';
      }

      if (themeToggleBtn) themeToggleBtn.addEventListener('click', toggleTheme);
      if (drawerThemeBtn) drawerThemeBtn.addEventListener('click', toggleTheme);

      // 5. RTL Toggle
      const rtlToggleBtn = document.getElementById('rtlToggleBtn');
      const drawerRtlBtn = document.getElementById('drawerRtlBtn');

      function toggleRtl() {
        document.body.classList.toggle('rtl');
      }

      if (rtlToggleBtn) rtlToggleBtn.addEventListener('click', toggleRtl);
      if (drawerRtlBtn) drawerRtlBtn.addEventListener('click', toggleRtl);

      // 6. Refresh Metrics Simulation
      const refreshBtn = document.getElementById('refreshMetricsBtn');
      if (refreshBtn) {
        refreshBtn.addEventListener('click', function() {
          const icon = this.querySelector('i');
          if (icon) icon.classList.add('fa-spin');
          setTimeout(() => {
            if (icon) icon.classList.remove('fa-spin');
            alert('Live Telemetry Metrics Refreshed from 6 Global Hubs!');
          }, 600);
        });
      }

      // 7. Shortcut (Ctrl + K) for Quick Search
      window.addEventListener('keydown', function(e) {
        if ((e.ctrlKey || e.metaKey) && e.key.toLowerCase() === 'k') {
          e.preventDefault();
          const searchInput = document.getElementById('topbarSearchInput');
          if (searchInput && window.innerWidth > 1024) {
            searchInput.focus();
          } else {
            openDrawer();
            const drawerSearch = document.getElementById('drawerSearchInput');
            if (drawerSearch) drawerSearch.focus();
          }
        }
        if (e.key === 'Escape') {
          closeDrawer();
          closeAllModals();
        }
      });
    });

    // Global Modal Helpers
    function openModal(id) {
      const m = document.getElementById(id);
      if (m) m.classList.add('open');
    }

    function closeModal(id) {
      const m = document.getElementById(id);
      if (m) m.classList.remove('open');
    }

    function closeAllModals() {
      document.querySelectorAll('.admin-modal-overlay').forEach(m => m.classList.remove('open'));
    }

    function handleModalSubmit(e, successMsg) {
      e.preventDefault();
      alert(successMsg);
      closeAllModals();
    }

    function switchModule(moduleName) {
      const targetBtn = document.querySelector(`.nav-module-item[data-module="${moduleName}"]`);
      if (targetBtn) targetBtn.click();
    }

    function exportOverviewReport() {
      alert('Generating EventSphere Executive Operational Audit Report (PDF)... Download starting!');
    }
  