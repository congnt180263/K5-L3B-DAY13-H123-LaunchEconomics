# Báo cáo nhóm

Báo cáo ngắn, tối đa 2 trang. Số liệu chi tiết nằm trong các file hồ sơ; ở đây chỉ dẫn lại con số chính.

## 1. Thông tin nhóm

- Tên nhóm: H123
- Lớp: L3B
- Thành viên: xem `TEAM.md`

## 2. Mục tiêu và cách tiếp cận

Xây dựng bộ hồ sơ launch v0 cho trợ lý hoàn phí LogiX-VN (Gate 2a) nhằm trả lời 4 câu hỏi: hiệu quả kinh tế thực tế so với nhân viên tự làm (`12.000 đ/yêu cầu`), chỉ số sử dụng và bộ event theo dõi, phân loại lỗi và cách khắc phục, và thiết kế pilot tách được tác động. Nhóm dùng `src/lab13.py` để tính toàn bộ chi phí từ dữ liệu giả lập (`1.200` yêu cầu, `1.624` lần chạy) và thiết kế kế hoạch pilot theo cụm nhân viên.

## 3. Giải pháp

- **Nhiệm vụ A & B ([bang_chi_phi.md](bang_chi_phi.md)):** Hoàn thiện `src/lab13.py` đạt 3 phép thử A1 (`1,20 · 1,25 · 1,25`), xây dựng `mo_hinh` tính cả token, tool, giờ xem lại, làm lại trên mọi lần chạy; phân tách theo `loai`, cộng chi phí cố định `40 triệu/tháng`, phân tích độ nhạy 9 kịch bản, giới hạn chạy lại và kịch bản xem lại 100%.
- **Nhiệm vụ C ([bang_loi.md](bang_loi.md)):** Hai thành viên gắn nhãn độc lập 20 ca lỗi theo 5 loại Google PAIR (đồng thuận `17/20 = 85%`), thống nhất quy tắc phân biệt các ca không trùng (ca 6, 8, 13) và lập bảng khắc phục 5 ca (mỗi loại một ca, có cách phát hiện đo được và 1 vai trò phụ trách).
- **Nhiệm vụ D ([pilot_plan.yaml](pilot_plan.yaml)):** Tính cỡ mẫu 5 kịch bản trong `src/lab13.py` (`co_mau` và `statsmodels`), chọn chia ngẫu nhiên theo nhân viên (`20 + 20`), chấp nhận MDE 6 điểm (`n_per_arm = 859`, `m >= 299`, `DE = 6,96`) và viết 3 luật dừng đủ 4 vế.
- **Nhiệm vụ E ([chi_so.md](chi_so.md), [ho_so_launch_v0.md](ho_so_launch_v0.md)):** Đặc tả 5 chỉ số, 10 event có `trace_id`, 3 rủi ro kinh tế và tổng hợp hồ sơ 1 trang với đề xuất **Go có điều kiện**.

## 4. Kết quả

- **Chi phí (simulated):** `4.472 đ/việc` toàn bộ (gấp `16,3×` hóa đơn token+tool/yêu cầu `275 đ`); chi phí cả hệ thống `5.865 đ/yc` (`0,49×` của `12.000 đ`). Phạm vi `noi_dia + hang_nang` cộng cố định ở `45.000 yc/tháng` đạt `4.599 đ/việc` (`0,38×`). Ba yếu tố nhạy nhất: số ca làm lại (`+51,8%`), tỉ lệ xem lại (`+40,7%`), lương nhân viên (`+23,1%`). Nếu xem lại 100%: `11.743 đ/việc` (`0,98×`, với 9 phút làm lại) hoặc `12.414 đ/việc` (`1,03×`, với 15,3 phút làm lại trung bình dữ liệu, simulated).
- **Chỉ số đợt chạy thử:** Chỉ số chính `82,83%` (`994/1.200`), bỏ qua gợi ý `27,12%` (`48/177`), mở lại trong 7 ngày `4,25%` (`51/1.200`).
- **Đề xuất Gate 2a:** **Go có điều kiện** cho pilot `noi_dia + hang_nang` (loại `quoc_te` `1,88×` và `doi_tac` `0,85×`, simulated).
- **Kết quả duyệt chéo nhận từ hội đồng:** *(Điền sau buổi duyệt chéo 17:00)*

## 5. Khó khăn và cách xử lý

- Với 40 nhân viên hiện có, không cách chia theo cụm nào đủ mẫu cho mức chênh 5 điểm (`20 / 0,02 = 1.000 < 1.251`). Nhóm xử lý bằng cách chọn chia theo nhân viên (đạt 20 cụm/nhóm để tách tác động), nâng MDE lên 6 điểm (`n = 859`, `m >= 299`) và ghi rõ rủi ro power giảm còn `~0,64` ở mức 5 điểm.
- Chênh lệch giữa dữ liệu giả lập (`phut_xem_lai_simulated`, `phut_lam_lai_simulated`) và thực tế: nhóm gắn nhãn `simulated` ở mọi con số liên quan và yêu cầu đo phút thật từ event sau tuần 1.

## 6. Tổng hợp đóng góp

Chi tiết đóng góp của từng thành viên nằm trong `TEAM.md`.

## 7. Hạn chế và hướng cải thiện

- Dữ liệu chạy thử chưa có nhóm đối chứng nên không kết luận được mức tăng chỉ số chính; cần chạy pilot ngẫu nhiên có đối chứng để kiểm chứng.
- Cần thu thập thời gian xem lại/làm lại thực tế qua `staff_review_decision` và `staff_rework_completed` để thay thế số liệu `simulated`.

## 8. Tài liệu tham khảo

- Erol và cộng sự, *Cost-of-Pass: An Economic Framework for Evaluating Language Models*, arxiv.org/abs/2504.13359
- Google PAIR, *People + AI Guidebook*, chương "Errors + Graceful Failure"
- Tài liệu `statsmodels` (`NormalIndPower`, `proportion_effectsize`)
