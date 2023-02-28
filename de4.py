# Tạo class hình thang vuông gồm độ dài các cạnh và 2 phương thức tính chu vi, tính diện tích.
#Nhập 1 list có 3 hình thang vuông (hình thang vuông là các object tạo bởi class trong yêu cầu 1. Khuyến khích tạo giao diện GUI)
#   Tính chu vi của 3 hình thang vuông vưà nhập 
#   In ra tổng diện tích của 3 hình vừa nhập 
#   Tìm hình có độ diện tích lớn nhất.
class Hinhthangvuong:
    def __init__(self, a, h, b, c):
        self.a = a
        self.h = h
        self.b = b
        self.c = c

    def chuvi(self):
        cv = self.a + self.h + self.b + self.c
        return cv

    def dientich(self):
        s = self.h * (self.a + self.b)/2
        return s

while(True):
    A = []
    for i in range(3):
        print("Hình thang vuông thứ %d: " %(i + 1))
        a = int(input("Nhập vào độ dài cạnh đáy trên: "))
        h = int(input("Nhập vào độ dài cạnh bên vuông góc với đáy: "))
        b = int(input("Nhập vào độ dài cạnh đáy dưới: "))
        c = (abs(a - b) ** 2 + h ** 2) ** 0.5
        A.append(Hinhthangvuong(a,h,b,c))

    for i in range(len(A)):
        print("Hình thang vuông thứ %d: " %(i + 1))
        print("Chu vi: ", A[i].chuvi())
    
    sum = A[0].dientich() + A[1].dientich() + A[2].dientich()
    print("Tổng diện tích của 3 hình vừa nhập là: ", sum)

    Max_dt = max(A[0].dientich(), A[1].dientich(), A[2].dientich())
    if Max_dt == A[0].dientich():
        dem = 1
    if Max_dt == A[1].dientich():
        dem = 2    
    if Max_dt == A[2].dientich():
        dem = 3
    
    print("Hình có diện tích lớn nhất là hình thứ {} với diện tích {}".format(dem, Max_dt))
    

