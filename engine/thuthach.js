/* THỬ THÁCH – phần chạy trên từng trang bài (lý thuyết / luyện tập / kiểm tra) và thư viện dùng chung cho bản đồ lộ trình.
   Nạp tự động bởi GNAuth.requireSet() khi học sinh đang ở chế độ Thử thách (user.tt === 'thuthach').
   Việc chính: chặn trang bài còn khoá, khoá tab bài sau, đồng hồ đọc lý thuyết, thông báo qua bài / chưa đạt sau khi nộp. */
(function () {
  'use strict';
  var A = window.GNAuth, ROOT = window.GN_ROOT || '';
  if (!A) return;
  var T = window.GNTT = window.GNTT || {};
  var sess = A.get(), U = sess && sess.user;
  var KEY = 'gn_tt_' + (U ? U.username : '');
  function lsGet(k) { try { return localStorage.getItem(k); } catch (e) { return null; } }
  function lsSet(k, v) { try { localStorage.setItem(k, v); } catch (e) {} }
  function esc(s) { return A.esc(s); }
  function hop(o, k) { return Object.prototype.hasOwnProperty.call(o || {}, k); }
  function mmss(s) { s = Math.max(0, s | 0); return ((s / 60) | 0) + ':' + (s % 60 < 10 ? '0' : '') + (s % 60); }

  T.on = function () { return !!U && U.role === 'student' && U.tt === 'thuthach'; };
  T.stars = function (best, need) { return best >= 95 ? 3 : (best >= Math.max(need, 85) ? 2 : (best >= need ? 1 : 0)); };
  T.need = function (cfg, kind) { return kind === 'test' ? +cfg.test_pass : (kind === 'practice' ? +cfg.practice_pass : 0); };

  /* ----- trạng thái (nhớ 60 giây để chuyển trang nhanh; chỗ nào quyết định khoá thì luôn hỏi lại máy chủ) ----- */
  T.cached = function () { try { var o = JSON.parse(lsGet(KEY) || 'null'); return o && o.u === U.username ? o : null; } catch (e) { return null; } };
  T.save = function (s) { lsSet(KEY, JSON.stringify({ u: U.username, t: Date.now(), s: s })); return s; };
  T.state = function (force) {
    var c = T.cached();
    if (!force && c && Date.now() - c.t < 60000) return Promise.resolve(c.s);
    return A.api('tt_state').then(T.save).catch(function (e) { if (c) return c.s; throw e; });
  };
  T.locate = function (st, id) {
    var ps = (st && st.paths) || [];
    for (var k = 0; k < ps.length; k++) { var i = ps[k].steps.indexOf(id); if (i >= 0) return { p: ps[k], i: i }; }
    return null;
  };
  T.lockedBy = function (st, id) {   /* id bước đang chặn, hoặc null */
    var l = T.locate(st, id); if (!l) return null;
    for (var j = 0; j < l.i; j++) if (!hop(l.p.done, l.p.steps[j])) return l.p.steps[j];
    return null;
  };
  var META = {};
  T.meta = function (pid) {   /* {steps: {id: {title, url, kind, chap, n}}, doc} */
    if (META[pid]) return META[pid];
    return META[pid] = fetch(ROOT + 'thuthach/' + pid + '.json').then(function (r) { if (!r.ok) throw new Error('http'); return r.json(); }).then(function (doc) {
      var m = {}; doc.chapters.forEach(function (c) { c.steps.forEach(function (s) { s.chap = c.title; m[s.id] = s; }); });
      return { steps: m, doc: doc };
    });
  };

  /* ----- giao diện nhỏ trong trang ----- */
  function css() {
    if (document.getElementById('tt-css')) return;
    var s = document.createElement('style'); s.id = 'tt-css';
    s.textContent = '.tt-hud{position:fixed;left:12px;bottom:12px;z-index:60;background:#6c4cf5;color:#fff!important;border-radius:99px;padding:8px 14px;font:700 14px system-ui;text-decoration:none;box-shadow:0 4px 14px rgba(0,0,0,.25)}' +
      'nav.tabs a.tt-lock{opacity:.5;cursor:not-allowed}nav.tabs a.tt-done::after{content:" ✓";color:#1b9e5a;font-weight:700}' +
      '.tt-toast{position:fixed;left:50%;top:18px;transform:translateX(-50%);z-index:200;background:#1f2140;color:#fff;padding:10px 16px;border-radius:12px;font:600 14px system-ui;box-shadow:0 6px 24px rgba(0,0,0,.35);max-width:92vw}' +
      '.tt-bar{position:fixed;left:0;right:0;bottom:0;z-index:70;background:#fff;border-top:3px solid #6c4cf5;box-shadow:0 -6px 20px rgba(0,0,0,.15);padding:10px 14px;font:15px system-ui;color:#1f2140}' +
      '@media(prefers-color-scheme:dark){.tt-bar{background:#1d1f3a;color:#eceefb}}' +
      '.tt-bar-in{max-width:900px;margin:0 auto;display:flex;align-items:center;gap:12px;flex-wrap:wrap}.tt-track{flex:1;min-width:120px;height:12px;border-radius:9px;background:#e6e4f7;overflow:hidden}.tt-track i{display:block;height:100%;width:0;background:linear-gradient(90deg,#6c4cf5,#ff5fa2);transition:width .5s}' +
      '.tt-btn{background:linear-gradient(90deg,#6c4cf5,#ff5fa2);color:#fff!important;border:0;border-radius:10px;padding:8px 14px;font:700 15px system-ui;text-decoration:none;cursor:pointer;display:inline-block}.tt-btn.sec{background:none;color:inherit!important;border:1px solid #bbb}' +
      '.tt-res{border-radius:14px;padding:12px 14px;margin:12px 0;font:15px/1.5 system-ui;border:2px solid}.tt-res.pass{background:#e8f8ef;border-color:#1b9e5a;color:#0d5c34}.tt-res.fail{background:#fff4e5;border-color:#f59e0b;color:#7a4a00}.tt-res.wait{background:#eef;border-color:#99f;color:#335}' +
      '.tt-res h3{margin:0 0 4px;font-size:18px}.tt-res .acts{display:flex;gap:8px;flex-wrap:wrap;margin-top:8px}.tt-chip{display:inline-block;margin-left:8px;background:#e8f8ef;color:#0d5c34;border:1px solid #1b9e5a;border-radius:99px;padding:0 10px;font:700 12px system-ui}';
    document.head.appendChild(s);
  }
  function toast(msg) {
    css(); var t = document.createElement('div'); t.className = 'tt-toast'; t.textContent = msg; document.body.appendChild(t); setTimeout(function () { t.remove(); }, 3800);
  }
  function whenDom(fn) { if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', fn); else fn(); }
  T.toast = toast;

  /* ----- chặn trang bài còn khoá ----- */
  T.guard = function (setId) {
    var page = (location.pathname.split('/').pop() || '').replace(/\.html$/, ''), id = setId + '|' + page, shown = false;
    function show() { if (shown) return; shown = true; document.documentElement.style.visibility = ''; }
    setTimeout(show, 7000);   /* mạng chậm: cho mở trang (máy chủ vẫn từ chối ghi điểm của bước khoá) */
    T.state(false).then(function (st) {
      if (!T.lockedBy(st, id)) return ready(st);
      return T.state(true).then(function (st2) {
        var by = T.lockedBy(st2, id);
        if (by) { location.replace(ROOT + 'thuthach.html?locked=' + encodeURIComponent(by)); return; }
        ready(st2);
      });
    }).catch(show);
    function ready(st) {
      show();
      var loc = T.locate(st, id); if (!loc) return;
      T.meta(loc.p.id).then(function (m) { whenDom(function () { init(st, id, loc, m); }); }).catch(function () {});
    }
  };

  function init(st, id, loc, m) {
    css();
    var step = m.steps[id], done = hop(loc.p.done, id), setId = id.split('|')[0], total = loc.p.steps.length, nd = Object.keys(loc.p.done).length;
    /* thanh tab: khoá các trang chưa mở; nút Trang chủ -> Lộ trình */
    [].forEach.call(document.querySelectorAll('nav.tabs a'), function (a) {
      var h = a.getAttribute('href') || '';
      if (/index\.html/.test(h)) { a.setAttribute('href', ROOT + 'thuthach.html'); a.textContent = '🗺 Lộ trình'; return; }
      if (h.indexOf('/') >= 0) return;
      var sid = setId + '|' + h.replace(/\.html$/, ''), ll = T.locate(st, sid); if (!ll) return;
      var by = T.lockedBy(st, sid);
      if (by) { a.classList.add('tt-lock'); a.textContent = '🔒 ' + a.textContent; a.addEventListener('click', function (e) { e.preventDefault(); toast('🔒 Hãy hoàn thành "' + ((m.steps[by] || {}).title || 'bước trước') + '" trước nhé!'); }); }
      else if (hop(ll.p.done, sid)) a.classList.add('tt-done');
    });
    var hud = document.createElement('a'); hud.className = 'tt-hud'; hud.href = ROOT + 'thuthach.html'; hud.textContent = '🗺 Lộ trình · ' + Math.round(nd * 100 / total) + '%'; document.body.appendChild(hud);
    var next = loc.p.steps[loc.i + 1] ? m.steps[loc.p.steps[loc.i + 1]] : null;
    function nextHref() { return next ? ROOT + next.url : ROOT + 'thuthach.html'; }
    if (!step) return;
    if (step.kind === 'theory') theory(st, id, loc, step, done, nextHref(), next, hud);
    else practice(st, id, loc, step, done, nextHref(), next);
  }

  /* ----- đồng hồ đọc lý thuyết ----- */
  function theory(st, id, loc, step, done, href, next, hud) {
    var need = Math.round((+loc.p.cfg.theory_min || 0) * 60), key = 'gn_tts_' + U.username + '_' + id, sec = done ? need : (+lsGet(key) || 0), fin = done, sending = false, last = Date.now();
    var bar = document.createElement('div'); bar.className = 'tt-bar';
    bar.innerHTML = '<div class="tt-bar-in"><b>📖 Đọc bài</b><span class="tt-time"></span><div class="tt-track"><i></i></div><span class="tt-msg"></span></div>';
    document.body.appendChild(bar); document.body.style.paddingBottom = '70px';
    var tm = bar.querySelector('.tt-time'), fill = bar.querySelector('.tt-track i'), msg = bar.querySelector('.tt-msg');
    function render() {
      tm.textContent = fin ? 'Đã đọc xong' : mmss(sec) + ' / ' + mmss(need);
      fill.style.width = (need ? Math.min(100, sec * 100 / need) : 100) + '%';
    }
    function complete(extra) {
      fin = true; render();
      msg.innerHTML = (extra || '<b style="color:#1b9e5a">✔ Hoàn thành phần Lý thuyết!</b> ') + '<a class="tt-btn" href="' + esc(href) + '">' + (next ? 'Làm tiếp: ' + esc(next.title) + ' ▶' : '🗺 Về lộ trình') + '</a>';
    }
    if (done) { complete('<b style="color:#1b9e5a">✔ Em đã đọc xong phần này.</b> '); return; }
    render();
    A.api('tt_theory', { step: id, event: 'start' }).catch(function () {});
    ['mousemove', 'scroll', 'keydown', 'touchstart', 'click', 'wheel'].forEach(function (ev) { window.addEventListener(ev, function () { last = Date.now(); }, { passive: true }); });
    var n = 0, timer = setInterval(function () {
      if (fin) { clearInterval(timer); return; }
      if (!document.hidden && Date.now() - last < 45000) {
        sec++; render(); if (++n % 5 === 0) lsSet(key, String(sec));
        if (sec >= need && !sending) {
          sending = true;
          A.api('tt_theory', { step: id, event: 'done' }).then(function (r) {
            if (r.state) T.save(r.state);
            complete(); hud.textContent = '🗺 Lộ trình';
          }).catch(function (e) { sending = false; if (e.server) { msg.textContent = e.message; sec = Math.max(0, need - 10); } });
        }
      } else if (!document.hidden) { msg.textContent = 'Hãy cuộn hoặc chạm vào trang để tiếp tục tính giờ nhé 👆'; }
      if (sec && sec % 2 === 0 && !document.hidden && Date.now() - last < 45000) msg.textContent = '';
    }, 1000);
    window.addEventListener('pagehide', function () { lsSet(key, String(sec)); });
  }

  /* ----- luyện tập / kiểm tra: báo kết quả sau khi nộp ----- */
  /* ----- lưu bài làm dở (trên máy này, 7 ngày): mở lại đúng chỗ đang làm ----- */
  function draft(id) {
    var key = 'gn_ttd_' + U.username + '|' + id, submitted = false, tm = 0;
    function qsa(sel, root) { return [].slice.call((root || document).querySelectorAll(sel)); }
    function collect() {
      var o = {}, any = false;
      qsa('.q[data-id]').forEach(function (q) {
        var arr = [];
        qsa('input,select,textarea', q).forEach(function (c, i) {
          if (c.type === 'radio' || c.type === 'checkbox') { if (c.checked) arr.push([i, 1]); }
          else if (c.type !== 'button' && c.type !== 'submit' && c.value) arr.push([i, c.value]);
        });
        if (arr.length) { o[q.getAttribute('data-id')] = arr; any = true; }
      });
      return any ? o : null;
    }
    function save() {
      if (submitted) return;
      var o = collect();
      try { if (o) localStorage.setItem(key, JSON.stringify({ t: Date.now(), a: o })); else localStorage.removeItem(key); } catch (e) {}
    }
    function sched() { clearTimeout(tm); tm = setTimeout(save, 700); }
    function restore() {
      var d = null; try { d = JSON.parse(localStorage.getItem(key) || 'null'); } catch (e) {}
      if (!d || !d.a || Date.now() - d.t > 7 * 86400000) { try { localStorage.removeItem(key); } catch (e) {} return; }
      if (window.__quiz && window.__quiz.isSubmitted && window.__quiz.isSubmitted()) return;
      var n = 0;
      Object.keys(d.a).forEach(function (qid) {
        var q = document.querySelector('.q[data-id="' + qid + '"]'); if (!q) return;
        var ctrls = qsa('input,select,textarea', q);
        d.a[qid].forEach(function (it) {
          var c = ctrls[it[0]]; if (!c) return;
          if (c.type === 'radio' || c.type === 'checkbox') { if (!c.checked) c.click(); }
          else { c.value = it[1]; c.dispatchEvent(new Event('input', { bubbles: true })); c.dispatchEvent(new Event('change', { bubbles: true })); }
          n++;
        });
      });
      if (n) toast('↩ Đã khôi phục ' + Object.keys(d.a).length + ' câu em làm dở trước đó.');
    }
    document.addEventListener('input', sched, true); document.addEventListener('change', sched, true);
    document.addEventListener('quiz:submitted', function () { submitted = true; clearTimeout(tm); try { localStorage.removeItem(key); } catch (e) {} });
    whenDom(function () { setTimeout(restore, 900); });
  }

  function practice(st, id, loc, step, done, href, next) {
    var need = T.need(loc.p.cfg, step.kind), best = loc.p.done[id];
    if (done) {
      var sub = document.querySelector('header .sub') || document.querySelector('header h1');
      if (sub) { var c = document.createElement('span'); c.className = 'tt-chip'; c.textContent = '✔ Đã qua' + (best ? ' · tốt nhất ' + best + '%' : ''); sub.appendChild(c); }
    }
    if (step.kind !== 'theory') draft(id);
    function onSubmitted(pct0) {
      var pct = pct0;
      if (pct === undefined) { var t = window.__quiz && window.__quiz.tally ? window.__quiz.tally() : null; if (!t || !t.total) return; pct = Math.round(t.ok / t.total * 1000) / 10; }
      var pass = pct >= need, nodes = [];
      function put(cls, html, acts) {
        var hosts = [document.getElementById('resultBox'), document.getElementById('result')].filter(Boolean);
        if (!hosts.length) {   /* trang không có khung kết quả (IELTS Reading): hiện thanh nổi cuối trang */
          var fx = document.getElementById('tt-fixed');
          if (!fx) { fx = document.createElement('div'); fx.id = 'tt-fixed'; fx.style.cssText = 'position:fixed;left:50%;bottom:14px;transform:translateX(-50%);z-index:99999;width:min(560px,94vw);max-height:80vh;overflow:auto;box-shadow:0 10px 40px rgba(0,0,0,.35);border-radius:16px'; document.body.appendChild(fx); }
          hosts = [fx];
        }
        if (!nodes.length) hosts.forEach(function (h) { var d = document.createElement('div'); d.className = 'tt-res'; h.appendChild(d); nodes.push(d); });
        nodes.forEach(function (d) { d.className = 'tt-res ' + cls; d.innerHTML = html + (acts ? '<div class="acts">' + acts + '</div>' : ''); });
        [].forEach.call(document.querySelectorAll('.tt-res [data-tt=again]'), function (b) { b.onclick = function () { location.reload(); }; });
      }
      var again = '<button class="tt-btn" data-tt="again" type="button">🔁 Làm lại</button><a class="tt-btn sec" href="' + ROOT + 'thuthach.html">🗺 Về lộ trình</a>';
      if (!pass) {
        put('fail', '<h3>Cố lên nào! 💪</h3>Em đạt <b>' + pct + '%</b>, cần từ <b>' + need + '%</b> để mở bước tiếp theo. Hãy xem lại đáp án bên dưới rồi làm lại nhé.', again);
        T.state(true).catch(function () {}); return;
      }
      put('wait', '<h3>Đang ghi nhận kết quả…</h3>');
      var tries = 0;
      (function poll() {
        T.state(true).then(function (s) {
          var l2 = T.locate(s, id);
          if (l2 && hop(l2.p.done, id)) fin(s, l2); else if (++tries < 5) setTimeout(poll, 1500); else fin(s, l2, true);
        }).catch(function () { if (++tries < 5) setTimeout(poll, 1500); else fin(null, null, true); });
      })();
      function fin(s, l2, soft) {
        var stars = T.stars(pct, need), star = stars ? new Array(stars + 1).join('⭐') : '';
        put('pass', '<h3>Tuyệt vời! 🎉 ' + star + '</h3>Em đạt <b>' + pct + '%</b> (cần ≥ ' + need + '%).' + (next ? ' Bước tiếp theo đã mở: <b>' + esc(next.title) + '</b>.' : ' Em đã hoàn thành bước cuối cùng!') + (soft ? ' <small>(đang cập nhật, nếu bước sau chưa mở hãy tải lại lộ trình)</small>' : ''),
          '<a class="tt-btn" href="' + esc(href) + '">' + (next ? 'Làm tiếp ▶' : '🏆 Xem lộ trình') + '</a><a class="tt-btn sec" href="' + ROOT + 'thuthach.html">🗺 Về lộ trình</a>');
      }
    }
    document.addEventListener('quiz:submitted', function () { onSubmitted(); });
    window.addEventListener('gn:result', function (e) { if (e.detail && e.detail.pct !== undefined) onSubmitted(+e.detail.pct); });
  }

  if (A._ttSet) T.guard(A._ttSet);
})();
