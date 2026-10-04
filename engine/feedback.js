/* Khung 💬 Hỏi · Góp ý (học sinh): tab "Giáo viên" (góp ý / hỏi giáo viên, xem lại cả cuộc trò chuyện) và tab "Trợ lý AI" (hỏi bài).
   Tự gắn vào MỌI trang (bài luyện tập, kiểm tra, IELTS, trang chủ, điểm của tôi). Học sinh luôn có tab Giáo viên; tab Trợ lý AI chỉ hiện khi admin cấp quyền (giáo viên/admin được cấp thì chỉ có AI).
   Trang không thuộc bộ bài nào → góp ý chung (set 'general'). Tin nhắn hiện ngay khi bấm Gửi, gửi ngầm phía sau. */
(function () {
  var A = window.GNAuth; if (!A) return;
  var s = A.get(); if (!s) return;
  function canT() { var x = A.get(); return !!x && x.user.role === 'student'; }   /* nhắn giáo viên: chỉ học sinh */
  function canA() { var x = A.get(); return !!x && (x.user.role === 'admin' || !!x.user.ai); }   /* trợ lý AI: chỉ khi được cấp quyền */
  if (!canT() && !canA()) return;
  var RD = window.GN_RD || {}, set = window.GN_SET || RD.set || 'general';
  var page = RD.page || decodeURIComponent((location.pathname.split('/').pop() || 'trang').replace(/\.html$/, '')) || 'trang';
  var rootPath; try { rootPath = new URL(window.GN_ROOT || '', location.href).pathname; } catch (e) { rootPath = ''; }
  var path = location.pathname.indexOf(rootPath) === 0 ? location.pathname.slice(rootPath.length) : '';
  var ROOT = window.GN_ROOT || '';
  var E = A.esc, open = false, timer = null, tab = 't', submitted = false, pend = [], srv = [], seq = 0;

  var css = document.createElement('style');
  css.textContent = '.gnfb-btn{position:fixed;right:0;top:38%;z-index:100000;font:600 13px/1 system-ui,sans-serif;background:#1d4ed8;color:#fff;border:0;border-radius:10px 0 0 10px;padding:12px 8px;cursor:pointer;box-shadow:-2px 2px 8px rgba(0,0,0,.25);writing-mode:vertical-rl}' +
    '.gnfb-btn .dot{display:none;position:absolute;top:-6px;left:-6px;writing-mode:horizontal-tb;min-width:18px;height:18px;border-radius:9px;background:#e11d48;color:#fff;font-size:11px;line-height:18px;text-align:center;padding:0 4px}' +
    '.gnfb-btn.has .dot{display:block}' +
    '.gnfb-box{position:fixed;right:40px;top:8vh;z-index:100001;width:min(360px,calc(100vw - 56px));height:min(560px,80vh);display:none;flex-direction:column;background:#fff;color:#111;border:1px solid #cbd5e1;border-radius:12px;box-shadow:0 8px 28px rgba(0,0,0,.28);font:14px/1.45 system-ui,sans-serif}' +
    '.gnfb-box.on{display:flex}.gnfb-h{padding:8px 12px;border-bottom:1px solid #e2e8f0;font-weight:600;display:flex;justify-content:space-between;gap:8px;align-items:center}' +
    '.gnfb-x{background:none;border:0;font-size:18px;cursor:pointer;color:#64748b}' +
    '.gnfb-tabs{display:flex;border-bottom:1px solid #e2e8f0}.gnfb-tabs button{flex:1;background:none;border:0;border-bottom:3px solid transparent;padding:8px 4px;font:600 13px system-ui;color:#64748b;cursor:pointer}.gnfb-tabs button.on{color:#1d4ed8;border-bottom-color:#1d4ed8}' +
    '.gnfb-sub{padding:6px 12px;font-size:12px;color:#64748b;border-bottom:1px solid #f1f5f9}.gnfb-sub a{color:#1d4ed8}' +
    '.gnfb-l{flex:1;overflow:auto;padding:10px;display:flex;flex-direction:column;gap:8px;min-height:90px}' +
    '.gnfb-m{max-width:88%;padding:7px 10px;border-radius:12px;white-space:pre-wrap;word-break:break-word}' +
    '.gnfb-m.me{align-self:flex-end;background:#dbeafe}.gnfb-m.tc{align-self:flex-start;background:#f1f5f9}.gnfb-m.ai{align-self:flex-start;background:#ecfdf5;border:1px solid #bbf7d0}' +
    '.gnfb-m.bad{background:#fee2e2}.gnfb-m small{display:block;color:#64748b;font-size:11px;margin-top:2px}.gnfb-m small a{color:#be123c;cursor:pointer;text-decoration:underline}.gnfb-e{color:#64748b;text-align:center;font-size:13px;padding:8px}' +
    '.gnfb-f{border-top:1px solid #e2e8f0;padding:8px;display:flex;flex-direction:column;gap:6px}' +
    '.gnfb-f textarea{width:100%;box-sizing:border-box;height:58px;resize:none;border:1px solid #cbd5e1;border-radius:8px;padding:6px;font:inherit;background:#fff;color:#111}' +
    '.gnfb-row{display:flex;gap:6px;justify-content:space-between;align-items:center}.gnfb-row small{color:#64748b}' +
    '.gnfb-f button,.gnfb-sel{background:#1d4ed8;color:#fff;border:0;border-radius:8px;padding:6px 14px;cursor:pointer;font:inherit}.gnfb-sel{background:#e2e8f0;color:#334155;padding:3px 8px;font-size:12px}.gnfb-f button:disabled{opacity:.5}' +
    '.gnfb-err{color:#be123c;font-size:12px}@media print{.gnfb-btn,.gnfb-box{display:none!important}}' +
    '.gnfb-box{min-width:300px;min-height:260px;max-width:calc(100vw - 8px);max-height:calc(100vh - 8px)}.gnfb-h{cursor:move;user-select:none;-webkit-user-select:none;touch-action:none}.gnfb-h button{cursor:pointer}' +
    '.gnfb-hb{display:flex;gap:4px;align-items:center}.gnfb-mx{background:none;border:0;font-size:16px;cursor:pointer;color:#64748b;padding:0 4px}.gnfb-mx:hover,.gnfb-x:hover{color:#1d4ed8}' +
    '.gnfb-g{position:absolute;width:18px;height:18px;z-index:3;touch-action:none}.gnfb-g::after{content:"";position:absolute;width:9px;height:9px;border:0 solid #94a3b8}' +
    '.gnfb-g[data-d="br"]{right:0;bottom:0;cursor:nwse-resize}.gnfb-g[data-d="br"]::after{right:3px;bottom:3px;border-right-width:3px;border-bottom-width:3px}' +
    '.gnfb-g[data-d="bl"]{left:0;bottom:0;cursor:nesw-resize}.gnfb-g[data-d="bl"]::after{left:3px;bottom:3px;border-left-width:3px;border-bottom-width:3px}' +
    '.gnfb-g[data-d="tl"]{left:0;top:0;cursor:nwse-resize}.gnfb-g[data-d="tl"]::after{left:3px;top:3px;border-left-width:3px;border-top-width:3px}' +
    '.gnfb-g[data-d="tr"]{right:0;top:0;cursor:nesw-resize}.gnfb-g[data-d="tr"]::after{right:3px;top:3px;border-right-width:3px;border-top-width:3px}' +
    '.gnfb-box .katex{font-size:1.02em}.gnfb-m .katex-display{overflow-x:auto;margin:.4em 0}.gnfb-box.big .gnfb-m{font-size:15px}';
  document.head.appendChild(css);

  var btn = document.createElement('button'); btn.type = 'button'; btn.className = 'gnfb-btn'; btn.innerHTML = '💬 Hỏi · Góp ý<span class="dot"></span>';
  var box = document.createElement('div'); box.className = 'gnfb-box';
  box.innerHTML = '<div class="gnfb-h"><span>Hỏi · Góp ý</span><span class="gnfb-hb"><button type="button" class="gnfb-mx" aria-label="Phóng to / thu nhỏ" title="Phóng to / thu nhỏ khung (hoặc kéo góc khung)">⛶</button><button type="button" class="gnfb-x" aria-label="Đóng">×</button></span></div>' +
    '<i class="gnfb-g" data-d="tl"></i><i class="gnfb-g" data-d="tr"></i><i class="gnfb-g" data-d="bl"></i><i class="gnfb-g" data-d="br"></i>' +
    '<div class="gnfb-tabs"><button type="button" data-t="t" class="on">👩‍🏫 Giáo viên</button><button type="button" data-t="a">🤖 Trợ lý AI</button></div>' +
    '<div class="gnfb-sub"></div><div class="gnfb-l"></div><div class="gnfb-f"><div class="gnfb-err"></div><textarea maxlength="1000"></textarea><div class="gnfb-row"><button type="button" class="gnfb-sel" hidden>Hỏi về đoạn đang bôi đen</button><small></small><button type="button" class="gnfb-go">Gửi</button></div></div>';
  document.body.appendChild(box); document.body.appendChild(btn);
  var $ = function (q) { return box.querySelector(q); };
  var list = $('.gnfb-l'), ta = $('textarea'), send = $('.gnfb-go'), err = $('.gnfb-err'), sub = $('.gnfb-sub'), dot = btn.querySelector('.dot'), selBtn = $('.gnfb-sel'), hint = $('.gnfb-row small');

  /* ---------- tab Giáo viên ---------- */
  function when(t) { return t || ''; }
  function nowStr() { var d = new Date(Date.now() + 7 * 3600e3 - new Date().getTimezoneOffset() * 0 ); return d.toISOString().slice(8, 10) + '/' + d.toISOString().slice(5, 7) + '/' + d.toISOString().slice(0, 4) + ' ' + d.toISOString().slice(11, 19); }
  function renderT() {
    var all = srv.concat(pend);
    if (!all.length) { list.innerHTML = '<div class="gnfb-e">Chưa có tin nhắn. Hãy gửi góp ý hoặc câu hỏi đầu tiên cho giáo viên.</div>'; return; }
    list.innerHTML = all.map(function (m, i) {
      var me = m.role === 'student', cls = me ? 'me' : 'tc', st = '';
      if (m._p === 'sending') st = ' · ⏳ đang gửi…'; else if (m._p === 'fail') { cls += ' bad'; st = ' · <a data-retry="' + m._id + '">Chưa gửi được – thử lại</a>'; }
      return '<div class="gnfb-m ' + cls + '">' + E(m.text) + '<small>' + (me ? 'Bạn' : E(m.name || 'Giáo viên')) + (m.time ? ' · ' + E(m.time) : '') + st + '</small></div>';
    }).join('');
    list.scrollTop = list.scrollHeight;
  }
  function ctx() { return { set_id: set, page_id: page }; }
  function loadT() { return A.api('fb_list', ctx()).then(function (j) { srv = j.msgs || []; pend = pend.filter(function (p) { return p._p !== 'sending' || !srv.some(function (m) { return m.text === p.text && m.role === 'student'; }); }); if (tab === 't') renderT(); setDot(0); }).catch(function () {}); }
  function setDot(n) { dot.textContent = n > 9 ? '9+' : n; btn.classList.toggle('has', n > 0); }
  function postT(p) {
    p._p = 'sending'; renderT();
    A.api('fb_send', { set_id: set, page_id: page, title: document.title, path: path, text: p.text, light: true }).then(function (j) {
      pend = pend.filter(function (x) { return x !== p; }); if (j.msg) srv.push(j.msg); renderT();
    }).catch(function (e) { p._p = 'fail'; p._why = e.message; renderT(); err.textContent = e.message || 'Không gửi được, hãy thử lại.'; });
  }
  function sendT() {
    var t = ta.value.trim(); if (!t) return; err.textContent = ''; ta.value = '';
    var p = { _id: ++seq, role: 'student', text: t, time: nowStr() }; pend.push(p); postT(p);
  }
  list.addEventListener('click', function (e) {
    var a = e.target.closest('a[data-retry]'); if (!a) return; var id = +a.dataset.retry, p = pend.filter(function (x) { return x._id === id; })[0]; if (p) { err.textContent = ''; postT(p); }
  });

  /* ---------- tab Trợ lý AI ---------- */
  var AK = 'gn_ai_' + set + '|' + page, hist = [], ai = { loaded: false, enabled: true, left: null, busy: false };
  try { hist = JSON.parse(sessionStorage.getItem(AK) || '[]'); } catch (e) { hist = []; }
  function saveH() { try { sessionStorage.setItem(AK, JSON.stringify(hist.slice(-20))); } catch (e) {} }
  function fmt(t) {   /* chat: bỏ dòng ---, gộp dòng trống, in đậm **, gạch đầu dòng → • */
    t = String(t || '').replace(/\r/g, '').replace(/^\s*[-*_]{3,}\s*$/gm, '').replace(/[ \t]+\n/g, '\n').replace(/\n{3,}/g, '\n\n').trim();
    t = t.replace(/\\\(([^\n]+?)\\\)/g, '$$$1$$').replace(/\\\[([\s\S]+?)\\\]/g, '$$$$$1$$$$');
    var maths = [];
    if (window.katex) t = t.replace(/\$\$([\s\S]+?)\$\$|\$([^$\n]+?)\$/g, function (m, a, b) { maths.push({ tex: a || b, disp: !!a }); return '\u0001' + (maths.length - 1) + '\u0002'; });
    var html = E(t).replace(/\$\\(?:right)?arrow\$/g, '→').replace(/\$\\leftarrow\$/g, '←').replace(/^#{1,4} ?/gm, '').replace(/\*\*([^*\n]+)\*\*/g, '<b>$1</b>').replace(/`([^`\n]+)`/g, '<code>$1</code>').replace(/^[ \t]*[-*] /gm, '• ').replace(/\n\n/g, '<div style="height:6px"></div>');
    return html.replace(/\u0001(\d+)\u0002/g, function (m, i) { var x = maths[+i]; try { return window.katex.renderToString(x.tex, { throwOnError: false, displayMode: x.disp }); } catch (e) { return E(x.tex); } });
  }
  /* Trang làm bài (có nút Nộp bài): AI chỉ mở SAU KHI nộp bài. Trang khác (trang chủ, điểm của tôi…): dùng được bình thường. */
  function isQuiz() { return !!(document.getElementById('submit') || document.getElementById('submitBtn') || RD.kind || document.body.classList.contains('testmode')); }
  function isLive() { if (window.GN_LY) return window.GN_LY.mode === 'test' && !submitted; return !submitted && isQuiz(); }   /* Vật lí: luyện tập dùng AI tự do; kiểm tra chỉ sau khi nộp */
  /* Đọc nội dung trang đang hiển thị (bài đọc + câu hỏi + đáp án/giải thích nếu đã hiện) để AI trả lời "câu 32" mà không cần bôi đen */
  function pageText(q) {
    if (window.GN_LY_API) { try { return window.GN_LY_API.pageText(); } catch (e) {} }
    var od = box.style.display, bd = btn.style.display, t = '';
    box.style.display = 'none'; btn.style.display = 'none';
    try { t = String(document.body.innerText || ''); } catch (e) {}
    box.style.display = od; btn.style.display = bd;
    t = t.replace(/[ \t ]+/g, ' ').replace(/\n\s*\n+/g, '\n').trim();
    var MAX = 20000; if (t.length <= MAX) return t;
    var head = t.slice(0, 13000), m = /(?:câu|cau|question|q)\s*(?:số\s*)?(\d{1,3})/i.exec(q || ''), tail = '';
    if (m) { var re = new RegExp('(?:^|\\n)\\s*' + m[1] + '\\s*[.)]?\\s', 'g'), x, pos = -1; while ((x = re.exec(t))) { if (x.index > 13000) { pos = x.index; break; } } if (pos > 0) tail = '\n…\n' + t.slice(Math.max(13000, pos - 1500), pos + 5500); }
    return head + (tail || '\n…\n' + t.slice(-(MAX - 13000)));
  }
  document.addEventListener('quiz:submitted', function () { submitted = true; if (tab === 'a') renderA(); });
  var rm = document.getElementById('resultModal');
  if (rm && window.MutationObserver) new MutationObserver(function () { if (!rm.classList.contains('hidden') && rm.style.display !== 'none' && (RD.kind === 'full' || RD.kind)) { submitted = true; if (tab === 'a') renderA(); } }).observe(rm, { attributes: true, attributeFilter: ['class', 'style'] });
  function renderA() {
    var live = isLive();
    sub.innerHTML = live ? '🔒 Trợ lý AI chỉ mở sau khi bạn nộp bài. Hãy tự làm bài trước nhé!' : (window.GN_LY && ai.enabled ? 'AI có thể sai – hãy kiểm tra lại. Điểm tự luận do giáo viên duyệt.' + (ai.left != null ? ' · Còn <b>' + ai.left + '</b> lượt hôm nay' : '') : null) ||  (ai.enabled ? 'AI có thể sai – hãy kiểm tra lại. Giáo viên có thể xem lại câu hỏi.' + (ai.left != null ? ' · Còn <b>' + ai.left + '</b> lượt hôm nay' : '') : 'Trợ lý AI chưa được bật.');
    var h = hist.map(function (m) { return '<div class="gnfb-m ' + (m.role === 'user' ? 'me' : (m.bad ? 'bad' : 'ai')) + '">' + fmt(m.text) + (m.role === 'ai' && !m.bad ? '<small>🤖 Trợ lý AI</small>' : '') + '</div>'; }).join('');
    if (ai.busy) h += '<div class="gnfb-m ai">⏳ Trợ lý đang trả lời…</div>';
    list.innerHTML = h || (window.GN_LY ? '<div class="gnfb-e">Mình đọc được đề và cả bài làm của bạn trên trang này.<br>Hãy hỏi, ví dụ: “Giải bài tự luận câu 2 từng bước”, “Xem bài làm của mình ở câu 5 sai chỗ nào?”, “Chấm giúp mình bài tự luận (cho điểm gợi ý)”.<br><small>Mẹo: kéo góc khung để phóng to, hoặc bấm ⛶.</small></div>' : '<div class="gnfb-e">Mình đọc được nội dung trang bài này.<br>Cứ hỏi, ví dụ: “Giải thích chi tiết câu 32 giúp mình”, “Vì sao câu 5 chọn B?”, “Giải thích thì hiện tại hoàn thành”.</div>');
    list.scrollTop = list.scrollHeight;
    var off = live || !ai.enabled; ta.disabled = off; send.disabled = off || ai.busy;
    ta.placeholder = off ? (live ? 'AI mở sau khi bạn nộp bài.' : 'Trợ lý AI chưa bật.') : 'Nhập câu hỏi (Ctrl+Enter để gửi)…';
  }
  function loadA() {
    renderA();   /* hiện ngay cuộc trò chuyện đã có, cập nhật số lượt khi máy chủ trả lời */
    if (ai.loaded) return;
    A.api('ai_status').then(function (j) { ai.loaded = true; ai.enabled = !!j.enabled && j.allowed !== false; ai.left = j.left; renderA(); }).catch(function () { renderA(); });
  }
  function selText() { try { return String(window.getSelection() || '').replace(/\s+/g, ' ').trim().slice(0, 500); } catch (e) { return ''; } }
  var lastSel = '';
  document.addEventListener('selectionchange', function () { var t = selText(); if (t && !box.contains(document.activeElement)) lastSel = t; });
  function sendA() {
    var t = ta.value.trim(); if (!t || ai.busy || isLive()) return; err.textContent = ''; ta.value = '';
    var ctxT = selBtn._ctx || ''; selBtn._ctx = ''; selBtn.hidden = !lastSel;
    var past = hist.filter(function (m) { return !m.bad; }).slice(-8).map(function (m) { return { role: m.role, text: m.text }; });
    hist.push({ role: 'user', text: t }); ai.busy = true; renderA();
    A.api('ai_chat', { text: t, history: past, context: ctxT, page_text: pageText(t), set_id: set, page_id: page, live: isLive() }).then(function (j) {
      hist.push({ role: 'ai', text: j.text }); ai.left = j.left;
    }).catch(function (e) { hist.push({ role: 'ai', text: e.message || 'Không hỏi được, hãy thử lại.', bad: true }); })
      .then(function () { ai.busy = false; saveH(); renderA(); });
  }
  selBtn.onclick = function () {
    var t = lastSel || selText(); if (!t) return; selBtn._ctx = t; ta.value = ta.value || 'Giải thích giúp mình đoạn này.'; ta.focus();
  };

  /* ---------- chung ---------- */
  function perm() {   /* ẩn/hiện tab theo quyền hiện tại */
    var t = canT(), a = canA(), bt = box.querySelector('[data-t="t"]'), ba = box.querySelector('[data-t="a"]');
    bt.hidden = !t; ba.hidden = !a; box.querySelector('.gnfb-tabs').style.display = (t && a) ? '' : 'none';
    box.querySelector('.gnfb-h span').textContent = t ? (a ? 'Hỏi · Góp ý' : 'Góp ý cho giáo viên') : 'Trợ lý AI';
    btn.firstChild.nodeValue = t ? (a ? '💬 Hỏi · Góp ý' : '💬 Góp ý') : '🤖 Trợ lý AI';
  }
  function setTab(t) {
    perm(); if (t === 't' && !canT()) t = 'a'; if (t === 'a' && !canA()) t = 't';
    tab = t; [].forEach.call(box.querySelectorAll('.gnfb-tabs button'), function (b) { b.classList.toggle('on', b.dataset.t === t); });
    err.textContent = ''; selBtn.hidden = t !== 'a' || !lastSel; hint.textContent = '';
    if (t === 't') {
      sub.innerHTML = 'Chỉ giáo viên của bạn thấy tin nhắn này. <a href="' + ROOT + 'me.html#gopy">Xem mọi góp ý</a>';
      ta.disabled = false; send.disabled = false; ta.placeholder = set === 'general' ? 'Viết góp ý hoặc câu hỏi cho giáo viên…' : 'Viết góp ý, báo lỗi đáp án hoặc đặt câu hỏi cho giáo viên…'; renderT(); loadT();
    } else { loadA(); }
  }
  function setOpen(v) {
    open = v; box.classList.toggle('on', v); clearInterval(timer);
    if (v) { setTab(tab); timer = setInterval(function () { if (tab === 't' && !document.hidden) loadT(); }, 20000); setTimeout(function () { if (!ta.disabled) ta.focus(); }, 50); }
  }
  /* ---------- kéo to / thu nhỏ / di chuyển khung (nhớ kích thước) ---------- */
  var SZK = 'gn_fb_geo', MINW = 300, MINH = 260;
  function vw() { return window.innerWidth || document.documentElement.clientWidth; }
  function vh() { return window.innerHeight || document.documentElement.clientHeight; }
  function geo() { var r = box.getBoundingClientRect(); return { l: r.left, t: r.top, w: r.width, h: r.height }; }
  function setGeo(g) {
    var w = Math.max(Math.min(MINW, vw() - 8), Math.min(g.w, vw() - 8)), h = Math.max(Math.min(MINH, vh() - 8), Math.min(g.h, vh() - 8));
    var l = Math.min(Math.max(4, g.l), vw() - w - 4), t = Math.min(Math.max(4, g.t), vh() - h - 4);
    box.style.right = 'auto'; box.style.left = l + 'px'; box.style.top = t + 'px'; box.style.width = w + 'px'; box.style.height = h + 'px';
    box.classList.toggle('big', w > 520);
  }
  function saveGeo() { try { localStorage.setItem(SZK, JSON.stringify(geo())); } catch (e) {} }
  function restoreGeo() {
    var g = null; try { g = JSON.parse(localStorage.getItem(SZK) || 'null'); } catch (e) {}
    if (g && g.w > 0 && g.h > 0) { setGeo(g); } else if (vw() < 480) { setGeo({ l: 4, t: Math.round(vh() * .08), w: vw() - 8, h: Math.round(vh() * .8) }); }
  }
  function drag(ev, dir) {   /* dir: 'move' hoặc tl|tr|bl|br */
    if (ev.button !== undefined && ev.button !== 0) return;
    ev.preventDefault(); var g0 = geo(), sx = ev.clientX, sy = ev.clientY, el = ev.currentTarget; try { el.setPointerCapture(ev.pointerId); } catch (e) {}
    function mv(e) {
      var dx = e.clientX - sx, dy = e.clientY - sy, g = { l: g0.l, t: g0.t, w: g0.w, h: g0.h };
      if (dir === 'move') { g.l += dx; g.t += dy; }
      else {
        if (dir.charAt(1) === 'r') g.w = g0.w + dx; else { g.w = g0.w - dx; g.l = g0.l + dx; }
        if (dir.charAt(0) === 'b') g.h = g0.h + dy; else { g.h = g0.h - dy; g.t = g0.t + dy; }
        if (g.w < MINW) { if (dir.charAt(1) === 'l') g.l -= MINW - g.w; g.w = MINW; }
        if (g.h < MINH) { if (dir.charAt(0) === 't') g.t -= MINH - g.h; g.h = MINH; }
      }
      setGeo(g);
    }
    function up() { el.removeEventListener('pointermove', mv); el.removeEventListener('pointerup', up); el.removeEventListener('pointercancel', up); saveGeo(); }
    el.addEventListener('pointermove', mv); el.addEventListener('pointerup', up); el.addEventListener('pointercancel', up);
  }
  [].forEach.call(box.querySelectorAll('.gnfb-g'), function (g) { g.addEventListener('pointerdown', function (e) { drag(e, g.getAttribute('data-d')); }); });
  box.querySelector('.gnfb-h').addEventListener('pointerdown', function (e) { if (e.target.closest('button')) return; drag(e, 'move'); });
  var prevGeo = null;
  box.querySelector('.gnfb-mx').onclick = function () {
    var g = geo(), full = { l: 8, t: 8, w: Math.min(vw() - 16, 980), h: vh() - 16 };
    if (g.w >= full.w - 6 && g.h >= full.h - 6 && prevGeo) { setGeo(prevGeo); prevGeo = null; }
    else { prevGeo = g; setGeo({ l: vw() - full.w - 8, t: 8, w: full.w, h: full.h }); }
    saveGeo();
  };
  window.addEventListener('resize', function () { if (box.style.left && box.classList.contains('on')) setGeo(geo()); });
  restoreGeo();
  window.GNFB = {   /* cho trang bài mở khung chat với câu hỏi soạn sẵn */
    open: function (t, text, auto) {
      perm(); if (t === 'a' && !canA()) return; setOpen(true); setTab(t || tab);
      if (text) { ta.value = text; if (auto) setTimeout(function () { if (!send.disabled && !ta.disabled) send.click(); }, 80); else ta.focus(); }
    }
  };
  perm(); window.addEventListener('gn-user', function () { perm(); if (open) setTab(tab); });
  btn.onclick = function () { perm(); lastSel = lastSel || selText(); setOpen(!open); };
  box.querySelector('.gnfb-x').onclick = function () { setOpen(false); };
  box.querySelector('.gnfb-tabs').onclick = function (e) { var b = e.target.closest('button[data-t]'); if (b) { setTab(b.dataset.t); } };
  send.onclick = function () { if (tab === 't') sendT(); else sendA(); };
  ta.addEventListener('keydown', function (e) { if (e.key === 'Enter' && (e.ctrlKey || e.metaKey)) { e.preventDefault(); send.click(); } });
  ta.addEventListener('paste', function (e) { e.stopPropagation(); });
  box.addEventListener('copy', function (e) { e.stopPropagation(); });
  ['mousedown', 'mouseup', 'pointerdown', 'touchstart', 'touchend', 'dblclick', 'contextmenu', 'cut', 'dragstart', 'drop'].forEach(function (ev) { box.addEventListener(ev, function (e) { e.stopPropagation(); }); });   /* các bộ chặn / công cụ của trang không được can thiệp vào khung chat */
  // chấm đỏ: tổng số tin trả lời chưa đọc của học sinh (mọi bài)
  if (canT()) A.api('fb_mine').then(function (j) {
    var n = (j.threads || []).reduce(function (a, x) { return a + (+x.unread || 0); }, 0);
    if (n && !open) setDot(n);
  }).catch(function () {});
})();
