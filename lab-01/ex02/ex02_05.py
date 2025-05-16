So_Gio = float(input("Nhập số giờ: "))
Luong_Gio = float(input("Nhập thù lao trên mỗi giờ làm tiêu chuẩn: "))

Gio_Tieu_Chuan = 44
Gio_Vuot_Chuan = max(0, So_Gio - Gio_Tieu_Chuan)
Thuc_Nhan = Gio_Tieu_Chuan * Luong_Gio + Gio_Vuot_Chuan * Luong_Gio * 1.5
print(f"Số tiền thực lĩnh của nhân viên: {Thuc_Nhan}")