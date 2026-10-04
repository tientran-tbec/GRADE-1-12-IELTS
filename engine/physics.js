/* Engine môn Vật lí (bản mở rộng của engine.js): trắc nghiệm, đúng/sai 4 ý (điểm theo số ý đúng), trả lời ngắn (đáp số, sai số cho phép),
   tự luận (AI gợi ý điểm + giáo viên duyệt), công thức KaTeX, tương tác với khung 🤖 Trợ lý AI (feedback.js). */
(function () {
  'use strict';
  var Q = window.QUIZ;
  var $ = function (s, r) { return (r || document).querySelector(s); };
  var $$ = function (s, r) { return Array.prototype.slice.call((r || document).querySelectorAll(s)); };
  function renderMath(el) {
    try { if (window.renderMathInElement) window.renderMathInElement(el || document.body, { delimiters: [{ left: '$$', right: '$$', display: true }, { left: '$', right: '$', display: false }], throwOnError: false, ignoredTags: ['script', 'noscript', 'style', 'textarea', 'option'] }); } catch (e) {}
  }
  window.GN_RENDER_MATH = renderMath;
  if (!Q) {   /* trang lý thuyết: chỉ vẽ công thức */
    var go0 = function () { renderMath(document.body); };
    if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', go0); else go0();
    return;
  }
  var state = { started: false, submitted: false, t0: 0, tab: 0, blur: 0, fs: 0, events: [], student: { name: '', cls: '' }, remain: 0, warned: false, timerId: null, essays: {}, mine: {} };
  var testMode = Q.mode === 'test';
  var TF = [0, 0.1, 0.25, 0.5, 1];

  /* ---------- tiện ích ---------- */
  function lsGet(k) { try { return localStorage.getItem(k); } catch (e) { return null; } }
  function lsSet(k, v) { try { localStorage.setItem(k, v); } catch (e) {} }
  function esc(s) { return String(s).replace(/[&<>"]/g, function (c) { return { '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' }[c]; }); }
  function pad(n) { return (n < 10 ? '0' : '') + n; }
  function fmtT(sec) { sec = Math.max(0, sec | 0); return pad((sec / 60) | 0) + ':' + pad(sec % 60); }
  function now() { return Date.now(); }
  function vn(x) { return (Math.round(x * 100) / 100).toString().replace('.', ','); }
  function toast(m) { var t = $('#toast'); if (!t) return; t.textContent = '⚠ ' + m; t.hidden = false; clearTimeout(t._t); t._t = setTimeout(function () { t.hidden = true; }, 4000); }

  /* ---------- đọc / chấm ---------- */
  function qEl(id) { return $('.q[data-id="' + id.replace(/"/g, '\\"') + '"]'); }
  function tf4Vals(el) {
    var o = [];
    for (var i = 0; i < 4; i++) { var c = $('input[name="' + el.getAttribute('data-id').replace(/"/g, '\\"') + '_' + i + '"]:checked', el); o.push(c ? c.value : '-'); }
    return o.join('');
  }
  function getVal(id) {
    var t = Q.items[id].t, el = qEl(id);
    if (t === 'mcq') { var c = $('input[type=radio]:checked', el); return c ? c.value : ''; }
    if (t === 'tf4') { var s = tf4Vals(el); return s === '----' ? '' : s; }
    if (t === 'short') return $('input.numin', el).value.trim();
    if (t === 'essay') return $('textarea', el).value.trim();
    return '';
  }
  function answered(id) {
    var v = getVal(id);
    if (Q.items[id].t === 'tf4') return v.indexOf('-') < 0 && v !== '';
    return v !== '';
  }
  function toNum(s) {
    s = String(s == null ? '' : s).toLowerCase().replace(/[−–—]/g, '-').replace(/\s+/g, '');
    s = s.replace(/×10\^?\{?(-?\d+)\}?/g, 'e$1').replace(/\*10\^\{?(-?\d+)\}?/g, 'e$1');
    var m = /^[-+]?(?:\d+[.,]?\d*|[.,]\d+)(?:e[-+]?\d+)?/.exec(s);
    if (!m) return NaN;
    return parseFloat(m[0].replace(',', '.'));
  }
  function numOk(v, it) {
    var x = toNum(v); if (isNaN(x)) return false;
    var cands = [it.ans].concat(it.alts || []);
    for (var i = 0; i < cands.length; i++) {
      var a = toNum(cands[i]); if (isNaN(a)) continue;
      if (it.tol === 'exact') { if (Math.abs(x - a) < 1e-9) return true; }
      else {
        var tol = typeof it.tol === 'number' ? it.tol : parseFloat(it.tol); if (!(tol > 0)) tol = 0.01;
        if (Math.abs(x - a) <= Math.max(tol * Math.abs(a), 1e-9)) return true;
      }
    }
    return false;
  }
  function tf4Right(v, a) { var n = 0; for (var i = 0; i < 4; i++) if (v.charAt(i) === a.charAt(i)) n++; return n; }
  function isCorrect(id) {
    var it = Q.items[id], v = getVal(id);
    if (it.t === 'essay') return null;
    if (it.t === 'mcq') return v === it.ans;
    if (it.t === 'tf4') return v.length === 4 && v === it.ans;
    return numOk(v, it);
  }
  function maxPts(id) { var t = Q.items[id].t; return t === 'tf4' ? 1 : (t === 'essay' ? 0 : 0.25); }
  function earned(id) {
    var it = Q.items[id], v = getVal(id);
    if (it.t === 'tf4') return v.length === 4 ? TF[tf4Right(v.replace(/-/g, 'x'), it.ans)] : 0;
    if (it.t === 'essay') return 0;
    return isCorrect(id) ? 0.25 : 0;
  }
  function ansText(id) {
    var it = Q.items[id];
    if (it.t === 'mcq') {
      var inp = $('input[value="' + it.ans + '"]', qEl(id)), lab = inp ? inp.parentNode.textContent.replace(/^\s*[A-D]\.\s*/, '').trim() : '';
      return it.ans + (lab ? '. ' + lab : '');
    }
    if (it.t === 'tf4') return it.ans.split('').map(function (c, i) { return 'abcd'.charAt(i) + ') ' + (c === 'T' ? 'Đúng' : 'Sai'); }).join(' · ');
    if (it.t === 'short') return it.ans + (it.unit ? ' ' + it.unit : '');
    return '';
  }
  function rubricHtml(it) {
    if (!it.rubric || !it.rubric.length) return '';
    return '<div class="rub"><b>Biểu điểm (' + vn(it.max) + ' điểm)</b><ul>' + it.rubric.map(function (r) { return '<li>' + esc(r.t) + ' <i>(' + vn(r.p) + ')</i></li>'; }).join('') + '</ul></div>';
  }
  function mark(id) {
    var it = Q.items[id], el = qEl(id), box = $('.exp', el), ok = isCorrect(id), sol = it.sol ? '<div class="sol">' + it.sol + '</div>' : '';
    if (it.t === 'essay') return;
    if (it.t === 'mcq') {
      $$('label.opt', el).forEach(function (l) { var v = $('input', l).value; l.classList.remove('right', 'wrong'); if (v === it.ans) l.classList.add('right'); else if ($('input', l).checked) l.classList.add('wrong'); });
    } else if (it.t === 'tf4') {
      var v4 = getVal(id) || '----';
      $$('.tfr', el).forEach(function (r, i) {
        r.classList.remove('right', 'wrong');
        var mine = v4.charAt(i); r.classList.add(mine === it.ans.charAt(i) ? 'right' : 'wrong');
        $$('label.opt', r).forEach(function (l) { l.classList.remove('right', 'wrong'); if ($('input', l).value === it.ans.charAt(i)) l.classList.add('right'); else if ($('input', l).checked) l.classList.add('wrong'); });
      });
    } else if (it.t === 'short') {
      var inp = $('input.numin', el); inp.classList.remove('right', 'wrong'); inp.classList.add(ok ? 'right' : 'wrong');
    }
    var head;
    if (it.t === 'tf4') {
      var n = getVal(id) ? tf4Right((getVal(id) || '').replace(/-/g, 'x'), it.ans) : 0;
      head = (n === 4 ? '✔ Chính xác' : (n ? '◐ Đúng ' + n + '/4 ý' : (answered(id) ? '✘ Chưa đúng' : '✘ Chưa trả lời'))) + ' · ' + vn(TF[n]) + ' điểm. ';
    } else head = ok ? '✔ Chính xác. ' : (answered(id) ? '✘ Chưa đúng. ' : '✘ Chưa trả lời. ');
    box.className = 'exp ' + (ok ? 'ok' : (it.t === 'tf4' && getVal(id) && tf4Right(getVal(id).replace(/-/g, 'x'), it.ans) > 0 && !ok ? 'na' : 'bad')); box.hidden = false;
    box.innerHTML = '<span class="ans">' + head + 'Đáp án: ' + esc(ansText(id)) + '</span>' + sol;
    renderMath(box);
    el.classList.add('marked');
  }
  function lock(id) {
    var it = Q.items[id]; if (it.t === 'essay') return;
    $$('input,button.chk', qEl(id)).forEach(function (x) { x.disabled = true; });
  }

  /* ---------- tổng hợp ---------- */
  function scorable() { return Q.order.filter(function (id) { return Q.items[id].t !== 'essay'; }); }
  function tally() {
    var ids = scorable(), full = 0, done = 0, pts = 0, max = 0;
    ids.forEach(function (id) { max += maxPts(id); if (answered(id)) done++; if (isCorrect(id)) full++; pts += earned(id); });
    return { total: ids.length, ok: full, done: done, pts: Math.round(pts * 100) / 100, max: max };
  }
  function updateStat() {
    var t = tally(), s = $('#stat'); if (!s) return;
    var pb = $('#progBar'); if (pb) pb.style.width = (t.total ? Math.round(t.done / t.total * 100) : 0) + '%';
    s.textContent = testMode && !state.submitted ? ('Đã trả lời ' + t.done + '/' + t.total) : ('Đã làm ' + t.done + '/' + t.total + (state.submitted || !testMode ? ' · Điểm ' + vn(t.pts) : ''));
  }

  /* ---------- gửi dữ liệu ---------- */
  function send(payload, beacon) {
    var url = Q.url; if (!url || /CHUA_CAU_HINH|YOUR_/.test(url)) return;
    payload.set_id = Q.setId; payload.page_id = Q.pageId; payload.mode = Q.mode;
    payload.student_name = state.student.name; payload.student_class = state.student.cls;
    var au = window.GNAuth && GNAuth.get(); if (au) payload.token = au.token;
    payload.ts = new Date().toISOString();
    var body = JSON.stringify(payload);
    try {
      if (beacon && navigator.sendBeacon) { navigator.sendBeacon(url, new Blob([body], { type: 'text/plain;charset=UTF-8' })); return; }
      fetch(url, { method: 'POST', mode: 'no-cors', headers: { 'Content-Type': 'text/plain;charset=UTF-8' }, body: body, keepalive: true }).catch(function () {});
    } catch (e) {}
  }
  function log(ev, extra) { state.events.push({ ev: ev, t: Math.round((now() - state.t0) / 1000), x: extra || '' }); }
  function collectAnswers() {
    var o = {};
    Q.order.forEach(function (id) { var v = getVal(id); if (v !== '') o[id] = Q.items[id].t === 'essay' ? v.slice(0, 1200) : v; });
    return o;
  }

  /* ---------- TỰ LUẬN: AI gợi ý điểm + giáo viên duyệt ---------- */
  function essayBox(id) { return $('.essay-res', qEl(id)); }
  function essayShowSol(id) {
    var it = Q.items[id], box = $('.exp', qEl(id));
    box.className = 'exp na'; box.hidden = false;
    box.innerHTML = '<span class="ans">Lời giải mẫu' + (it.final ? ' · Đáp số: ' + esc(it.final) : '') + '</span><div class="sol">' + (it.sol || '') + '</div>' + rubricHtml(it);
    renderMath(box);
  }
  function essayRender(id, j) {
    var it = Q.items[id], box = essayBox(id); box.hidden = false; box.className = 'essay-res';
    var h = '';
    if (j.official && j.official.score != null) {
      h += '<div class="eo"><b>✅ Giáo viên đã chấm: ' + vn(j.official.score) + ' / ' + vn(j.max || it.max) + ' điểm</b>' + (j.official.comment ? '<div>' + esc(j.official.comment).replace(/\n/g, '<br>') + '</div>' : '') + '</div>';
    }
    if (j.ai) {
      var a = j.ai;
      h += '<div class="ea"><b>🤖 AI gợi ý: ' + vn(a.score) + ' / ' + vn(a.max || j.max || it.max) + ' điểm</b> <small>(tạm tính — giáo viên sẽ duyệt điểm chính thức' + (j.official && j.official.score != null ? '; đã được duyệt ở trên' : '') + ')</small>';
      if (a.items && a.items.length) h += '<ul>' + a.items.map(function (r) { return '<li class="' + (r.got >= r.max - 1e-9 ? 'g' : (r.got > 0 ? 'p' : 'b')) + '">' + esc(r.t) + ' — <b>' + vn(r.got) + '/' + vn(r.max) + '</b>' + (r.note ? '<br><small>' + esc(r.note) + '</small>' : '') + '</li>'; }).join('') + '</ul>';
      if (a.comment) h += '<div class="ecm">' + esc(a.comment).replace(/\n/g, '<br>') + '</div>';
      h += '</div>';
    } else if (!j.official) {
      h += '<div class="ea"><b>📨 Đã nộp cho giáo viên.</b> ' + (j.note ? esc(j.note) : 'Giáo viên sẽ chấm và nhận xét.') + '</div>';
    }
    if (j.left != null) h += '<small class="hint">Còn ' + j.left + ' lượt AI chấm hôm nay.</small>';
    box.innerHTML = h;
    var sb = $('.esub', qEl(id)); if (sb) { sb.disabled = false; sb.textContent = 'AI chấm lại (sau khi sửa bài)'; }
  }
  function essaySubmit(id) {
    var it = Q.items[id], el = qEl(id), text = getVal(id);
    if (text.length < 8) { toast('Hãy viết bài làm (ít nhất vài dòng) rồi mới nộp.'); return Promise.resolve(); }
    if (!window.GNAuth || !GNAuth.get()) { toast('Cần đăng nhập để nộp tự luận.'); return Promise.resolve(); }
    var box = essayBox(id), sb = $('.esub', el); box.hidden = false; box.className = 'essay-res'; box.innerHTML = '<div class="ea">⏳ AI đang đọc và chấm bài của bạn… (khoảng 10–30 giây)</div>'; if (sb) sb.disabled = true;
    state.essays[id] = (state.essays[id] || 0) + 1;
    return GNAuth.api('ly_essay', { uid: id, set_id: Q.setId, page_id: Q.pageId, mode: Q.mode, answer: text.slice(0, 6000), attempt: state.essays[id], title: document.title })
      .then(function (j) { essayRender(id, j); if (!testMode || state.submitted) essayShowSol(id); log('essay', id); return j; })
      .catch(function (e) { box.innerHTML = '<div class="ea bad">' + esc(e.message || 'Không nộp được, hãy thử lại.') + '</div>'; if (sb) sb.disabled = false; });
  }
  function loadMine() {
    if (!window.GNAuth || !GNAuth.get() || !GNAuth.get().user || GNAuth.get().user.role !== 'student') return;
    var ids = Q.order.filter(function (id) { return Q.items[id].t === 'essay'; }); if (!ids.length) return;
    GNAuth.api('ly_essay_mine', { set_id: Q.setId, ids: ids }).then(function (j) {
      (j.rows || []).forEach(function (r) {
        if (!Q.items[r.uid]) return;
        var ta = $('textarea', qEl(r.uid)); if (ta && !ta.value) ta.value = r.answer || '';
        state.mine[r.uid] = r;
        if (!testMode) essayRender(r.uid, { ai: r.ai, official: r.official, max: r.max });
      });
    }).catch(function () {});
  }

  /* ---------- văn bản trang cho Trợ lý AI (có cả bài làm của học sinh) ---------- */
  function domText(el) {
    var c = el.cloneNode(true);
    $$('.katex', c).forEach(function (k) { var a = k.querySelector('annotation[encoding="application/x-tex"]'); k.replaceWith(document.createTextNode('$' + (a ? a.textContent : k.textContent) + '$')); });
    $$('.sym,.qtools,.essay-actions,button,script,style', c).forEach(function (x) { x.remove(); });
    return (c.innerText || c.textContent || '').replace(/[ \t ]+/g, ' ').replace(/\n\s*\n+/g, '\n').trim();
  }
  function pageText() {
    var out = ['TRANG: ' + document.title, state.submitted || !testMode ? '' : '(đang làm kiểm tra)'];
    $$('section.group').forEach(function (g) {
      var h = $('h3', g); out.push('\n=== ' + (h ? h.textContent : '') + ' ===');
      $$('.q', g).forEach(function (q) {
        var id = q.getAttribute('data-id'), it = Q.items[id], n = $('.qn', q).textContent, v = getVal(id), mine = '';
        var stem = domText($('.stem', q) || q);
        var opts = it.t === 'mcq' ? $$('label.opt', q).map(function (l) { return domText(l); }).join(' | ') : '';
        var sts = it.t === 'tf4' ? $$('.tfr .st', q).map(function (s) { return domText(s); }).join('\n') : '';
        if (it.t === 'mcq') mine = v ? v : '(chưa chọn)';
        else if (it.t === 'tf4') mine = v ? v.split('').map(function (c, i) { return 'abcd'.charAt(i) + '=' + (c === 'T' ? 'Đúng' : (c === 'F' ? 'Sai' : '?')); }).join(', ') : '(chưa chọn)';
        else mine = v ? v : '(chưa làm)';
        var ex = $('.exp', q), exT = ex && !ex.hidden ? '\n   Đáp án/lời giải hiển thị: ' + domText(ex) : '';
        out.push('Câu ' + n + ' [' + (h ? h.textContent.split('.')[0] : '') + ']: ' + stem + (opts ? '\n   ' + opts : '') + (sts ? '\n' + sts : '') + '\n   BÀI LÀM CỦA HỌC SINH: ' + mine + exT);
      });
    });
    var t = out.join('\n');
    return t.length > 20000 ? t.slice(0, 20000) + '\n…' : t;
  }
  window.GN_LY_API = { pageText: pageText, isLive: function () { return testMode && !state.submitted; } };

  /* ---------- kết quả ---------- */
  function essaySummary() {
    var ids = Q.order.filter(function (id) { return Q.items[id].t === 'essay'; });
    if (!ids.length) return '';
    var n = Object.keys(state.essays).length;
    return '<div>✍️ Tự luận: ' + n + '/' + ids.length + ' bài đã nộp. Điểm AI gợi ý hiển thị ngay dưới từng bài; điểm chính thức do giáo viên duyệt.</div>';
  }
  function resultHtml(t, d10, pct, spent, auto) {
    return '<h2>Kết quả' + (auto ? ' (hết giờ – tự động nộp)' : '') + '</h2><div class="big">' + vn(t.pts) + ' / ' + vn(t.max) + ' điểm</div>' +
      '<div>Phần trắc nghiệm (thang 10): <b>' + vn(d10) + '</b> · Câu đúng hoàn toàn: <b>' + t.ok + '/' + t.total + '</b> · Thời gian: <b>' + fmtT(spent) + '</b></div>' +
      (testMode ? '<div class="stat">Vi phạm ghi nhận — chuyển tab: ' + state.tab + ', mất focus: ' + state.blur + ', thoát toàn màn hình: ' + state.fs + '</div>' : '') +
      essaySummary() + '<p>Cuộn xuống để xem đáp án và lời giải chi tiết từng câu. Bạn có thể hỏi 🤖 Trợ lý AI.</p>';
  }
  function showResultModal(html) {
    var m = $('#resultModal');
    if (!m) {
      m = document.createElement('div'); m.className = 'modal'; m.id = 'resultModal';
      m.innerHTML = '<div class="box"><div id="resultBox"></div><div class="modal-actions"><button class="btn" id="resultClose" type="button">Đóng — Xem lại bài làm</button></div></div>';
      document.body.appendChild(m); $('#resultClose', m).onclick = function () { m.hidden = true; };
    }
    $('#resultBox', m).innerHTML = html; m.hidden = false;
  }

  /* ---------- nộp bài ---------- */
  function submit(auto) {
    if (state.submitted) return;
    var t = tally();
    if (!auto && testMode) {
      var left = t.total - t.done;
      if (left > 0 && !window.confirm('Bạn còn ' + left + ' câu chưa trả lời. Vẫn nộp bài?')) return;
    }
    state.submitted = true;
    if (state.timerId) clearInterval(state.timerId);
    Q.order.forEach(function (id) { mark(id); lock(id); });
    t = tally();
    var spent = Math.round((now() - state.t0) / 1000);
    var pct = t.max ? Math.round(t.pts / t.max * 1000) / 10 : 0, d10 = t.max ? Math.round(t.pts / t.max * 100) / 10 : 0;
    var essayIds = Q.order.filter(function (id) { return Q.items[id].t === 'essay' && getVal(id).length >= 8; });
    var r = $('#result'); r.hidden = false;
    r.innerHTML = resultHtml(t, d10, pct, spent, auto) + '<button class="btn" id="again">Làm lại từ đầu</button>';
    $('#again').onclick = function () { location.reload(); };
    showResultModal(resultHtml(t, d10, pct, spent, auto));
    document.dispatchEvent(new CustomEvent('quiz:submitted'));
    r.scrollIntoView({ behavior: 'smooth', block: 'start' });
    if (document.fullscreenElement && document.exitFullscreen) { try { document.exitFullscreen(); } catch (e) {} }
    updateStat();
    if (pct >= 80) confetti();
    var sb = $('#lySubmit'); if (sb) sb.disabled = true;
    log('submit', auto ? 'auto' : 'manual');
    send({ action: 'grade_save_result', score: t.pts, total: t.max, pct: pct, score10: d10, time_spent: spent, tab_switch: state.tab, blur: state.blur, fullscreen_exit: state.fs, audio_plays: 0,
      answers: collectAnswers(), events: state.events }, false);
    /* nộp tự luận lần lượt (mỗi bài một lượt AI chấm) */
    essayIds.reduce(function (p, id) { return p.then(function () { return state.essays[id] ? null : essaySubmit(id); }); }, Promise.resolve()).then(function () {
      Q.order.forEach(function (id) { if (Q.items[id].t === 'essay') { essayShowSol(id); var ta = $('textarea', qEl(id)); if (ta) ta.readOnly = false; } });
      var rr = $('#result'); if (rr) { var m = rr.querySelector('.es'); if (!m) { m = document.createElement('div'); m.className = 'es'; rr.insertBefore(m, rr.querySelector('#again')); } m.innerHTML = essaySummary(); }
    });
    setAskButtons();
  }

  function confetti() {
    try {
      var c = document.createElement('canvas'); c.className = 'confetti'; document.body.appendChild(c);
      var x = c.getContext('2d'), W = c.width = innerWidth, H = c.height = innerHeight, cols = ['#ff6b6b', '#ffd93d', '#6bcB77', '#4d96ff', '#b983ff'];
      var P = []; for (var i = 0; i < 120; i++) P.push({ x: Math.random() * W, y: -20 - Math.random() * H * .4, r: 4 + Math.random() * 5, v: 2 + Math.random() * 4, d: Math.random() * 6, c: cols[i % 5] });
      var f = 0; (function a() { x.clearRect(0, 0, W, H); P.forEach(function (p) { p.y += p.v; p.x += Math.sin(p.d += .05) * 2; x.fillStyle = p.c; x.fillRect(p.x, p.y, p.r, p.r * 1.6); });
        if (++f < 200) requestAnimationFrame(a); else c.remove(); })();
    } catch (e) {}
  }

  /* ---------- nhật ký luyện tập ---------- */
  function resetsGet() { try { return parseInt(sessionStorage.getItem('rs_' + Q.setId + Q.pageId) || '0', 10) || 0; } catch (e) { return 0; } }
  function practicePayload(ev) {
    var t = tally(), wrong = Q.order.filter(function (id) { return answered(id) && isCorrect(id) === false; });
    return { action: 'grade_practice', event: ev, done: t.done, score: t.pts, total: t.max, wrong: wrong.join(','), resets: resetsGet(), time_spent: state.t0 ? Math.round((now() - state.t0) / 1000) : 0 };
  }

  /* ---------- nút hỏi AI trên từng câu ---------- */
  function setAskButtons() {
    var live = testMode && !state.submitted;
    $$('.qtools button').forEach(function (b) { b.disabled = live; b.title = live ? 'Mở sau khi nộp bài' : ''; });
  }
  function addAskButtons() {
    if (!(window.GNAuth && GNAuth.get())) return;
    var u = GNAuth.get().user; if (!(u.role === 'admin' || u.ai)) return;
    Q.order.forEach(function (id) {
      var q = qEl(id), it = Q.items[id], n = $('.qn', q).textContent, part = ($('h3', q.closest('section.group')) || {}).textContent || '';
      var lab = 'câu ' + n + ' ' + part.split('.')[0].toLowerCase().replace('phần', '(phần') + ')';
      var d = document.createElement('div'); d.className = 'qtools';
      d.innerHTML = '<button type="button" data-k="solve">🤖 AI giải bài</button><button type="button" data-k="check">🤖 AI xem bài làm của mình</button>';
      d.addEventListener('click', function (ev) {
        var b = ev.target.closest('button'); if (!b || b.disabled) return;
        var p = b.getAttribute('data-k') === 'solve' ? 'Hãy giải chi tiết ' + lab + ' từng bước (viết công thức bằng LaTeX), rồi kết luận đáp án.'
          : 'Hãy xem bài làm của mình ở ' + lab + ' và chấm giúp mình: ý nào đúng, sai ở đâu, nên sửa thế nào' + (it.t === 'essay' ? ' (cho điểm gợi ý theo thang ' + vn(it.max) + ').' : '.');
        if (window.GNFB) window.GNFB.open('a', p, true);
      });
      q.querySelector('.qb').appendChild(d);
    });
    setAskButtons();
  }

  /* ---------- bắt đầu ---------- */
  function begin(name, cls) {
    state.student = { name: name, cls: cls };
    lsSet('gnomio_student', JSON.stringify(state.student));
    state.started = true; state.t0 = now();
    $('#startModal').hidden = true;
    log('enter');
    if (testMode) send({ action: 'grade_test_enter' }, false); else send(practicePayload('enter'), false);
    if (testMode) { enterFullscreen(); state.remain = (Q.minutes || 40) * 60; tick(); state.timerId = setInterval(tick, 1000); }
  }
  function enterFullscreen() {
    var el = document.documentElement, ov = $('#fsOverlay');
    try { if (el.requestFullscreen) { var pr = el.requestFullscreen(); if (pr && pr.catch) pr.catch(function () {}); } else if (el.webkitRequestFullscreen) el.webkitRequestFullscreen(); } catch (e) {}
    if (ov) ov.hidden = true;
  }
  function tick() {
    if (state.submitted) return;
    var te = $('#timer'), over = state.remain < 0;
    te.textContent = over ? '+' + fmtT(-state.remain) : fmtT(state.remain);
    te.classList.toggle('warn', !over && state.remain <= 600 && state.remain > 120);
    te.classList.toggle('low', over || state.remain <= 120);
    if (!state.warned && Q.warnAt && state.remain <= Q.warnAt * 60) {
      state.warned = true; $('#warnText').textContent = 'Còn ' + Q.warnAt + ' phút nữa là hết giờ. Hãy kiểm tra lại các câu chưa làm.'; $('#warnModal').hidden = false; log('warn', Q.warnAt);
    }
    if (state.remain === 0 && !state.timeUp) { state.timeUp = true; log('time_up'); $('#timeUpModal').hidden = false; }
    if (state.remain <= -300) { log('auto_submit_timeout'); submit(true); return; }
    state.remain--;
  }

  /* ---------- khởi tạo ---------- */
  function init() {
    var ses = window.GNAuth && GNAuth.get();
    if (ses) {
      $('#stName').value = ses.user.name; $('#stClass').value = ses.user.cls || '';
      $$('#startModal label').forEach(function (l) { l.hidden = true; l.style.display = 'none'; });
      var hp = $('#startModal p'); if (hp) hp.innerHTML = 'Xin chào <b>' + esc(ses.user.name || '') + '</b>' + (ses.user.cls ? ' · lớp ' + esc(ses.user.cls) : '') + (ses.user.role === 'student' ? '. Kết quả sẽ được ghi vào tài khoản của bạn.' : '. Bạn đang làm thử — kết quả không được lưu.');
      var skb = $('#skipBtn'); if (skb) skb.hidden = true;
    } else {
      try { var s = JSON.parse(lsGet('gnomio_student') || 'null'); if (s) { $('#stName').value = s.name || ''; $('#stClass').value = s.cls || ''; } } catch (e) {}
    }
    $('#startBtn').onclick = function () {
      var n = $('#stName').value.trim(), c = $('#stClass').value.trim();
      if (testMode && !ses && (!n || !c)) { $('#stErr').textContent = 'Vui lòng nhập họ tên và lớp.'; return; }
      begin(n || 'Ẩn danh', c);
    };
    if (ses && !testMode) begin(ses.user.name || '', ses.user.cls || '');
    var sk = $('#skipBtn'); if (sk) sk.onclick = function () { state.started = true; state.t0 = now(); $('#startModal').hidden = true; };
    $('#warnOk').onclick = function () { $('#warnModal').hidden = true; };

    Q.order.forEach(function (id) {
      var it = Q.items[id], el = qEl(id); if (!el) return;
      $$('input[type=radio]', el).forEach(function (r) {
        r.addEventListener('change', function () {
          $$('label.opt', el).forEach(function (l) { l.classList.toggle('sel', $('input', l).checked); });
          if (state.submitted) return;
          if (!testMode && it.t === 'mcq') { mark(id); lock(id); }
          updateStat();
        });
      });
      var chk = $('button.chk', el);
      if (it.t === 'tf4') {
        if (chk) { if (testMode) chk.hidden = true; else chk.onclick = function () { if (!answered(id)) { toast('Hãy chọn Đúng/Sai cho cả 4 ý.'); return; } mark(id); lock(id); updateStat(); }; }
      } else if (it.t === 'short') {
        var inp = $('input.numin', el);
        if (chk) { if (testMode) chk.hidden = true; else chk.onclick = function () { if (answered(id)) { mark(id); lock(id); updateStat(); } }; }
        inp.addEventListener('input', updateStat);
        inp.addEventListener('keydown', function (e) { if (e.key === 'Enter') { e.preventDefault(); if (chk && !testMode) chk.click(); } });
      } else if (it.t === 'essay') {
        var ta = $('textarea', el), dk = 'lydraft_' + Q.setId + '_' + id;
        try { var dr = lsGet(dk); if (dr && !ta.value) ta.value = dr; } catch (e) {}
        ta.addEventListener('input', function () { lsSet(dk, ta.value); updateStat(); });
        var sb = $('.esub', el), sw = $('.eshow', el);
        if (testMode) { if (sb) sb.hidden = true; if (sw) sw.hidden = true; }
        else {
          sb.onclick = function () { essaySubmit(id); };
          sw.onclick = function () { essayShowSol(id); };
        }
        $$('.sym button', el).forEach(function (b) {
          b.addEventListener('click', function () {
            var s = b.getAttribute('data-s'), a = ta.selectionStart || 0, z = ta.selectionEnd || 0;
            ta.value = ta.value.slice(0, a) + s + ta.value.slice(z); ta.focus(); ta.selectionStart = ta.selectionEnd = a + s.length; ta.dispatchEvent(new Event('input'));
          });
        });
      }
    });
    $$('textarea.ly-essay').forEach(function (ta) {
      var wc = document.createElement('div'); wc.className = 'wc'; ta.parentNode.insertBefore(wc, ta.nextSibling);
      var up = function () { wc.textContent = (ta.value.trim().match(/\S+/g) || []).length + ' từ'; };
      ta.addEventListener('input', up); up();
    });
    var sub = $('#lySubmit'); if (sub) sub.onclick = function () { submit(false); };
    var rs = $('#reset'); if (rs) rs.onclick = function () {
      if (window.confirm('Làm lại từ đầu? Kết quả hiện tại sẽ bị xoá.')) {
        try { sessionStorage.setItem('rs_' + Q.setId + Q.pageId, String(resetsGet() + 1)); } catch (e) {}
        Q.order.forEach(function (id) { if (Q.items[id].t === 'essay') { try { localStorage.removeItem('lydraft_' + Q.setId + '_' + id); } catch (e) {} } });
        if (state.started && !testMode) send(practicePayload('reset'), true); state.submitted = true; location.reload();
      }
    };
    renderMath(document.body);
    updateStat(); addAskButtons(); loadMine();

    if (testMode) {
      document.body.classList.add('testmode');
      var live = function () { return state.started && !state.submitted; };
      var banner = function (m) { toast(m); };
      var ov = $('#fsOverlay');
      if ($('#fsBack')) $('#fsBack').onclick = enterFullscreen;
      if ($('#timeUpSubmit')) $('#timeUpSubmit').onclick = function () { $('#timeUpModal').hidden = true; submit(true); };
      if ($('#timeUpBack')) $('#timeUpBack').onclick = function () { $('#timeUpModal').hidden = true; };
      document.addEventListener('visibilitychange', function () { if (document.hidden && live()) { state.tab++; log('tab_hidden', state.tab); banner('Bạn vừa chuyển tab / rời trang làm bài (lần ' + state.tab + '). Hành vi này được ghi nhận.'); } });
      window.addEventListener('blur', function () { if (live() && !document.hidden) { state.blur++; log('blur', state.blur); banner('Cửa sổ làm bài mất tiêu điểm (lần ' + state.blur + ').'); } });
      var onFs = function () {
        var inFs = document.fullscreenElement || document.webkitFullscreenElement;
        if (!inFs && live()) { state.fs++; log('fs_exit', state.fs); if (ov) ov.hidden = false; } else if (inFs && ov) ov.hidden = true;
      };
      document.addEventListener('fullscreenchange', onFs); document.addEventListener('webkitfullscreenchange', onFs);
      var logN = {}, logBad = function (ev, x) { logN[ev] = (logN[ev] || 0) + 1; if (logN[ev] <= 10) log(ev, x); };
      document.addEventListener('contextmenu', function (e) { if (live()) { e.preventDefault(); logBad('contextmenu'); } });
      ['copy', 'cut', 'paste', 'dragstart', 'drop'].forEach(function (ev) { document.addEventListener(ev, function (e) { if (live()) { e.preventDefault(); logBad(ev); if (ev === 'paste') banner('Không được dán nội dung vào bài làm.'); } }); });
      document.addEventListener('keydown', function (e) {
        if (!live()) return;
        if (e.target && e.target.closest && e.target.closest('.gnfb-box')) return;
        var k = (e.key || '').toLowerCase(), c = e.ctrlKey || e.metaKey, bad = false;
        if (e.key === 'F12' || e.key === 'Escape') bad = true;
        if (c && !e.shiftKey && 'casupv'.indexOf(k) >= 0 && k.length === 1) bad = true;
        if (c && e.shiftKey && 'ijck'.indexOf(k) >= 0 && k.length === 1) bad = true;
        if (bad) { e.preventDefault(); e.stopPropagation(); logBad('shortcut', (c ? 'Ctrl+' : '') + (e.shiftKey ? 'Shift+' : '') + (e.key || '')); }
      }, true);
      window.addEventListener('beforeunload', function (e) { if (live()) { e.preventDefault(); e.returnValue = ''; } });
    }
    window.addEventListener('pagehide', function () {
      if (state.started && !state.submitted && !testMode && state.student.name) send(practicePayload('leave'), true);
      if (state.started && !state.submitted && testMode) {
        var t = tally();
        send({ action: 'grade_save_partial', score: t.pts, total: t.max, tab_switch: state.tab, blur: state.blur, fullscreen_exit: state.fs, time_spent: Math.round((now() - state.t0) / 1000), answers: collectAnswers(), events: state.events }, true);
      }
    });
    window.__quiz = { isSubmitted: function () { return state.submitted; }, tally: tally, submit: submit, isCorrect: isCorrect, getVal: getVal, earned: earned, toNum: toNum, numOk: numOk };
  }
  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', init); else init();
})();
