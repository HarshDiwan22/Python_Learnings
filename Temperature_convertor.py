ask = float(input("Enter a temperature value : "))
unit = input("Enter a unit (c / f) : ").lower()

if unit == "c":
    ans = ask * 1.8 +32
    print(f"The conversion of {ask}{unit} in fahrenheit is {ans}.")

elif unit == "f":
        ans = round((ask - 32) * 0.556,2)
        print(f"The conversion of {ask}{unit} in calsius is {ans}.")

else:
    print("Invalid unit")