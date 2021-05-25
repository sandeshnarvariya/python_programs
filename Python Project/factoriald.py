n=input("enter no.")
x=str(n)
s=x[::-1]
s.lower()
print(s,x)
if s==x:
    print("palindrome")
else:
    print("not palindrome")