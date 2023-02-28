#Tạo class số nguyên gồm giá trị của số nguyên và 3 phương thức kiểm tra số âm/dương, kiểm tra số đối xứng, kiểm tra số hoàn thiện.
#   Nhập 1 list có 3 số nguyên (số nguyên là các object tạo bởi class trong yêu cầu 1. Khuyến khích tạo giao diện GUI)
#   In ra các số hoàn thiện 
#   Tính tích các đối xứng? 
#   Tìm số âm lớn nhất.
class Songuyen:
    def __init__(self,n):
        self.n = n
    
    def ktamduong(self):
        if self.n < 0:
            return False
        return True
    
    def ktdx(self):
        a = self.n
        sodao = 0
        while self.n > 0:
            sodao = sodao * 10 + self.n % 10
            self.n //= 10
        
        if sodao == a:
            return True
        return False
    
    def ktht(self):
        sum = 0
        for i in range(1, self.n):
            if self.n % i == 0:
                sum += i

        if sum == self.n:
            return True
        return False

while(True):
    sn = []
    tichsodx = 0
    nsoht = " "
    soam = []

    for i in range(1,4):
        print("Nhập vào số thứ: ",i)
        n = int(input("Nhập vào số: "))
        sn.append(n)

    for i in range(0,3):
        s = Songuyen(sn[i])
        if s.ktht() == True:
            nsoht += " " + str(sn[i])
        if s.ktdx() == True:
            tichsodx *= sn[i]
        if s.ktamduong() == False:
            soam.append(sn[i])
        
    if len(soam) == 0:
        Max = -1
    else:
        Max = max(soam)

    print("Các số hoàn thiện lần lượt là: ", nsoht)
    print("Tích các số hoàn thiện là: ", tichsodx)
    print("Số âm xứng lớn nhất là: ",Max)