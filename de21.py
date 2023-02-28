#Tạo class lũy thừa gồm giá trị của 1 số nguyên và 3 phương thức tính bình phương, tính lập phương, tính giai thừa
#   Nhập 1 list có N object lũy thừa (là object tạo bởi class trong yêu cầu 1. Khuyến khích tạo giao diện GUI)
#   Tạo 1 dictionary có key là số nguyên vừa nhập, value là lập phương của số nguyên đó. 
#   In ra giai thừa các số vừa nhập 
#   Tìm tổng lập phương các số vừa nhập.
class luythua():
    def __init__(self,a):
        self.a = a
    def binhphuong(self):
        return self.a**2
    def lapphuong(self):
        return self.a**3
    def giaithua(self):
        gt=1
        if(self.a==0 or self.a==1):
            return gt
        else:
            for i in range(2,self.a+1):
                gt = gt * i
            return gt       
l=[]
s=[]
d=dict()
tong = 0
for i in range(0,3):
    a = int(input("nhap so: "))
    s.append(a)
    obj =  luythua(a)
    l.append(obj)
for i in range(0,3):
    print("giai thua la"+str(l[i].giaithua()))
for i in range(0,3):
    tong =  tong + l[i].lapphuong()
print("tong la: "+str(tong))
for i in range(0,3):
    d[s[i]]=l[i].binhphuong()
print("dic la:",d)



