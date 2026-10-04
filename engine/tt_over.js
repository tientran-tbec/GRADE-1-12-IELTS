/* Giáo viên / admin: tab "Tổng quan" — bức tranh chung về Thử thách (lớp, học sinh cần chú ý, bị kẹt, vinh danh toàn thời gian). */
(function () {
  'use strict';
  var A = window.GNAuth, D = window.TTDash, E = D.E, TO = {}, host, busy = false;
  function kpi(label, val, hot) { return '<div class="hm-k' + (hot ? ' hot' : '') + '"><b>' + val + '</b><span>' + label + '</span></div>'; }
  function render(r) {
    var k = r.kpi, h = '<div class="hm-hero"><div class="grow"><h2>📊 Tổng quan Thử thách</h2><p>Cập nhật khi mở tab · số liệu lưu tạm tối đa 2 phút.</p></div><button class="btn sec" id="ovr">↻ Làm mới</button><a class="btn" href="#tt" style="text-decoration:none">🚀 Cài đặt chế độ</a></div>';
    h += '<div class="hm-kpi">' + kpi('Học sinh trong lớp', k.students) + kpi('Đang học Thử thách', k.tt, 1) + kpi('Học trong 24 giờ', k.active1) + kpi('Học trong 7 ngày', k.active7) + kpi('Hoàn thành TB', k.avg + '%') + kpi('Đã xong lộ trình', k.finished) + '</div>';
    if (!k.tt) h += '<div class="hm-empty" style="margin-bottom:18px"><div class="big">🧭</div><h3>Chưa có lớp nào ở chế độ Thử thách</h3><p class="mut">Vào tab <a href="#tt">Thử thách</a> để bật chế độ cho một lớp hoặc từng học sinh.</p></div>';
    h += '<div class="hm-panel" style="margin-bottom:16px"><h4>🏫 Các lớp</h4><div class="tw"><table class="hm-top"><thead><tr><th>Lớp</th><th>Chế độ</th><th>Học sinh</th><th>Đang Thử thách</th><th>Học 7 ngày</th><th style="min-width:150px">% TB</th><th>Dẫn đầu</th></tr></thead><tbody>' +
      (r.classes.map(function (c) {
        return '<tr><td><b>' + E(c.id) + '</b></td><td>' + (c.mode === 'thuthach' ? '<span class="hm-tag n">🚀 Thử thách</span>' : '<span class="mut">Tự do</span>') + '</td><td>' + c.n + '</td><td>' + c.tt + '</td><td>' + c.active7 + (c.tt ? ' <small class="mut">/ ' + c.tt + '</small>' : '') + '</td><td><div class="hm-bar"><i style="width:' + c.avg + '%"></i></div> <small>' + c.avg + '%</small></td><td>' + E(c.top || '—') + '</td></tr>';
      }).join('') || '<tr><td colspan="7" class="mut">Chưa có lớp.</td></tr>') + '</tbody></table></div></div>';
    h += '<div class="hm-two"><div class="hm-panel"><h4>⏰ Cần chú ý <small>chưa bắt đầu hoặc ≥ 5 ngày không vào</small></h4>' +
      (r.attention.length ? '<ul class="hm-list">' + r.attention.map(function (a) { return '<li><b>' + E(a.name) + '</b> <small class="mut">' + E(a.cls) + '</small>' + (a.days < 0 ? '<span class="hm-tag n">Chưa bắt đầu</span>' : '<span class="hm-tag w">' + a.days + ' ngày chưa vào</span>') + '<small class="mut">' + E(a.cur || '') + '</small></li>'; }).join('') + '</ul>' : '<div class="mut">Tất cả học sinh đều đang học đều 👍</div>') + '</div>' +
      '<div class="hm-panel"><h4>🧱 Đang bị kẹt <small>làm ≥ 3 lần chưa qua</small></h4>' +
      (r.stuck.length ? '<ul class="hm-list">' + r.stuck.map(function (a) { return '<li><b>' + E(a.name) + '</b> <small class="mut">' + E(a.cls) + '</small><span class="hm-tag">' + a.n + ' lần · tốt nhất ' + a.best + '%</span><small class="mut">' + E(a.step) + '</small></li>'; }).join('') + '</ul><p class="mut" style="margin:8px 0 0;font-size:13px">Vào tab <a href="#tt">Thử thách</a> → chọn học sinh để “Cho qua” nếu cần.</p>' : '<div class="mut">Chưa có học sinh nào bị kẹt.</div>') + '</div></div>';
    r.paths.forEach(function (p, i) {
      h += '<section class="hm-sec"><h3>🗺 ' + E(p.title) + ' <small>' + p.learners + ' học sinh đã tham gia · TB ' + p.avgDone + '/' + p.total + ' bước</small></h3><div class="hm-panel"><h4>🌟 Vinh danh toàn thời gian <small>mọi lớp, mọi học sinh</small></h4>' + D.fame(p.fame, p.fastMin) + '</div></section>';
    });
    host.innerHTML = h;
    var b = host.querySelector('#ovr'); if (b) b.onclick = function () { TO.load(true); };
  }
  TO.load = function (force) {
    if (busy) return; busy = true;
    if (force || !host.getAttribute('data-ok')) host.innerHTML = '<div class="hm-empty"><div class="big">📊</div><p class="mut">Đang tổng hợp số liệu…</p></div>';
    A.api('tt_overview').then(function (r) { host.setAttribute('data-ok', '1'); render(r); })
      .catch(function (e) { host.innerHTML = '<div class="hm-empty"><div class="big">📡</div><p class="err">' + E(e && e.server ? e.message : 'Không kết nối được máy chủ.') + '</p><button class="btn" id="ovr">Thử lại</button></div>'; var b = host.querySelector('#ovr'); if (b) b.onclick = function () { TO.load(true); }; })
      .then(function () { busy = false; });
  };
  TO.show = function (h) { host = h; h.className = 'hm-over'; TO.load(false); };
  window.TTOver = TO;
})();
