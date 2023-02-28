#Tạo class số nguyên gồm giá trị của số nguyên và 3 phương thức kiểm tra số âm/dương, kiểm hoàn thiện, kiểm tra số chính phương.
#Nhập 1 list có 3 số nguyên (số nguyên là các object tạo bởi class trong yêu cầu 1. Khuyến khích tạo giao diện GUI)
#   In ra các số hoàn thiện 
#   Tính tích các số chính phương? 
#   Tìm số âm lớn nhất.
class songuyen():
    def __init__(self,a):
        self.a=a
    def amduong(self):
        if(self.a>=0):
            return 0
        elif(self.a<0):
            return 1
    def sohoanthien(self):
        tong = 0
        for i in range(1,self.a):
            if self.a%i == 0:
                tong = tong + i
        if tong==self.a:
            return 1
        else:
            return 0
    def sochinhphuong(self):
        for i in range(1,self.a+1):
            if i**2==self.a:
                return 1
        else:
            return 0
l=[]
s=[]
k=[]
tich = 1
for i in range(0,3):
    a= int(input("nhap so: "))
    obj =  songuyen(a)
    l.append(obj)
    s.append(a)
for i in range(0,3):
    if l[i].sohoanthien() == 1:
        print("so hoan thien la: "+str(s[i]))
for i in range(0,3):
    if l[i].sochinhphuong() == 1:
        tich = tich * s[i]
if tich>1:
    print("tich la: "+str(tich))
else:
    print("ko co so chinh phuong")
for i in range(0,3):
    if l[i].amduong()==1:
        k.append(s[i])
if(k==[]):
    print("ko co so am")
else:
    print("so am lon nhat la" +str(max(k)))








