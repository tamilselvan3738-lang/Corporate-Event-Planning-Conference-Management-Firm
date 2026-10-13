
    // 1. Framer Motion Scroll Trigger Observers
    document.addEventListener('DOMContentLoaded', function () {
      var motionClasses = [
        '.framer-embassy-rise',
        '.framer-telephony-snap',
        '.framer-pgp-decrypt',
        '.framer-chronometer-spin',
        '.framer-wayfinding-zoom',
        '.framer-forge-expand',
        '.framer-bunker-pulse'
      ];

      var motionObserver = new IntersectionObserver(function (entries, obs) {
        entries.forEach(function (entry) {
          if (entry.isIntersecting) {
            entry.target.classList.add('framer-in-view');
            var children = entry.target.querySelectorAll('.framer-embassy-rise, .framer-telephony-snap, .framer-pgp-decrypt, .framer-chronometer-spin, .framer-wayfinding-zoom, .framer-forge-expand, .framer-bunker-pulse');
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

      // 2. Start Live World Clocks
      updateLiveClocks();
      setInterval(updateLiveClocks, 1000);
    });

    // World Clocks Updater
    function updateLiveClocks() {
      var now = new Date();

      function formatTime(date, timeZone) {
        try {
          return new Intl.DateTimeFormat('en-US', {
            timeZone: timeZone,
            hour: '2-digit',
            minute: '2-digit',
            second: '2-digit',
            hour12: false
          }).format(date);
        } catch (e) {
          return date.toTimeString().split(' ')[0];
        }
      }

      var nycEl = document.getElementById('clockNYC');
      var lonEl = document.getElementById('clockLON');
      var sgpEl = document.getElementById('clockSGP');
      var zurEl = document.getElementById('clockZUR');

      if (nycEl) nycEl.textContent = formatTime(now, 'America/New_York');
      if (lonEl) lonEl.textContent = formatTime(now, 'Europe/London');
      if (sgpEl) sgpEl.textContent = formatTime(now, 'Asia/Singapore');
      if (zurEl) zurEl.textContent = formatTime(now, 'Europe/Zurich');
    }

    // 3. Hub Selector Interaction
    function selectHubLocation(cityName) {
      alert('Selected ' + cityName + ' Regional Hub. Dialing direct local liaison desk...');
    }

    // 4. Copy Email to Clipboard
    function copyEmailToClipboard(email, btn) {
      if (navigator.clipboard && navigator.clipboard.writeText) {
        navigator.clipboard.writeText(email).then(function () {
          var original = btn.innerHTML;
          btn.innerHTML = '<i class="fas fa-check" style="color:#10b981;"></i> Copied!';
          setTimeout(function () { btn.innerHTML = original; }, 2000);
        });
      } else {
        prompt('Copy email address:', email);
      }
    }

    // 5. Dual-Track Form Switcher
    function switchFormMode(mode) {
      var tabConsult = document.getElementById('tabConsultation');
      var tabGen = document.getElementById('tabGeneral');
      var consultFields = document.getElementById('consultationFields');
      var msgLabel = document.getElementById('messageFieldLabel');

      if (mode === 'consultation') {
        if (tabConsult) tabConsult.classList.add('active');
        if (tabGen) tabGen.classList.remove('active');
        if (consultFields) consultFields.style.display = 'block';
        if (msgLabel) msgLabel.textContent = 'Project Scope & Strategic Objectives *';
      } else {
        if (tabGen) tabGen.classList.add('active');
        if (tabConsult) tabConsult.classList.remove('active');
        if (consultFields) consultFields.style.display = 'none';
        if (msgLabel) msgLabel.textContent = 'General Inquiry & Subject Details *';
      }
    }

    // 6. Form Submission & Modal Feedback
    function handleContactFormSubmit(e) {
      e.preventDefault();
      var code = 'INQ-2026-' + Math.floor(1000 + Math.random() * 9000);
      var codeEl = document.getElementById('trackingRefCode');
      if (codeEl) codeEl.textContent = code;

      var modal = document.getElementById('contactSuccessModal');
      if (modal) modal.style.display = 'flex';
    }

    function closeContactModal() {
      var modal = document.getElementById('contactSuccessModal');
      if (modal) modal.style.display = 'none';
      var form = document.getElementById('contactMainForm');
      if (form) form.reset();
    }
  