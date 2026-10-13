import re, sys

sys.stdout.reconfigure(encoding='utf-8')

# Active styles CSS to inject before '/* ===== RIGHT SECTION ===== */'
ACTIVE_NAV_CSS = """    /* ===== ACTIVE NAV LINK & DROPDOWN STYLES ===== */
    .nav-links > li > a.active,
    .nav-links > li.active > a,
    .nav-links > li.dropdown.active > a.dropdown-toggle {
      color: #2563eb !important;
      font-weight: 700 !important;
    }

    .nav-links > li > a.active::after,
    .nav-links > li.active > a::after,
    .nav-links > li.dropdown.active > a.dropdown-toggle::after {
      width: 100% !important;
      background: linear-gradient(90deg, #2563eb, #8b5cf6) !important;
      height: 2.5px !important;
      box-shadow: 0 2px 8px rgba(37, 99, 235, 0.4) !important;
    }

    .dropdown-item.active {
      background: linear-gradient(135deg, rgba(37, 99, 235, 0.12), rgba(139, 92, 246, 0.12)) !important;
      color: #2563eb !important;
      font-weight: 700 !important;
    }

    .dropdown-item.active .dropdown-item-icon {
      background: linear-gradient(145deg, #2563eb, #3b82f6) !important;
      color: #ffffff !important;
      box-shadow: 0 4px 12px rgba(37, 99, 235, 0.35) !important;
      transform: scale(1.06);
    }

    /* Active Mobile Links */
    .mobile-nav-links > li > a.active,
    .mobile-nav-links > li.active > a,
    .mobile-dropdown.active .mobile-dropdown-header > a,
    .mobile-dropdown-header > a.active {
      color: #2563eb !important;
      font-weight: 700 !important;
    }

    .mobile-nav-links > li > a.active::before,
    .mobile-nav-links > li.active > a::before,
    .mobile-dropdown.active .mobile-dropdown-header > a::before,
    .mobile-dropdown-header > a.active::before {
      opacity: 1 !important;
      left: -20px !important;
      color: #2563eb !important;
    }

    .mobile-submenu a.active {
      color: #2563eb !important;
      font-weight: 700 !important;
      padding-left: 0.35rem;
    }

    /* Dark Mode Active Styles */
    body.dark .nav-links > li > a.active,
    body.dark .nav-links > li.active > a,
    body.dark .nav-links > li.dropdown.active > a.dropdown-toggle {
      color: #60a5fa !important;
      font-weight: 700 !important;
      text-shadow: 0 0 16px rgba(96, 165, 250, 0.6) !important;
    }

    body.dark .nav-links > li > a.active::after,
    body.dark .nav-links > li.active > a::after,
    body.dark .nav-links > li.dropdown.active > a.dropdown-toggle::after {
      background: linear-gradient(90deg, #60a5fa, #a78bfa) !important;
      box-shadow: 0 0 12px rgba(96, 165, 250, 0.8) !important;
    }

    body.dark .dropdown-item.active {
      background: rgba(59, 130, 246, 0.22) !important;
      color: #93c5fd !important;
    }

    body.dark .dropdown-item.active .dropdown-item-icon {
      background: linear-gradient(145deg, #2563eb, #3b82f6) !important;
      color: #ffffff !important;
      box-shadow: 0 4px 16px rgba(59, 130, 246, 0.6) !important;
    }

    body.dark .mobile-nav-links > li > a.active,
    body.dark .mobile-nav-links > li.active > a,
    body.dark .mobile-dropdown.active .mobile-dropdown-header > a,
    body.dark .mobile-dropdown-header > a.active,
    body.dark .mobile-submenu a.active {
      color: #60a5fa !important;
    }

"""

