
    // 1. Framer Motion Scroll Trigger Observers
    document.addEventListener('DOMContentLoaded', function () {
      var motionClasses = [
        '.framer-monolith-panoramic',
        '.framer-rotary-dial',
        '.framer-keycard-matrix',
        '.framer-meridian-wave',
        '.framer-radar-sweep',
        '.framer-foundry-studio',
        '.framer-beacon-alert'
      ];

      var motionObserver = new IntersectionObserver(function (entries, obs) {
        entries.forEach(function (entry) {
          if (entry.isIntersecting) {
            entry.target.classList.add('framer-in-view');
            var children = entry.target.querySelectorAll('.framer-monolith-panoramic, .framer-rotary-dial, .framer-keycard-matrix, .framer-meridian-wave, .framer-radar-sweep, .framer-foundry-studio, .framer-beacon-alert');
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

    // 3. Copy Email to Clipboard
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

    // 4. Radar Pin Switcher
    function switchRadarPin(cityName, coords, address, btn) {
      document.querySelectorAll('.cnt-radar-city-btn').forEach(function (b) {
        b.classList.remove('active');
      });
      btn.classList.add('active');

      var nameEl = document.getElementById('radarTargetName');
      var coordsEl = document.getElementById('radarTargetCoords');
      var hudCityEl = document.getElementById('radarHudCity');

      if (nameEl) nameEl.textContent = cityName + ' Hub';
      if (coordsEl) coordsEl.textContent = coords;
      if (hudCityEl) hudCityEl.textContent = cityName.toUpperCase();
    }

    // 5. Foundry Studio Mode Switcher
    function setFoundryMode(mode) {
      var btnConsult = document.getElementById('btnModeConsultation');
      var btnGen = document.getElementById('btnModeGeneral');
      var consultFields = document.getElementById('foundryConsultationFields');
      var genFields = document.getElementById('foundryGeneralFields');
      var msgLabel = document.getElementById('foundryMessageLabel');

      if (mode === 'consultation') {
        if (btnConsult) btnConsult.classList.add('active');
        if (btnGen) btnGen.classList.remove('active');
        if (consultFields) consultFields.style.display = 'flex';
        if (genFields) genFields.style.display = 'none';
        if (msgLabel) msgLabel.textContent = 'Project Scope & Strategic Objectives *';
      } else {
        if (btnGen) btnGen.classList.add('active');
        if (btnConsult) btnConsult.classList.remove('active');
        if (consultFields) consultFields.style.display = 'none';
        if (genFields) genFields.style.display = 'flex';
        if (msgLabel) msgLabel.textContent = 'General Inquiry & Subject Details *';
      }
    }

    // 6. Form Submission & Modal
    function handleFoundrySubmit(e) {
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
      var form = document.getElementById('foundryStudioForm');
      if (form) form.reset();
    }
  