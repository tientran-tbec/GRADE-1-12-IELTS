/* Đăng nhập phía trình duyệt: lưu phiên, gọi API Apps Script, bảo vệ trang. */
(function () {
  var KEY = 'gn_auth';
  function ls(k, v) { try { if (v === undefined) return localStorage.getItem(k); if (v === null) localStorage.removeItem(k); else localStorage.setItem(k, v); } catch (e) {} return null; }
  function load() { try { return JSON.parse(ls(KEY) || 'null'); } catch (e) { return null; } }
  function tokenExp(t) {
    try { var p = String(t).split('.')[0].replace(/-/g, '+').replace(/_/g, '/'); while (p.length % 4) p += '='; return JSON.parse(decodeURIComponent(escape(atob(p)))).e || 0; } catch (e) { return 0; }
  }
  var ROOT = window.GN_ROOT || '';
  function deviceId() {
    var d = ls('gn_dev');
    if (!d) { d = (window.crypto && crypto.randomUUID ? crypto.randomUUID() : String(Math.random()).slice(2) + Date.now()); ls('gn_dev', d); }
    return d;
  }
  var ROLE = { admin: 'Quản trị viên', teacher: 'Giáo viên', student: 'Học sinh' };
  var A = window.GNAuth = {
    ROLE: ROLE,
    get: function () { var s = load(); return s && s.token && tokenExp(s.token) > Date.now() ? s : null; },
    set: function (token, user) { ls(KEY, JSON.stringify({ token: token, user: user })); try { window.dispatchEvent(new CustomEvent('gn-user')); } catch (e) {} },
    clear: function () { ls(KEY, null); ls('gn_ping', null); try { Object.keys(localStorage).forEach(function (k) { if (k.indexOf('gn_adm_') === 0 || k.indexOf('gn_ai_') === 0) localStorage.removeItem(k); }); } catch (e) {} },
    user: function () { var s = A.get(); return s ? s.user : null; },
    loginUrl: function (next) { return ROOT + 'login.html' + (next ? '?next=' + encodeURIComponent(next) : ''); },
    logout: function () {
      var s = load(); A.clear();
      var go = function () { location.href = ROOT + 'login.html'; };
      if (s && window.GN_URL) { try { fetch(window.GN_URL, { method: 'POST', headers: { 'Content-Type': 'text/plain;charset=UTF-8' }, body: JSON.stringify({ action: 'auth_logout', token: s.token }) }).then(go, go); setTimeout(go, 1500); return; } catch (e) {} }
      go();
    },
    sessionLost: function (msg) { A.clear(); location.replace(ROOT + 'login.html?msg=' + encodeURIComponent(msg || 'Phiên đăng nhập đã kết thúc. Hãy đăng nhập lại.')); },
    /* Học sinh chỉ vào được bài đã được giao cho lớp mình. */
    allowed: function (setId) { var s = A.get(); if (!s) return false; var u = s.user; if (u.role !== 'student') return true; return !!(u.sets && u.sets.indexOf(setId) >= 0) && !A.overdue(setId); },
    /* Hạn nộp (yyyy-mm-dd, giờ VN) của một bộ bài; '' nếu không có. */
    assigned: function (setId) { var s = A.get(); if (!s) return false; var u = s.user; return u.role !== 'student' || !!(u.sets && u.sets.indexOf(setId) >= 0); },
    due: function (setId) { var s = A.get(); return s && s.user.due && s.user.due[setId] || ''; },
    overdue: function (setId) { var d = A.due(setId); return !!d && new Date(Date.now() + 7 * 3600000).toISOString().slice(0, 10) > d; },
    unread: 0,
    /* Hiển thị thời gian: chuỗi ISO (…Z) → dd/MM/yyyy HH:mm:ss giờ VN; chuỗi khác giữ nguyên. */
    t: function (x) {
      if (x == null || x === '') return '';
      var m = /^(\d{4})-(\d{2})-(\d{2})T(\d{2}):(\d{2}):(\d{2})(?:\.\d+)?Z$/.exec(String(x)); if (!m) return String(x);
      var d = new Date(Date.UTC(+m[1], +m[2] - 1, +m[3], +m[4], +m[5], +m[6]) + 7 * 3600000), z = function (n) { return (n < 10 ? '0' : '') + n; };
      return z(d.getUTCDate()) + '/' + z(d.getUTCMonth() + 1) + '/' + d.getUTCFullYear() + ' ' + z(d.getUTCHours()) + ':' + z(d.getUTCMinutes()) + ':' + z(d.getUTCSeconds());
    },
    requireSet: function (setId) {
      if (!A.get() || A.allowed(setId)) return true;
      document.documentElement.style.visibility = 'hidden'; location.replace(ROOT + 'index.html?denied=1'); return false;
    },
    /* Bắt buộc đăng nhập (và đúng vai trò). Gọi sớm trong <head>. */
    require: function (roles) {
      var s = A.get();
      if (!s) { document.documentElement.style.visibility = 'hidden'; location.replace(A.loginUrl(location.href)); return null; }
      if (s.user.mustChange && !/login\.html/.test(location.pathname)) { document.documentElement.style.visibility = 'hidden'; location.replace(ROOT + 'login.html?change=1&next=' + encodeURIComponent(location.href)); return null; }
      if (roles && roles.indexOf(s.user.role) < 0) { document.documentElement.style.visibility = 'hidden'; location.replace(ROOT + 'index.html'); return null; }
      return s;
    },
    /* Gọi API. Trả về Promise<object>; lỗi → reject(Error(message)). */
    api: function (action, data) {
      var s = load(), body = Object.assign({ action: action, token: s && s.token, device: deviceId() }, data || {});
      return fetch(window.GN_URL, { method: 'POST', headers: { 'Content-Type': 'text/plain;charset=UTF-8' }, body: JSON.stringify(body) })
        .then(function (r) { return r.json(); })
        .then(function (j) {
          if (!j.ok) {
            var e = new Error(j.error || 'Có lỗi xảy ra'); e.server = true; e.code = j.code;
            if (action !== 'auth_login' && (j.code === 'session' || /không tồn tại hoặc đã bị khoá/.test(e.message))) A.sessionLost(e.message);
            throw e;
          }
          return j;
        });
    },
    /* Thanh người dùng: gắn vào phần tử (selector hoặc node). */
    chip: function (where, opts) {
      opts = opts || {};
      var s = A.get(), host = typeof where === 'string' ? document.querySelector(where) : where;
      if (!s || !host) return;
      if (!document.getElementById('gn-bell-css')) { var st = document.createElement('style'); st.id = 'gn-bell-css'; st.textContent = '.gn-bell{text-decoration:none!important}.gn-n{display:none;background:#e11d48;color:#fff;border-radius:9px;font-size:11px;font-weight:700;padding:0 6px;margin-left:3px;line-height:16px}'; document.head.appendChild(st); }
      var u = s.user, d = document.createElement('div');
      d.className = 'gn-chip';
      var links = '';
      if (u.role === 'admin' || u.role === 'teacher') links += '<a href="' + ROOT + 'admin.html">Quản trị</a>';
      var bell = u.role === 'student' ? ROOT + 'me.html#gopy' : ROOT + 'admin.html#gopy';
      links += '<a class="gn-bell" href="' + bell + '" title="Góp ý / tin nhắn">💬 Góp ý<b class="gn-n"></b></a>';
      links += '<a href="' + ROOT + 'me.html">Điểm của tôi</a><a href="' + ROOT + 'login.html?change=1">Đổi mật khẩu</a><a href="#" data-gn="out">Đăng xuất</a>';
      d.innerHTML = '<span class="gn-name">👤 ' + esc(u.name) + ' <small>' + (u.cls ? esc(u.cls) + ' · ' : '') + ROLE[u.role] + '</small></span><span class="gn-links">' + links + '</span>';
      d.querySelector('[data-gn=out]').onclick = function (e) { e.preventDefault(); A.logout(); };
      host.appendChild(d); A._bell();
    },
    _bell: function () {
      var n = A.unread || 0;
      [].forEach.call(document.querySelectorAll('.gn-bell .gn-n'), function (b) { b.textContent = n > 99 ? '99+' : n; b.style.display = n ? 'inline-block' : 'none'; });
    },
    /* Kiểm tra phiên với máy chủ (nền); phiên hỏng → đăng nhập lại. */
    verify: function (onUpdate) {
      if (!A.get() || !window.GN_URL) return;
      var MIN = 120000, EVERY = 180000;   /* không hỏi máy chủ quá thường xuyên: chuyển trang liên tục vẫn chỉ hỏi ≤ 1 lần / 2 phút */
      var tick = function () {
        if (document.hidden && A._t) return;
        var s0 = load(), now = Date.now(), c = null;
        try { c = JSON.parse(ls('gn_ping') || 'null'); } catch (e) {}
        if (c && s0 && s0.user.role === 'student' && c.u === s0.user.username && now - c.t < MIN) {   /* chỉ học sinh được giảm tần suất; giáo viên / admin luôn cập nhật quyền ngay khi mở trang */
          A.unread = +c.n || 0; A._bell(); try { window.dispatchEvent(new CustomEvent('gn-unread', { detail: A.unread })); } catch (e) {}
          return;
        }
        if (A._busy) return; A._busy = true;
        A.api('auth_ping').then(function (j) {
          A._busy = false;
          var s = load(); if (!s) return; var sig = function (u) { return JSON.stringify(u.sets || null) + JSON.stringify(u.due || null) + u.cls + JSON.stringify(u.perms || null) + JSON.stringify(u.ranks || null) + (u.ai ? 1 : 0); }, before = sig(s.user);
          A.set(s.token, j.user);
          A.unread = +j.unread || 0; A._bell(); try { window.dispatchEvent(new CustomEvent('gn-unread', { detail: A.unread })); } catch (e) {}
          ls('gn_ping', JSON.stringify({ u: j.user.username, t: Date.now(), n: A.unread }));
          if (onUpdate && sig(j.user) !== before) onUpdate(j.user);
        }).catch(function () { A._busy = false; });
      };
      A._tick = tick; A.refresh = function () { ls('gn_ping', null); tick(); };
      tick(); A._t = setInterval(tick, EVERY);
      document.addEventListener('visibilitychange', function () { if (!document.hidden) tick(); });
    }
  };
  function esc(s) { return String(s == null ? '' : s).replace(/[&<>"]/g, function (c) { return { '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' }[c]; }); }
  A.esc = esc;
})();

/* Khung tra từ / dịch (.dict-popup) kéo thả được: kéo ở dải trên cùng ("⠿ Kéo để di chuyển") hoặc phần viền khung.
   Vị trí đã kéo được nhớ cho các lần dịch sau. Dùng chung cho mọi trang (bài luyện tập, kiểm tra, IELTS). */
(function () {
  var st = document.createElement('style');
  st.textContent = '.dict-popup{touch-action:none;padding-top:22px!important}.dict-popup::before{content:"⠿  Kéo để di chuyển";position:absolute;left:0;right:30px;top:0;height:22px;line-height:22px;padding-left:12px;font-size:11px;opacity:.55;cursor:grab;user-select:none;-webkit-user-select:none}.dict-popup.gn-moving::before{cursor:grabbing}.dict-popup .dict-body{touch-action:pan-y}';
  (document.head || document.documentElement).appendChild(st);
  var pos = null, drag = null;
  function clamp(el, x, y) { var w = el.offsetWidth, h = el.offsetHeight; return [Math.min(Math.max(4, x), Math.max(4, innerWidth - w - 4)), Math.min(Math.max(4, y), Math.max(4, innerHeight - Math.min(h, 60) - 4))]; }
  function place(el, x, y) { var c = clamp(el, x, y); el.style.left = c[0] + 'px'; el.style.top = c[1] + 'px'; el.style.right = 'auto'; el.style.bottom = 'auto'; return c; }
  document.addEventListener('pointerdown', function (e) {
    var el = e.target && e.target.closest && e.target.closest('.dict-popup'); if (!el) return;
    var r = el.getBoundingClientRect();
    if (e.target !== el || e.button > 0) return;   /* chỉ kéo khi bấm vào dải trên / viền, không phải nút hay chữ */
    drag = { el: el, dx: e.clientX - r.left, dy: e.clientY - r.top, id: e.pointerId };
    el.classList.add('gn-moving'); try { el.setPointerCapture(e.pointerId); } catch (x) {}
    e.preventDefault();
  }, true);
  document.addEventListener('pointermove', function (e) { if (drag && e.pointerId === drag.id) place(drag.el, e.clientX - drag.dx, e.clientY - drag.dy); });
  function end(e) { if (!drag || e.pointerId !== drag.id) return; var r = drag.el.getBoundingClientRect(); pos = [r.left, r.top]; drag.el.classList.remove('gn-moving'); drag = null; }
  document.addEventListener('pointerup', end); document.addEventListener('pointercancel', end);
  function watch() {
    new MutationObserver(function (list) {
      if (!pos) return;
      list.forEach(function (m) { [].forEach.call(m.addedNodes, function (n) { if (n.nodeType === 1 && n.classList.contains('dict-popup')) place(n, pos[0], pos[1]); }); });
    }).observe(document.body, { childList: true });
  }
  if (document.body) watch(); else document.addEventListener('DOMContentLoaded', watch);
})();
