# Bảng chi phí · Nhiệm vụ A và B

Số tính bằng `src/lab13.py`. Mọi con số tính từ cột `_simulated` ghi nhãn `simulated`. Mỗi câu trả lời không quá ba dòng, có ít nhất một con số.

## A1 · Ba phép thử đáp án biết trước

| Phép thử (p = 0,8) | Kết quả của nhóm |
| --- | --- |
| Số lần chạy trung bình, tối đa 2 lần | 1,20 lần (ĐẠT) |
| Số lần chạy trung bình, chạy đến khi đúng | 1,25 lần (ĐẠT) |
| Hệ số chi phí mỗi việc thành công, tối đa 3 lần | 1,25 × giá một lần chạy (ĐẠT) |

## A2 · Mô hình chi phí từ trace

| Khoản | Số tiền (đ) | Nguồn | Nhãn |
| --- | ---: | --- | --- |
| Token | 245.585 | `logix_runs.csv` | đo từ trace |
| Tool | 84.000 | `logix_runs.csv` | đo từ trace |
| Trong đó, phần của lần chạy thứ 2 và 3 | 93.804 | attempt lớn hơn 1 | đo từ trace |
| Xem lại | 1.780.000 | `phut_xem_lai_simulated` | simulated |
| Làm lại | 2.264.000 | `phut_lam_lai_simulated` | simulated |
| Tổng chi phí | 4.373.585 | | simulated |
| Số việc thành công | 978 / 1.200 | `ket_qua` | |
| Chi phí mỗi việc thành công | 4.472 | | simulated |
| Hoá đơn token và tool chia cho số yêu cầu | 275 | | đo từ trace |

- Chi phí mỗi việc thành công gấp bao nhiêu lần "hoá đơn chia số yêu cầu"? Gấp khoảng 16,3 lần (4.472 đ so với 275 đ, simulated); hoá đơn token chỉ là phần nhỏ.
- Khoản nào chiếm tỉ trọng lớn nhất trong tổng chi phí, bao nhiêu phần trăm? Làm lại: 2.264.000 đ, 51,8% tổng (simulated); xem lại đứng thứ hai với 40,7%.

## A3 · Tách theo loại yêu cầu

| Loại | Số yêu cầu | Tỉ lệ thành công | Số lần chạy mỗi yêu cầu | Chi phí mỗi việc thành công | So với 12.000 đ |
| --- | ---: | ---: | ---: | ---: | ---: |
| noi_dia | 824 | 95,0% | 1,11 | 2.696 | 0,22× |
| hang_nang | 158 | 74,1% | 1,47 | 8.221 | 0,69× |
| quoc_te | 150 | 27,3% | 2,32 | 22.515 | 1,88× |
| doi_tac | 68 | 54,4% | 1,88 | 10.215 | 0,85× |

Tất cả là số simulated. Cả hệ thống (việc không thành công tính 12.000 đ): 5.865 đ mỗi yêu cầu, 0,49×.

- Loại nào không đáng để trợ lý xử lý? Với loại đó, cho chạy lại tới 3 lần có giúp không? quoc_te tốn 1,88× nhân viên (simulated). Chạy lại không giúp: tỉ lệ đúng giảm từ 30,0% ở lần 1 xuống 2,2% ở lần 3, chỉ 27,3% thành công.

## A4 · Chi phí cố định (phạm vi noi_dia + hang_nang)

| Khối lượng | Việc thành công mỗi tháng | Chi phí cố định mỗi việc | Chi phí mỗi việc thành công + cố định | So với 12.000 đ |
| --- | ---: | ---: | ---: | ---: |
| 45.000 yêu cầu/tháng | 33.750 | 1.185 | 4.599 | 0,38× |
| Một nửa khối lượng | 16.875 | 2.370 | 5.784 | 0,48× |

- Chi phí cố định có đổi kết luận không? Ở khối lượng nào? Không đổi: kể cả ở một nửa khối lượng vẫn 0,48× (simulated). Phải giảm còn khoảng 6.200 yêu cầu/tháng thì mới hoà 12.000 đ.

## B1 · Đổi từng yếu tố

Gốc (A2): 4.472 đ mỗi việc thành công (simulated).

| Kịch bản | Cách tính | Chi phí mỗi việc thành công | Thay đổi (%) |
| --- | --- | ---: | ---: |
| Giá token gấp đôi | 52 đ và 260 đ cho 1.000 token; giá tool giữ nguyên | 4.723 | +5,6% |
| Giá token giảm một nửa | 13 đ và 65 đ | 4.346 | −2,8% |
| Tỉ lệ xem lại gấp đôi | Tiền xem lại × 2 | 6.292 | +40,7% |
| Tỉ lệ xem lại giảm một nửa | Tiền xem lại ÷ 2 | 3.562 | −20,3% |
| Số ca làm lại gấp đôi | Tiền làm lại × 2 | 6.787 | +51,8% |
| Số ca làm lại giảm một nửa | Tiền làm lại ÷ 2 | 3.315 | −25,9% |
| Lương nhân viên tăng 25% | 2.500 đ mỗi phút | 5.506 | +23,1% |
| Chỉ cho chạy tối đa 2 lần | Bỏ lần chạy có attempt > 2; yêu cầu có so_lan_chay > 2 coi là chuyen_nhan_vien | 4.237 | −5,2% |
| Chỉ cho chạy 1 lần | Như trên với giới hạn 1 | 4.111 | −8,1% |

## B2 · Đổi một cặp và xếp hạng

- Giá token gấp đôi cùng lúc tỉ lệ xem lại gấp đôi: 6.543 đ, +46,3% (simulated), xấp xỉ tổng hai tác động riêng (+5,6% và +40,7%).
- Xếp hạng ba yếu tố ảnh hưởng mạnh nhất: 1. Số ca làm lại (+51,8%) · 2. Tỉ lệ xem lại (+40,7%) · 3. Lương nhân viên (+23,1%).

## B3 · Giới hạn chạy lại có thật sự rẻ hơn

| Giới hạn | Tổng chi phí trợ lý | Số yêu cầu không thành công | Chi phí cả hệ thống | Chi phí mỗi việc thành công |
| --- | ---: | ---: | ---: | ---: |
| 1 lần | 3.621.781 | 319 | 7.449.781 | 4.111 |
| 2 lần | 4.093.220 | 234 | 6.901.220 | 4.237 |
| 3 lần | 4.373.585 | 222 | 7.037.585 | 4.472 |

Tất cả là số simulated; việc không thành công tính 12.000 đ.

- Giới hạn nào rẻ nhất cho công ty? Có trùng với giới hạn cho chi phí mỗi việc thành công thấp nhất không? 2 lần rẻ nhất cả hệ thống: 6.901.220 đ (simulated). Không trùng: chi phí mỗi việc thành công thấp nhất ở 1 lần (4.111 đ) vì 319 ca bị đẩy sang nhân viên.

## B4 · Nếu phải xem lại tất cả

- Chi phí mỗi việc thành công khi xem lại 100% (`noi_dia` + `hang_nang`), so với 12.000 đ: 11.743 đ, 0,98× (simulated); 948 ca × 5 phút cộng 48 ca làm lại × 9 phút.
- Kết quả này nói gì về thứ pilot cần học được? Pilot phải đo được ngưỡng tin cậy để bỏ xem lại phần lớn ca; nếu vẫn phải xem lại 100% thì lợi thế gần như bằng 0 (chỉ tiết kiệm 2%).
