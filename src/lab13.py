"""Lab 13 · Định giá agent và lập kế hoạch pilot (Gate 2a) — bài làm của nhóm (file nộp).
Chạy trong thư mục src/: python3 lab13.py   (cần pandas; Nhiệm vụ D cần thêm statsmodels)
Không cần khoá API. Điền các chỗ ghi VIẾT Ở ĐÂY (đánh dấu TODO CP1…CP4). Dữ liệu trong hai file CSV là giả lập.
Bản gốc chưa sửa nằm ở lab13_starter.py.
"""
import math
from statistics import NormalDist
import pandas as pd
from statsmodels.stats.proportion import proportion_effectsize
from statsmodels.stats.power import NormalIndPower

# Bảng giá GIẢ ĐỊNH của lab (không phải giá thật của nhà cung cấp nào)
GIA_VAO = 26        # đồng cho 1.000 token đầu vào
GIA_RA = 130        # đồng cho 1.000 token đầu ra
GIA_TOOL = 15       # đồng cho 1 lần gọi tool
LUONG_PHUT = 2000   # đồng cho 1 phút của nhân viên (đã gồm bảo hiểm, văn phòng)
BASELINE = 12000    # đồng cho 1 yêu cầu khi nhân viên tự làm (6 phút)


# ---------- Nhiệm vụ A1 · Kinh tế của việc chạy lại ----------
# TODO CP1: viết ba hàm dưới đây cho tới khi kiem_tra_dap_an_biet_truoc() in ĐẠT.
def so_lan_chay_ky_vong(p, k=None):
    """Số lần chạy trung bình cho 1 yêu cầu khi mỗi lần đúng với xác suất p.
    k = số lần chạy tối đa; k=None nghĩa là chạy lại đến khi đúng."""
    if k is None:
        return 1 / p
    return (1 - (1 - p) ** k) / p


def ti_le_thanh_cong(p, k=None):
    """Xác suất yêu cầu thành công sau tối đa k lần chạy."""
    if k is None:
        return 1.0
    return 1 - (1 - p) ** k


def he_so_chi_phi_moi_viec_thanh_cong(p, k=None):
    """Chi phí mỗi việc thành công, tính bằng bội số của giá một lần chạy."""
    return so_lan_chay_ky_vong(p, k) / ti_le_thanh_cong(p, k)


def kiem_tra_dap_an_biet_truoc():
    """Ba phép thử bắt buộc đạt 100% trước khi tính trên dữ liệu."""
    assert abs(so_lan_chay_ky_vong(0.8, 2) - 1.20) < 1e-9, 'p=0,8, tối đa 2 lần → 1,20 lần chạy'
    assert abs(so_lan_chay_ky_vong(0.8) - 1.25) < 1e-9, 'p=0,8, chạy đến khi đúng → 1,25 lần chạy'
    assert abs(he_so_chi_phi_moi_viec_thanh_cong(0.8, 3) - 1.25) < 1e-9, 'p=0,8, tối đa 3 lần → 1,25 lần giá một lần chạy'
    print('Ba phép thử đáp án biết trước: ĐẠT')


