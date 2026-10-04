/* Bản đồ lộ trình THỬ THÁCH (trang thuthach.html): đường đi các chặng, cột % bên phải, nhiệm vụ tiếp theo, sao – huy hiệu – chuỗi ngày, bảng tiến độ lớp. */
(function () {
  'use strict';
  var A = window.GNAuth, T = window.GNTT, U = A.user(), $ = function (id) { return document.getElementById(id); }, E = A.esc;
  var road = $('road'), side = $('side'), PREVIEW = U.role !== 'student', DATA = null, RT = 0;
  function hop(o, k) { return Object.prototype.hasOwnProperty.call(o || {}, k); }
  var qs = {}; location.search.slice(1).split('&').forEach(function (p) { var a = p.split('='); if (a[0]) qs[a[0]] = decodeURIComponent(a[1] || ''); });
  function fail(m) { road.innerHTML = '<div class="sc">' + m + '</div>'; side.innerHTML = ''; }

  function load() {
    if (PREVIEW) {   /* giáo viên / admin: xem thử toàn bộ lộ trình, không khoá */
      return fetch('thuthach/index.json').then(function (r) { return r.json(); }).then(function (ix) {
        var ids = Object.keys(ix.paths).reduce(function (a, s) { if (a.indexOf(ix.paths[s]) < 0) a.push(ix.paths[s]); return a; }, []);
        return Promise.all(ids.map(function (id) { return T.meta(id).then(function (m) { var steps = []; m.doc.chapters.forEach(function (c) { c.steps.forEach(function (s) { steps.push(s.id); }); }); return { id: id, title: m.doc.title, cfg: m.doc.defaults, steps: steps, done: {}, manual: [] }; }); }));
      }).then(function (paths) { return { mode: 'preview', paths: paths, streak: 0, bestStreak: 0 }; });
    }
    return T.state(true);
  }

  function status(p, id, firstOpen) {
    if (PREVIEW) return 'open';
    if (hop(p.done, id)) return 'done';
    return id === firstOpen ? 'current' : 'locked';
  }
  function rowsPerLine() { var w = road.clientWidth - 24; return Math.max(2, Math.min(6, Math.floor(w / 96))); }

  function render(st) {
    DATA = st;
    if (!PREVIEW && st.mode !== 'thuthach') { fail('<b>Lớp của em đang học ở chế độ Tự do.</b><p><a class="btn" href="index.html">Vào trang bài tập</a></p>'); return; }
    if (!st.paths.length) { fail('<b>Chưa có lộ trình nào dành cho em.</b><p>Nhờ thầy/cô giao bài để mở lộ trình nhé.</p>'); return; }
    Promise.all(st.paths.map(function (p) { return T.meta(p.id); })).then(function (metas) {
      var n = rowsPerLine(), html = '', sideHtml = '', sum = { done: 0, total: 0, stars: 0, theory: 0, three: 0 }, chapStat = [], next = null, badges = [], banner = '';
      st.paths.forEach(function (p, pi) {
        var m = metas[pi], firstOpen = null;
        p.steps.some(function (id) { if (!hop(p.done, id)) { firstOpen = id; return true; } });
        html += '<div class="tthero"><div><h2>🚀 ' + E(p.title) + '</h2><small>' + (PREVIEW ? 'Chế độ xem thử của giáo viên — mọi bước đều mở' : 'Làm xong bước này mới mở bước sau. Cố lên nhé!') + '</small></div></div>';
        if (qs.locked && m.steps[qs.locked]) banner = '<div class="ttbanner lock">🔒 Bước đó chưa mở. Em hãy hoàn thành <b>' + E(m.steps[qs.locked].title) + '</b> trước nhé!</div>';
        if (PREVIEW) banner = '<div class="ttbanner prev">👀 Đây là giao diện học sinh thấy ở chế độ Thử thách. Giáo viên có thể bấm vào mọi bước.</div>';
        if (!PREVIEW && !firstOpen) banner = '<div class="ttbanner win">🏆 Chúc mừng! Em đã chinh phục toàn bộ lộ trình!</div>';
        html += banner;
        var inPath = {}; p.steps.forEach(function (id) { inPath[id] = 1; });
        m.doc.chapters.forEach(function (c, ci) {
          var steps = c.steps.filter(function (s) { return inPath[s.id]; }); if (!steps.length) return;
          var dn = steps.filter(function (s) { return hop(p.done, s.id); }).length, pct = Math.round(dn * 100 / steps.length);
          chapStat.push({ id: 'chap' + pi + '_' + ci, title: c.title, pct: pct, dn: dn, n: steps.length });
          html += '<section class="chap" id="chap' + pi + '_' + ci + '"><h3>' + (pct === 100 ? '🏁' : '🗺️') + ' ' + E(c.title) + ' <small style="font-weight:400;color:var(--mut)">' + dn + '/' + steps.length + ' bước</small></h3><div class="cbar"><i style="width:' + pct + '%"></i></div>';
          for (var i = 0; i < steps.length; i += n) {
            var chunk = steps.slice(i, i + n), rev = (i / n) % 2 === 1;
            html += '<div class="row' + (rev ? ' rev' : '') + '">';
            chunk.forEach(function (s, k) {
              var stt = status(p, s.id, firstOpen), need = T.need(p.cfg, s.kind), best = p.done[s.id], stars = 0, sub = '';
              if (stt === 'done') { stars = s.kind === 'theory' ? 1 : (T.stars(best, need) || 1); sub = s.kind === 'theory' ? '⭐ đã đọc' : new Array(stars + 1).join('⭐') + ' ' + (best || 0) + '%'; sum.done++; sum.stars += stars; if (s.kind === 'theory') sum.theory++; if (stars === 3) sum.three++; }
              else if (stt === 'current') { sub = s.kind === 'theory' ? 'Đọc ' + p.cfg.theory_min + ' phút' : 'Bắt đầu!'; next = { s: s, need: need, p: p, m: m }; }
              else if (stt === 'locked') sub = s.kind === 'theory' ? '' : 'cần ≥ ' + need + '%';
              else sub = s.kind === 'theory' ? '' : '≥ ' + need + '%';
              sum.total++;
              if (k) html += '<i class="seg' + (hop(p.done, chunk[k - 1].id) && !PREVIEW ? ' on' : '') + '"></i>';
              html += '<button class="nd ' + stt + ' k-' + s.kind + '" data-id="' + E(s.id) + '" data-url="' + E(s.url) + '" data-st="' + stt + '" title="' + E(s.title) + '">' + (stt === 'current' && !PREVIEW ? '<span class="me">🧒</span>' : '') + '<span class="ic">' + (stt === 'locked' ? '🔒' : (s.kind === 'theory' ? '📘' : (s.kind === 'test' ? '🏆' : '✏️'))) + '</span><b>' + E(s.title) + '</b><small>' + E(sub) + '</small></button>';
            });
            html += '</div>';
            if (i + n < steps.length) html += '<div class="turn ' + (rev ? 'l' : 'r') + (hop(p.done, chunk[chunk.length - 1].id) && !PREVIEW ? ' on' : '') + '"></div>';
          }
          html += '</section>';
        });
      });
      road.innerHTML = html;
      if (PREVIEW) { side.innerHTML = '<div class="sc"><h4>👩‍🏫 Xem thử</h4>Các thống kê, sao, huy hiệu và bảng lớp sẽ hiện khi học sinh vào lộ trình.</div>'; bind(); return; }

      var pct = sum.total ? Math.round(sum.done * 100 / sum.total) : 0, R = 46, C = 2 * Math.PI * R;
      sideHtml += '<div class="sc"><div class="ring"><svg width="110" height="110" viewBox="0 0 110 110"><circle cx="55" cy="55" r="' + R + '" fill="none" stroke="#e5e7eb" stroke-width="12"/><circle cx="55" cy="55" r="' + R + '" fill="none" stroke="#10b981" stroke-width="12" stroke-linecap="round" stroke-dasharray="' + (C * pct / 100).toFixed(1) + ' ' + C.toFixed(1) + '" transform="rotate(-90 55 55)"/></svg><div><div class="big">' + pct + '%</div><small>' + sum.done + '/' + sum.total + ' bước</small></div></div>' +
        '<div class="stat" style="margin-top:10px"><span>⭐ ' + sum.stars + '</span><span>🔥 ' + (st.streak || 0) + ' ngày</span></div></div>';
      if (next) sideHtml += '<div class="sc mission"><h4>🎯 Nhiệm vụ tiếp theo</h4><b>' + E(next.s.title) + '</b><div style="color:var(--mut);font-size:13px">' + E(next.s.chap) + ' · ' + (next.s.kind === 'theory' ? 'đọc đủ ' + next.p.cfg.theory_min + ' phút' : (next.s.kind === 'test' ? 'bài kiểm tra, cần ≥ ' + next.need + '%' : 'luyện tập, cần ≥ ' + next.need + '%')) + '</div><a class="btn" href="' + E(next.s.url) + '">Bắt đầu ▶</a></div>';
      sideHtml += '<div class="sc"><h4>📊 Từng chặng</h4><div class="cbars">' + chapStat.map(function (c) { return '<div data-go="' + c.id + '">' + E(c.title) + ' <b>' + c.pct + '%</b><div class="cbar"><i style="width:' + c.pct + '%"></i></div></div>'; }).join('') + '</div></div>';
      badges = [
        { i: '🌱', t: 'Khởi đầu', d: 'Hoàn thành bước đầu tiên', ok: sum.done >= 1 },
        { i: '📘', t: 'Mọt sách', d: 'Đọc xong 3 phần lý thuyết', ok: sum.theory >= 3 },
        { i: '⭐', t: 'Ngôi sao', d: 'Có 10 sao', ok: sum.stars >= 10 },
        { i: '🌟', t: 'Siêu sao', d: '5 bước đạt 3 sao', ok: sum.three >= 5 },
        { i: '🔥', t: '3 ngày liền', d: 'Học 3 ngày liên tiếp', ok: (st.bestStreak || 0) >= 3 },
        { i: '🚀', t: '7 ngày liền', d: 'Học 7 ngày liên tiếp', ok: (st.bestStreak || 0) >= 7 }
      ].concat(chapStat.map(function (c) { return { i: '🏅', t: 'Xong ' + c.title.split(/[–:-]/)[0].trim(), d: 'Hoàn thành chặng ' + c.title, ok: c.pct === 100 }; }));
      badges.push({ i: '🏆', t: 'Chinh phục', d: 'Hoàn thành cả lộ trình', ok: sum.total > 0 && sum.done === sum.total });
      sideHtml += '<div class="sc"><h4>🎖️ Huy hiệu (' + badges.filter(function (b) { return b.ok; }).length + '/' + badges.length + ')</h4><div class="badges">' + badges.map(function (b) { return '<div class="bd' + (b.ok ? '' : ' off') + '" title="' + E(b.d) + '"><span>' + b.i + '</span>' + E(b.t) + '</div>'; }).join('') + '</div></div>';
      sideHtml += '<div class="sc" id="boardBox" hidden><h4>👥 Các bạn trong lớp</h4><div id="board"></div></div>';
      side.innerHTML = sideHtml; bind();
      A.api('tt_board').then(function (r) {
        if (!r.rows || !r.rows.length) return;
        $('boardBox').hidden = false;
        $('board').innerHTML = '<table class="board">' + r.rows.map(function (x) { return '<tr class="' + (x.me ? 'me' : '') + '"><td>' + x.rank + '</td><td>' + E(x.me ? 'Em' : x.name) + '</td><td class="pc"><i style="width:' + x.pct + '%"></i></td><td>' + x.pct + '%</td><td>⭐' + x.stars + '</td></tr>'; }).join('') + '</table><small class="mut">Cùng cố gắng nhé! Chỉ xem được % hoàn thành, không xem điểm của bạn.</small>';
      }).catch(function () {});
      if (qs.locked || next) { var cur = road.querySelector('.nd.current'); if (cur) setTimeout(function () { cur.scrollIntoView({ block: 'center', behavior: 'smooth' }); }, 300); }
    }).catch(function () { fail('Không tải được lộ trình. Hãy thử tải lại trang.'); });
  }

  function bind() {
    road.onclick = function (e) {
      var b = e.target.closest('.nd'); if (!b) return;
      if (b.getAttribute('data-st') === 'locked') { b.classList.remove('shake'); void b.offsetWidth; b.classList.add('shake'); T.toast('🔒 Hoàn thành các bước trước để mở bước này nhé!'); return; }
      location.href = b.getAttribute('data-url');
    };
    side.onclick = function (e) { var c = e.target.closest('[data-go]'); if (c) { var t = $(c.getAttribute('data-go')); if (t) t.scrollIntoView({ behavior: 'smooth', block: 'start' }); } };
  }
  window.addEventListener('resize', function () { clearTimeout(RT); RT = setTimeout(function () { if (DATA) render(DATA); }, 200); });
  load().then(render).catch(function (e) { fail(E(e.server ? e.message : 'Không kết nối được máy chủ.')); });
})();
