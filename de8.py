#Tạo class hình hộp chữ nhật gồm độ dài cạnh và 2 phương thức tính diện tích xung quanh, tính thể tích.
#Nhập 1 list có 3 hình hộp chữ nhật (hình hộp chữ nhật là các object tạo bởi class trong yêu cầu 1. Khuyến khích tạo giao diện GUI)
#   Tính diện tích xung quanh của 3 hình vưà nhập 
#   In ra tổng thể tích của 3 hình vừa nhập 
#   Tìm hình có thể tích lớn nhất.
class Hinhhopchunhat:
    def __init__(self,a,b,h):
        self.a = a
        self.b = b
        self.h = h
    
    def dtxq(self):
        s = 2 * self.h * (self.a + self.b)
        return s
    
    def thetich(self):
        v = self.a * self.b * self.h
        return v
    
while(True):
    A = []
    for i in range(3):
        print("Hình hộp chữ nhật thứ %d: " %(i+1))
        a = int(input("Nhập vào chiều dài cạnh đáy: "))
        b = int(input("Nhập vào chiều rộng cạnh đáy: "))
        h = int(input("Nhập vào chiều cao: "))
        while a <= b or h <= 0:
            a = int(input("Nhập vào chiều dài cạnh đáy: "))
            b = int(input("Nhập vào chiều rộng cạnh đáy: "))
            h = int(input("Nhập vào chiều cao: "))
        
        A.append(Hinhhopchunhat(a,b,h))

    for i in range(len(A)):
        print("Hình hộp chữ nhật thứ %d: " %(i+1))
        print("Diện tích xung quanh: ", A[i].dtxq())

    sum = A[0].thetich() + A[1].thetich() + A[2].thetich()
    print("Tổng thể tích của 3 hình vừa nhập: ", sum)

    Max_v = max(A[0].thetich(), A[1].thetich(), A[2].thetich())
    if Max_v == A[0].thetich():
        dem = 1
    if Max_v == A[1].thetich():
        dem = 2
    if Max_v == A[2].thetich():
        dem = 3  
    
    print("Hình có thể tích lớn nhất là hình thứ {} với thể tích là: {}".format(dem,Max_v))