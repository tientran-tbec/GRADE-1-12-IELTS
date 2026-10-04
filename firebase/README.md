# Firebase – hướng dẫn nhanh

Kiến trúc: trang web (Firebase Hosting) → `/api` (Cloud Function `api`, chạy nguyên `code.gs`) → Firestore.
- `functions/gasrt.js` bộ chạy code.gs + kho dữ liệu; `functions/fsstore.js` kho Firestore; `functions/index.js` điểm vào.
- Mật khẩu/phiên giữ nguyên (cùng thuật toán băm, cùng GN_SECRET) nên **không phải đặt lại mật khẩu**.
- Kiểm thử: `node tests/_bt_rt.js` (242), `tests/fs_store_test.js`, `tests/migrate_test.js`.

## Việc cần làm một lần
1. `npm i -g firebase-tools` → `firebase login` → `firebase use --add` (chọn dự án).
2. Tạo file `functions/.env` có một dòng `IMPORT_KEY=<chuỗi ngẫu nhiên dài>` (xoá sau khi chuyển xong).
3. Trong Apps Script: Project Settings → Script properties → thêm `EXPORT_KEY=<chuỗi ngẫu nhiên>`; deploy lại bản có `export_*` (code.gs mới).
4. `deploy_firebase.bat`.
5. `node tools/migrate.js <URL Apps Script> <EXPORT_KEY> <URL hàm importer> <IMPORT_KEY> --dry` rồi chạy thật (bỏ `--dry`).
6. Đổi `APPS_SCRIPT_URL` trong build.py thành `https://<dự-án>.web.app/api`, build, deploy.
7. Sau khi ổn: xoá `EXPORT_KEY` (Apps Script) và `IMPORT_KEY`, deploy lại.
