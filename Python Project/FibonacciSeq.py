# fibonacci sequence is 0 1 1 2 3 5 8 13
def fibonacci_Sequence(num):   #using recursive mathod 
    if num==0 :
        return 0
    elif num==1:
        return 1
    else:
        return fibonacci_Sequence(num+1) + fibonacci_Sequence(num+2)

num=int(input("enter integr num for fibonacci squence "))
print(fibonacci_Sequence(num))
