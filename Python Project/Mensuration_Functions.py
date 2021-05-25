class Mensuration:
    def rectangle():
        while True:
            l = float(input("length = : "))
            w = float(input("width = : "))
            ops = int(input('''  type 1. for perimeter of rectangle. \n type 2. for Area of rectangle.\n'''))
            print("")
        
            if ops ==1:
                return print("Perimeter of rectangle is :", 2*(l+w))
            elif ops ==2:
                return print("Area of rectangle is :", l*w)
            else:
                print("::::enter only 1 or 2 try again ::::")
        return

    def square():
        while True:
            s= float(input("side :"))
            ops = int(input('''type 1. for perimeter of square. \n type 2 for area of square \n'''))
            if ops==1:
                return ("perimeter of square is :::",4*s)
            elif ops == 2:
                return ("area of square is ::::",s**2)
            else:
                print("::::enter valid input try again::::")
        return 


    def parallelogram():
        b=float(input("base::"))
        h=float(input("height"))
        return ("Area of parallelogram is: ",b*h)


    def circle():
        while True:
            r = float(input("radius "))
            ops = int(input('''type 1. for perimeter of circle. \n type 2 for area of circle \n'''))
            if ops==1:
                return("perimeter of circle:",2*(22/7)*r)
            elif (ops==2):
                return ("area of circle is :",2*3.14*r**2)
            else:
                print("::::enter valid input try again::::")
        return    


    def pentagon():
        while True:
            s = float(input("side :"))
            a = float(input("apothem :"))
            ops = int(input('''type 1. for perimeter of pentagon.\n type 2 for area of pentagon. \n'''))
            if ops==1:
                return("perimeter of pentagon:")

            elif ops==2:
                return("area of pentagon:")

            else:
                print("::::enter valid input try again::::")
        return


    def cube():
        while True:
            s =float(input("side :"))
            ops = int(input('''type 1. for Total Surface Area(TSA) of cube. \n type 2 for Volume of cube. \n'''))
            if ops == 1:
                print("Total Surface Area of cube is :" ,6*s**2)

            elif ops == 2:
                print("Volume of cube :",s**3)

            else:
                print("::::enter valid input try again::::")
        return 


    def cuboid():
        while True:
            l=float(input("length:"))
            b=float(input("breadth:"))
            h=float(input("height:"))
            ops = int(input('''type 1. for Total Surface Area(TSA) of cuboid. \n type 2 for Volume of cuboid. \n'''))
            if (ops==1):
                return("Total Surface Area(TSA) of cuboid is:",2 * (l*b+b*h+h*l))

            elif(ops==2):
                return(" Volume of cuboid is :",l*b*h)

            else:
                print("::::enter valid input try again::::")
        return 


    def sphere():
        while True:
            r = float(input("radius:"))
            ops = int(input('''type 1. for Total Surface Area(TSA) of sphere.\n type 2 for Volume of sphere. \n'''))
            if (ops == 1):
                return("total Surface Area(CSA) of sphere is:", 4*3.14*r**2)

            elif (ops == 2):
                return(" Volume of sphere is :",(4/3)*3.14*r**2)

            else:
                print("::::enter valid input try again::::")
        return


    def cylinder():
        while True:
            r = float(input("radius :"))
            h = float(input("height:"))
            ops = int(input('''type 1. for Total Surface Area(TSA) of cylinder. \n type 2. for Curved Surface Area(CSA) of cylinder. \n type 3 for Volume of cylinder\n'''))
            if(ops==1):
                return("Total Surface Area(TSA) of cylinder:",(2*3.14*r*h)+(2*3.14*r**2) )

            elif(ops==2):
                return("Curved Surface Area(CSA) of cylinder:",2*3.14*r*h)

            elif(ops==3):
                return("Volume of cylinder",3.14*(r**2)*h)

            else:
                print("::::enter valid input try again::::")
        return

            
    def cone():
        while True:
            r = float(input("radius:"))
            h = float(input("height:"))
            ops = int(input('''type 1. for Total Surface Area(TSA) of cone. \n type 2. for Curved Surface Area(CSA) of cone. \n type 3 for Volume of cone\n :::::>'''))
            if ops==1:
                print("Total Surface Area(TSA) of cone.:",3.14*r*(r+((r**2) + (h**2))))

            elif ops ==2:
                print("Curved Surface Area(CSA) of cone.:",3.14*r*(r**2)+(h**2))

            elif ops==3:
                print("Volume of cone :",(1/3)*3.14*(r**2)*h)

            else:
                print("::::enter valid input try again::::")
        return



if __name__ == '__main__':
    m = Mensuration
    print("//////////////////// ::::::Mensuration module :::::: /////////////////////")
    print(''':::::::::::::::::::::::{type any one in list}:::::::::::::::::::::::::::
    1.rectangle     ::::::(1. perimeter 2. Area)::::::
    2.square        ::::::(1. perimeter 2. Area)::::::
    3.parallelogram ::::::(1.Area)::::::
    4.circle        ::::::(1. perimeter 2. Area)::::::
    5.pentagon      ::::::(1. perimeter 2. Area)::::::
    6.cube          ::::::(1. Total Surface Area(TSA) 2.Volume)::::::
    7.cuboid        ::::::(1. Total Surface Area(TSA) 2.Volume)::::::
    8.sphere        ::::::(1. Total Surface Area(TSA) 2.Volume)::::::
    9.cylinder      ::::::(1. Total Surface Area(TSA) 2.Curved Surface Area(CSA) 3.Volume)::::::
    10.cone         ::::::(1. Total Surface Area(TSA) 2.Curved Surface Area(CSA) 3.Volume)::::::''')
    x=input("Please enter any input\n[hint: 1 or rectangle] \n::::::>")

    if (x=="rectangle" or x=="1") :
        m.rectangle()

    elif(x=="square" or x=="2"):
        m.square()

    elif(x=="parallelogram" or x=="3"):
        m.parallelogram()

    elif(x=="circle" or x=="4"):
        m.circle()

    elif(x=="pentagon" or x=="5"):
        m.pentagon()

    elif(x=="cube" or x=="6"):
        m.cube()

    elif(x=="cuboid" or x=="7"):
        m.cuboid()

    elif(x=="sphere" or x=="8"):
        m.sphere()

    elif(x=="cylinder" or x=="9"):
        m.cylinder()

    elif(x=="cone" or x=="10"):
        m.cone()

    else:
        print(":::::::::::Out of Course:::::::::::::")



