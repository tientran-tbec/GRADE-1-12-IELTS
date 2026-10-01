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
    set: function (token, user) { ls(KEY, JSON.stringify({ token: token, user: user })); },
    clear: function () { ls(KEY, null); },
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
    allowed: function (setId) { var s = A.get(); if (!s) return false; var u = s.user; if (u.role !== 'student') return true; return !!(u.sets && u.sets.indexOf(setId) >= 0); },
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
      var u = s.user, d = document.createElement('div');
      d.className = 'gn-chip';
      var links = '';
      if (u.role === 'admin' || u.role === 'teacher') links += '<a href="' + ROOT + 'admin.html">Quản trị</a>';
      links += '<a href="' + ROOT + 'me.html">Điểm của tôi</a><a href="' + ROOT + 'login.html?change=1">Đổi mật khẩu</a><a href="#" data-gn="out">Đăng xuất</a>';
      d.innerHTML = '<span class="gn-name">👤 ' + esc(u.name) + ' <small>' + (u.cls ? esc(u.cls) + ' · ' : '') + ROLE[u.role] + '</small></span><span class="gn-links">' + links + '</span>';
      d.querySelector('[data-gn=out]').onclick = function (e) { e.preventDefault(); A.logout(); };
      host.appendChild(d);
    },
    /* Kiểm tra phiên với máy chủ (nền); phiên hỏng → đăng nhập lại. */
    verify: function (onUpdate) {
      if (!A.get() || !window.GN_URL) return;
      var tick = function () {
        if (document.hidden && A._t) return;
        A.api('auth_ping').then(function (j) {
          var s = load(); if (!s) return; var before = JSON.stringify(s.user.sets || null) + s.user.cls;
          A.set(s.token, j.user);
          if (onUpdate && (JSON.stringify(j.user.sets || null) + j.user.cls) !== before) onUpdate(j.user);
        }).catch(function () {});
      };
      tick(); A._t = setInterval(tick, 60000);
      document.addEventListener('visibilitychange', function () { if (!document.hidden) tick(); });
    }
  };
  function esc(s) { return String(s == null ? '' : s).replace(/[&<>"]/g, function (c) { return { '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' }[c]; }); }
  A.esc = esc;
})();