# ---------- Nhiệm vụ A2 · Mô hình chi phí từ trace ----------
# TODO CP1: viết mo_hinh; CP2 gọi lại hàm này với tham số giá và hệ số đã đổi.
def mo_hinh(runs, reqs, gia_vao=26, gia_ra=130, gia_tool=15, luong_phut=2000,
            he_so_xem_lai=1.0, he_so_lam_lai=1.0, max_lan_chay=None):
    """Trả về dict gồm: token, tool, xem_lai, lam_lai, tong, thanh_cong, cps (chi phí mỗi việc thành công).
    - token, tool: cộng trên MỌI lần chạy trong runs, kể cả lần lỗi.
    - xem_lai, lam_lai: số phút (cột *_simulated) × LUONG_PHUT. Đây là số GIẢ LẬP, phải ghi nhãn simulated khi báo cáo.
    - thanh_cong: số yêu cầu có ket_qua == 'thanh_cong'.
    - Các tham số giá/hệ số/max_lan_chay dùng cho Nhiệm vụ B (độ nhạy, giới hạn số lần chạy); giữ mặc định ở A2.
    """
    reqs = reqs.copy()
    runs = runs[runs['request_id'].isin(reqs['request_id'])]
    if max_lan_chay is not None:  # B1, B3: bỏ lần chạy vượt giới hạn; yêu cầu vượt → chuyển nhân viên
        runs = runs[runs['attempt'] <= max_lan_chay]
        vuot = reqs['so_lan_chay'] > max_lan_chay
        reqs.loc[vuot, 'ket_qua'] = 'chuyen_nhan_vien'
        reqs.loc[vuot, ['phut_xem_lai_simulated', 'phut_lam_lai_simulated']] = 0
    tien_token = runs['tokens_in'] / 1000 * gia_vao + runs['tokens_out'] / 1000 * gia_ra
    tien_tool = runs['tool_calls'] * gia_tool
    xem_lai = reqs['phut_xem_lai_simulated'].sum() * luong_phut * he_so_xem_lai
    lam_lai = reqs['phut_lam_lai_simulated'].sum() * luong_phut * he_so_lam_lai
    tong = tien_token.sum() + tien_tool.sum() + xem_lai + lam_lai
    thanh_cong = int((reqs['ket_qua'] == 'thanh_cong').sum())
    return dict(token=tien_token.sum(), tool=tien_tool.sum(), xem_lai=xem_lai, lam_lai=lam_lai,
                tong=tong, thanh_cong=thanh_cong, cps=tong / thanh_cong)


CO_DINH = 40_000_000   # đồng / tháng
KHOI_LUONG = 45_000    # yêu cầu / tháng
PHAM_VI = ['noi_dia', 'hang_nang']


def a3_theo_loai(runs, reqs):
    print('\n== A3 · Theo loại [simulated] ==')
    d = runs.merge(reqs[['request_id', 'loai']]).assign(ok=lambda x: x.status == 'ok')
    print(d.pivot_table(index='loai', columns='attempt', values='ok', aggfunc='mean').round(3))
    for loai in ['noi_dia', 'hang_nang', 'quoc_te', 'doi_tac']:
        r = reqs[reqs.loai == loai]
        m = mo_hinh(runs, r)
        print(f'{loai:10s} n={len(r):4d} tc={m["thanh_cong"] / len(r):6.1%} '
              f'chay/yc={r.so_lan_chay.mean():.2f} cps={m["cps"]:>7,.0f} ({m["cps"] / BASELINE:.2f}x)')
    m = mo_hinh(runs, reqs)
    khong_tc = len(reqs) - m['thanh_cong']
    he_thong = (m['tong'] + khong_tc * BASELINE) / len(reqs)
    print(f'Cả hệ thống/yêu cầu = {he_thong:,.0f} ({he_thong / BASELINE:.2f}x), không thành công={khong_tc}')


def a4_co_dinh(runs, reqs):
    print('\n== A4 · Cộng cố định, phạm vi noi_dia + hang_nang [simulated] ==')
    m = mo_hinh(runs, reqs[reqs.loai.isin(PHAM_VI)])
    for ten, kl in [('45.000/tháng', KHOI_LUONG), ('Một nửa', KHOI_LUONG / 2)]:
        tc_thang = kl * m['thanh_cong'] / len(reqs)
        cd = CO_DINH / tc_thang
        print(f'{ten:13s} tc/tháng={tc_thang:,.0f} cố định/việc={cd:,.0f} '
              f'cps={m["cps"]:,.0f} + cd = {m["cps"] + cd:,.0f} ({(m["cps"] + cd) / BASELINE:.2f}x)')


