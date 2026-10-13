
    // 1. Intersection Observer for Bespoke Framer Motion Animations
    document.addEventListener('DOMContentLoaded', function() {
      var framerElements = document.querySelectorAll(
        '.framer-codex-stack, ' +
        '.framer-mission-gauge, ' +
        '.framer-ledger-cascade, ' +
        '.framer-spatial-radar, ' +
        '.framer-telemetry-nexus, ' +
        '.framer-monograph-editorial, ' +
        '.framer-vault-accordion'
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

      // Initialize Checklist Task Matrix
      renderChecklistPhase(0);
    });

    // 2. Guide Category Filter
    function filterGuides(category, btn) {
      var pills = document.querySelectorAll('.res-arch-pill');
      pills.forEach(function(p) { p.classList.remove('active'); });
      if (btn) btn.classList.add('active');

      var cards = document.querySelectorAll('.res-micro-card');
      cards.forEach(function(card) {
        if (category === 'all' || card.getAttribute('data-category') === category) {
          card.style.display = 'flex';
        } else {
          card.style.display = 'none';
        }
      });
    }

    // 3. Conference Preparation Checklist State & Phase Matrix
    var checklistData = [
      {
        phase: 'Phase I: Strategic Foundation Checkpoints (T-180 Days)',
        tasks: [
          { title: 'Executive Charter & Objectives Sign-off', desc: 'Secure alignment on key deliverables and attendee demographics.', tag: 'Governance', done: true },
          { title: 'Prime Venue Sourcing & RFP Shortlisting', desc: 'Distribute spatial criteria to verified convention centers.', tag: 'Procurement', done: true },
          { title: 'Keynote Speaker & Luminary Hold Dates', desc: 'Confirm availability and draft initial appearance agreements.', tag: 'Talent', done: true },
          { title: 'Preliminary Budget Allocation Model Lock', desc: 'Establish approved Capex and contingency variance thresholds.', tag: 'Finance', done: true },
          { title: 'Steering Committee Bi-Weekly Cadence', desc: 'Assign workstream leaders across marketing, AV, and VIP liaison.', tag: 'Operations', done: false }
        ]
      },
      {
        phase: 'Phase II: Production Matrix & RFP Vetting (T-90 Days)',
        tasks: [
          { title: 'Audiovisual & Stage Fabricator Contracting', desc: 'Review 3D CAD renders, rigging calculations, and LED volume specs.', tag: 'Technical', done: true },
          { title: 'Sponsorship Packages & Exhibitor Portal Launch', desc: 'Publish booth tiers and distribute technical electrical riders.', tag: 'Revenue', done: true },
          { title: 'Hospitality & VIP Menu Tasting Protocols', desc: 'Verify dietary certifications, banquet staffing, and cocktail logistics.', tag: 'Catering', done: true },
          { title: 'Emergency Management & Municipal Permit Filings', desc: 'Submit fire marshal plans and medical emergency egress maps.', tag: 'Safety', done: false },
          { title: 'Branding & Scenic Collateral Production Run', desc: 'Sign off high-resolution vector print assets and lanyard runs.', tag: 'Creative', done: false }
        ]
      },
      {
        phase: 'Phase III: Logistics & Rehearsals (T-30 Days)',
        tasks: [
          { title: 'Complete Minute-by-Minute Run-of-Show Lock', desc: 'Synchronize stage cues, presenter walk-ups, and audio stings.', tag: 'Show Calling', done: true },
          { title: 'Freight Dispatch & Custom Carnet Clearance', desc: 'Track transit trucks carrying proprietary lighting rigs and AV servers.', tag: 'Logistics', done: true },
          { title: 'Mobile App & Digital Credential Deployment', desc: 'Test barcode badge scanning and personalized delegate agendas.', tag: 'Digital', done: false },
          { title: 'VIP Motorcade Ingress & Green Room Walkthrough', desc: 'Dry-run dignitary arrival routes with municipal security escorts.', tag: 'Security', done: false },
          { title: 'Presenter Slide Deck Review & 16:9 Formatting', desc: 'Conduct technical rehearsals and check embedded video audio codecs.', tag: 'Content', done: false }
        ]
      },
      {
        phase: 'Phase IV: Zero-Hour Execution (T-24 Hours to Go-Live)',
        tasks: [
          { title: 'Complete Intercom & Radio Channel Sweep', desc: 'Verify clear comms between Show Caller, Audio Engineer, and Stage Manager.', tag: 'Comms', done: true },
          { title: 'Primary & Backup Generator Load Test', desc: 'Simulate municipal power failure and measure transfer switch response.', tag: 'Redundancy', done: true },
          { title: 'Confidence Monitor & Teleprompter Dry Run', desc: 'Ensure keynote scripts and downstage timer clocks are synchronized.', tag: 'Staging', done: true },
          { title: 'Catering Line Health & Sanitation Audit', desc: 'Inspect back-of-house culinary prep areas and refrigeration logs.', tag: 'Hospitality', done: true },
          { title: 'Doors Open Final Radio Clearance', desc: 'Authorize registration concourse opening and delegate badge flow.', tag: 'Launch', done: true }
        ]
      }
    ];

    var currentPhaseIdx = 0;

    function renderChecklistPhase(phaseIdx) {
      currentPhaseIdx = phaseIdx;
      var data = checklistData[phaseIdx];
      var titleEl = document.getElementById('activePhaseTitle');
      if (titleEl) titleEl.textContent = data.phase;

      var container = document.getElementById('taskItemsContainer');
      if (!container) return;

      container.innerHTML = '';
      var cleared = 0;

      data.tasks.forEach(function(task, idx) {
        if (task.done) cleared++;
        var item = document.createElement('div');
        item.className = 'res-task-item' + (task.done ? ' completed' : '');
        item.onclick = function() {
          task.done = !task.done;
          renderChecklistPhase(currentPhaseIdx);
        };

        var checkIcon = task.done ? '<i class="fas fa-check"></i>' : '';
        item.innerHTML = 
          '<div class="res-task-check">' + checkIcon + '</div>' +
          '<div class="res-task-content">' +
            '<div class="res-task-title">' + task.title + '</div>' +
            '<div class="res-task-desc">' + task.desc + '</div>' +
            '<span class="res-task-tag">' + task.tag + '</span>' +
          '</div>';
        container.appendChild(item);
      });

      var badgeEl = document.getElementById('clearedCountBadge');
      if (badgeEl) badgeEl.textContent = cleared + ' of ' + data.tasks.length + ' Cleared';

      // Update Radial Gauge across all phases
      updateOverallGauge();
    }

    function updateOverallGauge() {
      var total = 0;
      var done = 0;
      checklistData.forEach(function(phase) {
        phase.tasks.forEach(function(t) {
          total++;
          if (t.done) done++;
        });
      });

      var pct = Math.round((done / total) * 100);
      var textEl = document.getElementById('radialGaugeText');
      if (textEl) textEl.textContent = pct + '%';

      var bar = document.getElementById('radialGaugeBar');
      if (bar) {
        // circumference for r=36 is ~226
        var offset = 226 - (226 * (pct / 100));
        bar.style.strokeDashoffset = offset;
      }
    }

    function switchChecklistPhase(idx, btn, card) {
      if (btn) {
        var btns = document.querySelectorAll('.res-phase-btn');
        btns.forEach(function(b) { b.classList.remove('active'); });
        btn.classList.add('active');
      }

      var cards = document.querySelectorAll('.res-phase-card');
      cards.forEach(function(c, cIdx) {
        if (cIdx === idx) c.classList.add('active');
        else c.classList.remove('active');
      });

      renderChecklistPhase(idx);
    }

    // 4. Budget Planning Slider & Dynamic Allocation
    function updateBudgetSimulation(val) {
      val = parseInt(val, 10);
      var display = document.getElementById('sliderDisplayVal');
      if (display) display.textContent = '$' + val.toLocaleString();

      // Allocations
      var c1 = Math.round(val * 0.35); // 35% Venue & Staging
      var c2 = Math.round(val * 0.25); // 25% AV & Tech
      var c3 = Math.round(val * 0.20); // 20% Hospitality
      var c4 = Math.round(val * 0.20); // 20% Contingency

      var el1 = document.getElementById('costCenter1');
      var el2 = document.getElementById('costCenter2');
      var el3 = document.getElementById('costCenter3');
      var el4 = document.getElementById('costCenter4');

      if (el1) el1.textContent = '$' + c1.toLocaleString();
      if (el2) el2.textContent = '$' + c2.toLocaleString();
      if (el3) el3.textContent = '$' + c3.toLocaleString();
      if (el4) el4.textContent = '$' + c4.toLocaleString();

      // Estimated ROI (4.2x multiplier)
      var roiVal = document.getElementById('projectedRoiVal');
      if (roiVal) roiVal.textContent = '$' + Math.round(val * 4.2).toLocaleString() + ' Estimated Value';
    }

    // 5. Venue Guide Hotspots & Dimension Switcher
    function switchVenueDimension(dim, btn) {
      var tabs = document.querySelectorAll('.res-dim-tab');
      tabs.forEach(function(t) { t.classList.remove('active'); });
      if (btn) btn.classList.add('active');

      if (dim === 'structural') {
        activateHotspot(1, 'Truss Rigging & 28ft Clear Height', 'Structural roof supports certified for 45,000 lbs distributed AV payload and dynamic line arrays.');
      } else if (dim === 'ingress') {
        activateHotspot(2, 'Direct Freight Ingress Dock', 'Twin roll-up freight bays (16ft x 14ft) capable of receiving 53ft semitruck trailers directly onto plenary floor.');
      } else if (dim === 'acoustics') {
        activateHotspot(3, 'VIP Green Room Isolation Zone', 'Soundproofed green room with private executive restroom, secure fiber optic feed, and discreet motorcade egress.');
      } else if (dim === 'power') {
        activateHotspot(4, 'Emergency Egress & Fire Marshal Matrix', 'Dual-redundant primary egress corridors exceeding municipal NFPA-101 crowd dispersion standards by 35%.');
      }
    }

    function activateHotspot(num, title, detail) {
      var tagEl = document.getElementById('hotspotTag');
      var titleEl = document.getElementById('hotspotTitle');
      var detailEl = document.getElementById('hotspotDetail');

      if (tagEl) tagEl.textContent = 'Hotspot ' + num + ' Selected';
      if (titleEl) titleEl.textContent = title;
      if (detailEl) detailEl.textContent = detail;
    }

    // 6. Article Taxonomy Filter
    function filterArticles(cat, btn) {
      var btns = document.querySelectorAll('.res-tax-btn');
      btns.forEach(function(b) { b.classList.remove('active'); });
      if (btn) btn.classList.add('active');

      var briefs = document.querySelectorAll('.res-brief-card');
      briefs.forEach(function(b) {
        if (cat === 'all' || b.getAttribute('data-category') === cat) {
          b.style.display = 'flex';
        } else {
          b.style.display = 'none';
        }
      });
    }

    // 7. FAQ Smart Accordion & Live Search
    function toggleFaqItem(header) {
      var item = header.closest('.res-faq-item');
      if (!item) return;
      var isActive = item.classList.contains('active');

      // Optional: keep single open or accordion
      var allItems = document.querySelectorAll('.res-faq-item');
      allItems.forEach(function(i) { i.classList.remove('active'); });

      if (!isActive) {
        item.classList.add('active');
      }
    }

    function filterFaqLive(query) {
      query = query.toLowerCase().trim();
      var items = document.querySelectorAll('.res-faq-item');
      items.forEach(function(item) {
        var text = item.textContent.toLowerCase();
        if (query === '' || text.indexOf(query) !== -1) {
          item.style.display = 'block';
        } else {
          item.style.display = 'none';
        }
      });
    }

    function filterFaqCategory(cat, btn) {
      var btns = document.querySelectorAll('.res-faq-cat-btn');
      btns.forEach(function(b) { b.classList.remove('active'); });
      if (btn) btn.classList.add('active');

      var searchInput = document.getElementById('faqSearchInput');
      if (searchInput) searchInput.value = '';

      var items = document.querySelectorAll('.res-faq-item');
      items.forEach(function(item) {
        if (cat === 'all' || item.getAttribute('data-category') === cat) {
          item.style.display = 'block';
        } else {
          item.style.display = 'none';
        }
      });
    }

    function rateFaq(btn, isPositive) {
      btn.style.background = isPositive ? 'rgba(5, 150, 105, 0.2)' : 'rgba(220, 38, 38, 0.2)';
      btn.style.borderColor = isPositive ? '#059669' : '#dc2626';
      btn.innerHTML = '<i class="fas fa-check"></i> Feedback Recorded';
      btn.disabled = true;
    }

    // 8. Download / Quick View Modals
    function openDownloadModal(docName) {
      var modal = document.getElementById('resDownloadModal');
      var title = document.getElementById('resModalTitle');
      var desc = document.getElementById('resModalDesc');

      if (title) title.textContent = 'Resource Download Ready';
      if (desc) desc.textContent = 'You are downloading "' + docName + '". This certified document includes full ISO-20121 templates and implementation worksheets.';
      if (modal) modal.style.display = 'flex';
    }

    function openQuickView(docName) {
      var modal = document.getElementById('resDownloadModal');
      var title = document.getElementById('resModalTitle');
      var desc = document.getElementById('resModalDesc');

      if (title) title.textContent = 'Executive Preview Mode';
      if (desc) desc.textContent = 'Previewing: ' + docName + '. All proprietary production rubrics and spatial guidelines have been initialized for client review.';
      if (modal) modal.style.display = 'flex';
    }

    function closeResModal() {
      var modal = document.getElementById('resDownloadModal');
      if (modal) modal.style.display = 'none';
    }

    function confirmDownload() {
      alert('Your document download has commenced! Thank you for accessing the Apex Knowledge Repository.');
      closeResModal();
    }

    function handleNewsletterSubmit(e) {
      e.preventDefault();
      alert('Thank you! You have been successfully subscribed to our Quarterly Strategic Intelligence Briefings.');
      e.target.reset();
    }
  