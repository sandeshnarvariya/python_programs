# ////////Disarium number//////////

if __name__ == '__main__':
    #fnum=int(input())
   # lnum=int(input())
    #for x in range(1,10):
        x=175
        digit=[]
        num1=x
        num=0
        while (x!=0):
            temp=x
            y=temp%10
            x=x//10
            digit.append(y)
        digit.reverse()
        for i in range(0,len(digit)):
            num=num+(digit[i])**(i+1)

        if num==num1:
            print(num1,"is Disarium Number")
