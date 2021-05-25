class pettern:
    def A():
        for row in range(5):
            for col in range(4):
                if (row == 0 and col == 0 or row == 0 and col == 3):
                    print(" ", end=" ")
                else:
                    if (row == 0 or col == 3 or col == 0 or row == 2):
                        print("*", end=" ")
                    else:
                        print(" ", end=" ")
            print()
        return

    def B():
        for row in range(5):
            for col in range(4):
                if (col == 3 and row == 2 or col == 3 and row == 0 or col == 3 and row == 4):
                    print(" ", end=" ")
                else:
                    if (row == 0 or col == 0 or row == 4 or row == 2):
                        print("*", end=" ")
                    else:
                        if (row == 1 and col == 3 or row == 3 and col == 3):
                            print("*", end=" ")
                        else:
                            print(" ", end=" ")
            print()
        return

    def C():
        for row in range(5):
            for col in range(4):
                if (col == 3 and row == 2 or row == 0 and col == 0 or row == 4 and col == 0):
                    print(" ", end=" ")
                else:
                    if (row == 0 or col == 0 or row == 4):
                        print("*", end=" ")
                    else:
                        print(" ", end=" ")
            print()
        return

    def D():
        for row in range(5):
            for col in range(4):
                if (col == 3 and row == 0 or col == 3 and row == 4):
                    print(" ", end=" ")
                else:
                    if (row == 0 or col == 0 or row == 4 or col == 3):
                        print("*", end=" ")
                    else:
                        if (row == 1 and col == 3 or row == 3 and col == 3):
                            print("*", end=" ")
                        else:
                            print(" ", end=" ")
            print()
        return

    def E():
        for row in range(5):
            for col in range(4):
                if (col == 3 and row == 2):
                    print(" ", end=" ")
                else:
                    if (row == 0 or col == 0 or row == 4 or row == 2):
                        print("*", end=" ")
                    else:
                        print(" ", end=" ")
            print()
        return

    def F():
        for row in range(5):
            for col in range(4):
                if (col == 3 and row == 2):
                    print(" ", end=" ")
                else:
                    if (row == 0 or col == 0 or row == 2):
                        print("*", end=" ")
                    else:
                        print(" ", end=" ")
            print()
        return

    def G():
        for row in range(5):
            for col in range(4):
                if (col == 0 and (row == 0 or row == 4) or row == 4 and col == 3):
                    print(" ", end=" ")
                else:
                    if (row == 2 and (col == 3 or col == 2) or row == 3 and col == 3):
                        print("*", end=" ")
                    else:
                        if (row == 0 or col == 0 or row == 4):
                            print("*", end=" ")
                        else:
                            print(" ", end=" ")
            print()
        return

    def H():
        for row in range(5):
            for col in range(4):
                if (col == 0 or col == 3 or row == 2):
                    print("*", end=" ")
                else:
                    print(" ", end=" ")
            print()
        return

    def I():
        for row in range(5):
            for col in range(3):
                if (row == 0 or row == 4 or col == 1):
                    print("*", end=" ")
                else:
                    print(" ", end=" ")
            print()
        return

    def J():
        for row in range(5):
            for col in range(4):
                if (row == 4 and col == 2 or row == 4 and col == 0 or col == 0 and row == 0 or col == 3 and row == 4):
                    print(" ", end=" ")
                else:
                    if (row == 4 or col == 2 or col == 0 and row == 3 or row == 0):
                        print("*", end=" ")
                    else:
                        print(" ", end=" ")
            print()
        return

    def K():
        for row in range(5):
            for col in range(4):
                if (col == 0 or row + col == 3 or row - col == 1):
                    print("*", end=" ")
                else:
                    print(" ", end=" ")
            print()
        return

    def L():
        for row in range(5):
            for col in range(3):
                if (row == 4 or col == 0):
                    print("*", end=" ")
                else:
                    print(" ", end=" ")
            print()
        return

    def M():
        for row in range(5):
            for col in range(5):
                if (row == 3 and col == 3):
                    print(" ", end=" ")
                else:
                    if (col == 0 or col == 4 or col - row == 0 or col == 3 and row == 1):
                        print("*", end=" ")
                    else:
                        print(" ", end=" ")
            print()
        return

    def N():
        for row in range(5):
            for col in range(5):
                if (col == 0 or col == 4 or col - row == 0):
                    print("*", end=" ")
                else:
                    print(" ", end=" ")
            print()
        return

    def O():
        for row in range(5):
            for col in range(5):
                if (row == 0 and col == 0 or row == 4 and col == 4 or row == 0 and col == 4 or row == 4 and col == 0):
                    print(" ", end=" ")
                else:
                    if (col == 0 or col == 4 or row == 0 or row == 4):
                        print("*", end=" ")
                    else:
                        print(" ", end=" ")
            print()
        return

    def P():
        for row in range(5):
            for col in range(4):
                if (col == 3 and (row == 0 or row == 2)):
                    print(" ", end=" ")
                else:
                    if (col == 0 or row == 0 or row == 2 or row == 1 and col == 3):
                        print("*", end=" ")
                    else:
                        print(" ", end=" ")
            print()
        return

    def Q():
        for row in range(6):
            for col in range(5):
                if (
                        row == 0 and col == 0 or row == 4 and col == 4 or row == 0 and col == 4 or row == 4 and col == 0 or row == 5 and col == 0):
                    print(" ", end=" ")
                else:
                    if (col == 0 or col == 4 or row == 0 or row == 4 or col == 2 and row == 3):
                        print("*", end=" ")
                    else:
                        print(" ", end=" ")
            print()
        return

    def R():
        for row in range(5):
            for col in range(4):
                if (col == 3 and (row == 0 or row == 2)):
                    print(" ", end=" ")
                else:
                    if (col == 0 or row == 0 or row == 2 or row == 1 and col == 3 or row - col == 1):
                        print("*", end=" ")
                    else:
                        print(" ", end=" ")
            print()
        return

    def S():
        for i in range(5):
            for j in range(3):
                if (i == 0 or i == 2 or i == 4):
                    print("*", end=" ")
                else:
                    if (j == 0 and i <= 2):
                        print("*", end=" ")
                    else:
                        if (j == 2 and i >= 3):
                            print("*", end=" ")
                        else:
                            print(" ", end=" ")
            print()
        return

    def T():
        for row in range(5):
            for col in range(5):
                if (col == 2 or row == 0):
                    print("*", end=" ")
                else:
                    print(" ", end=" ")
            print()
        return

    def U():
        for row in range(5):
            for col in range(4):
                if (row == 4 and (col == 0 or col == 3)):
                    print(" ", end=" ")
                else:
                    if (col == 0 or col == 3 or row == 4):
                        print("*", end=" ")
                    else:
                        print(" ", end=" ")
            print()
        return

    def V():
        for row in range(5):
            for col in range(5):
                if (row == 4 and (col == 0 or col == 4 or col % 2 != 0) or row == 3 and (col == 0 or col == 4)):
                    print(" ", end=" ")
                else:
                    if (row == 4 or col == 0 or col == 4 or row == 3 and col % 2 != 0):
                        print("*", end=" ")
                    else:
                        print(" ", end=" ")
            print()
        return

    def W():
        for row in range(5):
            for col in range(5):
                if (col == 0 or col == 4 or row == 3 and col % 2 != 0 or row == 2 and col % 2 == 0):
                    print("*", end=" ")
                else:
                    print(" ", end=" ")
            print()
        return

    def X():
        for row in range(5):
            for col in range(5):
                if (row == col or col + row == 4):
                    print("*", end=" ")
                else:
                    print(" ", end=" ")
            print()
        return

    def Y():
        for row in range(5):
            for col in range(5):
                if (row == 0 and (col == 0 or col == 4) or row == 1 and col % 2 != 0 or col == 2 and (
                        row == 2 or row == 3 or row == 4)):
                    print("*", end=" ")
                else:
                    print(" ", end=" ")
            print()
        return

    def Z():
        for row in range(5):
            for col in range(5):
                if (row == 0 or row == 4 or col + row == 4):
                    print("*", end=" ")
                else:
                    print(" ", end=" ")
            print()
        return



