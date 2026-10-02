/* Ô góp ý: học sinh gửi ý kiến về bài đang làm cho giáo viên; giáo viên trả lời, hai bên xem lại cả cuộc trò chuyện.
   Tự gắn vào MỌI trang bài (luyện tập, kiểm tra, IELTS) khi build. Chỉ hiện với tài khoản học sinh.
   Cấu hình: window.GN_SET (mã bộ bài) hoặc window.GN_RD.set; tên trang lấy từ tên file. */
(function () {
  var A = window.GNAuth; if (!A) return;
  var s = A.get(); if (!s || s.user.role !== 'student') return;
  var set = window.GN_SET || (window.GN_RD && window.GN_RD.set); if (!set) return;
  var page = (window.GN_RD && window.GN_RD.page) || decodeURIComponent((location.pathname.split('/').pop() || 'trang').replace(/\.html$/, ''));
  var rootPath; try { rootPath = new URL(window.GN_ROOT || '', location.href).pathname; } catch (e) { rootPath = ''; }
  var path = location.pathname.indexOf(rootPath) === 0 ? location.pathname.slice(rootPath.length) : '';
  var E = A.esc, open = false, timer = null;

  var css = document.createElement('style');
  css.textContent = '.gnfb-btn{position:fixed;right:0;top:38%;z-index:100000;font:600 13px/1 system-ui,sans-serif;background:#1d4ed8;color:#fff;border:0;border-radius:10px 0 0 10px;padding:12px 8px;cursor:pointer;box-shadow:-2px 2px 8px rgba(0,0,0,.25);writing-mode:vertical-rl;letter-spacing:.5px}' +
    '.gnfb-btn .dot{display:none;position:absolute;top:-6px;left:-6px;writing-mode:horizontal-tb;min-width:18px;height:18px;border-radius:9px;background:#e11d48;color:#fff;font-size:11px;line-height:18px;text-align:center;padding:0 4px}' +
    '.gnfb-btn.has .dot{display:block}' +
    '.gnfb-box{position:fixed;right:40px;top:10vh;z-index:100001;width:min(340px,calc(100vw - 56px));max-height:76vh;display:none;flex-direction:column;background:#fff;color:#111;border:1px solid #cbd5e1;border-radius:12px;box-shadow:0 8px 28px rgba(0,0,0,.28);font:14px/1.4 system-ui,sans-serif}' +
    '.gnfb-box.on{display:flex}.gnfb-h{padding:10px 12px;border-bottom:1px solid #e2e8f0;font-weight:600;display:flex;justify-content:space-between;gap:8px}' +
    '.gnfb-h small{display:block;font-weight:400;color:#64748b}.gnfb-x{background:none;border:0;font-size:18px;cursor:pointer;color:#64748b}' +
    '.gnfb-l{flex:1;overflow:auto;padding:10px;display:flex;flex-direction:column;gap:8px;min-height:90px}' +
    '.gnfb-m{max-width:85%;padding:7px 10px;border-radius:12px;white-space:pre-wrap;word-break:break-word}' +
    '.gnfb-m.me{align-self:flex-end;background:#dbeafe}.gnfb-m.tc{align-self:flex-start;background:#f1f5f9}' +
    '.gnfb-m small{display:block;color:#64748b;font-size:11px;margin-top:2px}.gnfb-e{color:#64748b;text-align:center;font-size:13px;padding:8px}' +
    '.gnfb-f{border-top:1px solid #e2e8f0;padding:8px;display:flex;flex-direction:column;gap:6px}' +
    '.gnfb-f textarea{width:100%;box-sizing:border-box;height:62px;resize:none;border:1px solid #cbd5e1;border-radius:8px;padding:6px;font:inherit}' +
    '.gnfb-f button{align-self:flex-end;background:#1d4ed8;color:#fff;border:0;border-radius:8px;padding:6px 14px;cursor:pointer;font:inherit}.gnfb-f button:disabled{opacity:.5}' +
    '.gnfb-err{color:#be123c;font-size:12px}@media print{.gnfb-btn,.gnfb-box{display:none!important}}';
  document.head.appendChild(css);

  var btn = document.createElement('button'); btn.type = 'button'; btn.className = 'gnfb-btn'; btn.innerHTML = '💬 Góp ý<span class="dot"></span>';
  var box = document.createElement('div'); box.className = 'gnfb-box';
  box.innerHTML = '<div class="gnfb-h"><div>Góp ý về bài này<small>Chỉ giáo viên của bạn thấy tin nhắn này.</small></div><button type="button" class="gnfb-x" aria-label="Đóng">×</button></div>' +
    '<div class="gnfb-l"></div><div class="gnfb-f"><div class="gnfb-err"></div><textarea maxlength="1000" placeholder="Viết góp ý, báo lỗi đáp án hoặc đặt câu hỏi cho giáo viên…"></textarea><button type="button">Gửi</button></div>';
  document.body.appendChild(box); document.body.appendChild(btn);
  var list = box.querySelector('.gnfb-l'), ta = box.querySelector('textarea'), send = box.querySelector('.gnfb-f button'), err = box.querySelector('.gnfb-err'), dot = btn.querySelector('.dot');

  function render(msgs) {
    if (!msgs.length) { list.innerHTML = '<div class="gnfb-e">Chưa có tin nhắn. Hãy gửi góp ý đầu tiên.</div>'; return; }
    list.innerHTML = msgs.map(function (m) {
      var me = m.role === 'student';
      return '<div class="gnfb-m ' + (me ? 'me' : 'tc') + '">' + E(m.text) + '<small>' + (me ? 'Bạn' : E(m.name || 'Giáo viên')) + ' · ' + E(m.time) + '</small></div>';
    }).join('');
    list.scrollTop = list.scrollHeight;
  }
  function ctx() { return { set_id: set, page_id: page }; }
  function load() { return A.api('fb_list', ctx()).then(function (j) { render(j.msgs); setDot(0); }).catch(function () {}); }
  function setDot(n) { dot.textContent = n > 9 ? '9+' : n; btn.classList.toggle('has', n > 0); }
  function setOpen(v) {
    open = v; box.classList.toggle('on', v); clearInterval(timer);
    if (v) { load(); timer = setInterval(load, 20000); setTimeout(function () { ta.focus(); }, 50); }
  }
  btn.onclick = function () { setOpen(!open); };
  box.querySelector('.gnfb-x').onclick = function () { setOpen(false); };
  send.onclick = function () {
    var t = ta.value.trim(); if (!t) return; err.textContent = ''; send.disabled = true;
    A.api('fb_send', { set_id: set, page_id: page, title: document.title, path: path, text: t }).then(function (j) { ta.value = ''; render(j.msgs); })
      .catch(function (e) { err.textContent = e.message || 'Không gửi được, hãy thử lại.'; }).then(function () { send.disabled = false; });
  };
  ta.addEventListener('keydown', function (e) { if (e.key === 'Enter' && (e.ctrlKey || e.metaKey)) { e.preventDefault(); send.click(); } });
  ta.addEventListener('paste', function (e) { e.stopPropagation(); });
  ['mousedown', 'mouseup', 'pointerdown', 'touchstart', 'touchend', 'dblclick', 'contextmenu', 'cut', 'dragstart', 'drop'].forEach(function (ev) { box.addEventListener(ev, function (e) { e.stopPropagation(); }); });   /* các bộ chặn / công cụ của trang không được can thiệp vào khung chat */
  box.addEventListener('copy', function (e) { e.stopPropagation(); });
  // chấm đỏ: cuộc trò chuyện của trang này có tin trả lời chưa đọc?
  A.api('fb_mine').then(function (j) {
    var t = (j.threads || []).filter(function (x) { return x.set === set && x.page === page; })[0];
    if (t && t.unread && !open) setDot(t.unread);
  }).catch(function () {});
})();
