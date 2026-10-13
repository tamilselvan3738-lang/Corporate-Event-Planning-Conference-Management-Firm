
    // 1. Intersection Observer for Unique Framer Motion Animations
    document.addEventListener('DOMContentLoaded', function() {
      var framerElements = document.querySelectorAll(
        '.framer-atrium-unfold, ' +
        '.framer-rack-mount, ' +
        '.framer-gastronomy-float, ' +
        '.framer-scenic-forge, ' +
        '.framer-fleet-manifest, ' +
        '.framer-procurement-gate, ' +
        '.framer-terminal-onboard'
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

    // 2. Venue Cluster Filter
    function filterVenueCluster(cluster, btn) {
      var btns = document.querySelectorAll('.vnd-cluster-btn');
      btns.forEach(function(b) { b.classList.remove('active'); });
      if (btn) btn.classList.add('active');

      var cards = document.querySelectorAll('.vnd-tier-card');
      cards.forEach(function(card) {
        if (cluster === 'all' || card.getAttribute('data-cluster') === cluster) {
          card.style.display = 'block';
        } else {
          card.style.display = 'none';
        }
      });
    }

    function highlightVenue(name) {
      alert('Selected Venue Campus: ' + name + '\nPreparing technical spatial dimensions and floorplan dossier.');
    }

    // 3. Scenic Forge Swatch Selector
    function selectSwatch(card, name) {
      var boxes = document.querySelectorAll('.vnd-swatch-box');
      boxes.forEach(function(b) { b.classList.remove('active'); });
      card.classList.add('active');
    }

    // 4. Dropzone Simulator
    function simulateFileUpload() {
      var textEl = document.getElementById('dropzoneText');
      if (textEl) {
        textEl.innerHTML = '<i class="fas fa-check text-success"></i> COI_Apex_2026_Certified.pdf (4.8 MB) Attached';
        textEl.style.color = '#059669';
      }
    }

    // 5. Form Submissions & Feedback Modals
    function handlePartnershipSubmit(e) {
      e.preventDefault();
      var modal = document.getElementById('vndFeedbackModal');
      var title = document.getElementById('vndModalTitle');
      var desc = document.getElementById('vndModalDesc');
      if (title) title.textContent = 'Partnership Application Transmitted';
      if (desc) desc.textContent = 'Your company portfolio and capability profile have been assigned tracking code APX-VND-' + Math.floor(1000 + Math.random() * 9000) + '. Our procurement director will review within 24 hours.';
      if (modal) modal.style.display = 'flex';
      e.target.reset();
    }

    function handleRegistrationSubmit(e) {
      e.preventDefault();
      var modal = document.getElementById('vndFeedbackModal');
      var title = document.getElementById('vndModalTitle');
      var desc = document.getElementById('vndModalDesc');
      if (title) title.textContent = 'Vendor Credentials Registered';
      if (desc) desc.textContent = 'Your entity tax documentation, COI certificates, and compliance declarations have been cryptographically secured in escrow under Dispatch ID #VP-' + Math.floor(10000 + Math.random() * 90000) + '.';
      if (modal) modal.style.display = 'flex';
      e.target.reset();
      var drop = document.getElementById('dropzoneText');
      if (drop) {
        drop.textContent = 'Drag & Drop COI, W-9, or Click to Browse';
        drop.style.color = '';
      }
    }

    function openVendorModal(itemName) {
      var modal = document.getElementById('vndFeedbackModal');
      var title = document.getElementById('vndModalTitle');
      var desc = document.getElementById('vndModalDesc');
      if (title) title.textContent = 'Documentation Queued';
      if (desc) desc.textContent = 'Technical specifications and procurement riders for "' + itemName + '" are ready for transmission. Please check your corporate inbox.';
      if (modal) modal.style.display = 'flex';
    }

    function closeVndModal() {
      var modal = document.getElementById('vndFeedbackModal');
      if (modal) modal.style.display = 'none';
    }
  