import random
x=random.random()
y = int(x * 100)
i=0
s=[]
while(True):
    i+=1
    inp = int(input("find the guess no.:\n"))
    s.append(inp)
    if (inp<y):
        print("your no small then guess. "
              "please try again:")
    elif(inp>y):
        print("your no is grater then guess. "
              "please try again:")
    else:
        break
print(f"you have using {i} step: {s} \n:::::::: congratulation :::::::")