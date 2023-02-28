#Tạo class thí sinh gồm tên, năm sinh, điểm toán, điểm văn, điểm ngoại ngữ và 2 phương thức tính tuổi (tuồi = năm hiện tại – năm sinh), tính tổng điểm 3 môn
#Nhập 1 list có 3 thí sinh (thí sinh là các object tạo bởi class trong yêu cầu).(Khuyến khích tạo giao diện GUI)
#   Tính tổng điểm 3 môn của mỗi thí sinh vừa nhập 
#   Tìm thí sinh ít tuổi nhất? 
#   Tìm thí sinh có điểm toán lớn nhất.
from datetime import date
class Thisinh:
    def __init__(self, namsinh, diemtoan, diemvan, diemnn):
        self.namsinh = namsinh
        self.diemtoan = diemtoan
        self.diemvan = diemvan
        self.diemnn = diemnn

    def tuoi(self):
        age = date.today().year - self.namsinh
        return age
    
    def tongdiem(self):
        s = self.diemtoan + self.diemvan + self.diemnn
        return s
    
while(True):
    A = []
    for i in range(3):
        print("Sinh viên thứ %d: "%(i+1))
        namsinh = int(input("Nhập vào năm sinh: "))
        diemtoan = int(input("Nhập vào điểm toán: "))
        diemvan = int(input("Nhập vào điểm văn: "))
        diemnn = int(input("Nhập vào điểm ngoại ngữ: "))
        while (diemtoan < 0 or diemtoan > 10) or (diemvan < 0 or diemvan > 10) or (diemnn < 0 or diemnn > 10):
            diemtoan = int(input("Nhập vào điểm toán: "))
            diemvan = int(input("Nhập vào điểm văn: "))
            diemnn = int(input("Nhập vào điểm ngoại ngữ: "))
        
        A.append(Thisinh(namsinh,diemtoan,diemvan,diemnn))

    for i in range(len(A)):
        print("Sinh viên thứ %d: "%(i+1))
        print("Tổng điểm 3 môn: ",A[i].tongdiem())
    
    Min_age = min(A[0].tuoi(), A[1].tuoi(), A[2].tuoi())
    Max_math = max(A[0].diemtoan, A[1].diemtoan, A[2].diemtoan)

    if Min_age == A[0].tuoi():
        dem = 1
    if Min_age == A[1].tuoi():
        dem = 2
    if Min_age == A[2].tuoi():
        dem = 3   
    
    if Max_math == A[0].diemtoan:
        count = 1
    if Max_math == A[1].diemtoan:
        count = 2
    if Max_math == A[2].diemtoan:
        count = 3 
    
    print("Thí sinh ít tuổi nhất là sinh viên thứ {} với số tuổi là: {}".format(dem,Min_age))
    print("Thí sinh có điểm toán lớn nhất là sinh viên thứ {} với số điểm là: {}".format(count, Max_math))

