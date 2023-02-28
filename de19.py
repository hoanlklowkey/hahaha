#Tạo class hình tròn gồm bán kính và 2 phương thức tính chu vi, diện tích.
#Tạo 1 list có 5 hình tròn (hình tròn là các object tạo bởi class trong yêu cầu 1. Khuyến khích tạo giao diện GUI)
#   Tính chu vi của 5 hình tròn vừa nhập 
#   Tìm tổng diện tích các hình tròn 
#   Tìm hình tròn nhỏ nhất.
class hinhtron():
    def __init__(self,a):
        self.a=a
    def chuvi(self):
        return self.a*2*3.14
    def dientich(self):
        return self.a**2*3.14
l=[]
s=[]
tong = 0
for i in range(0,5):
    a = int(input("nhap ban kinh: "))
    s.append(a)
    obj = hinhtron(a)
    l.append(obj)
for i in range(0,5):
    print("chu vi hinh " + str(i+1)+" la: "+str(l[i].chuvi()))
for i in range(0,5):
    tong =  tong + l[i].dientich()
print(tong)
m = min(s)
for i in range(0,5):
    if(m==s[i]):
        print("hinh torng nhowr nhats la: "+str(i+1))  





