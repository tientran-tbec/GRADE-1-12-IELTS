/* Trang chủ học sinh ở chế độ THỬ THÁCH: mỗi lộ trình một khung lối tắt (vào thẳng bước đang làm), top 5 lớp, bảng vinh danh. */
(function () {
  'use strict';
  var A = window.GNAuth, D = window.TTDash, E = D.E, host = document.getElementById('home'), U = A.user();
  function esc(s) { return E(s); }
  function hero(o) {
    var hi = o.streak > 0 ? '<span class="hm-chip fire">🔥 ' + o.streak + ' ngày liên tiếp</span>' : '<span class="hm-chip off">🔥 Bắt đầu chuỗi ngày học nào!</span>';
    var nudge = o.today ? 'Hôm nay em đã học rồi — giữ vững phong độ nhé! 💪' : (o.streak > 0 ? 'Hôm nay em chưa học. Làm xong 1 bước để giữ chuỗi 🔥 nhé!' : 'Làm xong 1 bước hôm nay để nhận ngọn lửa đầu tiên!');
    return '<div class="hm-hero"><div class="grow"><h2>Chào ' + esc(o.name || U.name) + '! 👋</h2><p>' + nudge + '</p></div>' + hi + (o.bestStreak > o.streak ? '<span class="hm-chip">🏅 Kỷ lục ' + o.bestStreak + ' ngày</span>' : '') + '</div>';
  }
  function card(p, i) {
    var c = p.current, g = D.GRAD[i % D.GRAD.length], now, go;
    if (c) {
      now = '<div class="hm-now"><span>📍 Em đang ở</span><b>' + esc(c.chap) + ' · ' + esc(c.title) + '</b></div>';
      go = '<a class="hm-go" href="' + esc(c.url) + '">' + (c.kind === 'theory' ? '📖 Đọc lý thuyết' : c.kind === 'test' ? '📝 Vào làm bài kiểm tra' : '▶ Tiếp tục luyện tập') + '</a>';
    } else {
      now = '<div class="hm-now"><span>🎉 Hoàn thành</span><b>Em đã chinh phục cả lộ trình!</b></div>';
      go = '<a class="hm-go done" href="thuthach.html">🏆 Xem bản đồ chiến thắng</a>';
    }
    return '<article class="hm-card" style="--g:' + g + '"><div class="hm-head"><div class="hm-ico">' + D.ICON[i % D.ICON.length] + '</div><div class="t"><h2>' + esc(p.title) + '</h2><small>' + (c ? 'Bước ' + c.pos + ' / ' + p.total : 'Đã xong ' + p.total + ' bước') + '</small></div>' + D.ring(p.pct) + '</div>' +
      '<div class="hm-body">' + now + go + '<div class="hm-meta"><span>✅ ' + p.done + '/' + p.total + ' bước</span><span>⭐ ' + p.stars + '</span><a href="thuthach.html">🗺 Bản đồ</a></div></div></article>';
  }
  function medal(r) { return r <= 3 ? D.MEDAL[r - 1] : r; }
  function top(p) {
    if (!p.board) return '<div class="hm-panel"><h4>🏁 Top 5 của lớp</h4><div class="mut">Thầy/cô đang tắt bảng xếp hạng lớp.</div></div>';
    var rows = p.top.map(function (r) { return '<tr class="' + (r.me ? 'me' : '') + '"><td class="n">' + medal(r.rank) + '</td><td>' + esc(r.name) + (r.me ? ' (em)' : '') + '</td><td class="v">' + r.done + ' bước</td><td class="v">' + r.stars + ' ⭐</td></tr>'; }).join('');
    var me = p.me ? '<tr class="sep"><td colspan="4">· · · vị trí của em · · ·</td></tr><tr class="me"><td class="n">' + p.me.rank + '</td><td>' + esc(p.me.name) + ' (em)</td><td class="v">' + p.me.done + ' bước</td><td class="v">' + p.me.stars + ' ⭐</td></tr>' : '';
    return '<div class="hm-panel"><h4>🏁 Top 5 của lớp ' + esc(p.cls) + ' <small>' + p.classTotal + ' bạn</small></h4><table class="hm-top"><thead><tr><th>#</th><th>Tên</th><th style="text-align:right">Đã xong</th><th style="text-align:right">Sao</th></tr></thead><tbody>' + (rows || '<tr><td colspan="4" class="mut">Chưa có ai bắt đầu.</td></tr>') + me + '</tbody></table></div>';
  }
  function dash(p) {
    return '<section class="hm-sec"><h3>📊 ' + esc(p.title) + ' <small>Bảng vinh danh tính trên tất cả các lớp, từ trước đến nay</small></h3><div class="hm-grid">' + top(p) + '<div class="hm-panel"><h4>🌟 Vinh danh toàn thời gian</h4>' + D.fame(p.fame, p.fastMin) + '</div></div></section>';
  }
  function render(o) {
    if (o.mode !== 'thuthach') { location.replace('index.html'); return; }
    if (!o.paths.length) { host.innerHTML = hero(o) + '<div class="hm-empty"><div class="big">🧭</div><h3>Chưa có lộ trình nào dành cho em</h3><p class="mut">Nhờ thầy/cô giao bài để mở lộ trình nhé.</p><a class="btn sec" href="index.html?free=1">Xem bài tự do</a></div>'; return; }
    host.innerHTML = hero(o) + '<div class="hm-cards">' + o.paths.map(card).join('') + '</div>' + o.paths.map(dash).join('');
  }
  if (U.role !== 'student') { location.replace('admin.html'); return; }
  host.innerHTML = '<div class="hm-empty"><div class="big">🚀</div><p class="mut">Đang chuẩn bị đường bay…</p></div>';
  var tries = 0;
  (function load() {
    A.api('tt_home').then(render).catch(function (e) {
      if (++tries < 2 && !(e && e.server)) return setTimeout(load, 1500);
      host.innerHTML = '<div class="hm-empty"><div class="big">📡</div><h3>Chưa tải được dữ liệu</h3><p class="mut">' + esc(e && e.server ? e.message : 'Kiểm tra mạng rồi thử lại nhé.') + '</p><p><button class="btn" onclick="location.reload()">Thử lại</button> <a class="btn sec" href="thuthach.html">Vào bản đồ</a></p></div>';
    });
  })();
})();
