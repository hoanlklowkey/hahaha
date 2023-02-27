import math


class SoNguyen():
    def __init__(self, a):
        self.a = a

    def Check(self):
        if (self.a % 2 == 0):
            return True
        else:
            return False

    def SCP(self):
        if ((round(math.sqrt(self.a)))**2 == self.a):
            return True
        else:
            return False

    def SNT(self):
        self.a = int(self.a)
        check = 1
        for i in range(2, self.a):
            if (self.a % i == 0):
                check = 0
                break
            else:
                check = 1
        return check


myList = []
listChan = []
listSNT = []
tongCp = 0
for i in range(3):
    print("Nhap so thu %d" % i)
    so = int(input())
    myList.append(so)

for i in range(3):
    so = SoNguyen(myList[i])
    if so.Check():
        listChan.append(myList[i])

    if so.SCP():
        tongCp += myList[i]

    if so.SNT():
        listSNT.append(myList[i])
for i in range(len(listSNT)):
    Max = 0
    if listSNT[i] > Max:
        Max = listSNT[i]

print(listChan)
print(tongCp)
print(Max)
