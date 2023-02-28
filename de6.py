#Tạo class hình tam giác vuông gồm độ dài 2 cạnh góc vuông và 3 phương thức tính độ dài cạnh huyền, tính diện tích, tính chu vi.
#Nhập 1 list có 3 hình tam giác (hình tam giác là các object tạo bởi class trong yêu cầu 1. Khuyến khích tạo giao diện GUI)
#   Tính độ dài cạnh huyền của 3 hình vưà nhập 
#   In ra tổng diện tích của 3 hình vừa nhập 
#   Tìm hình có chu vi lớn nhất.
from math import sqrt
class Tamgiacvuong:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    
    def canhhuyen(self):
        c = sqrt(self.a**2 + self.b**2)
        return c

    def dientich(self):
        s = 1/2 * self.a * self.b
        return s
    
    def chuvi(self):
        c = sqrt(self.a**2 + self.b**2)
        cv = self.a + self.b + c
        return cv
    
while(True):
    A = []
    for i in range(3):
        print("Tam giác vuông thứ %d: "%(i+1))
        a = int(input("Nhập vào cạnh góc vuông thứ nhất: "))
        b = int(input("Nhập vào cạnh góc vuông thứ hai: "))

        while a <= 0 or b <= 0:
            print("Nhập lại độ dài cạnh của tam giác vuông thứ %d: "%(i+1))
            a = int(input("Nhập vào cạnh góc vuông thứ nhất: "))
            b = int(input("Nhập vào cạnh góc vuông thứ hai: "))
            
        A.append(Tamgiacvuong(a,b))
    
    for i in range(len(A)):
        print("Hình thứ %d: "%(i+1))
        print("Độ dài cạnh huyền: ", A[i].canhhuyen())
    
    sum = A[0].dientich() + A[1].dientich() + A[2].dientich()
    print('Tổng diện tích của 3 hình vừa nhập là: ', sum)

    Max_cv = max(A[0].chuvi(), A[1].chuvi(), A[2].chuvi())
    if Max_cv == A[0].chuvi():
        dem = 1
    if Max_cv == A[1].chuvi():
        dem = 2
    if Max_cv == A[2].chuvi():
        dem = 3
    
    print("Hình có chu vi lớn nhất là hình thứ {} có chu vi là: {}".format(dem,Max_cv))
    
