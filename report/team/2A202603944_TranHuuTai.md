# Báo cáo cá nhân — TranHuuTai-2A202603944

## 1. Thông tin thành viên

- Họ tên: Trần Hữu Tài
- MSSV: 2A202603944
- Email: taitran04.work@gmail.com
- Vai trong nhóm: người viết code (trước giải lao), người gắn nhãn 2

## 2. Phần việc phụ trách

- CP1: Nhiệm vụ A (A1–A4) trong `src/lab13.py`.
- CP2: Nhiệm vụ B (B1–B4) và điền `report/team/bang_chi_phi.md`.
- CP3: gắn nhãn độc lập 20 ca lỗi (người gắn nhãn 2).

## 3. Đóng góp cụ thể

- A1: viết ba hàm kỳ vọng hình học: số lần chạy = (1 − (1 − p)^k) / p, tỉ lệ thành công = 1 − (1 − p)^k, hệ số chi phí = số lần chạy / tỉ lệ thành công.
- A2: viết `mo_hinh` cộng token, tool, phút xem lại và làm lại trên mọi lần chạy, kể cả lần lỗi: tổng 4.373.585 đ, 978 việc thành công, 4.472 đ/việc (0,37×, simulated).
- A3: tách theo loại; `quoc_te` 22.515 đ/việc (1,88×) đắt hơn nhân viên, nên đề xuất loại khỏi pilot (simulated).
- A4: cộng phí cố định 40 triệu/tháng cho `noi_dia + hang_nang`: 4.599 đ/việc ở 45.000 yêu cầu/tháng (simulated).
- B1–B4: độ nhạy (làm lại gấp đôi +51,8%, token gấp đôi chỉ +5,6%); giới hạn tối đa 2 lần chạy rẻ nhất cả hệ thống, 6.901.220 đ; xem lại 100% còn 0,98× (simulated).
- CP3: gắn nhãn 20 ca độc lập, khác người gắn nhãn 1 ở ca 6, 8, 13; đồng thuận 17/20 = 85%.

## 4. Bằng chứng

- Commit `c28d3c4` "CP1 + CP2" (merge qua PR #1): `src/lab13.py`, `report/team/bang_chi_phi.md`.
- Cột "Nhãn người 2" trong `report/team/bang_loi.md`.
- Output `cd src && python lab13.py`: ba phép thử A1 in ĐẠT (1,20 · 1,25 · 1,25).

## 5. Công cụ AI đã dùng

- Claude (trợ lý lập trình): gợi ý code cho A1–A4, B1–B4 và soát cách trình bày bảng trong `bang_chi_phi.md`.
- Tự kiểm tra: chạy ba phép thử đáp án biết trước của A1; tính tay lại một số (A2: 4.373.585 / 978 = 4.472 đ) để đối chiếu với output; mọi số trong hồ sơ lấy từ output `lab13.py`.
- Không dùng AI để gắn nhãn CP3: nhãn tự gắn trong 8 phút, không trao đổi trước khi so.

## 6. Tự đánh giá

- Hoàn thành CP1, CP2 đúng hạn; code chạy hết, 3/3 phép thử ĐẠT.
- Điểm học được: chi phí nằm chủ yếu ở công người (làm lại 51,8%, xem lại 40,7% độ nhạy), không ở token; chạy lại không cứu được loại có tỉ lệ đúng thấp như `quoc_te`.
- Cần cải thiện: một số tỉ lệ phụ (16,3×) tôi tính bằng lệnh riêng, lần sau nên đưa vào `lab13.py` để in trực tiếp.
