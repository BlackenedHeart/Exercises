def sum(*args):
    total = 0
    for num in args:
        total += num
    return total

tuple1 = (1, 2, 3, 4, 5)
tuple2 = (1.5, 2.5, 3.5, 4.5)

result1 = sum(*tuple1)
result2 = sum(*tuple2)

print(f"The sum of tuple1 is: {result1}")
print(f"The sum of tuple2 is: {result2}")
