/* Thành phần dùng chung của bảng điều khiển Thử thách. */
(function () {
  'use strict';
  var E = function (s) { return String(s == null ? '' : s).replace(/[&<>"]/g, function (c) { return { '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' }[c]; }); };
  var MEDAL = ['🥇', '🥈', '🥉'];
  var GRAD = ['linear-gradient(135deg,#6c4cf5,#ff5fa2)', 'linear-gradient(135deg,#0ea5e9,#22c55e)', 'linear-gradient(135deg,#f59e0b,#ef4444)', 'linear-gradient(135deg,#14b8a6,#6366f1)'];
  var ICON = ['🚀', '🛸', '🪐', '🌟'];
  function ring(pct) {
    var C = 2 * Math.PI * 32, off = C * (1 - Math.max(0, Math.min(100, pct)) / 100);
    return '<div class="hm-ring"><svg viewBox="0 0 78 78"><circle class="bg" cx="39" cy="39" r="32" fill="none" stroke-width="8"/><circle class="fg" cx="39" cy="39" r="32" fill="none" stroke-width="8" stroke-dasharray="' + C.toFixed(1) + '" stroke-dashoffset="' + off.toFixed(1) + '"/></svg><b>' + Math.round(pct) + '%</b></div>';
  }
  function secTxt(s) { return s < 90 ? s + ' giây/bước' : (s / 60).toFixed(1).replace('.0', '') + ' phút/bước'; }
  function list(arr, fmt, empty) {
    if (!arr || !arr.length) return '<div class="none">' + empty + '</div>';
    return '<ol>' + arr.map(function (r, i) { return '<li><i>' + MEDAL[i] + '</i><span><b>' + E(r.n) + '</b><small>' + (r.c ? 'Lớp ' + E(r.c) + ' · ' : '') + '<em>' + fmt(r.v) + '</em></small></span></li>'; }).join('') + '</ol>';
  }
  /* bảng vinh danh toàn thời gian: 3 cột × 3 người */
  function fame(f, fastMin) {
    f = f || {};
    return '<div class="hm-fame">' +
      '<div class="hm-f a"><h5>🏆 Thành tích cao nhất<small>Tổng số ⭐ đạt được</small></h5>' + list(f.stars, function (v) { return v + ' ⭐'; }, 'Chưa có ai — cơ hội của em!') + '</div>' +
      '<div class="hm-f b"><h5>💪 Làm nhiều nhất<small>Số bước đã chinh phục</small></h5>' + list(f.count, function (v) { return v + ' bước'; }, 'Chưa có ai — cơ hội của em!') + '</div>' +
      '<div class="hm-f c"><h5>⚡ Nhanh nhất<small>Thời gian làm trung bình mỗi bước (từ ' + (fastMin || 8) + ' bước)</small></h5>' + list(f.fast, secTxt, 'Chưa ai đủ ' + (fastMin || 8) + ' bước.') + '</div></div>';
  }
  window.TTDash = { E: E, ring: ring, fame: fame, secTxt: secTxt, GRAD: GRAD, ICON: ICON, MEDAL: MEDAL };
})();