def generate_desktop_nav(page):
    is_home = page in ('index.html', 'navbar.html')
    is_home2 = page == 'home-2.html'
    is_home_active = is_home or is_home2
    
    home_dropdown_class = "dropdown active" if is_home_active else "dropdown"
    home_toggle_class = "dropdown-toggle active" if is_home_active else "dropdown-toggle"
    home1_item_class = "dropdown-item active" if is_home else "dropdown-item"
    home2_item_class = "dropdown-item active" if is_home2 else "dropdown-item"

    about_li = ' class="active"' if page == 'about.html' else ''
    about_a = ' class="active"' if page == 'about.html' else ''

    services_li = ' class="active"' if page == 'services.html' else ''
    services_a = ' class="active"' if page == 'services.html' else ''

    portfolio_li = ' class="active"' if page == 'portfolio.html' else ''
    portfolio_a = ' class="active"' if page == 'portfolio.html' else ''

    planning_li = ' class="active"' if page == 'event-planning.html' else ''
    planning_a = ' class="active"' if page == 'event-planning.html' else ''

    vendors_li = ' class="active"' if page == 'vendors.html' else ''
    vendors_a = ' class="active"' if page == 'vendors.html' else ''

    resources_li = ' class="active"' if page == 'resources.html' else ''
    resources_a = ' class="active"' if page == 'resources.html' else ''

    contact_li = ' class="active"' if page == 'contact.html' else ''
    contact_a = ' class="active"' if page == 'contact.html' else ''

    is_admin = page == 'admin-dashboard.html'
    is_user = page == 'user-dashboard.html'
    dash_active = is_admin or is_user
    dash_dropdown_class = "dropdown dropdown-right active" if dash_active else "dropdown dropdown-right"
    dash_toggle_class = "dropdown-toggle active" if dash_active else "dropdown-toggle"
    admin_item_class = "dropdown-item active" if is_admin else "dropdown-item"
    user_item_class = "dropdown-item active" if is_user else "dropdown-item"

    return f"""\n\n      <ul class="nav-links">
        <li class="{home_dropdown_class}">
          <a href="index.html" class="{home_toggle_class}">Home <i class="fas fa-chevron-down dropdown-arrow"></i></a>
          <ul class="dropdown-menu">
            <li>
              <a href="index.html" class="{home1_item_class}">
                <span class="dropdown-item-icon"><i class="fas fa-home"></i></span>
                <span class="dropdown-item-title">Home 1</span>
              </a>
            </li>
            <li>
              <a href="home-2.html" class="{home2_item_class}">
                <span class="dropdown-item-icon"><i class="fas fa-building"></i></span>
                <span class="dropdown-item-title">Home 2</span>
              </a>
            </li>
          </ul>
        </li>
        <li{about_li}><a href="about.html"{about_a}>About</a></li>
        <li{services_li}><a href="services.html"{services_a}>Services</a></li>
        <li{portfolio_li}><a href="portfolio.html"{portfolio_a}>Portfolio</a></li>
        <li{planning_li}><a href="event-planning.html"{planning_a}>Event Planning</a></li>
        <li{vendors_li}><a href="vendors.html"{vendors_a}>Vendors</a></li>
        <li{resources_li}><a href="resources.html"{resources_a}>Resources</a></li>
        <li{contact_li}><a href="contact.html"{contact_a}>Contact</a></li>
        <li class="{dash_dropdown_class}">
          <a href="admin-dashboard.html" class="{dash_toggle_class}">Dashboard <i class="fas fa-chevron-down dropdown-arrow"></i></a>
          <ul class="dropdown-menu">
            <li>
              <a href="admin-dashboard.html" class="{admin_item_class}">
                <span class="dropdown-item-icon"><i class="fas fa-shield-alt"></i></span>
                <span class="dropdown-item-title">Admin Dashboard</span>
              </a>
            </li>
            <li>
              <a href="user-dashboard.html" class="{user_item_class}">
                <span class="dropdown-item-icon"><i class="fas fa-user-circle"></i></span>
                <span class="dropdown-item-title">User Dashboard</span>
              </a>
            </li>
          </ul>
        </li>
      </ul>\n\n      """


