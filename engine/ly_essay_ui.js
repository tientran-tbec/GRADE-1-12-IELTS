/* Giao diện tự luận Vật lí: (1) LyAdmin – giáo viên xem bài làm, điểm AI gợi ý, duyệt điểm chính thức; (2) LyMe – học sinh xem điểm tự luận của mình. */
(function () {
  'use strict';
  var A = window.GNAuth, E = A.esc, KEY = null, KX = false;
  function fmt(s) { return E(s || '').replace(/\*\*([^*\n]+)\*\*/g, '<b>$1</b>').replace(/\n/g, '<br>'); }
  function vn(x) { return (Math.round(x * 100) / 100).toString().replace('.', ','); }
  function loadKatex(cb) {
    if (window.renderMathInElement) { cb(); return; }
    if (KX) { setTimeout(function () { loadKatex(cb); }, 150); return; }
    KX = true;
    var l = document.createElement('link'); l.rel = 'stylesheet'; l.href = 'engine/katex/katex.min.css'; document.head.appendChild(l);
    var a = document.createElement('script'); a.src = 'engine/katex/katex.min.js';
    a.onload = function () { var b = document.createElement('script'); b.src = 'engine/katex/auto-render.min.js'; b.onload = cb; document.head.appendChild(b); };
    document.head.appendChild(a);
  }
  function math(el) { loadKatex(function () { try { window.renderMathInElement(el, { delimiters: [{ left: '$$', right: '$$', display: true }, { left: '$', right: '$', display: false }], throwOnError: false }); } catch (e) {} }); }
  function loadKey() { return KEY ? Promise.resolve(KEY) : fetch('WebBaiTap/Lop11/Ly/essay_key.json').then(function (r) { return r.json(); }).then(function (j) { KEY = j; return j; }).catch(function () { KEY = {}; return KEY; }); }
  function css() {
    if (document.getElementById('lyessay-css')) return;
    var s = document.createElement('style'); s.id = 'lyessay-css';
    s.textContent = '.ey{padding:12px}.ey .bar{margin-bottom:6px}.ey .ans{white-space:pre-wrap;word-break:break-word;background:var(--bg);border:1px solid var(--line);border-radius:10px;padding:8px 10px;margin:4px 0 8px}' +
      '.ey .ai{border-left:4px solid #1d4ed8;background:var(--bg);padding:6px 10px;border-radius:0 10px 10px 0;margin:6px 0}.ey .ai li{margin:2px 0}.ey details{margin:6px 0}.ey summary{cursor:pointer;color:var(--pri)}' +
      '.ey .gv{display:flex;gap:8px;flex-wrap:wrap;align-items:center}.ey .gv input[type=number]{width:90px}.ey .gv input[type=text]{flex:1;min-width:200px}.tag.ok{color:var(--ok);border-color:var(--ok)}.tag.wait{color:#b45309;border-color:#b45309}' +
      '.ey .katex{font-size:1.02em}';
    document.head.appendChild(s);
  }
  function stTag(st) { return '<span class="tag ' + (st === 'Đã duyệt' ? 'ok' : 'wait') + '">' + E(st || '') + '</span>'; }

  /* ---------------- giáo viên ---------------- */
  var LyAdmin = {
    show: function (host, S) {
      css();
      if (!host.getAttribute('data-init')) {
        host.setAttribute('data-init', '1');
        host.innerHTML = '<div class="bar"><select id="eyc"></select><select id="eys"><option value="pending">Chờ duyệt</option><option value="">Tất cả</option><option value="done">Đã duyệt</option></select>' +
          '<input id="eyq" type="search" placeholder="Tìm tên / tài khoản…" class="grow"><button class="btn sec" id="eyr">↻ Tải lại</button><span class="mut" id="eyn"></span></div>' +
          '<p class="mut" style="margin-top:0">Học sinh nộp tự luận ở các trang Vật lí → AI chấm gợi ý theo biểu điểm → thầy/cô xem lại và bấm <b>Duyệt</b> để chốt điểm chính thức (học sinh sẽ thấy điểm và nhận xét của thầy/cô).</p><div id="eyl"></div>';
        host.querySelector('#eyr').onclick = function () { LyAdmin.load(); };
        ['eyc', 'eys'].forEach(function (i) { host.querySelector('#' + i).onchange = function () { LyAdmin.load(); }; });
        var tm; host.querySelector('#eyq').oninput = function () { clearTimeout(tm); tm = setTimeout(function () { LyAdmin.load(); }, 400); };
      }
      var sel = host.querySelector('#eyc'), cur = sel.value;
      sel.innerHTML = '<option value="">Mọi lớp tôi phụ trách</option>' + (S.classes || []).map(function (c) { return '<option value="' + E(c.id) + '"' + (c.id === cur ? ' selected' : '') + '>' + E(c.id) + '</option>'; }).join('');
      LyAdmin.host = host; LyAdmin.load();
    },
    load: function () {
      var h = LyAdmin.host, l = h.querySelector('#eyl'); l.innerHTML = '<p class="mut">Đang tải…</p>';
      Promise.all([A.api('ly_essay_list', { cls: h.querySelector('#eyc').value, status: h.querySelector('#eys').value, q: h.querySelector('#eyq').value, limit: 300 }), loadKey()]).then(function (r) {
        var rows = r[0].rows || [], K = r[1];
        h.querySelector('#eyn').textContent = rows.length + ' bài';
        l.innerHTML = rows.length ? rows.map(function (x) { return LyAdmin.card(x, K[x.uid]); }).join('') : '<p class="mut">Chưa có bài tự luận nào cần xem.</p>';
        math(l);
      }).catch(function (e) { l.innerHTML = '<p class="err">' + E(e.server ? e.message : 'Không kết nối được máy chủ.') + '</p>'; });
    },
    card: function (x, k) {
      var ai = x.ai, off = x.official, sc = off ? off.score : (ai ? ai.score : 0);
      var rub = k && k.rubric && k.rubric.length ? '<div><b>Biểu điểm:</b><ul>' + k.rubric.map(function (r) { return '<li>' + E(r.t) + ' <i>(' + vn(r.p) + ')</i></li>'; }).join('') + '</ul></div>' : '';
      return '<div class="card ey" data-id="' + E(x.id) + '" data-max="' + x.max + '"><div class="bar"><b>' + E(x.name) + '</b><span class="tag">' + E(x.cls) + '</span><span class="tag">' + E(x.set_id) + '</span>' +
        '<span class="tag">nộp ' + x.attempts + ' lần</span>' + stTag(x.status) + '<span class="grow"></span><small class="mut">' + E(A.t(x.time)) + '</small></div>' +
        '<details><summary>Đề · lời giải mẫu · biểu điểm</summary>' + (k ? '<div>' + fmt(k.q) + '</div><div style="margin-top:6px"><b>Đáp số:</b> ' + fmt(k.final) + '</div><div style="margin-top:6px"><b>Lời giải mẫu:</b><br>' + fmt(k.sol) + '</div>' + rub : '<p class="mut">Không tải được đề (' + E(x.uid) + ').</p>') + '</details>' +
        '<div><b>Bài làm của học sinh:</b></div><div class="ans">' + E(x.answer) + '</div>' +
        '<div class="ai">' + (ai ? '<b>🤖 AI gợi ý: ' + vn(ai.score) + ' / ' + vn(ai.max) + '</b><ul>' + (ai.items || []).map(function (r) { return '<li>' + E(r.t) + ' — <b>' + vn(r.got) + '/' + vn(r.max) + '</b>' + (r.note ? ' <small class="mut">' + E(r.note) + '</small>' : '') + '</li>'; }).join('') + '</ul>' + (ai.comment ? '<div>' + fmt(ai.comment) + '</div>' : '') : '<span class="mut">AI chưa chấm bài này.</span>') + '</div>' +
        '<div class="gv"><label style="margin:0">Điểm chính thức <input type="number" class="eysc" min="0" max="' + x.max + '" step="0.05" value="' + sc + '"> / ' + vn(x.max) + '</label>' + (ai ? '<button class="btn sec sm eyuse" type="button">Dùng điểm AI</button>' : '') +
        '<input type="text" class="eycm" maxlength="1500" placeholder="Nhận xét cho học sinh…" value="' + E(off ? off.comment : '') + '"><button class="btn sm eyok" type="button">' + (off ? '✔ Cập nhật' : '✔ Duyệt') + '</button><span class="mut eymsg"></span></div></div>';
    },
    bind: function (host) {
      host.addEventListener('click', function (e) {
        var c = e.target.closest('.ey'); if (!c) return;
        var b = e.target.closest('.eyok'), u = e.target.closest('.eyuse');
        if (u) { var m = /AI gợi ý: ([\d,]+)/.exec(c.querySelector('.ai').textContent); if (m) c.querySelector('.eysc').value = m[1].replace(',', '.'); return; }
        if (!b) return;
        var sc = c.querySelector('.eysc').value, msg = c.querySelector('.eymsg'); b.disabled = true; msg.textContent = '…';
        A.api('ly_essay_review', { id: c.getAttribute('data-id'), score: sc, comment: c.querySelector('.eycm').value }).then(function (j) {
          msg.textContent = '✔ Đã lưu'; var t = c.querySelector('.bar .tag.wait'); if (t) { t.className = 'tag ok'; t.textContent = 'Đã duyệt'; } b.textContent = '✔ Cập nhật'; b.disabled = false;
        }).catch(function (er) { msg.textContent = er.server ? er.message : 'Không kết nối được máy chủ.'; b.disabled = false; });
      });
    }
  };

  /* ---------------- học sinh ---------------- */
  var LyMe = {
    mount: function (host) {
      css();
      Promise.all([A.api('ly_essay_mine', {}), loadKey()]).then(function (r) {
        var rows = r[0].rows || [], K = r[1]; if (!rows.length) return;
        host.hidden = false;
        host.querySelector('.lyb').innerHTML = '<div class="tw"><table><thead><tr><th>Câu</th><th>Điểm AI (tạm tính)</th><th>Điểm giáo viên</th><th>Trạng thái</th><th>Nhận xét của giáo viên</th></tr></thead><tbody>' +
          rows.map(function (x) {
            var k = K[x.uid], q = k ? k.q.replace(/\s+/g, ' ').slice(0, 90) : x.uid;
            return '<tr><td style="white-space:normal;min-width:220px">' + E(q) + '…<br><small class="mut">' + E(x.set_id) + '</small></td><td>' + (x.ai ? vn(x.ai.score) + '/' + vn(x.max) : '—') + '</td><td><b>' + (x.official ? vn(x.official.score) + '/' + vn(x.max) : '—') + '</b></td><td>' + stTag(x.status) + '</td><td style="white-space:normal;min-width:200px">' + E(x.official ? x.official.comment : '') + '</td></tr>';
          }).join('') + '</tbody></table></div>';
        math(host);
      }).catch(function () {});
    }
  };
  window.LyAdmin = LyAdmin; window.LyMe = LyMe;
})();
