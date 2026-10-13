
    document.addEventListener('DOMContentLoaded', function() {
      // 1. Framer Motion Scroll Trigger using IntersectionObserver
      const framerSections = document.querySelectorAll(
        '.framer-cinema-hero, .framer-chamber-matrix, .framer-neuro-lab, .framer-footprint-grid, .framer-impact-dossier, .framer-feasibility-gateway'
      );

      const observerOptions = {
        root: null,
        rootMargin: '0px 0px -100px 0px',
        threshold: 0.15
      };

      const framerObserver = new IntersectionObserver((entries, obs) => {
        entries.forEach(entry => {
          if (entry.isIntersecting) {
            entry.target.classList.add('framer-in-view');
          }
        });
      }, observerOptions);

      framerSections.forEach(sec => framerObserver.observe(sec));

      // Trigger first section immediately
      const hero = document.getElementById('hero-cinema');
      if (hero) {
        setTimeout(() => hero.classList.add('framer-in-view'), 100);
      }

      // 2. Section 2: Chamber Matrix Typology Switcher
      const matrixTabs = document.querySelectorAll('#matrixTabBar .matrix-tab-btn');
      const matrixBadge = document.getElementById('matrixBadge');
      const matrixTitle = document.getElementById('matrixTitle');
      const matrixDesc = document.getElementById('matrixDesc');
      const specCeiling = document.getElementById('specCeiling');
      const specAcoustics = document.getElementById('specAcoustics');
      const specSightline = document.getElementById('specSightline');
      const specSecurity = document.getElementById('specSecurity');

      const typologyData = {
        plenary: {
          badge: 'CAPACITY: 1,000 - 10,000+ DELEGATES',
          title: 'Giga-Plenary Amphitheatre Architecture',
          desc: "Engineered for Fortune 50 annual shareholders' meetings, global economic plenaries, and presidential addresses. Features 360-degree curved panoramic microLED backdrops, multi-tier raked amphitheater sightlines, and calibrated spatial acoustic dispersion.",
          ceiling: '18.5 Meters',
          acoustics: '-48 dB Isolation',
          sightline: '100% Zero-Obstruction',
          security: 'Tier-1 Diplomatic'
        },
        roundtable: {
          badge: 'CAPACITY: 20 - 80 C-SUITE LEADERS',
          title: 'Sovereign G7 / B20 Closed-Door Roundtables',
          desc: 'High-security diplomatic sanctuary designed for inter-governmental treaty negotiations and Fortune 10 boardroom conclaves. Equipped with RF/microwave eavesdropping countermeasures, biometric airlocks, and discrete transcription pods.',
          ceiling: '7.5 Meters',
          acoustics: '-62 dB Eavesdrop Shield',
          sightline: 'Circular Equidistant',
          security: 'Diplomatic Secret Compartment'
        },
        expo: {
          badge: 'CAPACITY: 500 - 5,000 ATTENDEES',
          title: 'Frontier Tech & Innovation Brand Pavilions',
          desc: 'Immersive experiential exhibition halls built for radical technological unveilings and sovereign investor demos. Modular kinetic trusses, high-density fiber routing, and holographic demonstration stages.',
          ceiling: '12.0 Meters',
          acoustics: 'Zoned Directional Sound',
          sightline: 'Dynamic Multi-Angle',
          security: 'Enterprise NDA Enforced'
        },
        telepresence: {
          badge: 'CAPACITY: GLOBAL SYNCHRONOUS NODES',
          title: 'Multi-City Synchronous Telepresence Pods',
          desc: 'Synchronizes executive gatherings across Zurich, New York, Tokyo, and Singapore into a single unified broadcast environment. Sub-18ms transatlantic fiber routing with zero perceived conversational delay.',
          ceiling: '9.0 Meters',
          acoustics: 'Harmonic 432Hz Matched',
          sightline: 'Bilateral Eye-Contact Camera',
          security: 'Quantum-Encrypted Uplink'
        }
      };

      matrixTabs.forEach(btn => {
        btn.addEventListener('click', function() {
          matrixTabs.forEach(b => b.classList.remove('active'));
          this.classList.add('active');
          const type = this.getAttribute('data-typology');
          const data = typologyData[type];
          if (data) {
            matrixBadge.textContent = data.badge;
            matrixTitle.textContent = data.title;
            matrixDesc.textContent = data.desc;
            specCeiling.textContent = data.ceiling;
            specAcoustics.textContent = data.acoustics;
            specSightline.textContent = data.sightline;
            specSecurity.textContent = data.security;
          }
        });
      });

      // Section 2: Capacity Slider Math
      const capSlider = document.getElementById('matrixCapacitySlider');
      const valDisplay = document.getElementById('sliderValueDisplay');
      const footprintCalc = document.getElementById('footprintCalc');
      if (capSlider) {
        capSlider.addEventListener('input', function() {
          const val = parseInt(this.value);
          valDisplay.textContent = Number(val).toLocaleString() + ' Attendees';
          const sqft = Math.round(val * 20);
          footprintCalc.textContent = Number(sqft).toLocaleString() + ' sq ft';
        });
      }

      // 3. Section 3: Neuro-Simulator Toggle
      const neuroToggleBtn = document.getElementById('neuroToggleBtn');
      const neuroModeTitle = document.getElementById('neuroModeTitle');
      const statCortisol = document.getElementById('statCortisol');
      const statRetention = document.getElementById('statRetention');
      const statAcoustic = document.getElementById('statAcoustic');
      let isNeuroOptimized = true;

      if (neuroToggleBtn) {
        neuroToggleBtn.addEventListener('click', function() {
          isNeuroOptimized = !isNeuroOptimized;
          if (isNeuroOptimized) {
            neuroModeTitle.textContent = 'EventSphere Neuro-Engineered Mode';
            neuroToggleBtn.textContent = 'Switch to Standard';
            neuroToggleBtn.style.background = '#2563eb';
            statCortisol.textContent = '-34%';
            statCortisol.style.color = '#38bdf8';
            statRetention.textContent = '8.5 Hrs';
            statRetention.style.color = '#38bdf8';
            statAcoustic.textContent = '99.4%';
            statAcoustic.style.color = '#38bdf8';
          } else {
            neuroModeTitle.textContent = 'Standard Commercial Hotel Ballroom';
            neuroToggleBtn.textContent = 'Re-engage Neuro-Lab';
            neuroToggleBtn.style.background = '#e11d48';
            statCortisol.textContent = '+42%';
            statCortisol.style.color = '#f87171';
            statRetention.textContent = '3.2 Hrs';
            statRetention.style.color = '#f87171';
            statAcoustic.textContent = '64.2%';
            statAcoustic.style.color = '#f87171';
          }
        });
      }

      // 4. Section 4: Global City Node Selector
      const cityCards = document.querySelectorAll('#cityHubsGrid .city-hub-card');
      const activeCityLabel = document.getElementById('activeCityLabel');
      const cityLabels = {
        zurich: 'Active Hub: ZURICH & GENEVA COMMAND',
        london: 'Active Hub: LONDON MAYFAIR SOVEREIGN',
        newyork: 'Active Hub: NEW YORK MANHATTAN CONVENE',
        singapore: 'Active Hub: SINGAPORE MARINA OPERATIONS',
        dubai: 'Active Hub: DUBAI DIFC SOVEREIGN PALACE',
        tokyo: 'Active Hub: TOKYO MARUNOUCHI CLEAN GRID'
      };

      cityCards.forEach(card => {
        card.addEventListener('click', function() {
          cityCards.forEach(c => c.classList.remove('active'));
          this.classList.add('active');
          const cityKey = this.getAttribute('data-city');
          if (cityLabels[cityKey] && activeCityLabel) {
            activeCityLabel.textContent = cityLabels[cityKey];
          }
        });
      });

      // 5. Section 5: Casebook Dossier Switcher
      const caseChips = document.querySelectorAll('#caseNavTabs .case-tab-chip');
      const caseBadge = document.getElementById('caseBadge');
      const caseTitle = document.getElementById('caseTitle');
      const caseSummary = document.getElementById('caseSummary');
      const kpiVal1 = document.getElementById('kpiValue1');
      const kpiLbl1 = document.getElementById('kpiLabel1');
      const kpiVal2 = document.getElementById('kpiValue2');
      const kpiLbl2 = document.getElementById('kpiLabel2');
      const kpiVal3 = document.getElementById('kpiValue3');
      const kpiLbl3 = document.getElementById('kpiLabel3');
      const caseQuote = document.getElementById('caseQuote');
      const caseAuthor = document.getElementById('caseAuthor');

      const casebookData = {
        fintech: {
          badge: 'JURISDICTION: GENEVA, SWITZERLAND',
          title: 'World FinTech Sovereign Summit 2025',
          summary: 'Convened 5,800 institutional finance leaders, central bank governors, and fintech founders across 42 countries. Delivered triple-redundant satellite feeds, bilateral treaty lounges, and biometric voting telemetry with zero latency.',
          kpis: ['$4.2B+', 'M&A Liquidity Closed', '0.00%', 'Stream Downtime', '99.1%', 'Net Promoter Score'],
          quote: '"EventSphere Sovereign executed our 3-day ministerial assembly with flawless precision. Their neuro-acoustic zoning kept our delegates focused through 14 hours of contentious treaty negotiations."',
          author: '— Lord Alistair Vance, Secretary General, International Banking Forum'
        },
        climate: {
          badge: 'JURISDICTION: ZURICH ALPINE PAVILION',
          title: 'Global Decarbonization Leadership Plenary',
          summary: '1,400 ministerial and Fortune 100 executives convened to execute cross-border green accords. Certified ISO-20121 carbon-neutral execution with live blockchain carbon offset telemetry on a 60m panoramic LED screen.',
          kpis: ['100%', 'Zero-Waste Certified', '1,400', 'Cabinet Leaders Present', '18.4k', 'Tons CO2 Offset'],
          quote: '"The spatial elegance and zero-emission delivery established an entirely new global benchmark for sustainable sovereign assemblies."',
          author: '— Dr. Elena Rostova, High Commissioner for Clean Infrastructure'
        },
        ai: {
          badge: 'JURISDICTION: NEW YORK & SINGAPORE DUAL-NODE',
          title: 'Frontier AI Enterprise Architecture Conclave',
          summary: 'Synchronous transcontinental summit linking 3,200 senior engineers and enterprise CEOs. Live interactive code compilations broadcast across 12 timezones with sub-18ms ping and facial biometric check-in.',
          kpis: ['18ms', 'Trans-Pacific Latency', '3,200', 'Enterprise Architects', '100%', 'Biometric Precision'],
          quote: '"The dual-stage holographic telepresence felt as if the Singapore keynote speaker was standing physically on our Manhattan plenary stage."',
          author: '— Marcus Chen, Chief Technology Officer, NexGen Cloud Holdings'
        }
      };

      caseChips.forEach(chip => {
        chip.addEventListener('click', function() {
          caseChips.forEach(c => c.classList.remove('active'));
          this.classList.add('active');
          const key = this.getAttribute('data-case');
          const d = casebookData[key];
          if (d) {
            caseBadge.textContent = d.badge;
            caseTitle.textContent = d.title;
            caseSummary.textContent = d.summary;
            kpiVal1.textContent = d.kpis[0];
            kpiLbl1.textContent = d.kpis[1];
            kpiVal2.textContent = d.kpis[2];
            kpiLbl2.textContent = d.kpis[3];
            kpiVal3.textContent = d.kpis[4];
            kpiLbl3.textContent = d.kpis[5];
            caseQuote.textContent = d.quote;
            caseAuthor.innerHTML = d.author;
          }
        });
      });

      // 6. Section 6: Feasibility Engine Live Calculations
      const calcDelegateRange = document.getElementById('calcDelegateRange');
      const calcDelegateDisplay = document.getElementById('calcDelegateDisplay');
      const calcFootprint = document.getElementById('calcFootprint');
      const calcCrew = document.getElementById('calcCrew');
      const calcWindow = document.getElementById('calcWindow');
      const calcTier = document.getElementById('calcTier');
      const calcTypology = document.getElementById('calcTypology');

      function updateFeasibilityMath() {
        if (!calcDelegateRange) return;
        const pax = parseInt(calcDelegateRange.value);
        calcDelegateDisplay.textContent = Number(pax).toLocaleString() + ' Delegates';

        // Calculation algorithms
        let sqftPerPerson = 22;
        if (calcTypology.value === 'roundtable') sqftPerPerson = 45;
        if (calcTypology.value === 'expo') sqftPerPerson = 35;
        const totalSqft = Math.round(pax * sqftPerPerson);
        calcFootprint.textContent = Number(totalSqft).toLocaleString() + ' sq ft';

        // Crew
        let crewScale = Math.round(14 + (pax / 75));
        if (calcTier.value === 'sovereign') crewScale += 18;
        calcCrew.textContent = crewScale + ' Specialists';

        // Lead time
        let weeks = '8 - 10 Weeks';
        if (pax > 2000) weeks = '12 - 16 Weeks';
        if (pax > 5000) weeks = '20 - 24 Weeks';
        calcWindow.textContent = weeks;
      }

      if (calcDelegateRange) {
        calcDelegateRange.addEventListener('input', updateFeasibilityMath);
      }
      if (calcTier) {
        calcTier.addEventListener('change', updateFeasibilityMath);
      }
      if (calcTypology) {
        calcTypology.addEventListener('change', updateFeasibilityMath);
      }
      updateFeasibilityMath();
    });

    // Form submission handler
    function handleScopingSubmit(e) {
      e.preventDefault();
      const form = document.getElementById('scopingConsultForm');
      const successMsg = document.getElementById('scopingSuccessMsg');
      if (form && successMsg) {
        form.style.display = 'none';
        successMsg.style.display = 'block';
      }
    }
  