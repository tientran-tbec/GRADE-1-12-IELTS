# -*- coding: utf-8 -*-
"""SỬA ĐÁP ÁN / ĐỀ sau khi sinh dữ liệu (áp dụng trong build.py, không cần sửa file sinh).

FIXES[<set id>][<item id>] = {
    'ans':     đáp án mới. mcq/tf: 'B' hoặc ['B','D'] (nhiều đáp án đều được tính đúng); mcq plain: nội dung phương án;
               fill: danh sách cách viết chấp nhận.
    'exp':     thay giải thích;   'exp_add': thêm một câu vào cuối giải thích.
    'q':       thay nội dung câu hỏi;   'o': {chỉ số phương án: 'nội dung mới'}.
}
Quy ước: câu nào Word gốc sai/mơ hồ → sửa ở đây và ghi vào BAO_CAO_RA_SOAT.md (mục "Đã tự sửa").
"""

FIXES = {
    # ------------------------------------------------------------------ UNIT 1
    'lop11-u1-4kn': {
        'pr1.4': {
            'o': {2: 'surg<u>e</u>ry'}, 'ans': 'A',
            'exp': 'Âm gạch chân: en<b>e</b>rgy /ˈenədʒi/ → /e/; treatm<b>e</b>nt /ˈtriːtmənt/, surg<b>e</b>ry /ˈsɜːdʒəri/, nutri<b>e</b>nt /ˈnjuːtriənt/ → âm yếu /ə/. Vậy <b>energy</b> khác ba từ còn lại. (Đề gốc dùng "strength" khiến có hai nhóm 2–2 nên đã thay bằng "surgery".)',
        },
    },
    'lop11-u1-botro': {
        'sp3.5': {'ans': ['B', 'D'], 'exp_add': '(Cả B và D đều là lời nhận lịch sự → hệ thống chấp nhận cả hai.)'},
    },
    # ------------------------------------------------------------------ UNIT 2
    'lop11-u2-botro': {
        'vg2.28': {'ans': ['A', 'B', 'C'], 'exp_add': '(mustn\'t, had better not, ought not to đều đúng ngữ pháp và nghĩa → chấp nhận cả ba.)'},
        'vg2.29': {'ans': ['B', 'D'], 'exp_add': '(must và have to đều đúng → chấp nhận cả hai.)'},
        'vg2.31': {'ans': ['A', 'B'], 'exp_add': '(must và have to đều chỉ nghĩa vụ → chấp nhận cả hai.)'},
        'vg2.35': {'ans': ['A', 'B'], 'exp_add': '(have to và must đều đúng → chấp nhận cả hai.)'},
        'vg2.39': {'ans': ['B', 'D'], 'exp_add': '(must và has to đều đúng → chấp nhận cả hai.)'},
        'kt.11': {'ans': ['B', 'C'], 'exp_add': '(must và have to đều đúng → chấp nhận cả hai.)'},
    },
    # ------------------------------------------------------------------ UNIT 3
    'lop11-u3-botro': {
        'vg1.2': {'ans': 'D', 'exp': 'Khu phố cổ giờ là khu dành cho người đi bộ → cụm chuẩn <b>pedestrian zone</b> (khu vực đi bộ). traffic/crossing/site không tạo thành cụm này. (Khoá Word ghi "site" là sai nên đã sửa.)'},
        're3.5': {'ans': 'T', 'exp': 'Đoạn 2: "The smart technology in self-driven cars will enable you to save on gas and other non-renewable energy sources." → xe tự lái giúp tiết kiệm năng lượng → <b>True</b>. (Khoá Word ghi F là sai nên đã sửa.)'},
        're3.8': {'ans': 'T', 'exp': 'Đoạn cuối: chi phí xây dựng thành phố thông minh "is going to be considerable" và Thủ tướng Ấn Độ "is pushing to attract investments to fuel rapid development projects" → <b>True</b>. (Khoá Word ghi F không khớp bài nên đã sửa.)'},
        'ph3.6': {'o': {3: 'telecommunication'}, 'ans': 'D',
                  'exp': 'teleconference /ˈtelɪkɒnfərəns/, television /ˈtelɪvɪʒn/, telephone /ˈtelɪfəʊn/ đều nhấn âm 1; <b>telecommunication</b> /ˌtelɪkəˌmjuːnɪˈkeɪʃn/ nhấn âm 4 (-ca-). (Đề gốc dùng "telephoto" cũng nhấn âm 1 nên cả 4 từ trùng → đã thay.)'},
        'sp4.4': {'ans': 'No doubt', 'exp': '"<b>No doubt</b> that is the jacket…" = chắc chắn đó là chiếc áo khoác… ("I wonder" phải đi với if/whether, "I\'m sure" cần "that" nhưng không hợp nghĩa ở đây). (Khoá Word chọn "I wonder" là sai nên đã sửa.)'},
        'vg3.8': {'ans': ['A', 'D'], 'exp_add': '(latest cũng gần nghĩa với advanced → chấp nhận cả A và D.)'},
        'vg6.11': {'ans': ['depend', 'am depending', "'m depending"], 'exp': 'I <b>depend</b> on you (cách dùng thông thường, hiện tại đơn). Dạng "am depending" cũng được chấp nhận.'},
        'vg6.13': {'ans': ['am seeing', "'m seeing", 'see'], 'exp': 'I <b>am seeing</b> double (đang nhìn thấy hai hình – tạm thời); "I see double" cũng được chấp nhận.'},
    },
    'lop11-u3-4kn': {
        'kt.45': {'ans': 'B', 'exp': 'Câu hỏi "can be inferred" về vai trò của nhà phát triển: bài viết nói họ cần cân nhắc các thách thức hạ tầng và cân bằng giữa chất lượng sống với quyền riêng tư → <b>B</b>. (Khoá Word ghi C là sai nên đã sửa.)'},
        'wr2.1': {'o': {1: 'Information about people and their activities is collected by sensors and cameras.'},
                  'exp': 'Câu gốc chủ động → B là câu bị động tương ứng: Information… <b>is collected</b> by… (information không đếm được nên dùng "is"). C thiếu động từ "to be"; A, D sai nghĩa. (Đã sửa "are" thành "is".)'},
    },
}
