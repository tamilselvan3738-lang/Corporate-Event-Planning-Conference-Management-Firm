
  // 1. Framer Motion Scroll Trigger Observers
    document.addEventListener('DOMContentLoaded', () => {
      const motionClasses = [
        '.framer-colonnade-reveal',
        '.framer-hardware-dial',
        '.framer-culinary-float',
        '.framer-scenic-construct',
        '.framer-transit-glide',
        '.framer-compliance-stamp',
        '.framer-portal-unlock'
      ];

      const motionObserver = new IntersectionObserver((entries, obs) => {
        entries.forEach(entry => {
          if (entry.isIntersecting) {
            entry.target.classList.add('framer-in-view');
            // Stagger child elements if any
            const children = entry.target.querySelectorAll('.framer-colonnade-reveal, .framer-hardware-dial, .framer-culinary-float, .framer-scenic-construct, .framer-transit-glide, .framer-compliance-stamp, .framer-portal-unlock');
            children.forEach((c, idx) => {
              setTimeout(() => c.classList.add('framer-in-view'), idx * 80);
            });
            obs.unobserve(entry.target);
          }
        });
      }, {
        threshold: 0.15,
        rootMargin: '0px 0px -50px 0px'
      });

      motionClasses.forEach(selector => {
        document.querySelectorAll(selector).forEach(el => motionObserver.observe(el));
      });
    });

    // 2. Section 1: Venue Tier Selector
    const venueTiersData = [
      {
        title: "The Grand Plenary Palace & Exposition Atrium",
        desc: "Featuring clear-span columnless architecture, acoustic wall baffle treatments, and automated rigging trusses capable of hosting up to 12,500 delegates in full plenary configuration.",
        cap: "12,500 Delegates",
        sound: "54 dB STC",
        rig: "120 Metric Tons"
      },
      {
        title: "Marina Waterfront Amphitheater & Glasshouse",
        desc: "Acoustically tuned curved shells overlooking the bay with adjacent floor-to-ceiling glass pavilions, direct boat dock ingress, and sunset networking terraces.",
        cap: "4,500 Delegates",
        sound: "48 dB STC",
        rig: "75 Metric Tons"
      },
      {
        title: "Alpine Heritage Castle & Sovereign Sovereign Estate",
        desc: "Private 18th-century baroque architecture retrofitted with secure satellite fiber uplinks, sovereign VIP security perimeter, and private helicopter landing pads.",
        cap: "1,200 Delegates",
        sound: "50 dB STC",
        rig: "40 Metric Tons"
      }
    ];

    function selectVenueTier(index) {
      const pods = document.querySelectorAll('.vn-colonnade-pod');
      pods.forEach((p, idx) => {
        if (idx === index) p.classList.add('active');
        else p.classList.remove('active');
      });

      const data = venueTiersData[index];
      const titleEl = document.getElementById('currentVenueTitle');
      const descEl = document.getElementById('currentVenueDesc');
      const capEl = document.getElementById('venueCapStat');
      const soundEl = document.getElementById('venueSoundStat');
      const rigEl = document.getElementById('venueRigStat');

      if (titleEl) {
        titleEl.style.opacity = '0';
        setTimeout(() => {
          titleEl.textContent = data.title;
          if (descEl) descEl.textContent = data.desc;
          if (capEl) capEl.textContent = data.cap;
          if (soundEl) soundEl.textContent = data.sound;
          if (rigEl) rigEl.textContent = data.rig;
          titleEl.style.opacity = '1';
        }, 180);
      }
    }

    // 3. Section 2: AV Hardware Mode Switcher
    const avPresets = [
      { latency: '1.2 ms', refresh: '7,680 Hz', uptime: '99.999%' },
      { latency: '2.8 ms', refresh: '3,840 Hz', uptime: '99.995%' },
      { latency: '0.8 ms', refresh: '7,680 Hz', uptime: '100.00%' }
    ];

    function switchAVPreset(index, btn) {
      document.querySelectorAll('.vn-switch-btn').forEach(b => b.classList.remove('active'));
      btn.classList.add('active');

      const data = avPresets[index];
      const latEl = document.getElementById('avLatencyVal');
      const refEl = document.getElementById('avRefreshVal');
      const upEl = document.getElementById('avUptimeVal');

      if (latEl) latEl.textContent = data.latency;
      if (refEl) refEl.textContent = data.refresh;
      if (upEl) upEl.textContent = data.uptime;
    }

    // 4. Section 4: Production Material Swatch Selector
    function activateSwatch(card, description) {
      document.querySelectorAll('.vn-swatch-card').forEach(c => c.classList.remove('active'));
      card.classList.add('active');
      const noteEl = document.getElementById('swatchNote');
      if (noteEl) noteEl.textContent = description;
    }

    // 5. Section 5: VIP Fleet Category Filter
    function filterFleet(category, btn) {
      document.querySelectorAll('.vn-transport-filter-btn').forEach(b => b.classList.remove('active'));
      btn.classList.add('active');

      const pods = document.querySelectorAll('.vn-fleet-pod');
      pods.forEach(pod => {
        const podFleet = pod.getAttribute('data-fleet');
        if (category === 'all' || podFleet === category) {
          pod.style.display = 'flex';
          pod.style.opacity = '1';
        } else {
          pod.style.display = 'none';
        }
      });
    }

    // 6. Section 6: Compliance Auditor Tool
    let currentComplianceScore = 100;
    function updateComplianceScore(checkbox, weight) {
      if (checkbox.checked) {
        currentComplianceScore += weight;
      } else {
        currentComplianceScore -= weight;
      }
      currentComplianceScore = Math.max(0, Math.min(100, currentComplianceScore));

      const numEl = document.getElementById('complianceScoreNum');
      const badgeEl = document.getElementById('complianceScoreBadge');

      if (numEl) numEl.textContent = currentComplianceScore;
      if (badgeEl) {
        if (currentComplianceScore >= 85) {
          badgeEl.textContent = 'Tier-1 Qualified';
          badgeEl.style.background = '#10b981';
        } else if (currentComplianceScore >= 60) {
          badgeEl.textContent = 'Tier-2 Preferred';
          badgeEl.style.background = '#f59e0b';
        } else {
          badgeEl.textContent = 'Needs Review';
          badgeEl.style.background = '#ef4444';
        }
      }
    }

    // 7. Section 7: File Upload & Registration Submission
    function triggerFileUpload() {
      const input = document.getElementById('hiddenFileInput');
      if (input) input.click();
    }

    function handleFileSelected(input) {
      if (input.files && input.files.length > 0) {
        const fileName = input.files[0].name;
        const textEl = document.getElementById('dropzoneText');
        if (textEl) {
          textEl.innerHTML = `<span style="color:#10b981;"><i class="fas fa-check-circle"></i> File Attached: ${fileName}</span>`;
        }
      }
    }

    function handleVendorSubmit(e) {
      e.preventDefault();
      const code = 'VR-2026-' + Math.floor(1000 + Math.random() * 9000);
      const codeEl = document.getElementById('trackingRefCode');
      if (codeEl) codeEl.textContent = code;

      const modal = document.getElementById('vendorSuccessModal');
      if (modal) modal.style.display = 'flex';
    }

    function closeVendorModal() {
      const modal = document.getElementById('vendorSuccessModal');
      if (modal) modal.style.display = 'none';
      const form = document.getElementById('vendorRegForm');
      if (form) form.reset();
      const textEl = document.getElementById('dropzoneText');
      if (textEl) textEl.textContent = 'Drag & Drop COI or Click to Browse Files';
    }
    