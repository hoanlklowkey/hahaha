from math import sqrt


class Songuyen:
    def __init__(self, n):
        self.n = n

    def ktchanle(self):
        if self.n % 2 == 0:
            return True
        return False

    def ktnt(self):
        if self.n < 2:
            return False
        for i in range(2, self.n):
            if self.n % i == 0:
                return False
            return True

    def ktcp(self):
        if sqrt(self.n) % 1 == 0:
            return True
        return False


while (True):
    sn = []
    sole = []
    tichnt = 1
    socp = []

    for i in range(1, 4):
        print("Số thứ ", i)
        n = int(input(" "))
        sn.append(n)

    for i in range(0, 3):
        s = Songuyen(sn[i])
        if s.ktchanle() == False:
            sole += " " + str(sn[i])
        if s.ktnt() == True:
            tichnt *= sn[i]
        if s.ktcp() == True:
            socp.append(sn[i])

    if len(socp) == 0:
        Min = - 1
    else:
        Min = min(socp)

    print("cac so le lan luot la: ", sole)
    print("tich cac so nguyen to: ", tichnt)
    print("so chinh phuong nho nhat: ", Min)

