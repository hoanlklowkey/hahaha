# Tạo class hình vuông gồm độ dài các cạnh và 3 phương thức tính chu vi, tính diện tích, tính độ dài đường chéo.
#Nhập 1 list có 3 hình vuông (hình vuông là các object tạo bởi class trong yêu cầu 1. Khuyến khích tạo giao diện GUI)
# Tính chu vi của 3 hình vuông vưà nhập 
# In ra tổng diện tích của 3 hình vừa nhập 
# Tìm hình có độ dài đường chéo lớn nhất.
from math import sqrt
class Hinhvuong:
    def __init__(self, a):
        self.a = a
    
    def chuvi(self):
        cv = self.a * 4
        return cv
    
    def dientich(self):
        s = self.a ** 2
        return s
    
    def dodaiduongcheo(self):
        dodaidc = self.a * sqrt(2)
        return dodaidc
    
while(True):
    A = []

    for i in range(3):
        print("Hình vuông thứ %d: " %(i + 1))
        a = int(input('Nhập vào cạnh của hình vuông: '))
        A.append(Hinhvuong(a))

    for i in range(len(A)):
        print("Chu vi: ", A[i].chuvi())
    
    sum = A[0].dientich() + A[1].dientich() + A[2].dientich()
    print('Tổng diện tích của 3 hình vuông: ', sum)

    Max_dc = max(A[0].dodaiduongcheo(), A[1].dodaiduongcheo(), A[2].dodaiduongcheo())
    if Max_dc == A[0].dodaiduongcheo():
        dem = 1
    if Max_dc == A[1].dodaiduongcheo():
        dem = 2
    if Max_dc == A[2].dodaiduongcheo():
        dem = 3
    
    print("Hình vuông có độ dài đường chéo lớn nhất là hình thứ {} có độ dài đường chéo {}".format(dem, Max_dc))
