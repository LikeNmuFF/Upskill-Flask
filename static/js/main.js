 // ── THEME ────────────────────────────────────────────────────────────────────
    const html = document.documentElement;
    const btn = document.getElementById('theme-toggle');
    const saved = localStorage.getItem('flask-roadmap-theme') || 'dark';
    applyTheme(saved);
    btn.addEventListener('click', () => {
      const next = html.getAttribute('data-theme') === 'light' ? 'dark' : 'light';
      applyTheme(next);
      localStorage.setItem('flask-roadmap-theme', next);
    });
    function applyTheme(t) {
      html.setAttribute('data-theme', t);
      btn.textContent = t === 'light' ? '🌙' : '☀️';
      setTimeout(drawLines, 300);
    }

    // ── PROGRESS ─────────────────────────────────────────────────────────────────
    function updateProgress() {
      const total = document.querySelectorAll('.node').length;
      const done = document.querySelectorAll('.node.done').length;
      const current = document.querySelectorAll('.node.current').length;
      const left = total - done - current;
      const pct = total > 0 ? Math.round(done / total * 100) : 0;
      document.getElementById('progFill').style.width = pct + '%';
      document.getElementById('progTxt').textContent = done + ' / ' + total + ' nodes';
      document.getElementById('statDone').textContent = done;
      document.getElementById('statCurrent').textContent = current;
      document.getElementById('statLeft').textContent = left;
    }

    // ── DATE ──────────────────────────────────────────────────────────────────────
    const mo = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'];
    const d = new Date();
    document.getElementById('footerDate').textContent =
      d.getDate() + ' ' + mo[d.getMonth()] + ' ' + d.getFullYear();

    // ── SECTION REVEAL ───────────────────────────────────────────────────────────
    const observer = new IntersectionObserver(entries => {
      entries.forEach(e => {
        if (e.isIntersecting) { e.target.classList.add('visible'); observer.unobserve(e.target); }
      });
    }, { threshold: 0.08, rootMargin: '0px 0px -40px 0px' });
    document.querySelectorAll('.phase-section').forEach(s => observer.observe(s));

    // ── ACTIVE NAV ───────────────────────────────────────────────────────────────
    const navLinks = Array.from(document.querySelectorAll('.pnav'));
    function syncNav() {
      const pos = window.scrollY + 120;
      let active = navLinks[0];
      navLinks.forEach(link => {
        const target = document.querySelector(link.getAttribute('href'));
        if (target && target.offsetTop <= pos) active = link;
      });
      navLinks.forEach(l => l.classList.toggle('active', l === active));
    }
    window.addEventListener('scroll', syncNav, { passive: true });

    // ── SVG CONNECTOR LINES ──────────────────────────────────────────────────────
    function drawLines() {
      const svg = document.getElementById('svg-lines');
      svg.innerHTML = '';
      const canvas = document.getElementById('roadmap-canvas');
      const canvasRect = canvas.getBoundingClientRect();
      const scrollTop = window.scrollY;
      const isLight = html.getAttribute('data-theme') === 'light';

      const dark = ['#38bdf8', '#a78bfa', '#f472b6', '#34d399', '#fb923c', '#facc15'];
      const light = ['#0284c7', '#7c3aed', '#db2777', '#059669', '#ea580c', '#b45309'];
      const cols = isLight ? light : dark;
      const phases = document.querySelectorAll('.phase-section');

      // Only draw if there's enough space (skip on very small viewports to avoid clutter)
      if (window.innerWidth < 360) return;

      phases.forEach((phase, pi) => {
        if (pi === phases.length - 1) return;
        const thisNodes = phase.querySelectorAll('.node');
        const nextPhase = phases[pi + 1];
        const nextNodes = nextPhase.querySelectorAll('.node');
        if (!thisNodes.length || !nextNodes.length) return;

        const fromNode = thisNodes[thisNodes.length - 1];
        const toNode = nextNodes[0];
        const fr = fromNode.getBoundingClientRect();
        const tr = toNode.getBoundingClientRect();

        const x1 = fr.left + fr.width / 2 - canvasRect.left;
        const y1 = fr.top + fr.height - canvasRect.top + scrollTop;
        const x2 = tr.left + tr.width / 2 - canvasRect.left;
        const y2 = tr.top - canvasRect.top + scrollTop;
        const mid = (y1 + y2) / 2;

        const path = document.createElementNS('http://www.w3.org/2000/svg', 'path');
        path.setAttribute('d', `M${x1},${y1} C${x1},${mid} ${x2},${mid} ${x2},${y2}`);
        path.setAttribute('fill', 'none');
        path.setAttribute('stroke', cols[pi]);
        path.setAttribute('stroke-width', '1.5');
        path.setAttribute('stroke-dasharray', '4 4');
        path.setAttribute('opacity', '0.32');
        path.style.animation = 'dash 6s ease-in-out infinite alternate';
        svg.appendChild(path);

        [[x1, y1], [x2, y2]].forEach(([cx, cy]) => {
          const dot = document.createElementNS('http://www.w3.org/2000/svg', 'circle');
          dot.setAttribute('cx', cx); dot.setAttribute('cy', cy);
          dot.setAttribute('r', '3'); dot.setAttribute('fill', cols[pi]);
          dot.setAttribute('opacity', '0.38');
          svg.appendChild(dot);
        });
      });

      const h = canvas.scrollHeight;
      svg.setAttribute('viewBox', `0 0 ${canvas.scrollWidth} ${h}`);
      svg.style.height = h + 'px';
    }

    // ── INIT ─────────────────────────────────────────────────────────────────────
    window.addEventListener('load', () => {
      updateProgress();
      setTimeout(drawLines, 500);
      syncNav();
    });

    let resizeTimer;
    window.addEventListener('resize', () => {
      clearTimeout(resizeTimer);
      resizeTimer = setTimeout(drawLines, 150);
    }, { passive: true });

    // Inject dash keyframe
    const s = document.createElement('style');
    s.textContent = '@keyframes dash{from{stroke-dashoffset:12}to{stroke-dashoffset:0}}';
    document.head.appendChild(s);