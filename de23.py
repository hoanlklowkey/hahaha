#Tạo class số nguyên gồm giá trị của số nguyên và 3 phương thức kiểm tra số chẵn/ lẻ, kiểm tra số chính phương, tìm số đảo.
#   Nhập 1 list có 3 số nguyên (số nguyên là các object tạo bởi class trong yêu cầu 1. Khuyến khích tạo giao diện GUI)
#   Tạo dictionary có key là các số nguyên đã nhập, value là số đảo của nó
#   Tính tổng các số đảo? 
#   Tìm số chính phương nhỏ nhất.

class songuyen():
    def __init__(self,a):
        self.a=a
    def chanle(self):
        if self.a%2==0:
            return 1
        else:
            return 0
    def sochinhphuong(self):
        for i in range(1,self.a+1):
            if i**2==self.a:
                return 1 
                break
        else:
            return 0
    def sodao(self):
        if self.a>=0:
            d = 0
            b = len(str(self.a))
            for i in range(0,b):
                c=self.a%10
                d = d*10 +c
                self.a=self.a//10
            return d
        if self.a<0:
            e = 0
            h= self.a*(-1)
            g= len(str(h))
            for i in range(0,g):
                w=h%10
                e = e*10 +w
                h=h//10
            return e *(-1)
l=[]
s=[]
k=[]
z=[]

dic=dict()
tong = 0
for i in range(0,3):
    a=int(input("nhap so: "))
    s.append(a)
    obj = songuyen(a)
    z.append(a)
    l.append(obj)
    if l[i].sochinhphuong()==1:
        k.append(a)
    tong = tong + obj.sodao()
for i in range(0,3):
    obj1 = songuyen(z[i])
    dic[s[i]]=obj1.sodao()
print(dic)

print(tong)
if k==[]:
    print("ko co so chinh phuong")
else:
    print("so lon nhat la:" +str(max(k)))
