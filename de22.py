#Tạo class số nguyên gồm giá trị của số nguyên và 3 phương thức kiểm tra số chẵn/ lẻ, kiểm tra số chính phương, tìm số đảo.
#Nhập 1 list có 3 số nguyên (số nguyên là các object tạo bởi class trong yêu cầu 1. Khuyến khích tạo giao diện GUI)
#   In ra các số đảo của list số nguyên
#   Tính tổng các số lẻ? 
#   Tìm số  chính phương lớn nhất.
class songuyen():
    def __init__(self,a):
        self.a=a
    def chanle(self):
        if (self.a%2)!=0:
            return 1
        else:
            return 0 
    def cp(self):
        for i in range(1,self.a+1):
            if i**2==self.a:
                return 1
        else:
            return 0
    def dao(self):
        s=0
        b=str(self.a)
        for i in range(0,len(b)):
            d=self.a%10
            s=s*10+d
            self.a=self.a//10
        return s
l=[]
k=[]
w=[]
tong = 0
for i in range(0,3):
    a = int(input("nhap so: "))
    obj = songuyen(a)
    l.append(obj)
    k.append(a)
for i in range(0,3):
    if (l[i].chanle()==1):
        tong=tong+k[i]
for i in range(0,3):
    if (l[i].cp()==1):
        w.append(k[i])
for i in range(0,3):
    print("so dao la: "+str(l[i].dao()))
if(w==[]):
    print("ko co so chinh phuong")
else:
    print("so cp lon nhat la: "+str(max(w)))
print("tong la: "+str(tong))