def generate_mobile_nav(page):
    is_home = page in ('index.html', 'navbar.html')
    is_home2 = page == 'home-2.html'
    is_home_active = is_home or is_home2

    home_mob_class = "mobile-dropdown active" if is_home_active else "mobile-dropdown"
    home_a_class = ' class="active"' if is_home_active else ''
    home1_sub_class = ' class="active"' if is_home else ''
    home2_sub_class = ' class="active"' if is_home2 else ''

    about_li = ' class="active"' if page == 'about.html' else ''
    about_a = ' class="active"' if page == 'about.html' else ''

    services_li = ' class="active"' if page == 'services.html' else ''
    services_a = ' class="active"' if page == 'services.html' else ''

    portfolio_li = ' class="active"' if page == 'portfolio.html' else ''
    portfolio_a = ' class="active"' if page == 'portfolio.html' else ''

    planning_li = ' class="active"' if page == 'event-planning.html' else ''
    planning_a = ' class="active"' if page == 'event-planning.html' else ''

    vendors_li = ' class="active"' if page == 'vendors.html' else ''
    vendors_a = ' class="active"' if page == 'vendors.html' else ''

    resources_li = ' class="active"' if page == 'resources.html' else ''
    resources_a = ' class="active"' if page == 'resources.html' else ''

    contact_li = ' class="active"' if page == 'contact.html' else ''
    contact_a = ' class="active"' if page == 'contact.html' else ''

    is_admin = page == 'admin-dashboard.html'
    is_user = page == 'user-dashboard.html'
    dash_active = is_admin or is_user
    dash_mob_class = "mobile-dropdown active" if dash_active else "mobile-dropdown"
    dash_a_class = ' class="active"' if dash_active else ''
    admin_sub_class = ' class="active"' if is_admin else ''
    user_sub_class = ' class="active"' if is_user else ''

    return f"""\n    <div class="mobile-menu" id="mobileMenu">
      <ul class="mobile-nav-links">
        <li class="{home_mob_class}">
          <div class="mobile-dropdown-header">
            <a href="index.html"{home_a_class}>Home</a>
            <button class="mobile-dropdown-toggle" aria-label="Toggle Home submenu"><i class="fas fa-chevron-down"></i></button>
          </div>
          <ul class="mobile-submenu">
            <li><a href="index.html"{home1_sub_class}><i class="fas fa-home"></i> Home 1</a></li>
            <li><a href="home-2.html"{home2_sub_class}><i class="fas fa-building"></i> Home 2</a></li>
          </ul>
        </li>
        <li{about_li}><a href="about.html"{about_a}>About</a></li>
        <li{services_li}><a href="services.html"{services_a}>Services</a></li>
        <li{portfolio_li}><a href="portfolio.html"{portfolio_a}>Portfolio</a></li>
        <li{planning_li}><a href="event-planning.html"{planning_a}>Event Planning</a></li>
        <li{vendors_li}><a href="vendors.html"{vendors_a}>Vendors</a></li>
        <li{resources_li}><a href="resources.html"{resources_a}>Resources</a></li>
        <li{contact_li}><a href="contact.html"{contact_a}>Contact</a></li>
        <li class="{dash_mob_class}">
          <div class="mobile-dropdown-header">
            <a href="admin-dashboard.html"{dash_a_class}>Dashboard</a>
            <button class="mobile-dropdown-toggle" aria-label="Toggle Dashboard submenu"><i class="fas fa-chevron-down"></i></button>
          </div>
          <ul class="mobile-submenu">
            <li><a href="admin-dashboard.html"{admin_sub_class}><i class="fas fa-shield-alt"></i> Admin Dashboard</a></li>
            <li><a href="user-dashboard.html"{user_sub_class}><i class="fas fa-user-circle"></i> User Dashboard</a></li>
          </ul>
        </li>
      </ul>\n      """


