/* Trang chủ học sinh ở chế độ THỬ THÁCH: mỗi lộ trình một khung lối tắt (vào thẳng bước đang làm), top 5 lớp, bảng vinh danh. */
(function () {
  'use strict';
  var A = window.GNAuth, D = window.TTDash, E = D.E, host = document.getElementById('home'), U = A.user();
  function esc(s) { return E(s); }
  function hero(o) {
    var hi = o.streak > 0 ? '<span class="hm-chip fire">🔥 ' + o.streak + ' ngày liên tiếp</span>' : '<span class="hm-chip off">🔥 Bắt đầu chuỗi ngày học nào!</span>';
    var nudge = o.today ? 'Hôm nay em đã học rồi — giữ vững phong độ nhé! 💪' : (o.streak > 0 ? 'Hôm nay em chưa học. Làm xong 1 bước để giữ chuỗi 🔥 nhé!' : 'Làm xong 1 bước hôm nay để nhận ngọn lửa đầu tiên!');
    var goal = '', warn = '';
    if (o.goal > 0) {
      var pc = Math.min(100, Math.round(o.todayDone * 100 / o.goal)), okg = o.todayDone >= o.goal;
      goal = '<div class="hm-goal' + (okg ? ' ok' : '') + '"><b>🎯 Mục tiêu hôm nay</b><div class="gbar"><i style="width:' + pc + '%"></i></div><b>' + Math.min(o.todayDone, o.goal) + '/' + o.goal + ' bước' + (okg ? ' 🎉' : '') + '</b></div>';
    }
    if (!o.today && o.streak > 0 && new Date().getHours() >= 17) warn = '<div class="hm-warn">⏰ Sắp mất chuỗi ' + o.streak + ' ngày! Làm xong 1 bước trước nửa đêm để giữ ngọn lửa 🔥</div>';
    return '<div class="hm-hero"><div class="grow"><h2>Chào ' + esc(o.name || U.name) + '! 👋</h2><p>' + nudge + '</p></div>' + hi + (o.bestStreak > o.streak ? '<span class="hm-chip">🏅 Kỷ lục ' + o.bestStreak + ' ngày</span>' : '') + warn + goal + '</div>';
  }
  function notes(o) {
    return (o.notes || []).map(function (n) { return '<div class="hm-note" data-note="' + esc(n.id) + '">📣 <span><b>' + esc(n.by) + ' nhắn em:</b> ' + esc(n.msg) + '<br><small class="mut">' + esc(n.time) + '</small></span><button class="btn sm" type="button" data-seen="' + esc(n.id) + '">Em đã đọc</button></div>'; }).join('');
  }
  function hasDraft(id) { try { return !!localStorage.getItem('gn_ttd_' + U.username + '|' + id); } catch (e) { return false; } }
  function card(p, i) {
    var c = p.current, g = D.GRAD[i % D.GRAD.length], now, go;
    if (c) {
      now = '<div class="hm-now"><span>📍 Em đang ở</span><b>' + esc(c.chap) + ' · ' + esc(c.title) + '</b></div>';
      go = '<a class="hm-go" href="' + esc(c.url) + '">' + (hasDraft(c.id) ? '↩ Làm tiếp bài đang dở' : c.kind === 'theory' ? '📖 Đọc lý thuyết' : c.kind === 'test' ? '📝 Vào làm bài kiểm tra' : '▶ Tiếp tục luyện tập') + '</a>';
    } else {
      now = '<div class="hm-now"><span>🎉 Hoàn thành</span><b>Em đã chinh phục cả lộ trình!</b></div>';
      go = '<a class="hm-go done" href="thuthach.html">🏆 Xem bản đồ chiến thắng</a>';
    }
    return '<article class="hm-card" style="--g:' + g + '"><div class="hm-head"><div class="hm-ico">' + D.ICON[i % D.ICON.length] + '</div><div class="t"><h2>' + esc(p.title) + '</h2><small>' + (c ? 'Bước ' + c.pos + ' / ' + p.total : 'Đã xong ' + p.total + ' bước') + '</small></div>' + D.ring(p.pct) + '</div>' +
      '<div class="hm-body">' + now + go + '<div class="hm-meta"><span>✅ ' + p.done + '/' + p.total + ' bước</span><span>⭐ ' + p.stars + '</span><a href="thuthach.html">🗺 Bản đồ</a></div></div></article>';
  }
  function medal(r) { return r <= 3 ? D.MEDAL[r - 1] : r; }
  var TABW = {};   /* lộ trình nào đang xem bảng "Tuần này" */
  function rowsHtml(rows, week) {
    return rows.map(function (r) { return '<tr class="' + (r.me ? 'me' : '') + '"><td class="n">' + medal(r.rank) + '</td><td>' + esc(r.name) + (r.me ? ' (em)' : '') + '</td><td class="v">' + (week ? r.w : r.done) + ' bước</td><td class="v">' + r.stars + ' ⭐</td></tr>'; }).join('');
  }
  function top(p) {
    if (!p.board) return '<div class="hm-panel"><h4>🏁 Top 5 của lớp</h4><div class="mut">Thầy/cô đang tắt bảng xếp hạng lớp.</div></div>';
    var week = !!TABW[p.id], list = week ? p.topW : p.top, me = week ? p.meW : p.me;
    var meRow = me ? '<tr class="sep"><td colspan="4">· · · vị trí của em · · ·</td></tr>' + rowsHtml([me], week) : '';
    return '<div class="hm-panel"><h4>🏁 Top 5 lớp ' + esc(p.cls) + ' <small>' + p.classTotal + ' bạn</small><span class="hm-tabs" data-p="' + esc(p.id) + '"><button type="button" data-w="0" class="' + (week ? '' : 'on') + '">Tổng</button><button type="button" data-w="1" class="' + (week ? 'on' : '') + '">Tuần này</button></span></h4>' +
      '<table class="hm-top"><thead><tr><th>#</th><th>Tên</th><th style="text-align:right">' + (week ? 'Tuần này' : 'Đã xong') + '</th><th style="text-align:right">Sao</th></tr></thead><tbody>' +
      (rowsHtml(list, week) || '<tr><td colspan="4" class="mut">Chưa có ai bắt đầu.</td></tr>') + meRow + '</tbody></table></div>';
  }
  function dash(p) {
    return '<section class="hm-sec"><h3>📊 ' + esc(p.title) + ' <small>Bảng vinh danh tính trên tất cả các lớp, từ trước đến nay</small></h3><div class="hm-grid">' + top(p) + '<div class="hm-panel"><h4>🌟 Vinh danh toàn thời gian</h4>' + D.fame(p.fame, p.fastMin) + '</div></div></section>';
  }
  var DATA = null;
  function render(o) {
    if (o.mode !== 'thuthach') { location.replace('index.html'); return; }
    if (!o.paths.length) { host.innerHTML = notes(o) + hero(o) + '<div class="hm-empty"><div class="big">🧭</div><h3>Chưa có lộ trình nào dành cho em</h3><p class="mut">Nhờ thầy/cô giao bài để mở lộ trình nhé.</p></div>'; return; }
    DATA = o;
    host.innerHTML = notes(o) + hero(o) + '<div class="hm-cards">' + o.paths.map(card).join('') + '</div>' + o.paths.map(dash).join('');
  }
  if (U.role !== 'student') { location.replace('admin.html'); return; }
  host.addEventListener('click', function (e) {
    var sb = e.target.closest('[data-seen]');
    if (sb) { var id = sb.getAttribute('data-seen'); A.api('tt_note_seen', { ids: [id] }).catch(function () {}); var n = sb.closest('.hm-note'); if (n) n.remove(); return; }
    var tb = e.target.closest('.hm-tabs button');
    if (tb && DATA) { TABW[tb.parentNode.getAttribute('data-p')] = tb.getAttribute('data-w') === '1'; render(DATA); }
  });
  host.innerHTML = '<div class="hm-empty"><div class="big">🚀</div><p class="mut">Đang chuẩn bị đường bay…</p></div>';
  var tries = 0;
  (function load() {
    A.api('tt_home').then(render).catch(function (e) {
      if (++tries < 2 && !(e && e.server)) return setTimeout(load, 1500);
      host.innerHTML = '<div class="hm-empty"><div class="big">📡</div><h3>Chưa tải được dữ liệu</h3><p class="mut">' + esc(e && e.server ? e.message : 'Kiểm tra mạng rồi thử lại nhé.') + '</p><p><button class="btn" onclick="location.reload()">Thử lại</button> <a class="btn sec" href="thuthach.html">Vào bản đồ</a></p></div>';
    });
  })();
})();
