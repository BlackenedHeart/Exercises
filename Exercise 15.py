def sum_three(a, b, c):
    return a + b + c

numbers = (10, 20, 30)

result = sum_three(*numbers)

print(f"The sum of the numbers in the tuple is: {result}")
