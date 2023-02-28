#Tạo class số nguyên gồm giá trị của số nguyên và 3 phương thức kiểm tra số chẵn/ lẻ, kiểm tra số nguyên tố, kiểm tra số chính phương.
#Nhập 1 list có 3 số nguyên (số nguyên là các object tạo bởi class trong yêu cầu 1. Khuyến khích tạo giao diện GUI)
#   In ra các số chẵn 
#   Tính tổng các số chính phương? 
#   Tìm số nguyên tố lớn nhất.
from math import sqrt
class Songuyen:
    def __init__(self,n):
        self.n = n
    
    def ktchanle(self):
        if self.n % 2 == 0:
            return True
        return False
    
    def ktnt(self):
        if self.n < 2:
            return False
        for i in range(2, self.n):
            if self.n % i == 0:
                return False
            return True

    def ktcp(self):
        if sqrt(self.n) % 1 == 0:
            return True
        else:
            return False

while(True):
    sn = []
    nsochan = " "
    tongchinhphuong = 0
    nguyento = []

    for i in range(1,4):
        print("Nhập số thứ %d: " %i)
        so = int(input("Nhập vào số: "))
        sn.append(so)

    for i in range(0,3):
        s = Songuyen(sn[i])
        if s.ktchanle() == True:
            nsochan += " " + str(sn[i])
        if s.ktcp() == True:
            tongchinhphuong += sn[i]
        if s.ktnt()==True:
            nguyento.append(sn[i])
    
    if len(nguyento) == 0:
        Max = 0
    else:
        Max = max(nguyento)

    print("Các số chẵn lần lượt là:  " +str(nsochan))
    print("Tổng các số chính phương là: " +str(tongchinhphuong))
    print("Số nguyên tố max là: " + str(Max))

    
    

        
    

             

