#Tạo class hình tam giác gồm độ dài các cạnh và 2 phương thức tính chu vi, tính diện tích
#Nhập 1 list có 3 hình tam giác (hình tam giác là các object tạo bởi class trong yêu cầu 1. Khuyến khích tạo giao diện GUI)
#   Tính chu vi của 3 hình vưà nhập 
#   In ra tổng diện tích của 3 hình vừa nhập 
#   Tìm hình có diện tích nhỏ nhất.
class Hinhtamgiac:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
    
    def chuvi(self):
        cv = self.a + self.b + self.c
        return cv
    
    def dientich(self):
        p = (self.a + self.b + self.c)/2
        s = (p*(p - self.a)*(p - self.b)*(p - self.c)) ** 0.5
        return s

while(True):
    A = []
    for i in range(3):
        print("Hình tam giác thứ %d: "%(i + 1))
        a = int(input("Nhập vào cạnh a: "))
        b = int(input("Nhập vào cạnh b: "))
        c = int(input("Nhập vào cạnh c: "))
        if a + b > c and a + c > b and b + c > a:
            A.append(Hinhtamgiac(a,b,c))
        else:
            print("Nhập lại độ dài các cạnh cho hình tam giác thứ %d: "%(i + 1))
            print("Hình tam giác thứ %d: "%(i + 1))
            a = int(input("Nhập vào cạnh a: "))
            b = int(input("Nhập vào cạnh b: "))
            c = int(input("Nhập vào cạnh c: "))
            A.append(Hinhtamgiac(a,b,c))
        
    for i in range(len(A)):
        print("Hình tam giác thứ %d: " %(i+1))
        print("Chu vi: ", A[i].chuvi())
    
    Sum = A[0].dientich() + A[1].dientich() + A[2].dientich()
    print('Tổng diện tích của 3 hình vừa nhập là: ',Sum)

    Min_dt = min(A[0].dientich(), A[1].dientich(), A[2].dientich())
    if Min_dt == A[0].dientich():
        dem = 1
    if Min_dt == A[1].dientich():
        dem = 2
    if Min_dt == A[2].dientich():
        dem = 3
    print("Hình có diện tích nhỏ nhất là hình thứ {} với diện tích {}".format(dem, Min_dt))
    