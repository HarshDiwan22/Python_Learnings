import random

logo = ''' __        ___           _        _         _   _                                     _               
 \ \      / / |__   __ _| |_     (_)___    | |_| |__   ___      _ __  _   _ _ __ ___ | |__   ___ _ __ 
  \ \ /\ / /| '_ \ / _` | __|    | / __|   | __| '_ \ / _ \    | '_ \| | | | '_ ` _ \| '_ \ / _ \ '__|
   \ V  V / | | | | (_| | |_     | \__ \   | |_| | | |  __/    | | | | |_| | | | | | | |_) |  __/ |   
    \_/\_/  |_| |_|\__,_|\__|    |_|___/    \__|_| |_|\___|    |_| |_|\__,_|_| |_| |_|_.__/ \___|_|   
                                                                                                      '''
print(logo)
print("\n" * 1 + "            Welcome to Number Guessing Project!!\n\n")
print("The range of number is between 1 and 100 \n" + "Please enter difficulty level (Easy, Medium, Hard):-")
level = input().lower()
actual_number = int(random.randint(1, 101))

def guess(attempts):
    flag = False
    while attempts != 0:
        print(f"You have {attempts} attempts to guess the number.")
        ask = int(input(f"Try a guess between 1 and 100 : "))
        if ask == actual_number:
            print(f"You got it! {actual_number} is correct !")
            flag = True
            break
        elif 0 >= ask >= 101:
            print("Please Check the range of searching..\n")
            attempts -= 1
        elif ask < actual_number:
            print("Too low, try again.\n")
            attempts -= 1
        elif ask > actual_number:
            print("Too high, try again.\n")
            attempts -= 1
    if flag == False:
        print(f"You have no more attempts to guess")
    else:
        print(f"CONGRATS :)")
attempt = 0
if level == "easy":
    attempt = 7
    guess(attempt)
elif level == "medium":
    attempt = 5
    guess(attempt)
elif level == "hard":
    attempt = 3
    guess(attempt)
else:
    print("Please enter a valid level.")