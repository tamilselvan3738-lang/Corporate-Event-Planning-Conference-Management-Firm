with open('admin-dashboard.html', 'r', encoding='utf-8') as f:
    c = f.read()

# 1. Update Card 7 to 'Event Performance Metrics'
old_card7 = """          <!-- Card 7: Verified Venue Partners -->
          <div class="telemetry-card">
            <div class="telemetry-top">
              <span class="telemetry-label">Verified Venue Partners</span>
              <div class="telemetry-icon-box" style="color: #fbbf24; background: rgba(245, 158, 11, 0.12);"><i class="fas fa-hotel"></i></div>
            </div>
            <div class="telemetry-val-large">890</div>
            <div class="telemetry-trend-row">
              <span class="trend-pill info">Global Luxury Network</span>
              <svg class="sparkline-svg" viewBox="0 0 80 24">
                <path d="M0,14 Q25,18 50,10 T80,6" fill="none" stroke="#fbbf24" stroke-width="2.5" stroke-linecap="round"/>
              </svg>
            </div>
          </div>"""

new_card7 = """          <!-- Card 7: Event Performance Metrics -->
          <div class="telemetry-card">
            <div class="telemetry-top">
              <span class="telemetry-label">Event Performance Metrics</span>
              <div class="telemetry-icon-box" style="color: #38bdf8; background: rgba(56, 189, 248, 0.12);"><i class="fas fa-chart-line"></i></div>
            </div>
            <div class="telemetry-val-large">99.4%</div>
            <div class="telemetry-trend-row">
              <span class="trend-pill positive"><i class="fas fa-check-circle"></i> Client SLA Verified</span>
              <svg class="sparkline-svg" viewBox="0 0 80 24">
                <path d="M0,14 Q25,18 50,10 T80,6" fill="none" stroke="#38bdf8" stroke-width="2.5" stroke-linecap="round"/>
              </svg>
            </div>
          </div>"""

if old_card7 in c:
    c = c.replace(old_card7, new_card7)
    print("Replaced Card 7 successfully!")
else:
    print("Could not find exact old_card7 string!")

# 2. Hide .console-pill on mobile & tablet <= 1024px
media_rule_old = """    @media (max-width: 1024px) {
      /* TOPBAR: ONLY LOGO ON LEFT AND HAMBURGER ON RIGHT! */
      .topbar-search {
        display: none !important;
      }"""

media_rule_new = """    @media (max-width: 1024px) {
      /* TOPBAR: ONLY LOGO ON LEFT AND HAMBURGER ON RIGHT! */
      .console-pill {
        display: none !important;
      }

      .topbar-search {
        display: none !important;
      }"""

if media_rule_old in c:
    c = c.replace(media_rule_old, media_rule_new)
    print("Updated media query successfully!")
else:
    print("Could not find exact media_rule_old string!")

with open('admin-dashboard.html', 'w', encoding='utf-8') as f:
    f.write(c)

print("Saved admin-dashboard.html!")
