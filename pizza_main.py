print("Welcome to the PIZZA HOUSE")
size = input("What size of Pizza do you want (SMALL/MEDIUM/LARGE) :> ")
extraCheese = str(input("Do you want extra cheese? (Y/N) :> "))
extraToppings = input ("Do you want extra toppings? (Y/N) :> ")
bill = 0
if size == "small":
    bill = 30
    if extraCheese == "y":
        bill += 2
    if extraToppings == "y":
        bill += 2
    print("Your total bill is $" + str(bill))
elif size == "medium":
    bill = 40
    if extraCheese == "y":
        bill += 2
    if extraToppings == "y":
        bill += 2

    print("Your total bill is $" + str(bill))
else :
    bill = 50
    if extraCheese == "y":
        bill += 2
    if extraToppings == "y":
        bill += 2

    print("Your total bill is $"+ str(bill))