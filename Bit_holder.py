logo = r'''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''
print(logo)
print("<<<< WELCOME TO THE BLIND AUCTION PROGRAM >>>>")
auction_list = {}
flag = True

def calculator(auction):
    highest_bid = 0
    winner = ""
    for first in auction:
        bid_amount = auction[first]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = first

    print(f"The Maximum bid is ${highest_bid} by {winner} ")

while flag:
    name = input("What is your name?\n")
    bid = int(input("Enter your bid -> $ "))
    auction_list[name] = bid
    ask = input("Do you have someone for the next bid ?(type 'yes' or 'no')\n").lower()
    if ask == 'yes':
        print("\n" * 30)

    else :
        flag = False
        print("\n" * 30)
        calculator(auction_list)