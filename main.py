# def tinh_thue_thu_nhap(thu_nhap):
#     # TODO: Sinh viên sẽ cập nhật công thức tính thuế ở đây
#     return 0
# print("Thuế phải nộp của bạn là:", tinh_thue_thu_nhap(10000000))

def tinh_thue_thu_nhap(thu_nhap):
    # Dev A áp dụng giảm trừ 4 trieu va thue 5%
    thu_nhap_tinh_thue = thu_nhap - 4000000
    return max(0, thu_nhap_tinh_thue * 0.05)