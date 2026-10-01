"""Giả lập học sinh đã đăng nhập (token chưa ký thật – chỉ để vượt qua cổng phía trình duyệt khi test offline)."""
import base64, json, time
def stub_js(role='teacher', name='Học Sinh Test', cls='11A1', username='hstest', must_change=False):
    pl = base64.urlsafe_b64encode(json.dumps({'u': username, 'r': role, 'e': int((time.time() + 86400) * 1000)}).encode()).decode().rstrip('=')
    sess = {'token': pl + '.sig', 'user': {'username': username, 'name': name, 'role': role, 'cls': cls, 'active': True, 'mustChange': must_change}}
    return "try{localStorage.setItem('gn_auth', %s)}catch(e){}" % json.dumps(json.dumps(sess))
def new_ctx(browser, **kw):
    c = browser.new_context(**kw.pop('ctx', {})); c.add_init_script(stub_js(**kw)); return c
