num = float(input("Enter a number: "))

if num >= 0:
    root = num ** 0.5
    print("The square root of", num, "is", root)
else:
    print("Error: The number is negative")