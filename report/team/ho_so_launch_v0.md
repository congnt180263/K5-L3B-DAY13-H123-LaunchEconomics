# Hồ sơ launch v0 · Trợ lý hoàn phí LogiX-VN · Gate 2a

Một trang. Cột trạng thái chỉ nhận: **Xong, có bằng chứng · Chưa · Giả lập**. Mục nào dựa trên cột `_simulated` ghi Giả lập. Người phụ trách là một vai trò, không ghi "cả đội". Gate 2a chỉ duyệt kế hoạch pilot: không viết như thể trợ lý đã được duyệt chạy chính thức (xem quy tắc 5 trong `README.md`).

Nhóm: H123 · Lớp: L3B

| Mục | Con số chính | Trạng thái | Người phụ trách |
| --- | --- | --- | --- |
| 1 · Chi phí mỗi việc thành công | 4.472 đ/việc toàn bộ (gấp 16,3× hoá đơn token+tool 275 đ); phạm vi `noi_dia + hang_nang`: 3.414 đ + 1.185 đ cố định (45.000 yc/tháng) = 4.599 đ = 0,38× (simulated) | Giả lập | PM trợ lý hoàn phí |
| 2 · Ba yếu tố nhạy nhất | 1. Số ca làm lại (+51,8%) · 2. Tỉ lệ xem lại (+40,7%) · 3. Lương nhân viên (+23,1%) (simulated) | Giả lập | PM trợ lý hoàn phí |
| 3 · So với nhân viên tự làm | Cả hệ thống: 5.865 đ/yc (0,49× của 12.000 đ); nếu xem lại 100%: 11.743 đ (0,98×) hoặc 12.414 đ (1,03× với 15,3 phút làm lại) (simulated) | Giả lập | Giám đốc vận hành LogiX-VN |
| 4 · Chỉ số chính, chỉ số dùng, chỉ số an toàn | Đợt chạy thử: chính 82,83% · bỏ qua gợi ý 27,12% · mở lại 7 ngày 4,25%; 10 event có `trace_id` | Xong, có bằng chứng | Kỹ sư trưởng agent |
| 5 · Bảng lỗi và cách khắc phục | 20 ca lỗi (đồng thuận 17/20 = 85%), đủ 5 loại Google PAIR kèm 5 phương án phát hiện đo được và khắc phục (`bang_loi.md`) | Xong, có bằng chứng | Trưởng nhóm CSKH |
| 6 · Pilot plan | Chia ngẫu nhiên theo nhân viên (20 + 20), phạm vi `noi_dia + hang_nang`, MDE 6 điểm (n=859/nhóm, m≥299, DE=6,96; power ~0,64 ở mức 5 điểm), 3 luật dừng | Xong, có bằng chứng | Giám đốc vận hành LogiX-VN |
| 7 · Rủi ro kinh tế | Làm lại ×2 → 6.787 đ (+51,8%); xem lại 100% → 11.743–12.414 đ (0,98×–1,03×); giảm 50% khối lượng → +2.370 đ cố định (simulated) | Giả lập | PM trợ lý hoàn phí |

**Đề xuất:** Go có điều kiện (chỉ pilot cho phạm vi `noi_dia` 0,22× và `hang_nang` 0,69×; loại `quoc_te` 1,88× và `doi_tac` 0,85× — đều là số simulated).

- **Điều kiện 1:** Sửa khoá chống trùng và đối soát sổ cái (khắc phục ca 7, 20 trong `bang_loi.md`) trước khi mở pilot — Phụ trách: Kỹ sư trưởng agent — Kiểm tra: trước ngày bắt đầu pilot.
- **Điều kiện 2:** Giám đốc vận hành ký chấp nhận đánh đổi MDE 6 điểm (power giảm còn ~0,64 nếu tác động thật là 5 điểm) — Phụ trách: Giám đốc vận hành LogiX-VN — Kiểm tra: trước ngày bắt đầu pilot (mốc chốt quyết định `2027-01-05`).
- **Điều kiện 3:** Bật đủ 10 event có `trace_id` và thay phút `simulated` bằng phút đo thật sau tuần đầu tiên — Phụ trách: Kỹ sư trưởng agent — Kiểm tra: cuối tuần 1 pilot.
- **Điều kiện 4:** Áp dụng lộ trình giảm tỉ lệ xem lại theo bậc khi tỉ lệ sửa + bỏ < 15%, vì xem lại 100% tốn 0,98×–1,03× nhân viên (simulated) — Phụ trách: Trưởng nhóm CSKH — Kiểm tra: cuối bước rollout 0.25.
