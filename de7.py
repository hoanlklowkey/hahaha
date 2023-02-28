#Tạo class hình tam giác đều gồm độ dài cạnh và 3 phương thức tính độ dài đường cao, tính diện tích, tính chu vi.
# Nhập 1 list có 3 hình tam giác đều(hình tam giác là các object tạo bởi class trong yêu cầu 1. Khuyến khích tạo giao diện GUI)
#   Tính độ dài đường cao của 3 hình vưà nhập 
#   In ra tổng diện tích của 3 hình vừa nhập 
#   Tìm hình có chu vi nhỏ nhất.
from math import sqrt
class Tamgiacdeu:
    def __init__(self, a):
        self.a = a
    
    def duongcao(self):
        h = self.a * sqrt(3)/2
        return h
    
    def dientich(self):
        s = self.a ** 2 * sqrt(3)/4
        return s
    
    def chuvi(self):
        cv = self.a * 3
        return cv
    
while(True):
    A = []
    for i in range(3):
        print("Tam giác đều thứ %d: "%(i+1))
        a = int(input("Nhập vào độ dài cạnh: "))
        while a <= 0:
            a = int(input("Nhập vào độ dài cạnh: "))
        A.append(Tamgiacdeu(a))

    for i in range(len(A)):
        print("Tam giác đều thứ %d: "%(i+1))
        print("Độ dài đường cao: ", A[i].duongcao())

    sum = A[0].dientich() + A[1].dientich() + A[2].dientich()
    print("Tổng diện tích của 3 tam giác vừa nhập là: ", sum)

    Min_cv = min(A[0].chuvi(), A[1].chuvi(), A[2].chuvi())
    if Min_cv == A[0].chuvi():
        dem = 1
    if Min_cv == A[1].chuvi():
        dem = 2
    if Min_cv == A[2].chuvi():
        dem = 3
    
    print("Hình có chu vi nhỏ nhất là hình thứ {} với chu vi là: {}".format(dem, Min_cv))
    

    
