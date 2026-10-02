/* Xem lại bài làm của học sinh + chi tiết vi phạm (dùng cho trang Quản trị và trang Tổng kết học sinh).
   GNReview.open(row)   row = {row, name, set_id, page_id, ...} một dòng trong danh sách kết quả.
   Cần: GNAuth, window.GN_PAGES = {mã bộ bài: 'WebBaiTap/Lop10/Unit1/luyentap'} (do build.py chèn). */
(function () {
  var E = function (s) { return GNAuth.esc(s); };
  var EVT = {
    tab_hidden: 'Chuyển sang tab / cửa sổ khác', blur: 'Cửa sổ mất tiêu điểm (bấm ra ngoài)', fs_exit: 'Thoát chế độ toàn màn hình',
    paste: 'Cố dán nội dung', copy: 'Cố sao chép', cut: 'Cố cắt nội dung', contextmenu: 'Bấm chuột phải', shortcut: 'Dùng phím tắt bị chặn', dragstart: 'Kéo thả', drop: 'Kéo thả'
  };
  function mmss(t) { t = Math.max(0, +t || 0); return Math.floor(t / 60) + ':' + ('0' + (t % 60)).slice(-2); }
  /* 'tab_hidden:31;blur:40' → [{ev,t,x,text}] */
  function parseEvents(str) {
    return String(str || '').split(';').filter(Boolean).map(function (p) {
      var a = p.split(':'); return { ev: a[0], t: +a[1] || 0, x: a[2] || '', text: (EVT[a[0]] || a[0]) + (a[2] ? ' (' + a[2] + ')' : '') };
    });
  }
  function countsText(r) {
    var o = [];
    if (+r.tab) o.push('chuyển tab ' + r.tab + ' lần');
    if (+r.blur) o.push('mất tiêu điểm ' + r.blur + ' lần');
    if (+r.fs) o.push('thoát toàn màn hình ' + r.fs + ' lần');
    return o.join(', ');
  }
  function ensureCss() {
    if (document.getElementById('gnrv-css')) return;
    var st = document.createElement('style'); st.id = 'gnrv-css';
    st.textContent = '.gnrv-w{position:fixed;inset:0;z-index:9995;background:rgba(0,0,0,.55);display:flex;align-items:flex-start;justify-content:center;overflow:auto;padding:24px 12px}' +
      '.gnrv-b{box-sizing:border-box;background:var(--card,#fff);color:var(--ink,#111);border:1px solid var(--line,#ddd);border-radius:14px;max-width:920px;width:100%;padding:16px 18px}' +
      '.gnrv-b h3{margin:0 0 4px}.gnrv-s{display:flex;flex-wrap:wrap;gap:6px 14px;margin:8px 0;color:var(--mut,#667)}' +
      '.gnrv-t{width:100%;border-collapse:collapse;margin-top:8px}.gnrv-t td,.gnrv-t th{min-width:70px;border-top:1px solid var(--line,#ddd);padding:7px 8px;vertical-align:top;text-align:left}' +
      '.gnrv-ok{color:#16a34a;font-weight:700}.gnrv-no{color:#e11d48;font-weight:700}.gnrv-na{color:#94a3b8}.gnrv-ins{background:var(--bg,#f5f5f5);font-weight:600;color:var(--mut,#667)}' +
      '.gnrv-ev{margin:8px 0 0;padding:8px 10px;border:1px solid #e11d48;border-radius:10px}.gnrv-ev li{margin:2px 0}';
    document.head.appendChild(st);
  }
  /* Lấy JSON của window.QUIZ=… từ mã nguồn trang (cân bằng ngoặc, bỏ qua chuỗi) */
  function extractQuiz(html) {
    var i = html.indexOf('window.QUIZ='); if (i < 0) return null;
    i = html.indexOf('{', i); var d = 0, str = false, esc = false;
    for (var j = i; j < html.length; j++) {
      var c = html[j];
      if (str) { if (esc) esc = false; else if (c === '\\') esc = true; else if (c === '"') str = false; continue; }
      if (c === '"') str = true; else if (c === '{') d++; else if (c === '}') { d--; if (!d) { try { return JSON.parse(html.slice(i, j + 1)); } catch (e) { return null; } } }
    }
    return null;
  }
  function norm(s) {
    s = String(s == null ? '' : s).toLowerCase().replace(/[’‘`´]/g, "'").replace(/[“”]/g, '"');
    s = s.replace(/won't/g, 'will not').replace(/can't/g, 'can not').replace(/cannot/g, 'can not').replace(/n't\b/g, ' not').replace(/'ve\b/g, ' have').replace(/'ll\b/g, ' will').replace(/'m\b/g, ' am').replace(/'re\b/g, ' are');
    return s.replace(/[.,;:!?"]+/g, ' ').replace(/\s*\/\s*/g, ' / ').replace(/\s+/g, ' ').trim();
  }
  function blanksOf(a) { if (a && a.blanks) return a.blanks; if (typeof a === 'string') return [[a]]; return [a]; }
  function tx(el) { return el ? el.textContent.replace(/\s+/g, ' ').trim() : ''; }
  function stemOf(el) {
    var st = el.querySelector('.stem') || el.querySelector('.qb') || el; var c = st.cloneNode(true);
    [].forEach.call(c.querySelectorAll('.blank'), function (b) { b.replaceWith(document.createTextNode(' ______ ')); });
    [].forEach.call(c.querySelectorAll('.opts,.exp,.tools,button,textarea'), function (b) { b.remove(); });
    return tx(c);
  }
  function optsOf(el) { var o = {}; [].forEach.call(el.querySelectorAll('.opt'), function (l) { var inp = l.querySelector('input'); if (inp) o[inp.value] = tx(l.querySelector('span')) || tx(l); }); return o; }

  function close() { var w = document.getElementById('gnrv'); if (w) w.remove(); }
  function shell(inner) {
    ensureCss(); close();
    var w = document.createElement('div'); w.className = 'gnrv-w'; w.id = 'gnrv';
    w.innerHTML = '<div class="gnrv-b">' + inner + '</div>';
    w.addEventListener('mousedown', function (e) { if (e.target === w) close(); });
    document.body.appendChild(w); return w;
  }
  function header(d) {
    return '<div style="display:flex;gap:8px;align-items:center"><h3 style="flex:1">' + E(d.name) + ' <small class="mut">' + E(d.username) + ' · ' + E(d.cls) + '</small></h3><button class="btn sm sec" id="gnrvx">Đóng</button></div>' +
      '<div class="gnrv-s"><span>Bộ bài: <b>' + E(d.set_id) + '</b></span><span>Trang: <b>' + E(d.page_id) + '</b></span><span>' + E(GNAuth.t(d.time)) + '</span><span>' + E(d.type) + '</span><span>Điểm: <b>' + E(d.score) + '/' + E(d.total) + '</b> (thang 10: <b>' + E(d.score10) + '</b>)</span><span>Thời gian làm: <b>' + Math.round((+d.time_spent || 0) / 60) + ' phút</b></span>' + (+d.plays ? '<span>Số lần nghe: <b>' + E(d.plays) + '</b></span>' : '') + '</div>';
  }
  function violations(d) {
    var ev = parseEvents(d.events), c = countsText(d);
    if (!ev.length && !c) return '<p class="gnrv-ok" style="margin:6px 0">✓ Không ghi nhận vi phạm.</p>';
    var bys = {}; ev.forEach(function (e) { bys[e.text] = (bys[e.text] || 0) + 1; });
    return '<div class="gnrv-ev"><b style="color:#e11d48">⚠ Vi phạm ghi nhận' + (c ? ': ' + E(c) : '') + '</b>' +
      (ev.length ? '<ul style="margin:6px 0 0;padding-left:18px">' + ev.map(function (e) { return '<li><b>' + mmss(e.t) + '</b> – ' + E(e.text) + '</li>'; }).join('') + '</ul><p class="mut" style="margin:6px 0 0;font-size:12px">Mốc thời gian tính từ lúc bắt đầu làm bài (phút:giây).' + (ev.length >= 80 ? ' Chỉ lưu tối đa 80 sự kiện.' : '') + '</p>' :
        '<p class="mut" style="margin:6px 0 0;font-size:12px">Bài nộp này chưa lưu chi tiết từng lần (chỉ có số lần).</p>') + '</div>';
  }
  function plain(d, msg) {   // không dựng lại được từng câu → hiện dữ liệu thô
    var a = d.answers || {}, keys = typeof a === 'string' ? [] : Object.keys(a);
    if (typeof a === 'string') msg = (msg ? msg + ' ' : '') + 'Dữ liệu lưu: ' + a;
    return header(d) + violations(d) + (msg ? '<p class="mut">' + E(msg) + '</p>' : '') + (keys.length ? '<table class="gnrv-t"><tbody>' + keys.map(function (k) { return '<tr><td><b>' + E(k) + '</b></td><td>' + E(Array.isArray(a[k]) ? a[k].join(' | ') : a[k]) + '</td></tr>'; }).join('') + '</tbody></table>' : '');
  }
  function render(d, quiz, doc) {
    var A = d.answers || {}, rows = [], ok = 0, bad = 0, na = 0, lastG = null;
    quiz.order.forEach(function (id) {
      var el = doc.querySelector('.q[data-id="' + id + '"]'); if (!el) return;
      var it = quiz.items[id] || {}, t = it.t, ans = quiz.ANS ? quiz.ANS[id] : undefined, v = A[id], opts = optsOf(el), res = null, mine = '', right = '';
      var grp = el.closest('.group'), ins = grp ? tx(grp.querySelector('.instr')) : '';
      if (grp !== lastG) { lastG = grp; if (ins) rows.push('<tr data-i="1"><td colspan="5" class="gnrv-ins">' + E(ins) + '</td></tr>'); }
      var txt = function (L) { return L ? (opts[L] ? L + '. ' + opts[L].replace(/^[A-D]\.\s*/, '') : L) : ''; };
      if (t === 'mcq' || t === 'tf' || t === 'tfng') {
        mine = v === undefined ? '' : (t === 'mcq' ? txt(v) : v);
        if (ans !== undefined) { var al = Array.isArray(ans) ? ans : [ans]; right = al.map(function (x) { return t === 'mcq' ? txt(x) : x; }).join('  hoặc  '); res = v === undefined ? 'na' : (al.indexOf(v) >= 0 ? 'ok' : 'no'); }
      } else if (t === 'fill') {
        var vs = v === undefined ? [] : String(v).split(' | ');
        mine = vs.join(' | ');
        if (ans !== undefined) {
          var bl = blanksOf(ans); right = bl.map(function (b) { return (b || []).join(' / '); }).join(' | ');
          if (v === undefined || !vs.some(function (x) { return x !== ''; })) res = 'na';
          else res = bl.every(function (b, i) { var g = norm(vs[i] || ''); return g && (b || []).some(function (x) { return norm(x) === g; }); }) ? 'ok' : 'no';
        }
      } else { mine = v === undefined ? '' : String(v); right = ''; res = 'open'; }
      if (res === 'ok') ok++; else if (res === 'no') bad++; else if (res === 'na') na++;
      var ic = res === 'ok' ? '<span class="gnrv-ok">✔</span>' : res === 'no' ? '<span class="gnrv-no">✘</span>' : res === 'na' ? '<span class="gnrv-na">—</span>' : '<span class="gnrv-na">tự luận</span>';
      rows.push('<tr data-r="' + (res || '') + '"><td>' + E(tx(el.querySelector('.qn')) || id) + '</td><td>' + E(stemOf(el)) + '</td><td>' + (mine ? E(mine) : '<span class="gnrv-na">(không trả lời)</span>') + '</td><td>' + E(right) + '</td><td style="white-space:nowrap">' + ic + '</td></tr>');
    });
    var h = header(d) + violations(d) + '<div class="gnrv-s"><span class="gnrv-ok">Đúng: ' + ok + '</span><span class="gnrv-no">Sai: ' + bad + '</span><span>Bỏ trống: ' + na + '</span><label style="margin-left:auto;cursor:pointer"><input type="checkbox" id="gnrvf" style="display:inline;width:auto"> Chỉ hiện câu sai / bỏ trống</label></div>' +
      '<div style="overflow-x:auto"><table class="gnrv-t"><thead><tr><th>Câu</th><th>Đề</th><th>Học sinh trả lời</th><th>Đáp án đúng</th><th></th></tr></thead><tbody id="gnrvb">' + rows.join('') + '</tbody></table></div>';
    var w = shell(h); w.querySelector('#gnrvx').onclick = close;
    w.querySelector('#gnrvf').onchange = function () { var on = this.checked; [].forEach.call(w.querySelectorAll('#gnrvb tr'), function (tr) { tr.hidden = on && (!!tr.dataset.i || tr.dataset.r === 'ok' || tr.dataset.r === 'open'); }); };
  }
  function open(row) {
    var w = shell('<p>Đang tải bài làm…</p>');
    GNAuth.api('adm_result_detail', { row: row.row }).then(function (d) {
      var dir = (window.GN_PAGES || {})[d.set_id];
      var fail = function (m) { shell(plain(d, m)).querySelector('#gnrvx').onclick = close; };
      if (!dir || !d.page_id) { fail('Bộ bài này không dựng lại được từng câu (bài IELTS chỉ lưu band và chi tiết tóm tắt).'); return; }
      fetch(dir + '/' + d.page_id + '.html').then(function (r) { if (!r.ok) throw new Error('http'); return r.text(); }).then(function (html) {
        var quiz = extractQuiz(html); if (!quiz) throw new Error('quiz');
        render(d, quiz, new DOMParser().parseFromString(html, 'text/html'));
      }).catch(function () { fail('Không mở được trang đề để dựng lại từng câu (có thể đề đã đổi). Dưới đây là dữ liệu thô đã lưu.'); });
    }).catch(function (e) { var b = shell('<p class="err">' + E(e.server ? e.message : 'Không kết nối được máy chủ.') + '</p><button class="btn sm sec" id="gnrvx">Đóng</button>'); b.querySelector('#gnrvx').onclick = close; });
  }
  window.GNReview = { open: open, close: close, parseEvents: parseEvents, countsText: countsText, mmss: mmss };
})();
