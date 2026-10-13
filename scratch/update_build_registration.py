with open('scratch/build_registration_page.py', 'r', encoding='utf-8') as f:
    code = f.read()

# 1. Update Font Awesome CDN to 6.5.1
old_fa = '<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0-beta3/css/all.min.css">'
new_fa = '<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.1/css/all.min.css">'
assert old_fa in code, "old_fa not found"
code = code.replace(old_fa, new_fa)

# 2. Update CSS for top utility actions
old_css_start = '/* ==========================================================================\n       FLOATING TOP-RIGHT UTILITY CONTROLS (MATCHING SCREENSHOT)\n       ========================================================================== */'
old_css_end = 'body.light .action-icon-pill.theme-pill {\n      background: #fefce8;\n      border-color: #fef08a;\n      color: #d97706;\n    }'

new_css = '''/* ==========================================================================
       FLOATING TOP UTILITY CONTROLS (3D SQUIRCLE SWITCHES MATCHING REFERENCE)
       ========================================================================== */
    .floating-top-actions {
      position: fixed;
      top: 1.15rem;
      right: 1.15rem;
      z-index: 50;
      display: flex;
      align-items: center;
      gap: 0.55rem;
    }

    body.rtl .floating-top-actions {
      right: auto;
      left: 1.15rem;
    }

    .btn-3d-switch {
      width: 34px;
      height: 34px;
      border-radius: 10px;
      display: flex;
      align-items: center;
      justify-content: center;
      cursor: pointer;
      background: linear-gradient(180deg, #1e293b 0%, #0f172a 100%);
      border: 1px solid #334155;
      box-shadow: 0 1.5px 0 #020617, 0 3px 8px rgba(0, 0, 0, 0.4);
      transition: all 0.18s cubic-bezier(0.16, 1, 0.3, 1);
      outline: none;
      user-select: none;
      -webkit-user-select: none;
    }

    .btn-3d-switch:hover {
      transform: translateY(-1.5px);
      box-shadow: 0 2.5px 0 #020617, 0 5px 12px rgba(0, 0, 0, 0.45);
      border-color: #475569;
    }

    .btn-3d-switch:active {
      transform: translateY(1px);
      box-shadow: 0 0.5px 0 #020617, 0 1px 3px rgba(0, 0, 0, 0.4);
    }

    .btn-3d-switch.rtl-switch {
      color: #f43f5e;
      font-size: 0.8rem;
    }

    .btn-3d-switch.rtl-switch:hover {
      color: #fb7185;
      border-color: rgba(244, 63, 94, 0.4);
    }

    .btn-3d-switch.theme-switch {
      color: #fbbf24;
      font-size: 0.88rem;
    }

    .btn-3d-switch.theme-switch:hover {
      color: #fde047;
      border-color: rgba(245, 158, 11, 0.4);
    }

    body.light .btn-3d-switch {
      background: linear-gradient(180deg, #ffffff 0%, #f1f5f9 100%);
      border: 1px solid #cbd5e1;
      box-shadow: 0 1.5px 0 #94a3b8, 0 2px 4px rgba(0, 0, 0, 0.06);
    }

    body.light .btn-3d-switch:hover {
      box-shadow: 0 2.5px 0 #94a3b8, 0 4px 8px rgba(0, 0, 0, 0.1);
      border-color: #94a3b8;
    }

    body.light .btn-3d-switch.rtl-switch {
      color: #e11d48;
    }

    body.light .btn-3d-switch.theme-switch {
      color: #334155;
    }'''

p1 = code.find(old_css_start)
p2 = code.find(old_css_end) + len(old_css_end)
assert p1 != -1 and p2 != -1, f"CSS block not found: {p1}, {p2}"
code = code[:p1] + new_css + code[p2:]

