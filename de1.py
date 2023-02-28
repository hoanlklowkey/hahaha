# Tạo class hình tứ giác gồm độ dài các cạnh và 2 phương thức tính chu vi, tìm độ dài cạnh lớn nhất.
# Nhập 1 list có 3 hình tứ giác (hình tứ giác là các object tạo bởi class trong yêu cầu 1. Khuyến khích tạo giao diện GUI)
#   Tính chu vi của 3 hình tứ giác vưà nhập 
#   In ra độ dài cạnh lớn nhất cuả mỗi hình tứ giác 
#   Tìm hình có chu vi nhỏ nhất.
class Hinhtugiac:
    def __init__(self, a, b, c, d):
        self.a = a
        self.b = b
        self.c = c
        self.d = d
    
    def chuvi(self):
        cv = self.a + self.b + self.c + self.d
        return cv
    
    def canhmax(self):
        return max(self.a, self.b, self.c, self.d)

while(True):
    A = []
    for i in range(3):
        print("Hình tứ giác thứ %d" %(i+1))
        a = int(input('Nhập vào cạnh a: '))
        b = int(input('Nhập vào cạnh b: '))
        c = int(input('Nhập vào cạnh c: '))
        d = int(input('Nhập vào cạnh d: '))
        A.append(Hinhtugiac(a,b,c,d))
    
    for i in range(len(A)):
        print("Hình tứ giác %d: " %(i+1))
        print("Chu vi: ", A[i].chuvi())
        print("Độ dài cạnh max: ", A[i].canhmax())
    
    Min_cv = min(A[0].chuvi(), A[1].chuvi(), A[2].chuvi())
    
    if Min_cv == A[0].chuvi():
        dem = 1
    if Min_cv == A[1].chuvi():
        dem = 2
    if Min_cv == A[2].chuvi():
        dem = 3

    print('Hình có chu vi nhỏ nhất là hình thứ {} với chu vi là {}'.format(dem,Min_cv))



    
    
        