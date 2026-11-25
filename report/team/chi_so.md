# Đặc tả chỉ số, event và rủi ro kinh tế · Nhiệm vụ E1, E2

## E1 · Đặc tả chỉ số

| Loại | Chỉ số | Công thức | Tính thử trên 1.200 yêu cầu |
| --- | --- | --- | --- |
| Chính (kết quả) | % yêu cầu đóng trong 24 giờ và không mở lại trong 7 ngày | `dong_trong_24h == 1` và `mo_lai_trong_7_ngay == 0`, chia tổng số yêu cầu | 82,83% (994 / 1.200) |
| Dùng | Tỉ lệ bỏ qua gợi ý | `quyet_dinh_xem_lai` là `sua` hoặc `bo`, chia số yêu cầu được xem lại | 27,12% (48 / 177) |
| An toàn | Tỉ lệ lỗi lọt đến khách | `mo_lai_trong_7_ngay == 1`, chia tổng số yêu cầu | 4,25% (51 / 1.200) |
| Dùng | Nhóm tự đề xuất: % yêu cầu của nhóm can thiệp được mở bằng trợ lý | Số yêu cầu có event `agent_suggestion_shown` chia tổng số yêu cầu của nhóm can thiệp | Không cần tính |
| An toàn | Nhóm tự đề xuất: % đơn hoàn sai tiền qua kiểm tra mẫu hằng tuần | Số đơn lệch số tiền trong `audit_sample_checked` chia tổng số đơn kiểm tra mẫu | Không cần tính |

Chỉ số trong đợt chạy thử là 82,83% (không viết "trợ lý đã nâng chỉ số" vì đợt chạy thử không có nhóm đối chứng).

## Danh sách event

Mỗi event đều có `trace_id` để nối với trace của agent.

| Event | Ai tạo | Thuộc tính chính | Thời điểm |
| --- | --- | --- | --- |
| `refund_request_created` | App khách | `request_id, loai, so_tien_vnd, arm, trace_id` | Khi khách gửi yêu cầu |
| `agent_run_completed` | Agent | `attempt, tokens_in, tokens_out, tool_calls, status, trace_id` | Sau mỗi lần chạy, kể cả lỗi |
| `agent_suggestion_shown` | Giao diện nhân viên | `staff_id, so_tien_de_xuat, trace_id` | Khi gợi ý của trợ lý hiện ra |
| `staff_review_decision` | Nhân viên | `quyet_dinh (giu/sua/bo), phut_xem_lai, trace_id` | Khi nhân viên bấm giữ, sửa hoặc bỏ |
| `staff_rework_completed` | Nhân viên | `phut_lam_lai, ly_do, trace_id` | Khi nhân viên làm lại xong |
| `refund_ledger_write` | Dịch vụ sổ cái | `idempotency_key, so_tien, ket_qua, trace_id` | Khi ghi giao dịch hoàn tiền |
| `handoff_to_staff` | Agent | `reason, tom_tat, trace_id` | Khi chuyển yêu cầu sang nhân viên |
| `ticket_closed` | Hệ thống ticket | `closed_at, trace_id` | Khi đóng yêu cầu |
| `ticket_reopened` | Khách hàng | `reopened_at, reason, trace_id` | Khi khách mở lại yêu cầu |
| `audit_sample_checked` | Kế toán | `so_tien_da_hoan, so_tien_dung, trace_id` | Kiểm tra mẫu hằng tuần |

**Kiểm tra chéo:**
- Chỉ số chính (`82,83%`): tính từ `refund_request_created`, `ticket_closed`, `ticket_reopened`.
- Tỉ lệ bỏ qua gợi ý (`27,12%`): tính từ `agent_suggestion_shown` và `staff_review_decision`.
- Tỉ lệ lỗi lọt đến khách (`4,25%`): tính từ `refund_request_created` và `ticket_reopened`.
- Chỉ số dùng tự đề xuất: tính từ `refund_request_created` và `agent_suggestion_shown`.
- Chỉ số an toàn tự đề xuất: tính từ `audit_sample_checked`.

## E2 · Rủi ro kinh tế

Số lấy trực tiếp từ bảng độ nhạy (`bang_chi_phi.md`).

| Rủi ro | Tác động đã tính | Dấu hiệu theo dõi | Hành động | Người phụ trách |
| --- | --- | --- | --- | --- |
| Số ca làm lại tăng gấp đôi | +51,8%, tăng từ 4.472 đ lên 6.787 đ/việc (simulated) | Tỉ lệ làm lại theo tuần > 7% (đợt chạy thử: 4,9% trong phạm vi) | Thu hẹp về `noi_dia`, rà soát 20 trace làm lại gần nhất | PM trợ lý hoàn phí |
| Phải xem lại 100% kéo dài | 11.743 đ = 0,98× (với 9 phút làm lại) hoặc 12.414 đ = 1,03× nếu làm lại 15,3 phút như trung bình dữ liệu (simulated) | % yêu cầu được xem lại còn > 50% cuối bước rollout 0.25 | Giảm tỉ lệ xem lại theo bậc khi tỉ lệ sửa + bỏ < 15% và rút thời gian xem lại ≤ 4,8 phút | Trưởng nhóm CSKH |
| Khối lượng thấp hơn dự kiến | Chi phí cố định 40 triệu/tháng: +1.185 đ/việc ở 45.000 yc/tháng, +2.370 đ/việc nếu còn một nửa (simulated) | Số việc thành công theo tuần < 50% kế hoạch | Tạm dừng mở rộng pilot, rà soát hợp đồng chi phí cố định | PM trợ lý hoàn phí |
