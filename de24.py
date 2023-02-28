#Tạo class giai thừa gồm giá trị của 1 số nguyên và 2 phương thức tính giai thừa của số nguyên, tính tổng các số từ 1 đến số nguyên đó.
#Nhập 1 list có 3 object giai thừa (là object tạo bởi class trong yêu cầu 1. Khuyến khích tạo giao diện GUI)
#Tạo 1 dictionary có key là số nguyên vừa nhập, value là giai thừa của số nguyên đó. 
#In ra các tổng các số từ 1 đến số vừa nhập 
#Tạo 1 tuple chứa giai thừa các số đã nhập.
class giaithua():
    def __init__(self,a):
        self.a=a 
    def giaithua(self):
        tich = 1
        for i in range(1,self.a+1):
            tich = tich*i
        return tich
    def tong(self):
        t = 0
        for i in range(0,self.a+1):
            t = t + i 
        return t
l=[]
s=[]
k=[]
d={}
for i in range(0,3):
    a=int(input("nhap so: "))
    obj=giaithua(a)
    l.append(obj)
    s.append(a)
    d[s[i]]=l[i].giaithua()
for i in range(0,3):
    print("tong la:"+str(l[i].tong()))
for i in range(0,3):
    k.append(l[i].giaithua())
t = tuple(k)
print(d)
print(t)
    
    

