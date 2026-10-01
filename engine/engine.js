/* Engine runtime dùng chung: chấm điểm, giải thích, timer, chống gian lận, gửi kết quả về Google Sheet, audio. */
(function () {
  'use strict';
  var Q = window.QUIZ;
  if (!Q) return;
  var $ = function (s, r) { return (r || document).querySelector(s); };
  var $$ = function (s, r) { return Array.prototype.slice.call((r || document).querySelectorAll(s)); };
  var state = { started: false, submitted: false, t0: 0, tab: 0, blur: 0, fs: 0, plays: 0, events: [], student: { name: '', cls: '' }, remain: 0, warned: false, timerId: null };
  var testMode = Q.mode === 'test';

  /* ---------- tiện ích ---------- */
  function lsGet(k) { try { return localStorage.getItem(k); } catch (e) { return null; } }
  function lsSet(k, v) { try { localStorage.setItem(k, v); } catch (e) {} }
  function esc(s) { return String(s).replace(/[&<>"]/g, function (c) { return { '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' }[c]; }); }
  function norm(s) {
    s = String(s == null ? '' : s).toLowerCase();
    s = s.replace(/[’‘`´]/g, "'").replace(/[“”]/g, '"');
    s = s.replace(/won't/g, 'will not').replace(/can't/g, 'can not').replace(/cannot/g, 'can not')
      .replace(/n't\b/g, ' not').replace(/'ve\b/g, ' have').replace(/'ll\b/g, ' will').replace(/'m\b/g, ' am').replace(/'re\b/g, ' are');
    s = s.replace(/[.,;:!?"]+/g, ' ').replace(/\s*\/\s*/g, ' / ').replace(/\s+/g, ' ').trim();
    return s;
  }
  function pad(n) { return (n < 10 ? '0' : '') + n; }
  function fmt(sec) { sec = Math.max(0, sec | 0); return pad((sec / 60) | 0) + ':' + pad(sec % 60); }
  function now() { return Date.now(); }

  /* ---------- đọc / chấm ---------- */
  function qEl(id) { return $('.q[data-id="' + id + '"]'); }
  function getVal(id) {
    var t = Q.items[id].t, el = qEl(id);
    if (t === 'mcq' || t === 'tf' || t === 'tfng') {
      var c = $('input[type=radio]:checked', el);
      return c ? c.value : '';
    }
    if (t === 'fill') return $$('.blank', el).map(function (i) { return i.value.trim(); });
    if (t === 'open') return $('textarea', el).value.trim();
    return '';
  }
  function answered(id) {
    var v = getVal(id);
    if (Array.isArray(v)) return v.some(function (x) { return x !== ''; });
    return v !== '';
  }
  function blanksOf(a) { // chuẩn hoá ANS của câu điền: mảng các ô, mỗi ô là mảng đáp án chấp nhận
    if (a && a.blanks) return a.blanks;
    if (typeof a === 'string') return [[a]];
    return [a];
  }
  function isCorrect(id) {
    var it = Q.items[id], a = Q.ANS[id], v = getVal(id);
    if (a === undefined || it.t === 'open') return null;
    if (it.t === 'fill') {
      var bl = blanksOf(a);
      for (var i = 0; i < bl.length; i++) {
        var got = norm(v[i] || '');
        if (!got) return false;
        if (!bl[i].some(function (x) { return norm(x) === got; })) return false;
      }
      return true;
    }
    return v === a;
  }
  function showAnsText(id) {
    var it = Q.items[id], a = Q.ANS[id], el = qEl(id);
    if (it.t === 'mcq') {
      var lab = $('input[value="' + a + '"]', el);
      var txt = lab ? lab.parentNode.textContent.replace(/^\s*[A-D]\.\s*/, '').trim() : '';
      return txt && txt !== a ? a + '. ' + txt : a;
    }
    if (it.t === 'tf') return a === 'T' ? 'True' : 'False';
    if (it.t === 'tfng') return { T: 'True', F: 'False', NG: 'Not given' }[a];
    if (it.t === 'fill') return blanksOf(a).map(function (b) { return b[0]; }).join('  |  ');
    return '';
  }
  function mark(id, reveal) {
    var it = Q.items[id], el = qEl(id), ok = isCorrect(id);
    var box = $('.exp', el);
    var a = Q.ANS[id], exp = Q.EXP[id] || '';
    if (it.t === 'open') {
      box.className = 'exp na'; box.hidden = false;
      box.innerHTML = '<span class="ans">Đáp án mẫu / gợi ý:</span> ' + (exp || '(chưa có)');
      return;
    }
    if (a === undefined) {
      box.className = 'exp na'; box.hidden = false;
      box.innerHTML = '<span class="ans">Đáp án đang được cập nhật.</span>';
      return;
    }
    if (it.t === 'mcq' || it.t === 'tf' || it.t === 'tfng') {
      $$('label.opt', el).forEach(function (l) {
        var v = $('input', l).value; l.classList.remove('right', 'wrong');
        if (v === a) l.classList.add('right');
        else if ($('input', l).checked) l.classList.add('wrong');
      });
    } else if (it.t === 'fill') {
      var bl = blanksOf(a);
      $$('.blank', el).forEach(function (inp, i) {
        var g = norm(inp.value), good = bl[i] && bl[i].some(function (x) { return norm(x) === g; });
        inp.classList.remove('right', 'wrong'); inp.classList.add(good ? 'right' : 'wrong');
      });
    }
    box.className = 'exp ' + (ok ? 'ok' : 'bad'); box.hidden = false;
    var head = ok ? '✔ Chính xác. ' : (answered(id) ? '✘ Chưa đúng. ' : '✘ Chưa trả lời. ');
    box.innerHTML = '<span class="ans">' + head + 'Đáp án: ' + esc(showAnsText(id)) + '</span>' + (exp ? '<div>' + exp + '</div>' : '');
  }
  function lock(id) {
    $$('input,textarea,button.chk', qEl(id)).forEach(function (x) { x.disabled = true; });
  }

  /* ---------- tổng hợp ---------- */
  function scorable() { return Q.order.filter(function (id) { return Q.ANS[id] !== undefined && Q.items[id].t !== 'open'; }); }
  function tally() {
    var ids = scorable(), ok = 0, done = 0;
    ids.forEach(function (id) { if (answered(id)) done++; if (isCorrect(id)) ok++; });
    return { total: ids.length, ok: ok, done: done };
  }
  function updateStat() {
    var t = tally(), s = $('#stat');
    if (!s) return;
    var pb = $('#progBar'); if (pb) pb.style.width = (t.total ? Math.round(t.done / t.total * 100) : 0) + '%';
    s.textContent = testMode && !state.submitted ? ('Đã trả lời ' + t.done + '/' + t.total) : ('Đã làm ' + t.done + '/' + t.total + (state.submitted || !testMode ? ' · Đúng ' + t.ok : ''));
  }

  /* ---------- gửi dữ liệu ---------- */
  function send(payload, beacon) {
    var url = Q.url;
    if (!url || /CHUA_CAU_HINH|YOUR_/.test(url)) return;
    payload.set_id = Q.setId; payload.page_id = Q.pageId; payload.mode = Q.mode;
    payload.student_name = state.student.name; payload.student_class = state.student.cls;
    payload.ts = new Date().toISOString();
    var body = JSON.stringify(payload);
    try {
      if (beacon && navigator.sendBeacon) { navigator.sendBeacon(url, new Blob([body], { type: 'text/plain;charset=UTF-8' })); return; }
      fetch(url, { method: 'POST', mode: 'no-cors', headers: { 'Content-Type': 'text/plain;charset=UTF-8' }, body: body, keepalive: true }).catch(function () {});
    } catch (e) {}
  }
  function log(ev, extra) {
    state.events.push({ ev: ev, t: Math.round((now() - state.t0) / 1000), x: extra || '' });
  }
  function collectAnswers() {
    var o = {};
    Q.order.forEach(function (id) { var v = getVal(id); if (Array.isArray(v)) v = v.join(' | '); if (v !== '') o[id] = v; });
    return o;
  }

  function showResultModal(t, d10, pct, spent, auto) {
    var m = $('#resultModal');
    if (!m) {
      m = document.createElement('div'); m.className = 'modal'; m.id = 'resultModal';
      m.innerHTML = '<div class="box"><div id="resultBox"></div><div class="modal-actions"><button class="btn" id="resultClose" type="button">Đóng — Xem lại bài làm</button></div></div>';
      document.body.appendChild(m);
      $('#resultClose', m).onclick = function () { m.hidden = true; };
    }
    $('#resultBox', m).innerHTML = '<h3>Kết quả bài làm' + (auto ? ' (hết giờ – tự động nộp)' : '') + '</h3><div class="big">' + t.ok + ' / ' + t.total + '</div>' +
      '<div>Thang điểm 10: <b>' + d10 + '</b> · Tỉ lệ đúng: <b>' + pct + '%</b> · Thời gian: <b>' + fmt(spent) + '</b></div>' +
      (testMode ? '<div class="stat">Vi phạm ghi nhận — chuyển tab: ' + state.tab + ', mất focus: ' + state.blur + ', thoát toàn màn hình: ' + state.fs + '</div>' : '') +
      '<p>Đáp án đúng và giải thích chi tiết hiển thị ngay dưới từng câu.</p>';
    m.hidden = false;
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
    Q.order.forEach(function (id) { mark(id, true); lock(id); });
    t = tally();
    var spent = Math.round((now() - state.t0) / 1000);
    var pct = t.total ? Math.round(t.ok / t.total * 1000) / 10 : 0;
    var d10 = t.total ? Math.round(t.ok / t.total * 100) / 10 : 0;
    var r = $('#result');
    r.hidden = false;
    r.innerHTML = '<h2>Kết quả' + (auto ? ' (hết giờ – tự động nộp)' : '') + '</h2><div class="big">' + t.ok + ' / ' + t.total + '</div>' +
      '<div>Thang điểm 10: <b>' + d10 + '</b> · Tỉ lệ đúng: <b>' + pct + '%</b> · Thời gian: <b>' + fmt(spent) + '</b></div>' +
      (testMode ? '<div class="stat">Vi phạm ghi nhận — chuyển tab: ' + state.tab + ', mất focus: ' + state.blur + ', thoát toàn màn hình: ' + state.fs + '</div>' : '') +
      '<p>Cuộn xuống để xem đáp án đúng và giải thích chi tiết từng câu.</p>' +
      '<button class="btn" id="again">Làm lại từ đầu</button>';
    $('#again').onclick = function () { location.reload(); };
    showResultModal(t, d10, pct, spent, auto);
    document.dispatchEvent(new CustomEvent('quiz:submitted'));
    r.scrollIntoView({ behavior: 'smooth', block: 'start' });
    if (document.fullscreenElement && document.exitFullscreen) { try { document.exitFullscreen(); } catch (e) {} }
    updateStat();
    if (pct >= 80) confetti();
    var sb = $('#submit'); if (sb) sb.disabled = true;
    log('submit', auto ? 'auto' : 'manual');
    send({ action: 'grade_save_result', score: t.ok, total: t.total, pct: pct, score10: d10, time_spent: spent,
      tab_switch: state.tab, blur: state.blur, fullscreen_exit: state.fs, audio_plays: state.plays,
      answers: collectAnswers(), events: state.events }, false);
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

  /* ---------- bắt đầu ---------- */
  function begin(name, cls) {
    state.student = { name: name, cls: cls };
    lsSet('gnomio_student', JSON.stringify(state.student));
    state.started = true; state.t0 = now();
    $('#startModal').hidden = true;
    log('enter');
    send({ action: 'grade_test_enter' }, false);
    if (testMode) {
      enterFullscreen();
      state.remain = (Q.minutes || 40) * 60;
      tick();
      state.timerId = setInterval(tick, 1000);
    }
  }
  function enterFullscreen() {
    var el = document.documentElement, ov = $('#fsOverlay');
    try {
      if (el.requestFullscreen) { var pr = el.requestFullscreen(); if (pr && pr.catch) pr.catch(function () {}); }
      else if (el.webkitRequestFullscreen) el.webkitRequestFullscreen();
    } catch (e) {}
    if (ov) ov.hidden = true;
  }
  function tick() {
    if (state.submitted) return;
    var te = $('#timer');
    var over = state.remain < 0;                     // đang trong 5 phút gia hạn
    te.textContent = over ? '+' + fmt(-state.remain) : fmt(state.remain);
    te.classList.toggle('warn', !over && state.remain <= 600 && state.remain > 120);
    te.classList.toggle('low', over || state.remain <= 120);
    if (!state.warned && Q.warnAt && state.remain <= Q.warnAt * 60) {
      state.warned = true;
      $('#warnText').textContent = 'Còn ' + Q.warnAt + ' phút nữa là hết giờ. Hãy kiểm tra lại các câu chưa làm.';
      $('#warnModal').hidden = false;
      log('warn', Q.warnAt);
    }
    if (state.remain === 0 && !state.timeUp) {
      state.timeUp = true; log('time_up');
      $('#timeUpModal').hidden = false;
    }
    if (state.remain <= -300) { log('auto_submit_timeout'); submit(true); return; }
    state.remain--;
  }

  /* ---------- khởi tạo ---------- */
  function init() {
    // thông tin học sinh
    try { var s = JSON.parse(lsGet('gnomio_student') || 'null'); if (s) { $('#stName').value = s.name || ''; $('#stClass').value = s.cls || ''; } } catch (e) {}
    $('#startBtn').onclick = function () {
      var n = $('#stName').value.trim(), c = $('#stClass').value.trim();
      if (testMode && (!n || !c)) { $('#stErr').textContent = 'Vui lòng nhập họ tên và lớp.'; return; }
      begin(n || 'Ẩn danh', c);
    };
    var sk = $('#skipBtn'); if (sk) sk.onclick = function () { state.started = true; state.t0 = now(); $('#startModal').hidden = true; };
    $('#warnOk').onclick = function () { $('#warnModal').hidden = true; };

    // câu hỏi
    Q.order.forEach(function (id) {
      var it = Q.items[id], el = qEl(id);
      if (!el) return;
      if (!testMode && (it.t === 'mcq' || it.t === 'tf' || it.t === 'tfng')) {
        $$('input[type=radio]', el).forEach(function (r) {
          r.addEventListener('change', function () { if (state.submitted) return; mark(id); lock(id); updateStat(); });
        });
      } else if (!testMode && it.t === 'fill') {
        var b = $('button.chk', el);
        if (b) b.onclick = function () { if (answered(id)) { mark(id); lock(id); updateStat(); } };
        $$('.blank', el).forEach(function (inp) { inp.addEventListener('keydown', function (e) { if (e.key === 'Enter') { e.preventDefault(); if (b) b.click(); } }); });
      } else if (!testMode && it.t === 'open') {
        var ob = $('button.chk', el); if (ob) ob.onclick = function () { mark(id); updateStat(); };
      } else {
        $$('input[type=radio]', el).forEach(function (r) { r.addEventListener('change', function () { updateStat(); }); });
        $$('.blank,textarea', el).forEach(function (x) { x.addEventListener('input', updateStat); });
      }
      $$('input[type=radio]', el).forEach(function (r) {
        r.addEventListener('change', function () { $$('label.opt', el).forEach(function (l) { l.classList.toggle('sel', $('input', l).checked); }); });
      });
    });
    var sub = $('#submit'); if (sub) sub.onclick = function () { submit(false); };
    var rs = $('#reset'); if (rs) rs.onclick = function () { if (window.confirm('Làm lại từ đầu? Kết quả hiện tại sẽ bị xoá.')) location.reload(); };
    $$('textarea.blank.long').forEach(function (ta) {
      var grow = function () { ta.style.height = 'auto'; ta.style.height = Math.max(96, ta.scrollHeight + 2) + 'px'; };
      ta.addEventListener('input', grow);
    });
    $$('textarea.open').forEach(function (ta) {
      var wc = document.createElement('div'); wc.className = 'wc'; ta.parentNode.insertBefore(wc, ta.nextSibling);
      var up = function () { var w = (ta.value.trim().match(/\S+/g) || []).length; wc.textContent = w + ' từ'; };
      ta.addEventListener('input', up); up();
    });
    updateStat();

    // audio
    var au = $('#audio');
    if (au) {
      var max = Q.audioMaxPlays || 0, last = 0, pc = $('#plays');
      au.addEventListener('play', function () {
        if (au.currentTime < 1) { state.plays++; log('audio_play', state.plays); }
        if (pc) pc.textContent = 'Đã nghe: ' + state.plays + (max ? '/' + max : '') + ' lần';
        if (max && state.plays > max) { au.pause(); au.controls = false; }
      });
      if (testMode && Q.lockSeek) {
        au.addEventListener('timeupdate', function () { if (!au.seeking) last = au.currentTime; });
        au.addEventListener('seeking', function () { if (Math.abs(au.currentTime - last) > 1.5) au.currentTime = last; });
      }
    }

    // chống gian lận (chỉ chế độ kiểm tra; tự tắt sau khi nộp bài)
    if (testMode) {
      document.body.classList.add('testmode');
      var live = function () { return state.started && !state.submitted; };
      var banner = function (m) { var t = $('#toast'); t.textContent = '⚠ ' + m; t.hidden = false; clearTimeout(t._t); t._t = setTimeout(function () { t.hidden = true; }, 4000); };
      var ov = $('#fsOverlay');
      if ($('#fsBack')) $('#fsBack').onclick = enterFullscreen;
      if ($('#timeUpSubmit')) $('#timeUpSubmit').onclick = function () { $('#timeUpModal').hidden = true; submit(true); };
      if ($('#timeUpBack')) $('#timeUpBack').onclick = function () { $('#timeUpModal').hidden = true; };
      document.addEventListener('visibilitychange', function () {
        if (document.hidden && live()) { state.tab++; log('tab_hidden', state.tab); banner('Bạn vừa chuyển tab / rời trang làm bài (lần ' + state.tab + '). Hành vi này được ghi nhận.'); }
      });
      window.addEventListener('blur', function () {
        if (live() && !document.hidden) { state.blur++; log('blur', state.blur); banner('Cửa sổ làm bài mất tiêu điểm (lần ' + state.blur + ').'); }
      });
      var onFs = function () {
        var inFs = document.fullscreenElement || document.webkitFullscreenElement;
        if (!inFs && live()) { state.fs++; log('fs_exit', state.fs); if (ov) ov.hidden = false; }
        else if (inFs && ov) ov.hidden = true;
      };
      document.addEventListener('fullscreenchange', onFs);
      document.addEventListener('webkitfullscreenchange', onFs);
      document.addEventListener('contextmenu', function (e) { if (live()) e.preventDefault(); });
      ['copy', 'cut', 'paste', 'dragstart', 'drop'].forEach(function (ev) { document.addEventListener(ev, function (e) { if (live()) { e.preventDefault(); if (ev === 'paste') banner('Không được dán nội dung vào bài làm.'); } }); });
      document.addEventListener('keydown', function (e) {
        if (!live()) return;
        var k = (e.key || '').toLowerCase(), c = e.ctrlKey || e.metaKey, bad = false;
        if (e.key === 'F12' || e.key === 'Escape') bad = true;
        if (c && !e.shiftKey && 'casupv'.indexOf(k) >= 0 && k.length === 1) bad = true;
        if (c && e.shiftKey && 'ijck'.indexOf(k) >= 0 && k.length === 1) bad = true;
        if (bad) { e.preventDefault(); e.stopPropagation(); }
      }, true);
      window.addEventListener('beforeunload', function (e) { if (live()) { e.preventDefault(); e.returnValue = ''; } });
    }
    window.addEventListener('pagehide', function () {
      if (state.started && !state.submitted && testMode) {
        var t = tally();
        send({ action: 'grade_save_partial', score: t.ok, total: t.total, tab_switch: state.tab, blur: state.blur, fullscreen_exit: state.fs,
          time_spent: Math.round((now() - state.t0) / 1000), answers: collectAnswers(), events: state.events }, true);
      }
    });
    window.__quiz = { isSubmitted: function () { return state.submitted; }, norm: norm, tally: tally, submit: submit, isCorrect: isCorrect };
  }
  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', init); else init();
})();
