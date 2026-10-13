
    // 1. Starfield Particles Canvas Animation (Matching Screenshot Background)
    (function initParticles() {
      const canvas = document.getElementById('particlesCanvas');
      if (!canvas) return;
      const ctx = canvas.getContext('2d');
      let width, height;
      let particles = [];
      const particleCount = 75;

      function resize() {
        width = canvas.width = window.innerWidth;
        height = canvas.height = window.innerHeight;
      }
      window.addEventListener('resize', resize);
      resize();

      class Particle {
        constructor() {
          this.reset(true);
        }
        reset(initial = false) {
          this.x = Math.random() * width;
          this.y = initial ? Math.random() * height : height + 10;
          this.radius = Math.random() * 2.2 + 0.6;
          this.vy = -(Math.random() * 0.45 + 0.15);
          this.vx = (Math.random() - 0.5) * 0.25;
          this.baseAlpha = Math.random() * 0.7 + 0.2;
          this.alpha = this.baseAlpha;
          this.fadeSpeed = Math.random() * 0.015 + 0.005;
          this.growing = true;
          // Colors: gold/amber and cyan/sapphire
          const colors = [
            'rgba(245, 158, 11, ', // Amber gold
            'rgba(56, 189, 248, ',  // Cyan sky
            'rgba(96, 165, 250, ',  // Soft blue
            'rgba(251, 191, 36, '   // Bright gold
          ];
          this.colorPrefix = colors[Math.floor(Math.random() * colors.length)];
        }
        update() {
          this.y += this.vy;
          this.x += this.vx;

          if (this.growing) {
            this.alpha += this.fadeSpeed;
            if (this.alpha >= this.baseAlpha + 0.2) this.growing = false;
          } else {
            this.alpha -= this.fadeSpeed;
            if (this.alpha <= 0.1) this.growing = true;
          }

          if (this.y < -10 || this.x < -10 || this.x > width + 10) {
            this.reset();
          }
        }
        draw() {
          ctx.beginPath();
          ctx.arc(this.x, this.y, this.radius, 0, Math.PI * 2);
          ctx.fillStyle = this.colorPrefix + Math.max(0, Math.min(1, this.alpha)) + ')';
          ctx.shadowBlur = this.radius * 4;
          ctx.shadowColor = this.colorPrefix + '0.8)';
          ctx.fill();
        }
      }

      for (let i = 0; i < particleCount; i++) {
        particles.push(new Particle());
      }

      function animate() {
        ctx.clearRect(0, 0, width, height);
        particles.forEach(p => {
          p.update();
          p.draw();
        });
        requestAnimationFrame(animate);
      }
      animate();
    })();

    // 2. Password Visibility Toggles
    function setupPasswordToggle(btnId, inputId, iconId) {
      const btn = document.getElementById(btnId);
      const input = document.getElementById(inputId);
      const icon = document.getElementById(iconId);
      if (btn && input && icon) {
        btn.addEventListener('click', function() {
          const isPassword = input.getAttribute('type') === 'password';
          input.setAttribute('type', isPassword ? 'text' : 'password');
          icon.className = isPassword ? 'fas fa-eye-slash' : 'fas fa-eye';
        });
      }
    }
    setupPasswordToggle('togglePasswordBtn1', 'passwordInput', 'togglePasswordIcon1');
    setupPasswordToggle('togglePasswordBtn2', 'confirmPasswordInput', 'togglePasswordIcon2');

    // 3. Form Submission & Client Onboarding
    function handleRegistrationSubmit(e) {
      e.preventDefault();
      const pwd = document.getElementById('passwordInput').value;
      const confirmPwd = document.getElementById('confirmPasswordInput').value;
      const fullName = document.getElementById('fullNameInput').value;

      if (pwd !== confirmPwd) {
        alert('Passwords do not match! Please check and re-enter.');
        return;
      }

      const submitBtn = document.getElementById('regSubmitBtn');
      const submitText = document.getElementById('submitBtnText');

      submitBtn.classList.add('loading');
      submitText.innerText = 'Provisioning Executive Account...';

      setTimeout(() => {
        window.location.href = 'user-dashboard.html';
      }, 700);
    }

    // 4. SSO Simulated Registration
    function handleSSORegistration(provider) {
      setTimeout(() => {
        window.location.href = 'user-dashboard.html';
      }, 500);
    }

    // 5. Theme Toggle (Dark / Light)
    const themeToggleBtn = document.getElementById('themeToggleBtn');
    if (themeToggleBtn) {
      themeToggleBtn.addEventListener('click', function() {
        document.body.classList.toggle('light');
        const isLight = document.body.classList.contains('light');
        this.innerHTML = isLight ? '<i class="fas fa-sun" style="color: #f59e0b;"></i>' : '<i class="fas fa-cog"></i>';
      });
    }

    // 6. RTL Toggle with Right-Left Icon
    const rtlToggleBtn = document.getElementById('rtlToggleBtn');
    if (rtlToggleBtn) {
      rtlToggleBtn.addEventListener('click', function() {
        document.body.classList.toggle('rtl');
      });
    }
  