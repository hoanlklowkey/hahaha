#Tạo class nhân viên gồm họ tên, số năm công tác, lương cơ bản, hệ số lương và phương thức tính lương giả thiết rằng lương = lương cơ bản * hệ số lương + số năm công tác *10% lương cơ bản.
#Tạo 1 list có 3 nhân viên (nhân viên là các object tạo bởi class trong yêu cầu 1. Khuyến khích tạo giao diện GUI)
#   In ra danh sách đầy đủ các thông tin của 3 nhân viên vừa nhập 
#   Tìm nhân viên có số năm công tác lớn nhất 
#   Tính tổng lương của cả 3 nhân viên.
class nhanvien():
    def __init__(self,hoten,namcongtac,luongcoban,hesoluong):
        self.hoten=hoten
        self.namcongtac=namcongtac
        self.luongcoban=luongcoban
        self.hesoluong=hesoluong
        return
    def luong(self):
        luong=self.luongcoban*self.hesoluong+self.namcongtac*0.1*luongcoban
        return luong
l=[]
s=[]
tong=0
for i in range(0,3):
    hoten= str(input("nhap ho ten: "))
    namcongtac= int(input("nhap nam cong tac: "))
    luongcoban= int(input("nhap luong co ban: "))
    hesoluong= int(input("nhap he so luong: "))
    obj =  nhanvien(hoten,namcongtac,luongcoban,hesoluong)
    l.append(obj)
    s.append(namcongtac)
    tong =  tong + l[i].luong()
    print("-------------")
for i in range(0,3):
    print("thong tin nhan vien "+str(i+1)+"ho ten: "+hoten+"nam cong tac: "+str(namcongtac)+"luong co ban: "+str(luongcoban)+"he so luong: "+str(hesoluong))
    print("luong: %d " %(l[i].luong()))
print("tong la: "+str(tong))


       
