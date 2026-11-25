# Báo cáo cá nhân — NguyenThanhCong-2A202603789

## 1. Thông tin thành viên

- Họ tên: Nguyễn Thành Công
- MSSV: 2A202603789
- Email: congc3c1@gmail.com
- Vai trong nhóm: nhóm trưởng; người viết code sau giải lao; người kiểm số

## 2. Phần việc phụ trách

- Tạo repo nhóm, review và merge pull request của các thành viên.
- CP4: Nhiệm vụ D, cỡ mẫu pilot (D1 trong `src/lab13.py`) và `report/team/pilot_plan.yaml`.
- Kiểm số: đối chiếu con số trong hồ sơ với output `lab13.py`.

## 3. Đóng góp cụ thể

- D1: tính 5 kịch bản cỡ mẫu (p1 = 0,70; alpha = 0,05; power = 0,80; ICC = 0,02): theo yêu cầu n = 1.251/nhóm; theo nhân viên m = 75 thì DE = 2,48, cần 84 người > 40; 20 người/nhóm chỉ đạt giới hạn 1.000 < 1.251.
- Chọn thiết kế chia ngẫu nhiên theo nhân viên 20 + 20, chấp nhận MDE 6 điểm: n = 859/nhóm, m ≥ 299, DE = 6,96; power ở +5 điểm chỉ 0,64.
- Viết `pilot_plan.yaml` không còn dấu `?`, 3 luật dừng đủ NẾU – TRONG – THÌ – KHÔNG THÌ; kiểm bằng `yaml.safe_load`.

## 4. Bằng chứng

- Commit `e7ee186` "finish CP4" (merge qua PR #2): `src/lab13.py`, `report/team/pilot_plan.yaml`.
- Merge PR #1 (CP1 + CP2) và PR #3 (CP5) vào `main`.

## 5. Công cụ AI đã dùng

- [Tự điền: công cụ AI đã dùng, dùng vào việc gì.]
- Tự kiểm tra: so output D1 với đáp án hướng dẫn (1.251 · 2,48 · 1.000 · 300 · 0,64); chạy `yaml.safe_load` cho `pilot_plan.yaml`.

## 6. Tự đánh giá

- Hoàn thành CP4; số D1 khớp 5/5 kịch bản với hướng dẫn.
- Điểm học được: chia ngẫu nhiên theo nhân viên làm cỡ mẫu tăng mạnh (DE từ 2,48 lên 6,96), nên phải đổi MDE hoặc kéo dài pilot.
