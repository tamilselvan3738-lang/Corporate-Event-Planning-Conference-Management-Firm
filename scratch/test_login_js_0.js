
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

    // 2. Password Visibility Toggle
    const togglePwdBtn = document.getElementById('togglePasswordBtn');
    const pwdInput = document.getElementById('passwordInput');
    const pwdIcon = document.getElementById('togglePasswordIcon');

    if (togglePwdBtn && pwdInput) {
      togglePwdBtn.addEventListener('click', function() {
        const isPassword = pwdInput.getAttribute('type') === 'password';
        pwdInput.setAttribute('type', isPassword ? 'text' : 'password');
        pwdIcon.className = isPassword ? 'fas fa-eye-slash' : 'fas fa-eye';
      });
    }

    // 3. Form Submission & Smooth Routing
    function handleLoginSubmit(e) {
      e.preventDefault();
      const submitBtn = document.getElementById('loginSubmitBtn');
      const submitText = document.getElementById('submitBtnText');
      const usernameVal = (document.getElementById('usernameInput')?.value || '').toLowerCase().trim();

      submitBtn.classList.add('loading');
      submitText.innerText = 'Authenticating Secure Session...';

      // Intelligent router: admin credentials route to admin-dashboard, others to user-dashboard
      const isAdmin = usernameVal.includes('admin') || usernameVal.includes('marcus') || usernameVal.includes('vance');

      setTimeout(() => {
        if (isAdmin) {
          window.location.href = 'admin-dashboard.html';
        } else {
          window.location.href = 'user-dashboard.html';
        }
      }, 600);
    }

    // 4. SSO Simulated Login
    function handleSSOLogin(provider) {
      setTimeout(() => {
        window.location.href = 'user-dashboard.html';
      }, 500);
    }

    // 5. Modals: Open & Close Helpers
    function openModal(id) {
      const modal = document.getElementById(id);
      if (modal) modal.classList.add('open');
    }

    function closeModal(id) {
      const modal = document.getElementById(id);
      if (modal) modal.classList.remove('open');
    }

    window.addEventListener('keydown', function(e) {
      if (e.key === 'Escape') {
        document.querySelectorAll('.modal-overlay').forEach(m => m.classList.remove('open'));
      }
    });

    // 6. Forgot Password Submit
    function handleForgotPasswordSubmit(e) {
      e.preventDefault();
      closeModal('forgotPasswordModal');
    }

    // 7. Register Submit
    function handleRegisterSubmit(e) {
      e.preventDefault();
      closeModal('registerModal');
    }

    // 8. Theme Toggle (Dark / Light)
    const themeToggleBtn = document.getElementById('themeToggleBtn');
    if (themeToggleBtn) {
      themeToggleBtn.addEventListener('click', function() {
        document.body.classList.toggle('light');
        const isLight = document.body.classList.contains('light');
        this.innerHTML = isLight ? '<i class="fas fa-sun" style="color: #f59e0b;"></i>' : '<i class="fas fa-cog"></i>';
      });
    }

    // 9. RTL Toggle
    const rtlToggleBtn = document.getElementById('rtlToggleBtn');
    if (rtlToggleBtn) {
      rtlToggleBtn.addEventListener('click', function() {
        document.body.classList.toggle('rtl');
      });
    }
  