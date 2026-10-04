/* Giáo viên: tab "Thử thách" trong trang quản trị — chế độ theo lớp / học sinh, tiến độ lớp, mở khoá cho học sinh bị kẹt, ngưỡng qua bài. */
(function () {
  'use strict';
  var A = window.GNAuth, E = A.esc, TA = {}, host, S, MODE = null, ROWS = [], PATHS = null;
  var MODES = { tudo: 'Tự do', thuthach: 'Thử thách' };
  function $(id) { return host.querySelector('#' + id); }
  function css() {
    if (document.getElementById('ttadm-css')) return;
    var s = document.createElement('style'); s.id = 'ttadm-css';
    s.textContent = '.tta .bar{display:flex;gap:8px;align-items:center;flex-wrap:wrap;margin:6px 0}.tta .pill{display:inline-block;border-radius:99px;padding:1px 10px;font-size:12px;font-weight:700;border:1px solid var(--line)}' +
      '.tta .pill.tt{background:#fff7ed;color:#c2410c;border-color:#fb923c}.tta .pb{height:8px;border-radius:6px;background:var(--line);overflow:hidden;min-width:70px}.tta .pb i{display:block;height:100%;background:#10b981}' +
      '.tta table{width:100%;border-collapse:collapse}.tta th,.tta td{padding:6px 8px;border-bottom:1px solid var(--line);text-align:left;font-size:14px}.tta .st{font-size:13px}.tta .st.done{color:var(--ok)}.tta .st.man{color:#2563eb}.tta details{margin:6px 0}.tta summary{cursor:pointer;font-weight:600}' +
      '.tta .cfg label{display:inline-block;margin:4px 12px 4px 0;font-weight:600}.tta .cfg input[type=number]{width:80px}.tta .skip{columns:2;font-size:13px}';
    document.head.appendChild(s);
  }
  TA.show = function (h, st) {
    css(); host = h; S = st;
    if (!h.getAttribute('data-init')) {
      h.setAttribute('data-init', '1'); h.className = 'tta';
      h.innerHTML = '<div class="card"><h3 style="margin-top:0">🚀 Chế độ Thử thách</h3><p class="mut" style="margin:0 0 8px">Ở chế độ <b>Thử thách</b>, học sinh phải làm xong bước trước mới mở bước sau (đọc lý thuyết đủ giờ → luyện tập ≥ ngưỡng → kiểm tra ≥ ngưỡng). Chế độ <b>Tự do</b> là giao diện hiện tại. Chế độ đặt theo lớp; từng học sinh có thể đặt riêng (ưu tiên hơn lớp).</p>' +
        '<div class="bar"><label style="margin:0">Lớp <select id="ttc"></select></label><label style="margin:0">Chế độ của lớp <select id="ttm"><option value="tudo">Tự do</option><option value="thuthach">Thử thách</option></select></label><button class="btn sec sm" id="ttr" type="button">↻ Tải lại</button> <button class="btn sec" id="ttex" type="button" title="Tải bảng tiến độ của lớp (mở bằng Excel)">⬇ Tải Excel</button><a class="btn sec sm" href="thuthach.html" target="_blank">👀 Xem thử giao diện học sinh</a><span class="mut" id="ttmsg"></span></div></div>' +
        '<div class="card"><h3 style="margin-top:0">Học sinh trong lớp</h3><div class="tw" id="ttl">Chọn lớp…</div></div><div class="card" id="ttd" hidden></div><div class="card" id="ttg" hidden></div>';
      $('ttc').onchange = function () { TA.load(); };
      $('ttr').onclick = function () { TA.load(true); };
      $('ttex').onclick = function () {
        var cls = $('ttc').value; if (!ROWS.length || !window.TTDash) return;
        TTDash.csv('thu-thach-' + cls + '.csv', ['Học sinh', 'Tài khoản', 'Lớp', 'Chế độ', 'Đã xong (bước)', 'Tổng số bước', '% hoàn thành', 'Sao', 'Chuỗi ngày', 'Đang học', 'Học lần cuối'],
          ROWS.map(function (x) { return [x.name, x.username, cls, MODES[x.mode] || x.mode, x.done, x.total, x.pct, x.stars, x.streak, x.current, x.last]; }));
      };
      $('ttm').onchange = function () { setMode('cls', $('ttc').value, this.value); };
      host.addEventListener('change', function (e) {
        if (e.target.classList.contains('ttall')) { [].forEach.call(host.querySelectorAll('#ttd .ttck,#ttd .ttckc'), function (x) { x.checked = e.target.checked; }); refreshSel(); return; }
        if (e.target.classList.contains('ttckc')) { [].forEach.call(e.target.closest('details').querySelectorAll('.ttck'), function (x) { x.checked = e.target.checked; }); refreshSel(); return; }
        if (e.target.classList.contains('ttck')) { refreshSel(); return; } var s = e.target.closest('.ttus'); if (s) setMode('user', s.getAttribute('data-u'), s.value); });
      host.addEventListener('click', function (e) {
        var b = e.target.closest('[data-det]'); if (b) { detail(b.getAttribute('data-det')); return; }
        var a = e.target.closest('[data-act]'); if (a) act(a);
        var un = e.target.closest('[data-undo]'); if (un) { A.api('tt_undo', { id: un.getAttribute('data-undo') }).then(function (r) { ok('Đã hoàn tác ' + r.count + ' bước.'); detail(un.getAttribute('data-u')); TA.load(true); }).catch(fail); }
        if (e.target.id === 'ttrs') bulk($('ttd').getAttribute('data-u'), { steps: checked() }, 'Đặt lại ' + checked().length + ' bước đã chọn? Kết quả đạt của các bước này bị xoá và các bước sau bị khoá lại. Bạn có thể hoàn tác.');
        if (e.target.id === 'ttra') bulk($('ttd').getAttribute('data-u'), { all: true }, 'Đặt lại TẤT CẢ các bước của học sinh này? Em sẽ quay về bước đầu. Bạn có thể hoàn tác ở “Lịch sử đặt lại”.');
        if (e.target.id === 'ttcs') saveCfg();
      });
    }
    A.api('tt_mode_get').then(function (r) {
      MODE = r; var sel = $('ttc'), cur = sel.value;
      sel.innerHTML = r.classes.map(function (c) { return '<option value="' + E(c.id) + '"' + (c.id === cur ? ' selected' : '') + '>' + E(c.id) + (c.mode === 'thuthach' ? ' · 🚀' : '') + '</option>'; }).join('');
      $('ttm').disabled = !r.canSet; TA.load(); cfgPanel();
    }).catch(fail);
  };
  function fail(e) { var m = $('ttmsg'); if (m) { m.className = 'err'; m.textContent = e && e.server ? e.message : 'Không kết nối được máy chủ.'; } }
  function ok(t) { var m = $('ttmsg'); m.className = 'okm'; m.textContent = t; setTimeout(function () { if (m.textContent === t) m.textContent = ''; }, 3500); }
  function setMode(scope, key, mode) {
    A.api('tt_mode_set', { scope: scope, key: key, mode: mode }).then(function () {
      if (scope === 'cls') { var c = MODE.classes.filter(function (x) { return x.id === key; })[0]; if (c) c.mode = mode; }
      else MODE.users[key] = mode;
      ok('Đã lưu chế độ'); TA.load(true);
    }).catch(function (e) { fail(e); TA.load(true); });
  }
  TA.load = function (fresh) {
    var cls = $('ttc').value; if (!cls) { $('ttl').innerHTML = '<p class="mut">Bạn chưa phụ trách lớp nào.</p>'; return; }
    var c = MODE.classes.filter(function (x) { return x.id === cls; })[0]; $('ttm').value = c ? c.mode : 'tudo';
    $('ttl').innerHTML = '<p class="mut">Đang tải…</p>';
    A.api('tt_progress', { cls: cls, fresh: !!fresh }).then(function (r) {
      ROWS = r.rows;
      $('ttl').innerHTML = r.rows.length ? '<table><thead><tr><th>Học sinh</th><th>Chế độ riêng</th><th>Đang học</th><th>Tiến độ</th><th>⭐</th><th>🔥</th><th>Gần nhất</th><th></th></tr></thead><tbody>' + r.rows.map(function (x) {
        var ov = MODE.users[x.username] || '';
        return '<tr><td>' + E(x.name) + '<br><small class="mut">' + E(x.username) + '</small></td><td><select class="ttus" data-u="' + E(x.username) + '"' + (MODE.canSet ? '' : ' disabled') + '><option value=""' + (ov === '' ? ' selected' : '') + '>Theo lớp (' + MODES[c ? c.mode : 'tudo'] + ')</option><option value="tudo"' + (ov === 'tudo' ? ' selected' : '') + '>Tự do</option><option value="thuthach"' + (ov === 'thuthach' ? ' selected' : '') + '>Thử thách</option></select>' + (x.mode === 'thuthach' ? ' <span class="pill tt">🚀</span>' : '') + '</td>' +
          '<td style="white-space:normal;min-width:150px">' + (x.total ? E(x.current) : '<span class="mut">chưa có lộ trình</span>') + '</td><td style="min-width:120px">' + (x.total ? '<div class="pb"><i style="width:' + x.pct + '%"></i></div><small>' + x.done + '/' + x.total + ' · ' + x.pct + '%</small>' : '—') + '</td><td>' + x.stars + '</td><td>' + x.streak + '</td><td><small>' + E(A.t(x.last)) + '</small></td><td>' + (x.total ? '<button class="btn sec sm" data-det="' + E(x.username) + '" type="button">Chi tiết</button>' : '') + '</td></tr>';
      }).join('') + '</tbody></table>' : '<p class="mut">Lớp chưa có học sinh.</p>';
    }).catch(function (e) { $('ttl').innerHTML = '<p class="err">' + E(e.server ? e.message : 'Không kết nối được máy chủ.') + '</p>'; });
  };
  function detail(u) {
    var d = $('ttd'); d.hidden = false; d.innerHTML = '<p class="mut">Đang tải…</p>'; d.scrollIntoView({ behavior: 'smooth' });
    A.api('tt_student', { username: u }).then(function (r) {
      var h = '<h3 style="margin-top:0">' + E(r.name) + ' <small class="mut">· ' + MODES[r.mode] + '</small> <button class="btn sec sm" id="ttx" type="button">Đóng</button></h3>';
      r.paths.forEach(function (p) {
        var chaps = {}, order = []; p.steps.forEach(function (s) { if (!chaps[s.chap]) { chaps[s.chap] = []; order.push(s.chap); } chaps[s.chap].push(s); });
        var firstOpen = order.filter(function (c) { return chaps[c].some(function (s) { return !(s.done || s.manual); }); })[0];
        h += '<h4>' + E(p.title) + '</h4>' + (MODE.canSet ? '<div class="bar ttbulk"><label style="margin:0"><input type="checkbox" class="ttall"> Chọn tất cả</label><button class="btn sec sm" id="ttrs" type="button" disabled>🔄 Đặt lại bước đã chọn (<span id="ttsn">0</span>)</button><button class="btn sec sm" id="ttra" type="button" data-u="' + E(u) + '">🗑 Đặt lại TẤT CẢ các bước</button><small class="mut">Có thể hoàn tác ở mục “Lịch sử đặt lại” bên dưới.</small></div>' : '') + order.map(function (c) {
          return '<details' + (c === firstOpen ? ' open' : '') + '><summary>' + E(c) + ' · ' + chaps[c].filter(function (s) { return s.done || s.manual; }).length + '/' + chaps[c].length + (MODE.canSet ? ' <input type="checkbox" class="ttckc" title="Chọn cả chương này"> <small class="mut">chọn cả chương</small>' : '') + '</summary><table><tbody>' + chaps[c].map(function (s) {
            var stt = s.done ? '<span class="st done">✔ Đạt ' + s.best + '%</span>' : (s.manual ? '<span class="st man">✔ Giáo viên cho qua</span>' : (s.n ? '<span class="st">chưa đạt (tốt nhất ' + s.best + '%)</span>' : '<span class="st mut">chưa làm</span>'));
            var ab = !MODE.canSet ? '' : ((s.done || s.manual) ? (s.manual ? '<button class="btn sec sm" data-act="revoke" data-u="' + E(u) + '" data-s="' + E(s.id) + '" type="button">Thu hồi</button>' : '') : '<button class="btn sm" data-act="pass" data-u="' + E(u) + '" data-s="' + E(s.id) + '" type="button">Cho qua</button>') + ' <button class="btn sec sm" data-act="reset" data-u="' + E(u) + '" data-s="' + E(s.id) + '" type="button" title="Xoá kết quả bước này của học sinh">Đặt lại</button>';
            return '<tr><td>' + (MODE.canSet ? '<input type="checkbox" class="ttck" data-s="' + E(s.id) + '"> ' : '') + E(s.title) + ' <small class="mut">' + ({ theory: 'lý thuyết', practice: 'luyện tập', test: 'kiểm tra' })[s.kind] + '</small></td><td>' + stt + '</td><td>' + s.n + ' lần</td><td>' + (MODE.canSet ? ab : '') + '</td></tr>';
          }).join('') + '</tbody></table></details>';
        }).join('');
      });
      if (MODE.canSet) h += '<h4>↩ Lịch sử đặt lại</h4><div id="tth"><p class="mut">Đang tải…</p></div>';
      d.innerHTML = h; d.setAttribute('data-u', u); $('ttx').onclick = function () { d.hidden = true; };
      if (MODE.canSet) history(u);
    }).catch(function (e) { d.innerHTML = '<p class="err">' + E(e.server ? e.message : 'Không kết nối được máy chủ.') + '</p>'; });
  }
  function checked() { return [].map.call(host.querySelectorAll('#ttd .ttck:checked'), function (x) { return x.getAttribute('data-s'); }); }
  function refreshSel() { var n = checked().length, b = $('ttrs'); if (b) { b.disabled = !n; $('ttsn').textContent = n; } }
  function history(u) {
    A.api('tt_resets', { username: u }).then(function (r) {
      var h = $('tth'); if (!h) return;
      h.innerHTML = r.list.length ? '<table><tbody>' + r.list.map(function (x) {
        return '<tr><td>' + E(x.time) + '</td><td>' + E(x.by) + '</td><td>' + x.count + ' bước</td><td>' + (x.undone ? '<span class="st man">đã hoàn tác</span>' : (r.canUndo || x.by === (A.user().username) ? '<button class="btn sm" data-undo="' + E(x.id) + '" data-u="' + E(u) + '" type="button">↩ Hoàn tác</button>' : '<span class="mut">chỉ admin hoàn tác</span>')) + '</td></tr>';
      }).join('') + '</tbody></table>' : '<p class="mut">Chưa có lần đặt lại nào.</p>';
    }).catch(function () { var h = $('tth'); if (h) h.innerHTML = ''; });
  }
  function bulk(u, body, label) {
    if (!window.confirm(label)) return;
    A.api('tt_reset', Object.assign({ username: u }, body)).then(function (r) { ok(r.count ? 'Đã đặt lại ' + r.count + ' bước (có thể hoàn tác).' : 'Không có bước nào có kết quả để đặt lại.'); detail(u); TA.load(true); }).catch(fail);
  }
  function act(b) {
    var how = b.getAttribute('data-act'), u = b.getAttribute('data-u');
    if (how === 'reset' && !window.confirm('Đặt lại bước này? Kết quả đạt của bước này sẽ bị xoá và bước sau bị khoá lại.')) return;
    b.disabled = true;
    A.api('tt_unlock', { username: u, step: b.getAttribute('data-s'), how: how }).then(function () { detail(u); TA.load(true); }).catch(function (e) { b.disabled = false; fail(e); });
  }
  /* cấu hình ngưỡng + bước bỏ qua */
  function cfgPanel() {
    var g = $('ttg'); if (!MODE.canSet) { g.hidden = true; return; }
    fetch('thuthach/index.json').then(function (r) { return r.json(); }).then(function (ix) {
      var ids = Object.keys(ix.paths).reduce(function (a, s) { if (a.indexOf(ix.paths[s]) < 0) a.push(ix.paths[s]); return a; }, []);
      return Promise.all(ids.map(function (id) { return fetch('thuthach/' + id + '.json').then(function (r) { return r.json(); }); }));
    }).then(function (docs) {
      PATHS = docs; g.hidden = false;
      g.innerHTML = '<h3 style="margin-top:0">⚙️ Luật qua bước & lộ trình</h3>' + docs.map(function (d) {
        var c = Object.assign({ theory_min: d.defaults.theory_min, practice_pass: d.defaults.practice_pass, test_pass: d.defaults.test_pass, board: true, goal: 2, skip: [] }, MODE.cfg[d.id] || {});
        return '<div class="cfg" data-p="' + E(d.id) + '"><h4>' + E(d.title) + '</h4><label>Đọc lý thuyết (phút) <input type="number" min="0" max="30" step="0.5" data-k="theory_min" value="' + c.theory_min + '"></label><label>Luyện tập qua bài ≥ (%) <input type="number" min="0" max="100" data-k="practice_pass" value="' + c.practice_pass + '"></label><label>Mục tiêu mỗi ngày (bước) <input type="number" min="0" max="20" data-k="goal" value="' + c.goal + '"></label><label>Kiểm tra qua bài ≥ (%) <input type="number" min="0" max="100" data-k="test_pass" value="' + c.test_pass + '"></label>' +
          '<label><input type="checkbox" data-k="board"' + (c.board !== false ? ' checked' : '') + '> Cho học sinh xem bảng % của các bạn</label>' +
          '<details><summary>Bỏ qua một số bước (học sinh không phải làm)</summary><div class="skip">' + d.chapters.map(function (ch) { return ch.steps.map(function (s) { return '<label style="display:block;font-weight:400"><input type="checkbox" data-skip="' + E(s.id) + '"' + (c.skip.indexOf(s.id) >= 0 ? ' checked' : '') + '> ' + E(ch.title.split(/[–:-]/)[0].trim()) + ' · ' + E(s.title) + '</label>'; }).join(''); }).join('') + '</div></details></div>';
      }).join('') + '<button class="btn" id="ttcs" type="button">Lưu luật</button> <span class="mut" id="ttcm"></span>';
    }).catch(function () { g.hidden = true; });
  }
  function saveCfg() {
    var jobs = [].map.call(host.querySelectorAll('#ttg .cfg'), function (box) {
      var cfg = {}; [].forEach.call(box.querySelectorAll('input[data-k]'), function (i) { cfg[i.getAttribute('data-k')] = i.type === 'checkbox' ? i.checked : +i.value; });
      cfg.skip = [].map.call(box.querySelectorAll('input[data-skip]:checked'), function (i) { return i.getAttribute('data-skip'); });
      return A.api('tt_cfg_set', { path: box.getAttribute('data-p'), cfg: cfg }).then(function (r) { MODE.cfg[box.getAttribute('data-p')] = r.cfg; });
    });
    Promise.all(jobs).then(function () { var m = $('ttcm'); m.className = 'okm'; m.textContent = '✔ Đã lưu'; setTimeout(function () { m.textContent = ''; }, 3000); }).catch(function (e) { var m = $('ttcm'); m.className = 'err'; m.textContent = e.server ? e.message : 'Không kết nối được máy chủ.'; });
  }
  window.TTAdmin = TA;
})();
