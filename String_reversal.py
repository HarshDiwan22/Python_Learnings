flag = True
while flag == True:
    string = input("Enter a string : ").lower()
    if string == "exit":
        flag = False
        break
    length = len(string)
    reversed_string = ""
    place_holder = -1
    for i in range(length):
        reversed_string += string[place_holder]
        place_holder -= 1
    print(reversed_string)