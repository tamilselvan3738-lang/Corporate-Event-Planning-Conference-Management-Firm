
    // 1. Intersection Observer for Unique Framer Motion Animations
    document.addEventListener('DOMContentLoaded', function() {
      var framerElements = document.querySelectorAll(
        '.framer-epoch-chronicle, ' +
        '.framer-polarity-gyro, ' +
        '.framer-triad-pedestal, ' +
        '.framer-council-quad, ' +
        '.framer-division-matrix, ' +
        '.framer-marquee-portfolio, ' +
        '.framer-citadel-moat'
      );

      var observer = new IntersectionObserver(function(entries) {
        entries.forEach(function(entry) {
          if (entry.isIntersecting) {
            entry.target.classList.add('framer-in-view');
          }
        });
      }, {
        threshold: 0.12,
        rootMargin: '0px 0px -40px 0px'
      });

      framerElements.forEach(function(el) {
        observer.observe(el);
      });
    });

    // 2. Epoch Timeline Selector
    function selectEpoch(card, era) {
      var cards = document.querySelectorAll('.abt-epoch-card');
      cards.forEach(function(c) { c.classList.remove('active'); });
      card.classList.add('active');
    }

    // 3. Division Selector
    function selectDivision(card, divName) {
      var cards = document.querySelectorAll('.abt-division-card');
      cards.forEach(function(c) { c.classList.remove('active'); });
      card.classList.add('active');
    }

    // 4. Executive Bio Modal
    function openBioModal(name, role, desc) {
      var modal = document.getElementById('abtBioModal');
      var nameEl = document.getElementById('abtModalName');
      var roleEl = document.getElementById('abtModalRole');
      var descEl = document.getElementById('abtModalDesc');

      if (nameEl) nameEl.textContent = name;
      if (roleEl) roleEl.textContent = role;
      if (descEl) descEl.textContent = desc;
      if (modal) modal.style.display = 'flex';
    }

    function closeAbtModal() {
      var modal = document.getElementById('abtBioModal');
      if (modal) modal.style.display = 'none';
    }
  