if __name__ == "__main__":
    p=pettern
    l = input()
    print("Pettern", l)
    for i in l:
        if (i == "a" or i == "A"):
            p.A()
            print("::::::::::::::::")
        elif(i == "b" or i == "B"):
            p.B()
            print("::::::::::::::::")
        elif (i == "c" or i == "C"):
            p.C()
            print("::::::::::::::::")
        elif (i == "d" or i == "D"):
            p.D()
            print("::::::::::::::::")
        elif (i == "e" or i == "E"):
            p.E()
            print("::::::::::::::::")
        elif (i == "f" or i == "F"):
            p.F()
            print("::::::::::::::::")
        elif (i == "g" or i == "G"):
            p.G()
            print("::::::::::::::::")
        elif (i == "h" or i == "H"):
            p.H()
            print("::::::::::::::::")
        elif (i == "i" or i == "I"):
            p.I()
            print("::::::::::::::::")
        elif (i == "j" or i == "J"):
            p.J()
            print("::::::::::::::::")
        elif (i == "k" or i == "K"):
            p.K()
            print("::::::::::::::::")
        elif (i == "l" or i == "L"):
            p.L()
            print("::::::::::::::::")
        elif (i == "m" or i == "M"):
            p.M()
            print("::::::::::::::::")
        elif (i == "n" or i == "N"):
            p.N()
            print("::::::::::::::::")
        elif (i == "o" or i == "O"):
            p.O()
            print("::::::::::::::::")
        elif (i == "p" or i == "P"):
            p.P()
            print("::::::::::::::::")
        elif (i == "q" or i == "Q"):
            p.Q()
            print("::::::::::::::::")
        elif (i == "r" or i == "R"):
            p.R()
            print("::::::::::::::::")
        elif (i == "s" or i == "S"):
            p.S()
            print("::::::::::::::::")
        elif (i == "t" or i == "T"):
            p.T()
            print("::::::::::::::::")
        elif (i == "u" or i == "U"):
            p.U()
            print("::::::::::::::::")
        elif (i == "v" or i == "V"):
            p.V()
            print("::::::::::::::::")
        elif (i == "w" or i == "W"):
            p.W()
            print("::::::::::::::::")
        elif (i == "x" or i == "X"):
            p.X()
            print("::::::::::::::::")
        elif (i == "y" or i == "Y"):
            p.Y()
            print("::::::::::::::::")
        elif (i == "z" or i == "Z"):
            p.Z()
            print("::::::::::::::::")

        else:
            print("no")