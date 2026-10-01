/* Công cụ làm bài: highlight 3 màu + tẩy, bút vẽ tay (SVG), tra từ (MyMemory). Dùng cho cả luyện tập & kiểm tra. */
(function () {
  'use strict';
  var Q = window.QUIZ; if (!Q) return;
  var testMode = Q.mode === 'test';
  var $ = function (s, r) { return (r || document).querySelector(s); };
  var $$ = function (s, r) { return Array.prototype.slice.call((r || document).querySelectorAll(s)); };
  var NS = 'http://www.w3.org/2000/svg';
  var mode = 'hl-yellow', ink = '#e11d48', submitted = false, dictOn = false;
  var wrap = $('body > .wrap'); if (!wrap) return;

  /* ---------- thanh công cụ ---------- */
  var bar = document.createElement('div'); bar.className = 'tools'; bar.id = 'tools';
  bar.innerHTML =
    '<span class="tg"><b>Tô màu</b>' +
    '<button type="button" data-m="hl-yellow" class="c y" title="Tô vàng"></button>' +
    '<button type="button" data-m="hl-green" class="c g" title="Tô xanh lá"></button>' +
    '<button type="button" data-m="hl-pink" class="c p" title="Tô hồng"></button>' +
    '<button type="button" data-m="erase" title="Tẩy: bấm vào vùng đã tô để xoá">🧹 Tẩy</button></span>' +
    '<span class="tg"><button type="button" data-m="pen" title="Bút: viết/khoanh/gạch chân trực tiếp lên bài">🖊️ Bút</button>' +
    '<span class="inks" hidden><button type="button" data-ink="#e11d48" class="c r" title="Mực đỏ"></button><button type="button" data-ink="#2563eb" class="c b" title="Mực xanh"></button><button type="button" data-ink="#111827" class="c k" title="Mực đen"></button>' +
    '<button type="button" data-m="penerase" title="Xoá nét: bấm gần nét mực">🧽 Xoá nét</button></span></span>' +
    (testMode ? '' : '<span class="tg"><button type="button" data-m="dict" title="Tra từ: bấm đúp vào từ hoặc bôi đen đoạn văn">📖 Tra từ</button></span>');
  wrap.parentNode.insertBefore(bar, wrap);
  var note = document.createElement('div'); note.className = 'tools-note'; note.hidden = true;
  note.textContent = '📖 Đã mở tra từ: click đúp vào từ hoặc bôi đen đoạn văn để dịch'; wrap.parentNode.insertBefore(note, wrap);

  function setMode(m) {
    mode = (mode === m ? 'none' : m);
    $$('button[data-m]', bar).forEach(function (b) { b.classList.toggle('on', b.getAttribute('data-m') === mode); });
    var pen = mode === 'pen' || mode === 'penerase';
    $('.inks', bar).hidden = !pen;
    layer.style.pointerEvents = pen ? 'auto' : 'none';
    layer.style.cursor = mode === 'pen' ? 'crosshair' : (mode === 'penerase' ? 'cell' : 'default');
    layer.style.touchAction = pen ? 'none' : 'auto';
    dictOn = mode === 'dict';
    document.body.classList.toggle('erasing', mode === 'erase');
  }
  bar.addEventListener('click', function (e) {
    var b = e.target.closest('button'); if (!b) return;
    if (b.hasAttribute('data-ink')) { ink = b.getAttribute('data-ink'); if (mode !== 'pen') setMode('pen'); $$('[data-ink]', bar).forEach(function (x) { x.classList.toggle('on', x === b); }); return; }
    if (b.hasAttribute('data-m')) setMode(b.getAttribute('data-m'));
  });

  /* ---------- highlight (bọc từng text node, không di chuyển phần tử → không phá ô nhập) ---------- */
  var SKIP = /^(INPUT|TEXTAREA|SELECT|SCRIPT|STYLE|BUTTON)$/;
  function okTarget(n) {
    var el = n.nodeType === 3 ? n.parentNode : n;
    return el && wrap.contains(el) && !el.closest('.tools,.bar,.modal,.dict-popup,textarea,input,select,button');
  }
  function highlight(cls) {
    var sel = window.getSelection(); if (!sel.rangeCount || sel.isCollapsed) return false;
    var r = sel.getRangeAt(0); if (!okTarget(r.commonAncestorContainer)) return false;
    var root = r.commonAncestorContainer.nodeType === 3 ? r.commonAncestorContainer.parentNode : r.commonAncestorContainer;
    var tw = document.createTreeWalker(root, NodeFilter.SHOW_TEXT, null), nodes = [], n;
    if (r.commonAncestorContainer.nodeType === 3) nodes.push(r.commonAncestorContainer);
    else while ((n = tw.nextNode())) if (r.intersectsNode(n) && n.nodeValue.trim() && !SKIP.test(n.parentNode.tagName) && !n.parentNode.closest('textarea,.tools')) nodes.push(n);
    nodes.forEach(function (node) {
      var s = node === r.startContainer ? r.startOffset : 0, e = node === r.endContainer ? r.endOffset : node.nodeValue.length;
      if (e <= s) return;
      var mid = node; if (s > 0) mid = node.splitText(s); if (e - s < mid.nodeValue.length) mid.splitText(e - s);
      if (mid.parentNode.classList && /^hl-/.test(mid.parentNode.className)) { mid.parentNode.className = cls; return; }
      var sp = document.createElement('span'); sp.className = cls; mid.parentNode.insertBefore(sp, mid); sp.appendChild(mid);
    });
    sel.removeAllRanges(); return true;
  }
  function unwrap(sp) { var p = sp.parentNode; while (sp.firstChild) p.insertBefore(sp.firstChild, sp); p.removeChild(sp); p.normalize(); }
  wrap.addEventListener('click', function (e) {
    if (mode !== 'erase') return;
    var sp = e.target.closest('span[class^="hl-"]'); if (sp) { e.preventDefault(); unwrap(sp); }
  });
  function onRelease() {
    if (submitted && !testMode && !dictOn) {}
    if (/^hl-/.test(mode)) { setTimeout(function () { highlight(mode); }, 0); }
    else if (dictOn || (testMode && submitted)) setTimeout(lookupSelection, 0);
  }
  document.addEventListener('mouseup', function (e) { if (e.target.closest && e.target.closest('.tools,.dict-popup,.modal,.bar')) return; onRelease(); });
  document.addEventListener('touchend', function (e) { if (e.target.closest && e.target.closest('.tools,.dict-popup,.modal,.bar')) return; setTimeout(onRelease, 250); });

  /* ---------- bút vẽ ---------- */
  var layer = document.createElementNS(NS, 'svg'); layer.setAttribute('class', 'draw-layer'); layer.style.pointerEvents = 'none';
  document.body.appendChild(layer);
  function fit() { layer.style.width = Math.max(document.documentElement.scrollWidth, innerWidth) + 'px'; layer.style.height = Math.max(document.documentElement.scrollHeight, innerHeight) + 'px'; }
  fit(); window.addEventListener('resize', fit);
  if (window.ResizeObserver) new ResizeObserver(fit).observe(document.body); else setInterval(fit, 1500);
  var cur = null, drawing = false;
  function pt(e) { return [Math.round(e.pageX * 10) / 10, Math.round(e.pageY * 10) / 10]; }
  function dist(p, a, b) { var dx = b[0] - a[0], dy = b[1] - a[1], l = dx * dx + dy * dy, t = l ? Math.max(0, Math.min(1, ((p[0] - a[0]) * dx + (p[1] - a[1]) * dy) / l)) : 0; var x = a[0] + t * dx - p[0], y = a[1] + t * dy - p[1]; return Math.sqrt(x * x + y * y); }
  function eraseAt(p) {
    $$('polyline', layer).some(function (pl) {
      var pts = (pl.getAttribute('points') || '').split(' ').map(function (s) { return s.split(',').map(Number); });
      for (var i = 0; i < pts.length - 1; i++) if (dist(p, pts[i], pts[i + 1]) < 10) { pl.remove(); return true; }
      return pts.length === 1 && dist(p, pts[0], pts[0]) < 10 && (pl.remove(), true);
    });
  }
  layer.addEventListener('pointerdown', function (e) {
    if (mode === 'pen') {
      drawing = true; layer.setPointerCapture && layer.setPointerCapture(e.pointerId);
      cur = document.createElementNS(NS, 'polyline'); cur.setAttribute('fill', 'none'); cur.setAttribute('stroke', ink); cur.setAttribute('stroke-width', '2.6');
      cur.setAttribute('stroke-linecap', 'round'); cur.setAttribute('stroke-linejoin', 'round'); cur.setAttribute('points', pt(e).join(','));
      layer.appendChild(cur); e.preventDefault();
    } else if (mode === 'penerase') { drawing = true; eraseAt(pt(e)); e.preventDefault(); }
  });
  layer.addEventListener('pointermove', function (e) {
    if (!drawing) return;
    if (mode === 'pen' && cur) cur.setAttribute('points', cur.getAttribute('points') + ' ' + pt(e).join(','));
    else if (mode === 'penerase') eraseAt(pt(e));
  });
  ['pointerup', 'pointercancel', 'pointerleave'].forEach(function (ev) { layer.addEventListener(ev, function () { drawing = false; cur = null; }); });

  /* ---------- tra từ (MyMemory) ---------- */
  var pop = null;
  function closePop() { if (pop) { pop.remove(); pop = null; } }
  function chunks(t) {
    var sents = t.replace(/\s+/g, ' ').match(/[^.!?]+[.!?]*\s*/g) || [t], out = [], c = '';
    sents.forEach(function (s) {
      while (s.length > 450) { if (c) { out.push(c); c = ''; } out.push(s.slice(0, 450)); s = s.slice(450); }
      if ((c + s).length > 450) { out.push(c); c = s; } else c += s;
    });
    if (c.trim()) out.push(c); return out;
  }
  function translate(text, cb, prog) {
    var parts = text.length > 70 ? chunks(text) : [text], res = [], i = 0;
    (function next() {
      if (i >= parts.length) { cb(null, res.join(' ')); return; }
      if (prog) prog(i + 1, parts.length, res.join(' '));
      fetch('https://api.mymemory.translated.net/get?q=' + encodeURIComponent(parts[i].trim()) + '&langpair=en|vi')
        .then(function (r) { if (!r.ok) throw new Error('HTTP ' + r.status); return r.json(); })
        .then(function (j) { var t = j && j.responseData && j.responseData.translatedText; if (!t) throw new Error('Không có kết quả'); res.push(t); i++; next(); })
        .catch(function (err) { cb(err.message || 'Lỗi mạng'); });
    })();
  }
  function lookupSelection() {
    var sel = window.getSelection(); if (!sel.rangeCount || sel.isCollapsed) return;
    var text = sel.toString().trim(); if (text.length < 2 || !okTarget(sel.getRangeAt(0).commonAncestorContainer)) return;
    var rc = sel.getRangeAt(0).getBoundingClientRect(), long = text.length > 70; closePop();
    pop = document.createElement('div'); pop.className = 'dict-popup' + (long ? ' dict-popup-wide' : '');
    pop.innerHTML = '<button class="x" type="button" aria-label="Đóng">×</button><div class="dict-body"></div>';
    document.body.appendChild(pop);
    var body = $('.dict-body', pop), esc = function (s) { return String(s).replace(/[&<>]/g, function (c) { return { '&': '&amp;', '<': '&lt;', '>': '&gt;' }[c]; }); };
    body.innerHTML = (long ? '<div class="dl">Đoạn gốc:</div><div class="dsrc">' + esc(text) + '</div><div class="dl">Bản dịch:</div>' : '<b>' + esc(text) + '</b><br>') + '<div class="dres">Đang dịch…</div>';
    var w = pop.offsetWidth, x = Math.min(Math.max(8, rc.left), innerWidth - w - 8), y = rc.bottom + 8;
    if (y + pop.offsetHeight > innerHeight - 8) y = Math.max(8, rc.top - pop.offsetHeight - 8);
    pop.style.left = x + 'px'; pop.style.top = y + 'px';
    $('.x', pop).onclick = closePop;
    var res = $('.dres', pop);
    translate(text, function (err, out) { if (!pop) return; res.textContent = err ? '⚠ Không dịch được (' + err + '). Kiểm tra kết nối mạng rồi thử lại.' : out; },
      function (i, n, so) { if (n > 1) res.textContent = (so ? so + ' ' : '') + '… Đang dịch (' + i + '/' + n + ')'; });
  }
  document.addEventListener('dblclick', function (e) { if ((dictOn || (testMode && submitted)) && !e.target.closest('.tools,.dict-popup,.bar,.modal')) setTimeout(lookupSelection, 0); });
  document.addEventListener('mousedown', function (e) { if (pop && !e.target.closest('.dict-popup')) closePop(); });

  /* ---------- sau khi nộp ---------- */
  document.addEventListener('quiz:submitted', function () {
    submitted = true; closePop();
    if (testMode) { // kiểm tra: tắt công cụ, mở tra từ tự động
      mode = 'none'; layer.style.pointerEvents = 'none'; bar.hidden = true; note.hidden = false; dictOn = true;
      document.body.classList.remove('erasing');
    }
  });
  setMode('hl-yellow'); mode = 'hl-yellow'; $$('button[data-m]', bar).forEach(function (b) { b.classList.toggle('on', b.getAttribute('data-m') === mode); });
  $('[data-ink="#e11d48"]', bar).classList.add('on');
  window.__tools = { highlight: highlight, setMode: setMode, translate: translate, chunks: chunks, layer: layer };
})();
