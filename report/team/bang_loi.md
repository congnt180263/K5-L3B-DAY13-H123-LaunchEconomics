# Bảng lỗi và cách khắc phục · Nhiệm vụ C

20 ca lỗi nằm trong `docs/Ngay13_Lab13_De_bai_hoc_vien.docx`. Năm loại theo Google PAIR: **Do người dùng · Hệ thống · Ngữ cảnh · Giới hạn hệ thống · Ngầm**. Gắn nhãn theo nguyên nhân gốc, không theo chỗ cần sửa.

## Hai bộ nhãn độc lập

Người gắn nhãn 1: *Đồng Văn Quyến*· Người gắn nhãn 2: *Trần Hữu Tài* (gắn độc lập trong 8 phút, không trao đổi)

| Ca | Nhãn người 1 | Nhãn người 2 | Trùng? | Nhãn thống nhất |
| --: | --- | --- | --- | --- |
| 1 | Do người dùng | Do người dùng | Có | Do người dùng |
| 2 | Hệ thống | Hệ thống | Có | Hệ thống |
| 3 | Ngữ cảnh | Ngữ cảnh | Có | Ngữ cảnh |
| 4 | Giới hạn hệ thống | Giới hạn hệ thống | Có | Giới hạn hệ thống |
| 5 | Ngầm | Ngầm | Có | Ngầm |
| 6 | Do người dùng | Hệ thống | Không | Do người dùng |
| 7 | Hệ thống | Hệ thống | Có | Hệ thống |
| 8 | Hệ thống | Ngầm | Không | Hệ thống |
| 9 | Do người dùng | Do người dùng | Có | Do người dùng |
| 10 | Ngữ cảnh | Ngữ cảnh | Có | Ngữ cảnh |
| 11 | Giới hạn hệ thống | Giới hạn hệ thống | Có | Giới hạn hệ thống |
| 12 | Ngầm | Ngầm | Có | Ngầm |
| 13 | Giới hạn hệ thống | Hệ thống | Không | Giới hạn hệ thống |
| 14 | Do người dùng | Do người dùng | Có | Do người dùng |
| 15 | Hệ thống | Hệ thống | Có | Hệ thống |
| 16 | Ngữ cảnh | Ngữ cảnh | Có | Ngữ cảnh |
| 17 | Ngầm | Ngầm | Có | Ngầm |
| 18 | Ngữ cảnh | Ngữ cảnh | Có | Ngữ cảnh |
| 19 | Giới hạn hệ thống | Giới hạn hệ thống | Có | Giới hạn hệ thống |
| 20 | Hệ thống | Hệ thống | Có | Hệ thống |

**Tỉ lệ đồng thuận:** 17 / 20 = 85% (đạt yêu cầu ≥ 80%). Ba ca không trùng: 6, 8, 13.

**Phân bố sau thống nhất:** Do người dùng (4 ca: 1, 6, 9, 14) · Hệ thống (5 ca: 2, 7, 8, 15, 20) · Ngữ cảnh (4 ca: 3, 10, 16, 18) · Giới hạn hệ thống (4 ca: 4, 11, 13, 19) · Ngầm (3 ca: 5, 12, 17).

## Quy tắc phân biệt cho các ca không trùng

- **Ca 6 (Do người dùng, không phải Hệ thống):** Gốc lỗi là khách chọn sai mục đầu vào ("Hoàn phí giao trễ" thay vì hàng vỡ); việc trợ lý chưa phát hiện mâu thuẫn để gợi ý lại nằm ở cột khắc phục.
- **Ca 8 (Hệ thống, không phải Ngầm):** Lỗi đã lộ ra trực tiếp trong câu trả lời (trích dẫn "Điều 7.2" không tồn tại); nhãn Ngầm chỉ dùng khi không ai nhận ra cho tới khi kiểm tra mẫu hoặc đối soát chi phí.
- **Ca 13 (Giới hạn hệ thống, không phải Hệ thống):** Yêu cầu thuộc sản phẩm bảo hiểm đối tác ngoài phạm vi xử lý của trợ lý nên gốc là giới hạn hệ thống, dù trợ lý xử lý giới hạn đó chưa tốt.

## Bảng khắc phục cho 5 ca, mỗi loại một ca

Cách phát hiện đo được (event, ngưỡng, tần suất). Người phụ trách là một vai trò có quyền quyết định.

| Ca | Loại lỗi | Phát hiện bằng gì | Khắc phục thế nào | Ai phụ trách |
| --: | --- | --- | --- | --- |
| 9 | Do người dùng | Event `input_validation_failed` (mã đơn không đúng định dạng vận đơn); cảnh báo khi > 2% tổng yêu cầu/ngày | Tự nhận diện mã sàn TMĐT để tra sang mã vận đơn; nếu không tra được thì hiển thị hướng dẫn kèm ảnh minh hoạ | PM trợ lý hoàn phí |
| 7 | Hệ thống | Đối soát tự động mỗi giờ giữa thông báo "đã hoàn" và event `refund_ledger_write` (`ket_qua = ok`) cùng `trace_id`; ngưỡng 0 ca lệch | Chỉ báo "đã hoàn" khi sổ cái trả `ok`; gặp lỗi 503 sau tối đa 2 lần chạy thì báo "đang xử lý" và phát `handoff_to_staff` | Kỹ sư trưởng agent |
| 18 | Ngữ cảnh | Theo dõi hằng tuần tỉ lệ `ticket_reopened` có `reason = thieu_tien` nhưng kiểm tra thấy số tiền đúng chính sách; ngưỡng > 1%/tuần | Sửa mẫu tin nhắn luôn hiển thị công thức tính rõ ràng (ví dụ: `30.000 đ × 50% = 15.000 đ`) | Trưởng nhóm CSKH |
| 4 | Giới hạn hệ thống | Theo dõi hằng ngày tỉ lệ event `handoff_to_staff` với `reason = thieu_du_lieu` tách theo `loai`; ngưỡng > 10% trong phạm vi pilot | Giữ luồng chuyển nhân viên kèm tóm tắt đầy đủ; loại nhóm `quoc_te` khỏi phạm vi pilot | PM trợ lý hoàn phí |
| 17 | Ngầm | Event `audit_sample_checked` kiểm tra mẫu 100 đơn/tuần so với bảng giá hiện hành; ngưỡng cảnh báo > 1% đơn lệch tiền | Tự động xoá bộ nhớ đệm khi cập nhật bảng giá mới và ghi phiên bản bảng giá vào `trace_id` | Kế toán trưởng |
