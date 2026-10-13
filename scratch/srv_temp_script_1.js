
    // 1. Intersection Observer for Unique Framer Motion Animations
    document.addEventListener('DOMContentLoaded', function() {
      var framerElements = document.querySelectorAll(
        '.framer-boardroom-elevation, ' +
        '.framer-plenary-amphitheater, ' +
        '.framer-spatial-cadence, ' +
        '.framer-broadcast-matrix, ' +
        '.framer-sculptural-prism, ' +
        '.framer-gastronomic-concierge, ' +
        '.framer-concourse-dispatch'
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

    // 2. Interactive Service Highlighter
    function highlightService(card, serviceName) {
      var siblings = card.parentElement.children;
      for (var i = 0; i < siblings.length; i++) {
        siblings[i].classList.remove('active');
      }
      card.classList.add('active');
    }

    // 3. Interactive Service Modal
    function openServiceModal(serviceName) {
      var modal = document.getElementById('srvModalOverlay');
      var title = document.getElementById('srvModalTitle');
      var desc = document.getElementById('srvModalDesc');

      if (title) title.textContent = serviceName;
      if (desc) desc.textContent = 'Detailed specifications, technical riders, and staffing matrices for "' + serviceName + '" are initialized for review. Our senior advisory leads are prepared to assist.';
      if (modal) modal.style.display = 'flex';
    }

    function closeServiceModal() {
      var modal = document.getElementById('srvModalOverlay');
      if (modal) modal.style.display = 'none';
    }
  