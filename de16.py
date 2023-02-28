#Tạo class số thực gồm giá trị của số thực và 3 phương thức kiểm tra số âm, kiểm tra số dương, đếm số chữ số sau dấy phẩy.
#Tạo 1 tuple có 3 số thưc (số thực là các object tạo bởi class trong yêu cầu 1. Khuyến khích tạo giao diện GUI)
#   In ra các số dương 
#   Tính tích các âm? 
#   Tìm số có số các chữ số sau dấu phảy nhiều nhất (số có phần thập phân dài nhất).
class Sothuc:
    def __init__(self, n):
        self.n = n
    
    def ktam(self):
        if self.n < 0:
            return True
    
    def ktduong(self):
        if self.n > 0:
            return True
    
    def dem(self):
        if self.n % 1 == 0:
            return 0
        else:
            self.n = str(self.n)
            return self.n[::-1].find('.')

while(True):   
    l = []
    s = []
    tich = 1
    for i in range(0,3):
        a = float(input("nhap: "))
        s.append(a)
        obj = Sothuc(a)
        l.append(obj)
    t = tuple(l)

    for i in range(0,3):
        if (t[i].ktduong()==1):
            print("so + " + str(s[i]))
    for i in range(0,3):
        if (t[i].ktam()==1):
            tich *= s[i]
    print(tich)
    for i in range(0,3):
        print("so so cua so %d sau dau phay: %d" %(i+1,t[i].dem()))