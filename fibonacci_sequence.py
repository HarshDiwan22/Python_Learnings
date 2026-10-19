flag = True
while flag:
    ask = int(input("Enter a number (1 to 30): "))
    sum = 0
    def fib(n):
        if n == 1 or n == 2:
            return 1
        elif 30 >= n >= 3:
            sum = fib(n - 1) + fib(n - 2)
            return sum
        else:
            return 0
    answer = fib(ask)
    if answer == 0:
        print("Please write a number in given range.")
    else:
        print(answer)