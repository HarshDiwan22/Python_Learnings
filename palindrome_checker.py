letter = []
check = []
flag = True
while flag == True:
    ask = input("Please enter a word : ").lower()
    for char in ask:
        letter.append(char)

    for i in range(-1,-len(letter)-1,-1):
        check.append(letter[i])
# clear() is used to clear the list.
    if letter == check:
        print("Yes it is a palindrome")
        letter.clear()
        check.clear()
    else:
        print("Not a palindrome")
        letter.clear()
        check.clear()