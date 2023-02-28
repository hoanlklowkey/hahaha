#Tạo class điện trở gồm 3 vòng màu và 1 phương thức xác định giá trị điện trở theo vòng màu
#Nhập 1 list có 3 điện trở (là object tạo bởi class trong yêu cầu 1. Khuyến khích tạo giao diện GUI)
#   In ra giá trị các điện trở (được xác định theo vòng màu) vừa nhập 
#   Tạo 1 tuple chứa giá trị của 3 điện trở trên
#   Tìm điện trở có trở kháng nhỏ nhất.
class dientro():
    def __init__(self,a,b,c):
        self.a=a
        self.b=b
        self.c=c
    def doc(self):
        if self.a=="den":
            gt=0
        if self.a=="nau":
            gt=1
        if self.a=="do":
            gt=2
        if self.a=="cam":
            gt=3
        if self.a=="vang":
            gt=4
        if self.a=="luc":
            gt=5
        if self.a=="lam":
            gt=6
        if self.a=="tim":
            gt=7
        if self.a=="xam":
            gt=8
        if self.a=="trang":
            gt=9
        if self.b=="den":
            gt1=10**0
        if self.b=="nau":
            gt1=10**1
        if self.b=="do":
            gt1=10**2
        if self.b=="cam":
            gt1=10**3
        if self.b=="vang":
            gt1=10**4
        if self.b=="luc":
            gt1=10**5
        if self.b=="lam":
            gt1=10**6
        if self.b=="tim":
            gt1=10**7
        if self.b=="xam":
            gt1=10**8
        if self.b=="trang":
            gt1=10**9
        if self.c=="nau":
            gt2="+-1%"
        if self.c=="do":
            gt2="+-2%"
        if self.c=="luc":
            gt2="+-0.5%"
        if self.c=="lam":
            gt2="+-0.25%"
        if self.c=="tim":
            gt2="+-0.1%"
        if self.c=="xam":
            gt2="+-0.05%"
        if self.c=="hoang kim":
            gt2="+-5%"
        if self.c=="bac":
            gt2="+-10%"
        if self.c=="khong co":
            gt2="+-20%"
        w=str(gt) +"x" +str(gt1)+"  " + gt2
        return w
class dientro1():
    def __init__(self,a,b,c):
        self.a=a
        self.b=b
        self.c=c
    def sapxep(self):
        if self.a=="den":
            gt=0
        if self.a=="nau":
            gt=1
        if self.a=="do":
            gt=2
        if self.a=="cam":
            gt=3
        if self.a=="vang":
            gt=4
        if self.a=="luc":
            gt=5
        if self.a=="lam":
            gt=6
        if self.a=="tim":
            gt=7
        if self.a=="xam":
            gt=8
        if self.a=="trang":
            gt=9
        if self.b=="den":
            gt1=10**0
        if self.b=="nau":
            gt1=10**1
        if self.b=="do":
            gt1=10**2
        if self.b=="cam":
            gt1=10**3
        if self.b=="vang":
            gt1=10**4
        if self.b=="luc":
            gt1=10**5
        if self.b=="lam":
            gt1=10**6
        if self.b=="tim":
            gt1=10**7
        if self.b=="xam":
            gt1=10**8
        if self.b=="trang":
            gt1=10**9
        f=gt*gt1
        return f
        
l=[]
h=[]
s=[]
k=[]
for i in range(0,3):
    print("tro thu %d"%(i+1))
    a=str(input("nhap vong 1: "))
    b=str(input("nhap vong 2: "))
    c=str(input("nhap vong 3: "))
    obj = dientro(a,b,c)
    l.append(obj)
    obj1 = dientro1(a,b,c)
    h.append(obj1)
for i in range(0,3):
    print(l[i].doc())
    s.append(l[i].doc())
t = tuple(s)
print(t)
for i in range(0,3):
    k.append(h[i].sapxep())
m = max(k)
for i  in range(0,3):
    if(m==h[i].sapxep()):
        print("tro %d co gia tri lon nhat"%(i+1))