FOOTER_NAV_REPLACEMENT = """\n        <div class="footer-col">
          <h3 class="footer-col-title">Navigation</h3>
          <ul class="footer-links">
            <li><a href="index.html"><i class="fas fa-chevron-right"></i> Home 1 (Main Agency)</a></li>
            <li><a href="home-2.html"><i class="fas fa-chevron-right"></i> Home 2 (Conference View)</a></li>
            <li><a href="about.html"><i class="fas fa-chevron-right"></i> About Our Firm</a></li>
            <li><a href="services.html"><i class="fas fa-chevron-right"></i> Services & Solutions</a></li>
            <li><a href="portfolio.html"><i class="fas fa-chevron-right"></i> Event Portfolio</a></li>
            <li><a href="event-planning.html"><i class="fas fa-chevron-right"></i> Event Planning Process</a></li>
            <li><a href="vendors.html"><i class="fas fa-chevron-right"></i> Vendors Directory</a></li>
            <li><a href="contact.html"><i class="fas fa-chevron-right"></i> Contact & Consultation</a></li>
          </ul>
        </div>\n\n        """


JS_ACCORDION_AND_ACTIVE = """    // ===== MOBILE SUBMENU ACCORDION =====
    const mobileDropdownHeaders = document.querySelectorAll('.mobile-dropdown-header');
    mobileDropdownHeaders.forEach(header => {
      header.addEventListener('click', (e) => {
        // If direct navigation link inside header was clicked, allow navigation
        if (e.target.closest('a')) {
          return;
        }
        const parent = header.closest('.mobile-dropdown');
        if (parent) {
          parent.classList.toggle('open');
        }
      });
    });

    // ===== NAVBAR ACTIVE STATUS DYNAMIC HANDLER =====
    (function syncNavbarActiveState() {
      try {
        const currentPath = window.location.pathname.toLowerCase();
        let currentPage = currentPath.substring(currentPath.lastIndexOf('/') + 1);
        if (!currentPage || currentPage === '/') currentPage = 'index.html';

        const navItems = document.querySelectorAll('.nav-links a, .mobile-nav-links a, .dropdown-item, .mobile-submenu a');
        navItems.forEach(item => {
          const href = (item.getAttribute('href') || '').toLowerCase();
          if (!href || href.startsWith('#') || href.startsWith('javascript:')) return;

          let matches = false;
          if (currentPage === 'index.html' || currentPage === '') {
            if (href === 'index.html' && (item.textContent.trim().toLowerCase().includes('home 1') || item.classList.contains('dropdown-toggle') || (item.parentElement && item.parentElement.classList.contains('mobile-dropdown-header')))) {
              matches = true;
            }
          } else if (href === currentPage) {
            matches = true;
          }

          if (matches) {
            item.classList.add('active');
            const pLi = item.closest('li');
            if (pLi) pLi.classList.add('active');
            const pDrop = item.closest('.dropdown, .mobile-dropdown');
            if (pDrop) {
              pDrop.classList.add('active');
              const tog = pDrop.querySelector('.dropdown-toggle, .mobile-dropdown-header > a');
              if (tog) tog.classList.add('active');
            }
          }
        });

        // Instant active feedback upon clicking
        navItems.forEach(item => {
          item.addEventListener('click', function() {
            const href = this.getAttribute('href');
            if (href && !href.startsWith('#') && !href.startsWith('javascript:')) {
              document.querySelectorAll('.nav-links .active, .mobile-nav-links .active, .dropdown-item.active, .mobile-submenu .active').forEach(el => el.classList.remove('active'));
              this.classList.add('active');
              const pLi = this.closest('li');
              if (pLi) pLi.classList.add('active');
              const pDrop = this.closest('.dropdown, .mobile-dropdown');
              if (pDrop) {
                pDrop.classList.add('active');
                const tog = pDrop.querySelector('.dropdown-toggle, .mobile-dropdown-header > a');
                if (tog) tog.classList.add('active');
              }
            }
          });
        });
      } catch (err) {
        console.warn('Navbar active sync error:', err);
      }
    })();"""

