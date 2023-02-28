#   Tạo class hình chữ nhật gồm độ dài các cạnh và 3 phương thức tính chu vi, tính diện tích, tính độ dài đường chéo.
#   Nhập 1 list có 3 hình chữ nhật (hình chữ nhật là các object tạo bởi class trong yêu cầu 1. Khuyến khích tạo giao diện GUI)
#   Tính chu vi của 3 hình chữ nhật vưà nhập 
#   In ra tổng diện tích của 3 hình vừa nhập 
#   Tìm hình có độ dài đường chéo nhỏ nhất.
from math import sqrt
class Hinhchunhat:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    
    def chuvi(self):
        cv = (self.a + self.b) * 2
        return cv
    
    def dientich(self):
        s = self.a * self.b
        return s
    
    def dodaiduongcheo(self):
        dodaidc = sqrt(self.a ** 2 + self.b ** 2)
        return dodaidc
    
while(True):
    A = []
    for i in range(3):
        print("Hình chữ nhật thứ %d: " %(i + 1))
        a = int(input('Nhập vào cạnh a: '))
        b = int(input('Nhập vào cạnh b: '))
        A.append(Hinhchunhat(a,b))

    for i in range(len(A)):
        print("Hình chữ nhật %d: " %(i + 1))
        print("Chu vi: ", A[i].chuvi())

    Sum = A[0].dientich() + A[1].dientich() + A[2].dientich()
    print("Tổng diện tích của 3 hình vừa nhập: ", Sum)

    Min_dc = min(A[0].dodaiduongcheo(), A[1].dodaiduongcheo(), A[2].dodaiduongcheo())
    if Min_dc == A[0].dodaiduongcheo():
        dem = 1
    if Min_dc == A[1].dodaiduongcheo():
        dem = 2
    if Min_dc == A[2].dodaiduongcheo():
        dem = 3    
    print("Hình có độ dài đường chéo nhỏ nhất là hình thứ {} có độ dài đường chéo {}". format(dem,Min_dc))
