// ---------- Tungsten cubes ----------
// Each cube is shaded as metal on an off-screen canvas (rotated corners, faces sorted back to front,
// a key light, a sky/ground reflection, specular, bevel highlights on the edges, a contact shadow and an
// engraved W), then sampled down to a character grid and drawn as ASCII in the page's own ink.
// Heat (0–1) lights only the edges and a halo. One clock turns every cube on the page; a cube that is
// off screen is not drawn, a hidden tab stops the clock, and reduced motion leaves each cube still.
// build/assemble.py pastes this file into both pages at their CUBE placeholder.
const Cubes = (() => {
  const off = document.createElement('canvas'), octx = off.getContext('2d');
  const tiny = document.createElement('canvas'), tctx = tiny.getContext('2d', { willReadFrequently: true });
  const reduce = matchMedia('(prefers-reduced-motion: reduce)');
  const RAMP = ' .,:;-=+*#%@';
  const MONO = '"JetBrains Mono", ui-monospace, Menlo, monospace';
  const V = [[-1,-1,-1],[1,-1,-1],[1,1,-1],[-1,1,-1],[-1,-1,1],[1,-1,1],[1,1,1],[-1,1,1]];
  const F = [[0,1,2,3],[5,4,7,6],[4,0,3,7],[1,5,6,2],[3,2,6,7],[4,5,1,0]];
  const LT = norm([-0.5, -0.7, 0.65]);
  const HOT = [255, 150, 48];
  const W_GLYPH = [[-0.46, -0.3], [-0.27, 0.3], [-0.02, -0.12], [0.23, 0.3], [0.46, -0.3]];
  const all = [];
  const io = 'IntersectionObserver' in window ? new IntersectionObserver(es => es.forEach(e => {
    const k = all.find(k => k.cv === e.target); if (k) k.seen = e.isIntersecting;
  })) : null;
  let dark = false, INK = '#000', HOTC = '#f60', last = 0, lastDraw = 0, raf = 0;
  const css = n => getComputedStyle(document.documentElement).getPropertyValue(n).trim();
  function norm(v) { const l = Math.hypot(...v) || 1; return v.map(c => c / l); }
  function paint(c2, size, k) {
    const cy = Math.cos(k.ay), sy = Math.sin(k.ay), cx = Math.cos(k.ax), sx = Math.sin(k.ax);
    const rot = ([x, y, z]) => {
      const x1 = x * cy + z * sy, z1 = -x * sy + z * cy;
      return [x1, y * cx - z1 * sx, y * sx + z1 * cx];
    };
    // Edges are drawn wider when the cube is drawn in fewer rows of text, so they survive the downsampling.
    const c = size / 2, s = size * k.scale, persp = 5, k1 = size / 340 * Math.max(1, 34 / k.rows), heat = k.heat;
    const base = dark ? [98, 104, 112] : [78, 84, 92];
    const sky = dark ? [205, 212, 220] : [245, 248, 250];
    const ground = dark ? [24, 27, 31] : [92, 100, 108];
    if (heat > 0.02 && k.halo) {
      const g = c2.createRadialGradient(c, c, s * 0.6, c, c, s * 2.2);
      g.addColorStop(0, `rgba(${HOT},${0.32 * heat})`); g.addColorStop(1, `rgba(${HOT},0)`);
      c2.fillStyle = g; c2.fillRect(0, 0, size, size);
    }
    const sh = c2.createRadialGradient(c, c + s * 1.55, 0, c, c + s * 1.55, s * 1.5);
    sh.addColorStop(0, `rgba(0,0,0,${dark ? 0.5 : 0.3})`); sh.addColorStop(1, 'rgba(0,0,0,0)');
    c2.save(); c2.translate(c, c + s * 1.55); c2.scale(1, 0.32); c2.translate(-c, -(c + s * 1.55));
    c2.fillStyle = sh; c2.fillRect(0, 0, size, size); c2.restore();
    const P = V.map(rot);
    const proj = p => { const q = persp / (persp - p[2]); return [c + p[0] * s * q, c + p[1] * s * q]; };
    const faces = F.map((idx, fi) => {
      const pts = idx.map(i => P[i]);
      const a = pts[0], b = pts[1], d = pts[3];
      const e1 = [b[0]-a[0], b[1]-a[1], b[2]-a[2]], e2 = [d[0]-a[0], d[1]-a[1], d[2]-a[2]];
      const n = norm([e2[1]*e1[2]-e2[2]*e1[1], e2[2]*e1[0]-e2[0]*e1[2], e2[0]*e1[1]-e2[1]*e1[0]]);
      return { fi, pts, n, z: pts.reduce((t, p) => t + p[2], 0) / 4 };
    }).filter(f => f.n[2] > 0).sort((p, q) => p.z - q.z);
    faces.forEach(f => {
      const n = f.n;
      const diff = Math.max(0, n[0] * LT[0] + n[1] * LT[1] + n[2] * LT[2]);
      const ry = 2 * n[2] * n[1];
      const skyMix = Math.max(0, Math.min(1, 0.5 - ry * 0.5));
      const R = [2 * diff * n[0] - LT[0], 2 * diff * n[1] - LT[1], 2 * diff * n[2] - LT[2]];
      const spec = Math.pow(Math.max(0, R[2]), 26) * 0.8;
      const fresnel = Math.pow(1 - n[2], 2) * 0.25;
      const lit = 0.28 + 0.55 * diff + fresnel;
      const col = m => base.map((cc, i) => {
        const env = ground[i] + (sky[i] - ground[i]) * skyMix;
        return Math.min(255, Math.round((cc * 0.55 + env * 0.45) * lit * m + 255 * spec));
      });
      const q = f.pts.map(proj);
      const g = c2.createLinearGradient(q[0][0], q[0][1], q[2][0], q[2][1]);
      g.addColorStop(0, `rgb(${col(1.12)})`); g.addColorStop(0.55, `rgb(${col(0.97)})`); g.addColorStop(1, `rgb(${col(0.86)})`);
      c2.beginPath(); q.forEach((p, i) => i ? c2.lineTo(p[0], p[1]) : c2.moveTo(p[0], p[1])); c2.closePath();
      c2.fillStyle = g; c2.fill();
      if (f.fi === 1) {
        const w = W_GLYPH.map(([u, v]) => proj(rot([u * 0.95, v * 0.95, 1.003])));
        c2.lineCap = 'round'; c2.lineJoin = 'round';
        c2.lineWidth = Math.max(2, size * 0.03);
        c2.strokeStyle = `rgba(${dark ? '230,235,240' : '20,22,25'},${0.55 + 0.25 * diff})`;
        c2.beginPath(); w.forEach((p, i) => i ? c2.lineTo(p[0], p[1]) : c2.moveTo(p[0], p[1])); c2.stroke();
      }
    });
    const edges = new Map();
    faces.forEach(f => f.pts.forEach((p, i) => {
      const a = f.pts[i], b = f.pts[(i + 1) % 4];
      const key = [a, b].map(v => v.map(x => x.toFixed(3)).join(',')).sort().join('|');
      const e = edges.get(key) || { a, b, faces: [] }; e.faces.push(f); edges.set(key, e);
    }));
    c2.lineCap = 'round';
    edges.forEach(e => {
      const n = norm(e.faces.reduce((t, f) => t.map((x, i) => x + f.n[i]), [0, 0, 0]));
      const lk = Math.max(0, n[0] * LT[0] + n[1] * LT[1] + n[2] * LT[2]);
      const pa = proj(e.a), pb = proj(e.b);
      c2.lineWidth = 2.6 * k1;
      c2.strokeStyle = `rgba(${sky},${0.2 + 0.55 * lk})`;
      c2.beginPath(); c2.moveTo(pa[0], pa[1]); c2.lineTo(pb[0], pb[1]); c2.stroke();
      if (heat > 0.02) {
        c2.lineWidth = 3.6 * k1;
        c2.strokeStyle = `rgba(${HOT},${heat * (0.55 + 0.4 * lk)})`;
        c2.beginPath(); c2.moveTo(pa[0], pa[1]); c2.lineTo(pb[0], pb[1]); c2.stroke();
      }
    });
  }
  function draw(k) {
    const { cv, ctx } = k;
    const dpr = Math.min(2, devicePixelRatio || 1);
    const size = cv.clientWidth || 300;
    if (cv.width !== Math.round(size * dpr)) { cv.width = cv.height = Math.round(size * dpr); }
    ctx.setTransform(dpr, 0, 0, dpr, 0, 0);
    ctx.clearRect(0, 0, size, size);
    const rows = k.rows = Math.max(12, Math.min(40, Math.round(size / k.cell)));
    const cellH = size / rows, cellW = cellH * 0.6, cols = Math.floor(size / cellW);
    const S = 256;
    if (off.width !== S) { off.width = off.height = S; }
    octx.setTransform(1, 0, 0, 1, 0, 0); octx.clearRect(0, 0, S, S);
    paint(octx, S, k);
    tiny.width = cols; tiny.height = rows;
    tctx.imageSmoothingEnabled = true; tctx.imageSmoothingQuality = 'high';
    tctx.drawImage(off, 0, 0, cols, rows);
    const px = tctx.getImageData(0, 0, cols, rows).data;
    ctx.font = `700 ${(cellH * 0.95).toFixed(1)}px ${MONO}`;
    ctx.textAlign = 'center'; ctx.textBaseline = 'middle';
    const ox = (size - cols * cellW) / 2;
    // Stretch this frame's brightness range across the whole ramp, so each face gets its own texture.
    // Percentiles over the face pixels only (not the hot edges), so a thin bright edge cannot flatten the faces.
    const lums = [];
    for (let i = 0; i < px.length; i += 4) {
      if (px[i + 3] < 140 || (px[i] - px[i + 2]) > 56) continue;
      lums.push((0.3 * px[i] + 0.59 * px[i + 1] + 0.11 * px[i + 2]) / 255);
    }
    lums.sort((a, b) => a - b);
    const lo = lums.length ? lums[Math.floor(lums.length * 0.06)] : 0;
    const hi = lums.length ? lums[Math.floor(lums.length * 0.9)] : 1;
    const span = Math.max(0.06, hi - lo);
    for (let r = 0; r < rows; r++) {
      for (let q = 0; q < cols; q++) {
        const i = (r * cols + q) * 4, a = px[i + 3] / 255;
        if (a < 0.05) continue;
        const R = px[i], G = px[i + 1], B = px[i + 2];
        const lum = (0.3 * R + 0.59 * G + 0.11 * B) / 255;
        const warm = Math.max(0, (R - B) / 255);
        const x = ox + q * cellW + cellW / 2, y = r * cellH + cellH / 2;
        if (a < 0.55) {
          if ((q + r) % 3 !== 0) continue;
          ctx.globalAlpha = Math.min(1, 0.2 + a);
          if (warm > 0.25) { ctx.fillStyle = HOTC; ctx.fillText('.', x, y); }
          else if (!dark) { ctx.fillStyle = INK; ctx.fillText(',', x, y); }
          continue;
        }
        const t = Math.max(0, Math.min(1, (lum - lo) / span));      // 0 darkest face, 1 brightest
        const ink = Math.min(1, 0.12 + 0.88 * (dark ? t : 1 - t) + warm * 0.2);
        const ch = RAMP[Math.max(1, Math.min(RAMP.length - 1, Math.round(ink * (RAMP.length - 1))))];
        if (warm > 0.22) { ctx.globalAlpha = 1; ctx.fillStyle = HOTC; }
        else { ctx.globalAlpha = 0.38 + 0.62 * ink; ctx.fillStyle = INK; }
        ctx.fillText(ch, x, y);
      }
    }
    ctx.globalAlpha = 1;
  }
  function frame(t) {
    const dt = Math.min(80, t - last); last = t;
    all.forEach(k => { k.ay += dt * 0.00028 * k.speed; k.ax = k.tilt + Math.sin(t * 0.00019 + k.phase) * 0.07; });
    if (t - lastDraw > 66) { lastDraw = t; all.forEach(k => k.seen && draw(k)); }
    raf = requestAnimationFrame(frame);
  }
  function start() {
    cancelAnimationFrame(raf);
    if (reduce.matches || document.hidden) { all.forEach(draw); return; }
    last = performance.now(); raf = requestAnimationFrame(frame);
  }
  document.addEventListener('visibilitychange', start);
  reduce.addEventListener('change', start);
  addEventListener('resize', () => all.forEach(draw));
  if (document.fonts && document.fonts.ready) document.fonts.ready.then(() => all.forEach(draw));
  return {
    // o: heat 0–1, turn (starting angle), tilt (how far the camera looks down), speed, phase (of the nod),
    //    cell (px per text row), scale (cube size in the canvas), halo
    make(cv, o = {}) {
      const k = { cv, ctx: cv.getContext('2d'), heat: o.heat ?? 1, ay: o.turn ?? 0.7, ax: o.tilt ?? -0.56, tilt: o.tilt ?? -0.56, speed: o.speed ?? 1,
                  phase: o.phase ?? 0, cell: o.cell ?? 8, rows: 38, scale: o.scale ?? 0.29, halo: o.halo ?? true, seen: true };
      all.push(k);
      if (io) io.observe(cv);
      return { setHeat(h) { k.heat = Math.max(0, Math.min(1, h)); draw(k); } };
    },
    setTheme(d) { dark = d; INK = css('--ink'); HOTC = css('--hot'); all.forEach(draw); },
    start
  };
})();