def b_do_nhay(runs, reqs):
    print('\n== B1 · Độ nhạy [simulated] ==')
    kich_ban = {
        'Giá token gấp đôi':        dict(gia_vao=52, gia_ra=260),
        'Giá token giảm một nửa':   dict(gia_vao=13, gia_ra=65),
        'Xem lại gấp đôi':          dict(he_so_xem_lai=2),
        'Xem lại giảm một nửa':     dict(he_so_xem_lai=0.5),
        'Làm lại gấp đôi':          dict(he_so_lam_lai=2),
        'Làm lại giảm một nửa':     dict(he_so_lam_lai=0.5),
        'Lương tăng 25%':           dict(luong_phut=2500),
        'Tối đa 2 lần chạy':        dict(max_lan_chay=2),
        'Chỉ 1 lần chạy':           dict(max_lan_chay=1),
    }
    goc = mo_hinh(runs, reqs)['cps']
    print(f'{"Gốc (A2)":25s} {goc:8,.0f}')
    for ten, kw in kich_ban.items():
        cps = mo_hinh(runs, reqs, **kw)['cps']
        print(f'{ten:25s} {cps:8,.0f} {(cps / goc - 1) * 100:+6.1f}%')

    print('\n== B2 · Cặp token×2 + xem lại×2 [simulated] ==')
    cps = mo_hinh(runs, reqs, gia_vao=52, gia_ra=260, he_so_xem_lai=2)['cps']
    print(f'{cps:,.0f} {(cps / goc - 1) * 100:+.1f}%')

    print('\n== B3 · Giới hạn chạy lại, cả hệ thống [simulated] ==')
    for k in [1, 2, 3]:
        m = mo_hinh(runs, reqs, max_lan_chay=k)
        khong_tc = len(reqs) - m['thanh_cong']
        print(f'k={k} tổng trợ lý={m["tong"]:>10,.0f} không tc={khong_tc:3d} '
              f'cả hệ thống={m["tong"] + khong_tc * BASELINE:>10,.0f} cps={m["cps"]:,.0f}')

    print('\n== B4 · Xem lại 100%, phạm vi noi_dia + hang_nang [simulated] ==')
    pv = reqs[reqs.loai.isin(PHAM_VI)]
    r = runs[runs.request_id.isin(pv.request_id)]
    co_ok = r.loc[r.status == 'ok', 'request_id'].nunique()
    so_lam_lai = int((pv.ket_qua == 'lam_lai').sum())
    tien_may = (r.tokens_in / 1000 * GIA_VAO + r.tokens_out / 1000 * GIA_RA + r.tool_calls * GIA_TOOL).sum()
    tong = co_ok * 5 * LUONG_PHUT + so_lam_lai * 9 * LUONG_PHUT + tien_may
    tc = int((pv.ket_qua == 'thanh_cong').sum())
    print(f'có ok={co_ok} làm lại={so_lam_lai} token+tool={tien_may:,.0f} tổng={tong:,.0f} '
          f'cps={tong / tc:,.0f} ({tong / tc / BASELINE:.2f}x)')


def co_mau(p1, p2, alpha=0.05, power=0.8):
    """Cỡ mẫu mỗi nhóm (so hai tỉ lệ) theo công thức NormalDist."""
    za = NormalDist().inv_cdf(1 - alpha / 2)
    zb = NormalDist().inv_cdf(power)
    pb = (p1 + p2) / 2
    return math.ceil((za * math.sqrt(2 * pb * (1 - pb))
                      + zb * math.sqrt(p1 * (1 - p1) + p2 * (1 - p2))) ** 2 / (p2 - p1) ** 2)