OLD_JS_ACCORDION = """    // ===== MOBILE SUBMENU ACCORDION =====
    const mobileDropdownHeaders = document.querySelectorAll('.mobile-dropdown-header');
    mobileDropdownHeaders.forEach(header => {
      header.addEventListener('click', (e) => {
        const parent = header.closest('.mobile-dropdown');
        if (parent) {
          parent.classList.toggle('open');
        }
      });
    });"""

pages = [
    'index.html', 'home-2.html', 'about.html', 'services.html', 
    'portfolio.html', 'event-planning.html', 'vendors.html', 
    'resources.html', 'contact.html', 'navbar.html'
]

print("Starting navbar updates...")
for p in pages:
    with open(p, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Inject Active CSS if not present
    if '.nav-links > li > a.active' not in content:
        if '/* ===== RIGHT SECTION ===== */' in content:
            content = content.replace('/* ===== RIGHT SECTION ===== */', ACTIVE_NAV_CSS + '    /* ===== RIGHT SECTION ===== */', 1)
            print(f"  [{p}] Injected Active CSS")
        else:
            print(f"  [{p}] ERROR: '/* ===== RIGHT SECTION ===== */' not found")

    # 2. Replace Desktop Nav Links
    pattern_desk = r'<!-- CENTER: DESKTOP NAV LINKS -->(.*?)<!-- RIGHT: ICONS & LOGIN -->'
    new_desk = '<!-- CENTER: DESKTOP NAV LINKS -->' + generate_desktop_nav(p) + '<!-- RIGHT: ICONS & LOGIN -->'
    content, count_d = re.subn(pattern_desk, new_desk, content, count=1, flags=re.DOTALL)
    print(f"  [{p}] Desktop Nav replaced: {count_d == 1}")

    # 3. Replace Mobile Nav Links
    pattern_mob = r'<!-- MOBILE MENU -->(.*?)<div class="mobile-actions">'
    new_mob = '<!-- MOBILE MENU -->' + generate_mobile_nav(p) + '<div class="mobile-actions">'
    content, count_m = re.subn(pattern_mob, new_mob, content, count=1, flags=re.DOTALL)
    print(f"  [{p}] Mobile Nav replaced: {count_m == 1}")

    # 4. Replace Footer Nav Links
    pattern_footer = r'<!-- COL 2: MAIN NAVIGATION -->(.*?)<!-- COL 3:'
    new_footer = '<!-- COL 2: MAIN NAVIGATION -->' + FOOTER_NAV_REPLACEMENT + '<!-- COL 3:'
    content, count_f = re.subn(pattern_footer, new_footer, content, count=1, flags=re.DOTALL)
    print(f"  [{p}] Footer Nav replaced: {count_f == 1}")

    # 5. Update Accordion & Navbar Active JS
    if OLD_JS_ACCORDION in content:
        content = content.replace(OLD_JS_ACCORDION, JS_ACCORDION_AND_ACTIVE, 1)
        print(f"  [{p}] JS Accordion & Active sync injected: True")
    else:
        print(f"  [{p}] WARNING: OLD_JS_ACCORDION exact string not found, checking regex")
        # Try regex if slight whitespace difference
        js_pattern = r'// ===== MOBILE SUBMENU ACCORDION =====\s+const mobileDropdownHeaders = document\.querySelectorAll\(\'\.mobile-dropdown-header\'\);\s+mobileDropdownHeaders\.forEach\(header => \{\s+header\.addEventListener\(\'click\', \(e\) => \{\s+const parent = header\.closest\(\'\.mobile-dropdown\'\);\s+if \(parent\) \{\s+parent\.classList\.toggle\(\'open\'\);\s+\}\s+\}\);\s+\}\);'
        content, count_js = re.subn(js_pattern, JS_ACCORDION_AND_ACTIVE, content, count=1)
        print(f"  [{p}] Regex JS Accordion replaced: {count_js == 1}")

    with open(p, 'w', encoding='utf-8') as f:
        f.write(content)

print("\nNavbar update complete for all 10 pages.")
