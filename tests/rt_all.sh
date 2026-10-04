#!/bin/sh
# Chạy toàn bộ bộ test backend trên bộ chạy Firebase (rt_mock) + test kho Firestore giả + test di chuyển dữ liệu.
cd "$(dirname "$0")"
for t in backend_test tt_backend_test ly_backend_test; do sed "s#require('./gas_mock')#require('./rt_mock')#" $t.js > _rt_$t.js; node _rt_$t.js | tail -1; rm -f _rt_$t.js; done
node fs_store_test.js | tail -1
node migrate_test.js | tail -1
