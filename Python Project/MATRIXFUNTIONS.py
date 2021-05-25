class MatrixFunctions(self):
    def __init__(self, a, b):
        self.a=a
        self.b=b

    def matrixaddf(self):
        c=[[],[],[]]
        for i in range(0,3):
            for j in range(0,3):
                z=self.a[i][j]+self.b[i][j]
                c[i].append(z)
        return c

    def matrixsubf(self):
        c=[[],[],[]]
        for i in range(0,3):
            for j in range(0,3):
                z=self.a[i][j]-self.b[i][j]
                c[i].append(z)
        return c

    def matrixequalf(self):
        c = [[],[],[]]
        z=0
        for i in range(0, 3):
            for j in range(0, 3):
                x = self.a[i][j] - self.b[i][j]
                z+=x
        if z== 0:
            return("matrix are equal")
        else:
            return("matrix not equal")

if __name__ == "__main__":
    a=[]
    b=[]
    for i in range(0,3):
        print("matrix enter:a",i+1,sep="")
        x=list(map(int,input().split()))
        a.append(x)
    for i in range(0,3):
        print("matrix enter b.",i+1,sep="")
        x = list(map(int, input().split()))
        b.append(x)
    m = MatrixFunctions(a, b)
    ops=input("1.Addition 2.Subtraction 3.equal ")
    if (ops=="1" or ops=="addition"):
        print(m.matrixaddf())

    elif(ops=="2" or ops=="Subtraction"):
        print(m.matrixsubf())

    elif(ops=="3" or ops=="equal"):
        print(m.matrixequalf())


