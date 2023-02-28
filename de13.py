#Tạo class số nguyên gồm giá trị của số nguyên và 3 phương thức kiểm tra số âm/dương, kiểm tra số đối xứng, kiểm tra số hoàn thiện.
#Nhập 1 list có 3 số nguyên (số nguyên là các object tạo bởi class trong yêu cầu 1. Khuyến khích tạo giao diện GUI)
#   In ra các số âm 
#   Tính tổng các số đối xứng? 
#   Tìm số hoàn thiện nhỏ nhất.
class Songuyen:
    def __init__(self,n):
        self.n = n
    
    def ktamduong(self):
        if self.n < 0:
            return True
        return False
    
    def ktsodx(self):
        a = self.n
        sodao = 0
        while self.n > 0:
            sodao = sodao * 10 + self.n % 10
            self.n //= 10

        if sodao == a:
            return True
        return False

    def ktsoht(self):
        sum = 0
        for i in range(1,self.n):
            if self.n % i == 0:
                sum += i

        if sum == self.n:
            return True
        return False

while(True):
    sn = []
    nsoam = " "
    tongsodx = 0
    soht = []

    for i in range(1,4):
        print("Số thứ: ", i)
        n = int(input("Nhập vào số: "))
        sn.append(n)

    for i in range(0,3):
        s = Songuyen(sn[i])
        if s.ktamduong() == True:
            nsoam += " " + str(sn[i])
        if s.ktsodx() == True:
            tongsodx += sn[i]
        if s.ktsoht() == True:
            soht.append(sn[i])
    
    if len(soht) == 0:
        Min = - 1
    else:
        Min = min(soht)

    print("Các số âm lần lượt là: ", nsoam)
    print("Tổng các số đối xứng: ", tongsodx)
    print("Số hoàn thiện nhỏ nhất: ", Min)