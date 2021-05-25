
def GuessPass(passcode,Hint=None):
    count = 1
    password = input("Enter password\n")
    print(f"::::::::Hint::::::\n{Hint}\n-------------------")
    while (password != passcode):
        count += 1
        print("Try again.....")
        password = input("Enter password\n")
    return print(f"Congratulation and your attenmt is: {count}")
    
if __name__ == "__main__":
    GuessPass("GuessWord","Give hint")
