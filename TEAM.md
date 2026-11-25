# Team

## Thông tin nhóm

- Tên nhóm: H123
- Lớp: L3B
- Repo nhóm: `K5-L3B-DAY13-H123-LaunchEconomics` (xem [SUBMISSION.md](SUBMISSION.md))
- URL repo, nhánh nộp, commit chốt: https://github.com/congnt180263/K5-L3B-DAY13-H123-LaunchEconomics · nhánh `main` · commit chốt: commit cuối trên `main` trước 23h59

## Thành viên

| STT | Họ tên | MSSV | Email | GitHub | Vai trò |
| --: | ------ | ---- | ----- | ------ | ------- |
|   1 | Nguyễn Thành Công | 2A202603789 | congc3c1@gmail.com | congnt180263 | Nhóm trưởng; người viết code sau giải lao (CP4); người kiểm số |
|   2 | Đồng Văn Quyến | 2A202603769 | quyenv2609@gmail.com | dvquyen2609 | Người gắn nhãn 1; giữ hồ sơ launch (CP5) |
|   3 | Trần Hữu Tài | 2A202603944 | taitran04.work@gmail.com | taitran04work | Người viết code trước giải lao (CP1, CP2); người gắn nhãn 2 |

Nhóm có 3 thành viên nên vai "người kiểm số" do Nguyễn Thành Công kiêm, vai "giữ hồ sơ" do Đồng Văn Quyến kiêm. Người viết code đổi sau giờ giải lao (Tài → Công), nên hai người tự tính được chi phí.

## Cá nhân

Báo cáo riêng của từng thành viên:

- `report/team/2A202603789_NguyenThanhCong.md`
- `report/team/2A202603769_DongVanQuyen.md`
- `report/team/2A202603944_TranHuuTai.md`

## Nguyễn Thành Công - 2A202603789

### Phần việc phụ trách

- Nhóm trưởng: tạo repo nhóm, review và merge pull request.
- CP4: cỡ mẫu pilot D1 trong `src/lab13.py` và `report/team/pilot_plan.yaml`.
- Kiểm số: đối chiếu số trong hồ sơ với output `lab13.py`.

### Đóng góp cụ thể

- Viết phần D1 (5 kịch bản cỡ mẫu): n = 1.251/nhóm; chọn chia theo nhân viên 20 + 20, MDE 6 điểm, n = 859/nhóm, DE = 6,96.
- Viết `pilot_plan.yaml` với 3 luật dừng đủ NẾU – TRONG – THÌ – KHÔNG THÌ.

### Bằng chứng

- Commit `e7ee186` "finish CP4", merge PR #2.

## Đồng Văn Quyến - 2A202603769

### Phần việc phụ trách

- CP3: người gắn nhãn 1 cho 20 ca lỗi.
- CP5: `chi_so.md`, `ho_so_launch_v0.md`, `group_report.md`.

### Đóng góp cụ thể

- Gắn nhãn độc lập 20 ca; đồng thuận với người gắn nhãn 2 là 17/20 = 85%; viết quy tắc phân biệt ca 6, 8, 13 và bảng khắc phục 5 ca.
- Viết hồ sơ launch v0 bảy mục, đề xuất Go có điều kiện; chỉ số chính 82,83% (994/1.200).

### Bằng chứng

- Commit `8fb6082` "cp5 complete", merge PR #3.

## Trần Hữu Tài - 2A202603944

### Phần việc phụ trách

- CP1, CP2: Nhiệm vụ A (A1–A4) và B (B1–B4) trong `src/lab13.py`, `report/team/bang_chi_phi.md`.
- CP3: người gắn nhãn 2 cho 20 ca lỗi.

### Đóng góp cụ thể

- Viết hàm kỳ vọng số lần chạy và `mo_hinh`; ba phép thử A1 ĐẠT (1,20 · 1,25 · 1,25).
- Tính chi phí mỗi việc thành công 4.472 đ (0,37× so với 12.000 đ, simulated), độ nhạy B1 và giới hạn chạy lại B3 (tối đa 2 lần rẻ nhất, 6.901.220 đ, simulated).

### Bằng chứng

- Commit `c28d3c4` "CP1 + CP2", merge PR #1.
