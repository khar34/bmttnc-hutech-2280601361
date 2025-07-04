from SinhVien import SinhVien

class QuanLySinhVien:
    listSinhVien = []

    def generateID(self):
        maxId = 1
        if self.soLuongSinhVien() > 0:
            maxId = self.listSinhVien[0]._id
            for sv in self.listSinhVien:
                if maxId < sv._id:
                    maxId = sv._id
            maxId = maxId + 1
        return maxId

    def soLuongSinhVien(self):
        return len(self.listSinhVien)

    def nhapSinhVien(self):
        svId = self.generateID()
        name = input("Nhap ten sinh vien: ")
        if not name.strip():
            print("Ten khong duoc de trong!")
            return
        sex = input("Nhap gioi tinh sinh vien: ")
        if not sex.strip():
            print("Gioi tinh khong duoc de trong!")
            return
        major = input("Nhap chuyen nganh sinh vien: ")
        if not major.strip():
            print("Chuyen nganh khong duoc de trong!")
            return
        try:
            diemTB = float(input("Nhap diem cua sinh vien: "))
            if not (0 <= diemTB <= 10):
                print("Diem TB phai nam trong khoang 0 den 10!")
                return
        except ValueError:
            print("Vui long nhap mot so thuc hop le!")
            return
        sv = SinhVien(svId, name, sex, major, diemTB)
        self.xepLoaiHocLuc(sv)
        self.listSinhVien.append(sv)

    def updateSinhVien(self, ID):
        sv: SinhVien = self.findByID(ID)
        if sv is not None:
            name = input("Nhap ten sinh vien: ")
            if not name.strip():
                print("Ten khong duoc de trong!")
                return
            sex = input("Nhap gioi tinh sinh vien: ")
            if not sex.strip():
                print("Gioi tinh khong duoc de trong!")
                return
            major = input("Nhap chuyen nganh sinh vien: ")
            if not major.strip():
                print("Chuyen nganh khong duoc de trong!")
                return
            try:
                diemTB = float(input("Nhap diem cua sinh vien: "))
                if not (0 <= diemTB <= 10):
                    print("Diem TB phai nam trong khoang 0 den 10!")
                    return
            except ValueError:
                print("Vui long nhap mot so thuc hop le!")
                return
            sv._name = name
            sv._sex = sex
            sv._major = major
            sv._diemTB = diemTB
            self.xepLoaiHocLuc(sv)
        else:
            print(f"Sinh vien co ID = {ID} khong ton tai.")
            return

    def sortByID(self):
        self.listSinhVien.sort(key=lambda x: x._id, reverse=False)

    def sortByName(self):
        self.listSinhVien.sort(key=lambda x: x._name.lower(), reverse=False)

    def sortByDiemTb(self):
        self.listSinhVien.sort(key=lambda x: x._diemTB, reverse=True)

    def sortByMajor(self):
        self.listSinhVien.sort(key=lambda x: x._major.lower(), reverse=False)

    def findByID(self, ID):
        for sv in self.listSinhVien:
            if sv._id == ID:
                return sv
        return None

    def findByName(self, keyword):
        listSV = []
        if self.soLuongSinhVien() > 0:
            for sv in self.listSinhVien:
                if keyword.upper() in sv._name.upper():
                    listSV.append(sv)
        return listSV

    def deleteById(self, ID):
        sv = self.findByID(ID)
        if sv is not None:
            self.listSinhVien.remove(sv)
            return True
        return False

    def xepLoaiHocLuc(self, sv: SinhVien):
        if sv._diemTB >= 8:
            sv._hocLuc = "Gioi"
        elif sv._diemTB >= 6.5:
            sv._hocLuc = "Kha"
        elif sv._diemTB >= 5:
            sv._hocLuc = "Trung binh"
        else:
            sv._hocLuc = "Yeu"

    def showSinhVien(self, listSV):
        print("{:<8} {:<18} {:<8} {:<12} {:<8} {:<8}".format("ID", "Name", "Sex", "Major", "DiemTB", "Hoc Luc"))
        if len(listSV) > 0:
            for sv in listSV:
                print("{:<8} {:<18} {:<8} {:<12} {:<8.2f} {:<8}".format(sv._id, sv._name, sv._sex, sv._major, sv._diemTB, sv._hocLuc))
        print("\n")

    def getListSinhVien(self):
        return self.listSinhVien