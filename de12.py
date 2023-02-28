#Tạo class số nguyên gồm giá trị của số nguyên và 3 phương thức kiểm tra số chẵn/ lẻ, kiểm tra số nguyên tố, kiểm tra số chính phương.
#Nhập 1 list có 3 số nguyên (số nguyên là các object tạo bởi class trong yêu cầu 1. Khuyến khích tạo giao diện GUI)
#   In ra các số lẻ
#   Tính tích các số nguyên tố?
from math import sqrt
class Songuyen:
    def __init__(self, n):
        self.n = n
    
    def ktchanle(self):
        if self.n % 2 == 0:
            return True
        return False
    
    def ktnt(self):
        if self.n < 2:
            return False
        for i in range(2,self.n):
            if self.n % i == 0:
                return False
            return True
    
    def ktcp(self):
        if sqrt(self.n) % 1 == 0:
            return True
        return False

while(True):
    sn = []
    nsole = " "
    tichnguyento = 1
    socp = []

    for i in range(1,4):
        print("Số thứ: ", i)
        n = int(input("Nhập vào số: "))
        sn.append(n)
    
    for i in range(0,3):
        s = Songuyen(sn[i])
        if s.ktchanle() == False:
            nsole += " " + str(sn[i])
        if s.ktnt() == True:
            tichnguyento *= sn[i]
        if s.ktcp() == True:
            socp.append(sn[i])
    
    if len(socp) == 0:
        Min = - 1
    else:
        Min = min(socp)

    print("Các số lẻ lần lượt là: ", nsole)
    print("Tích các số nguyên tố: ",tichnguyento)
    print("Số chính phương nhỏ nhất là: ", Min)
    
