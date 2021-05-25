num=int(input())
temp=num
while sum !=1 and sum!= 4:
    sum=0
    while temp != 0:
        rem = int(temp%10)
        sum = sum+rem*rem
        temp = temp/10
    temp=sum
if (sum==1):
    print(num,"happy no.")
else:
    print(num, "unhappy no.")