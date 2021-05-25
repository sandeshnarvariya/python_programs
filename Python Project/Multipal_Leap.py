# List of Years and check who are leap year
year = list(map(int,input().split()))
for i in range(0, len(year)):
    if (year[i] % 100 == 0):
        if (year[i] % 400 == 0):
            print(year[i],"leap year")
        else:
            print(year[i],"not leap year")
    elif (year[i] % 4 == 0):
        print(year[i],"leap year")
    else:
        print(year[i],"not leap year")