# 3. Update HTML markup for floating buttons
old_html = '''  <!-- Floating Utility Actions (Right-Left Swap & Theme Controls matching screenshot) -->
  <div class="floating-top-actions">
    <button class="action-icon-pill rtl-pill" id="rtlToggleBtn" title="Toggle Text Direction (Left / Right)">
      <i class="fas fa-right-left fa-exchange-alt"></i>
    </button>
    <button class="action-icon-pill theme-pill" id="themeToggleBtn" title="Toggle Dark / Light Theme">
      <i class="fas fa-cog"></i>
    </button>
  </div>'''

new_html = '''  <!-- Floating Utility Actions (Right-Left Swap & Theme Controls matching reference mockup) -->
  <div class="floating-top-actions">
    <button class="btn-3d-switch rtl-switch" id="rtlToggleBtn" onclick="toggleRTL()" title="Toggle RTL / LTR Text Direction" aria-label="Toggle RTL">
      <i id="rtlIcon" class="fa-solid fa-right-left"></i>
    </button>
    <button class="btn-3d-switch theme-switch" id="themeToggleBtn" onclick="toggleTheme()" title="Toggle Dark / Light Theme" aria-label="Toggle Dark/Light Mode">
      <i id="themeIcon" class="fa-solid fa-sun"></i>
    </button>
  </div>'''

assert old_html in code, "old_html not found"
code = code.replace(old_html, new_html)

# 4. Update JavaScript for Theme & RTL
old_js = '''    // 5. Theme Toggle (Dark / Light)
    const themeToggleBtn = document.getElementById('themeToggleBtn');
    if (themeToggleBtn) {
      themeToggleBtn.addEventListener('click', function() {
        document.body.classList.toggle('light');
        const isLight = document.body.classList.contains('light');
        this.innerHTML = isLight ? '<i class="fas fa-sun" style="color: #f59e0b;"></i>' : '<i class="fas fa-cog"></i>';
      });
    }

    // 6. RTL Toggle with Right-Left Icon
    const rtlToggleBtn = document.getElementById('rtlToggleBtn');
    if (rtlToggleBtn) {
      rtlToggleBtn.addEventListener('click', function() {
        document.body.classList.toggle('rtl');
      });
    }'''

new_js = '''    // 5. Theme Toggle (Dark / Light)
    function toggleTheme() {
      const isDark = !document.body.classList.contains('light');
      const themeIcon = document.getElementById('themeIcon');
      if (isDark) {
        document.body.classList.add('light');
        localStorage.setItem('eventsphere_theme', 'light');
        if (themeIcon) {
          themeIcon.className = 'fa-solid fa-moon';
        }
      } else {
        document.body.classList.remove('light');
        localStorage.setItem('eventsphere_theme', 'dark');
        if (themeIcon) {
          themeIcon.className = 'fa-solid fa-sun';
        }
      }
    }

    // 6. RTL Toggle with Right-Left Icon
    function toggleRTL() {
      document.body.classList.toggle('rtl');
      const isRTL = document.body.classList.contains('rtl');
      document.documentElement.dir = isRTL ? 'rtl' : 'ltr';
      localStorage.setItem('eventsphere_rtl', isRTL ? 'rtl' : 'ltr');
    }

    // Initialize saved Theme & RTL preference
    (function initThemeAndRTL() {
      const savedTheme = localStorage.getItem('eventsphere_theme');
      const themeIcon = document.getElementById('themeIcon');
      if (savedTheme === 'light') {
        document.body.classList.add('light');
        if (themeIcon) themeIcon.className = 'fa-solid fa-moon';
      }
      const savedRTL = localStorage.getItem('eventsphere_rtl');
      if (savedRTL === 'rtl') {
        document.body.classList.add('rtl');
        document.documentElement.dir = 'rtl';
      }
    })();'''

assert old_js in code, "old_js not found"
code = code.replace(old_js, new_js)

with open('scratch/build_registration_page.py', 'w', encoding='utf-8') as f:
    f.write(code)

print("Updated scratch/build_registration_page.py successfully!")
