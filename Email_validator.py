character = ['@']
check = []
mail = ['g','m','a','i','l','.','c','o','m']
chance = 3
for i in range(chance):
    enter = input("Enter your mail id : ")
    if enter[-10] in character:
        for i in range(-9,0):
            check.append(enter[i])
        if check == mail:
            print("Yes it is a valid mail")

    else:
        print("Not valid")