#Tạo class phương trình bậc 2 gồm giá trị a,b,c và 1 phương thức tìm nghiệm.
#Tạo 1 list có 2 phương trình bậc 2 (phương trình bậc 2 là các object tạo bởi class trong yêu cầu 1. Khuyến khích tạo giao diện GUI)
#In ra nghiệm của 2 phương trình vừa nhập 
#Tạo 1 tuple chứa các nghiệm của 2 phương trình? 
#Tìm nghiệm lớn nhất trong các nghiệm của 2 phương trình trên.
import math
class pt():
    def __init__(self,a,b,c):
        self.a=a
        self.b=b
        self.c=c
    def timnghiem(self):
        if self.a==0 and self.b!=0 and self.c!=0:
            print("nghiem cua phuong trinh la:"+ str(-c/b))
        elif self.a==0 and self.b==0 and self.c!=0:
            print("phuong trinh vo  nghiem")
        elif self.a==0 and self.b==0 and self.c==0:
            print("phuong trinh vo so nghiem")
        else:
            d =  self.b**2-4*self.a*self.c
            if d>0:
                x1 = (-self.b+math.sqrt(d))/2*self.a
                x2 = (-self.b-math.sqrt(d))/2*self.a
                print("phuong trinh co 2 nghiem la:"+str(x1)+str(x2))
            elif d<0:
                print("phuong trinh vo nghiem")
            elif d==0:
                print("phuong trinh co nghiem kep"+str(-self.b/2*self.a))
l=[]
for i in range(0,2):
    print("phuong trinh %d"%(i+1))
    a = int(input("nhap gia tri a: "))
    b = int(input("nhap gia tri b: "))
    c = int(input("nhap gia tri c: "))
    obj = pt(a,b,c)
    l.append(obj)
for i in range(0,2):
    l[i].timnghiem()


