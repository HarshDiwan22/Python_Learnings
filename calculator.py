logo = r"""
 _____________________
|  _________________  |
| | Pythonista   0. | |  .----------------.  .----------------.  .----------------.  .----------------. 
| |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
|  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
| | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
| |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
| | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
| |___|___|___| |___| | | |  \ `.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ `.___.'\  | |
| | 1 | 2 | 3 | | x | | | |   `._____.'  | || ||____|  |____|| || |  |________|  | || |   `._____.'  | |
| |___|___|___| |___| | | |              | || |              | || |              | || |              | |
| | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
| |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' 
|_____________________|
"""

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    if n1 > n2:
        return n1 - n2
    else:
        return n2 - n1

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

print(logo)
cal = {"+" : add, "-" : subtract, "*" : multiply, "/" : divide}
print("Welcome to the Calculator!!")
num1 = float(input("Enter first number: "))
flag = True
while flag:
    choice = input("Please select one of the options ( + , - , * , / ) -> ")
    num2 = float(input("Enter second number: "))
    answer = cal[choice](num1, num2)
    print(f"{num1} {choice} {num2} = {answer}")
    ask = input(f"Would you like to continue with {answer} (y/n) ? ").lower()
    if ask == "y":
        num1 = answer
    else:
        flag = False
