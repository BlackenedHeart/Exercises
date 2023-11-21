import math

for x in range(-3, 4):
    try:
        result = math.sin(x) / x
        print(f"The value of sin({x}) / {x} is {result}")
    except ZeroDivisionError:
        print(f"The value of sin({x}) / {x} is undefined")