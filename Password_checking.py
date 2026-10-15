letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
Upper_case = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+', '-', '_']

print("\n     Welcome to the Python Password Checker!\n")
c = 0
flag = True
while flag:
    ask = input("Enter any password :- ")
    def check():
        global c
        for char in ask:
            if char in symbols:
                c += 1
            if char in numbers:
                c += 1
            if char in Upper_case:
                c += 1
            if ask in letters:
                c += 1
    check()
    if c >= 4:
        print("Your password is good enough to use.")
        flag = False
    else:
        print("Please try a stronger password")
        c = 0


