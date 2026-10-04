/* Cầu nối giữa các trang IELTS Reading (viết sẵn) và hệ thống đăng nhập chung.
   - Điền tên/lớp từ tài khoản, ẩn ô nhập.
   - Chuyển các lời gọi save_result / save_result_bytype / log_event của trang sang action chung (grade_*) + gắn token, mã bộ bài.
   Cấu hình: window.GN_RD = {set:'ielts-rd-test01', page:'Test1_Reading', kind:'full'|'COMPLETION'...}. */
(function () {
  var C = window.GN_RD || {}, URL = window.GN_URL;
  function secs(t) { var m = /(\d+)\s*phút\s*(\d+)\s*giây/.exec(String(t || '')); return m ? (+m[1]) * 60 + (+m[2]) : 0; }
  function map(body) {
    var d; try { d = JSON.parse(body); } catch (e) { return null; }
    if (!d || !/^(save_result|save_result_bytype|log_event)$/.test(d.action)) return null;
    var au = window.GNAuth && GNAuth.get(), o = { token: au && au.token, set_id: C.set, page_id: C.page, ts: d.timestamp || new Date().toISOString() };
    if (d.action === 'log_event') {
      o.action = 'grade_rd_event'; o.event = d.eventType || ''; o.detail = d.detail || ''; o.elapsed = d.elapsed || '';
    } else {
      var sc = +d.score || 0, tot = +d.total || 0, pct = tot ? Math.round(sc / tot * 1000) / 10 : 0;
      o.action = 'grade_save_result'; o.mode = 'ielts-reading'; o.score = sc; o.total = tot; o.pct = pct; o.score10 = tot ? Math.round(sc / tot * 100) / 10 : 0;
      o.time_spent = secs(d.timeTaken); o.tab_switch = +d.tabViol || 0; o.blur = +d.focusViol || 0; o.fullscreen_exit = +d.fsViol || 0; o.audio_plays = 0;
      o.answers = 'Band ' + (d.band || '?') + ' | ' + (d.details || '');
    }
    return JSON.stringify(o);
  }
  var f0 = window.fetch;
  if (f0) window.fetch = function (u, opt) {
    try { if (String(u) === URL && opt && typeof opt.body === 'string') { var b = map(opt.body); if (b) { opt.body = b; opt.keepalive = true; } else if (/"action":"(save_|log_)/.test(opt.body)) return Promise.resolve(); } } catch (e) {}
    return f0.apply(this, arguments);
  };
  var b0 = navigator.sendBeacon && navigator.sendBeacon.bind(navigator);
  /* Blob không đọc đồng bộ được → thay beacon bằng fetch keepalive (qua map ở trên). */
  if (b0) navigator.sendBeacon = function (u, data) {
    if (String(u) === URL && window.Blob && data instanceof Blob) {
      var fr = new FileReader();
      fr.onload = function () { try { window.fetch(u, { method: 'POST', mode: 'no-cors', headers: { 'Content-Type': 'text/plain;charset=UTF-8' }, body: fr.result, keepalive: true }); } catch (e) {} };
      fr.readAsText(data); return true;
    }
    return b0(u, data);
  };
  document.addEventListener('DOMContentLoaded', function () {
    var au = window.GNAuth && GNAuth.get(); if (!au) return;
    var n = document.getElementById('stuName'), c = document.getElementById('stuClass');
    if (n) n.value = au.user.name || au.user.username;
    if (c) c.value = au.user.cls || 'IELTS';
    var box = document.querySelector('#nameOverlay .name-box');
    if (box) {
      [].forEach.call(box.querySelectorAll('label,input'), function (e) { e.style.display = 'none'; });
      var p = box.querySelector('.sub');
      if (p) p.innerHTML += '<br>Xin chào <b>' + String(au.user.name || '').replace(/</g, '&lt;') + '</b>' + (au.user.cls ? ' · lớp ' + au.user.cls : '') + '. ' +
        (au.user.role === 'student' ? 'Kết quả sẽ được ghi vào tài khoản của bạn.' : 'Bạn đang làm thử — kết quả không được lưu.');
    }
    var back = document.createElement('a'); back.href = (window.GN_ROOT || '') + 'index.html'; back.textContent = '← Trang chủ';
    back.style.cssText = 'position:fixed;left:8px;bottom:8px;z-index:5;font:12px sans-serif;background:#fff;border:1px solid #ccd;border-radius:8px;padding:4px 8px;text-decoration:none;color:#345;opacity:.85';
    document.body.appendChild(back);
  });
})();
