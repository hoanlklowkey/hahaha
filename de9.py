#Tạo class đường thẳng gồm tọa độ của 2 điểm trong mặt phẳng và 1 phương thức tính độ dài của đoạn thẳng.
#Nhập 1 list có 3 đoạn thẳng (đoạn thẳng là các object tạo bởi class trong yêu cầu 1. Khuyến khích tạo giao diện GUI)
#   Tính độ dài 3 đoạn thẳng vừa nhập 
#   Kiểm tra xem 3 cạnh vừa nhập có lập thành tam giác không? 
#   Tìm đoạn thẳng dài nhất nhất.
from math import sqrt
class Duongthang:
    def __init__(self, x1, y1, x2, y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
    
    def dodaidt(self):
        L = sqrt((self.x2 - self.x1)**2 + (self.y2 - self.y1)**2)
        return L
    
while(True):
    A = []
    for i in range(3):
        print("Đoạn thẳng thứ %d: " %(i + 1))
        x1 = int(input("Nhập vào x1: "))
        y1 = int(input("Nhập vào y1: "))
        x2 = int(input("Nhập vào x2: "))
        y2 = int(input("Nhập vào y2: "))
        while x1 == x2 and y2 == y1:
            x1 = int(input("Nhập vào x1: "))
            y1 = int(input("Nhập vào y1: "))
            x2 = int(input("Nhập vào x2: "))
            y2 = int(input("Nhập vào y2: "))
        
        A.append(Duongthang(x1,y1,x2,y2))
    
    for i in range(len(A)):
        print("Đoạn thẳng thứ %d: " %(i + 1))
        print("Độ dài đoạn thẳng: ", A[i].dodaidt())

    if A[0].dodaidt() + A[1].dodaidt() > A[2].dodaidt() and A[0].dodaidt() + A[2].dodaidt() > A[1].dodaidt() and A[1].dodaidt() + A[2].dodaidt() > A[0].dodaidt():
        print("3 cạnh vừa nhập tạo thành 1 tam giác")
    else:
        print("3 cạnh vừa nhập không tạo thành 1 tam giác")
    
    Max = max(A[0].dodaidt(), A[1].dodaidt(), A[2].dodaidt())
    if Max == A[0].dodaidt():
        dem = 1
    if Max == A[1].dodaidt():
        dem = 2
    if Max == A[2].dodaidt():
        dem = 3
    print("Đoạn thẳng có độ dài lớn nhất là đoạn thẳng thứ {} với độ dài là: {}".format(dem, Max))
    