def d_co_mau(reqs):
    """CP4 · Nhiệm vụ D: tính 5 câu D1, power ở mức 5 điểm và tỉ lệ mở lại hiện tại."""
    print('\n== D1 · Cỡ mẫu pilot (p1=0,70; alpha=0,05; power=0,80; ICC=0,02) ==')
    icc = 0.02
    n_5 = co_mau(0.70, 0.75)
    de_b = 1 + (75 - 1) * icc
    n_b = math.ceil(n_5 * de_b)
    nguoi_moi_nhom = math.ceil(n_b / 75)
    print(f'a) Theo yêu cầu (MDE +5đ): n = {n_5:,} mỗi nhóm')
    print(f'b) Theo nhân viên m=75: DE = {de_b:.2f}, n = {n_b:,}/nhóm ({nguoi_moi_nhom} người/nhóm, tổng {nguoi_moi_nhom * 2} > 40)')
    print(f'c) 20 nhân viên/nhóm: giới hạn c/ICC = {20 / icc:,.0f} < {n_5:,} (không đạt)')
    print(f'd) 6 depot/nhóm: giới hạn c/ICC = {6 / icc:,.0f} < {n_5:,} (không đạt)')

    n_6 = co_mau(0.70, 0.76)
    m_min = math.ceil(n_6 * (1 - icc) / (20 - n_6 * icc))
    de_e = 1 + (m_min - 1) * icc
    power_5 = NormalIndPower().power(
        effect_size=proportion_effectsize(0.70, 0.75),
        nobs1=n_6, alpha=0.05, ratio=1.0
    )
    print(f'e) MDE +6đ (n={n_6:,}/nhóm), 20 người/nhóm: m >= {m_min}, DE = {de_e:.2f}; power ở +5đ = {power_5:.2f}')

    pv = reqs[reqs.loai.isin(PHAM_VI)]
    print(f'Tỉ lệ mo_lai_trong_7_ngay hiện tại: toàn bộ = {reqs.mo_lai_trong_7_ngay.mean():.2%} '
          f'({int(reqs.mo_lai_trong_7_ngay.sum())}/{len(reqs)}), '
          f'phạm vi = {pv.mo_lai_trong_7_ngay.mean():.2%} ({int(pv.mo_lai_trong_7_ngay.sum())}/{len(pv)})')


def e1_chi_so(reqs):
    """CP5 · Nhiệm vụ E1: tính thử 3 chỉ số trên 1.200 yêu cầu."""
    print('\n== E1 · Chỉ số đợt chạy thử (1.200 yêu cầu) ==')
    chinh_mask = (reqs.dong_trong_24h == 1) & (reqs.mo_lai_trong_7_ngay == 0)
    xem = reqs[reqs.duoc_xem_lai == 1]
    bo_qua_mask = xem.quyet_dinh_xem_lai.isin(['sua', 'bo'])
    an_toan_mask = reqs.mo_lai_trong_7_ngay == 1
    print(f'Chính (đóng 24h, không mở lại 7 ngày): {chinh_mask.mean():.2%} ({int(chinh_mask.sum())}/{len(reqs)})')
    print(f'Dùng (bỏ qua gợi ý sua+bo):            {bo_qua_mask.mean():.2%} ({int(bo_qua_mask.sum())}/{len(xem)})')
    print(f'An toàn (mở lại trong 7 ngày):         {an_toan_mask.mean():.2%} ({int(an_toan_mask.sum())}/{len(reqs)})')


if __name__ == '__main__':
    runs = pd.read_csv('logix_runs.csv')
    reqs = pd.read_csv('logix_requests.csv', keep_default_na=False)
    kiem_tra_dap_an_biet_truoc()
    ket_qua = mo_hinh(runs, reqs)
    for ten, gia_tri in ket_qua.items():
        print(f'{ten:12s} {gia_tri:>14,.0f}')
    a3_theo_loai(runs, reqs)   # CP1 · A3
    a4_co_dinh(runs, reqs)     # CP1 · A4
    b_do_nhay(runs, reqs)      # CP2 · B1–B4
    d_co_mau(reqs)             # CP4 · D1, D3
    e1_chi_so(reqs)            # CP5 · E1
