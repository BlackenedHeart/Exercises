import math

def cube(x):
    return x ** 3

def volumeSphere(r):
    volume = (4/3) * math.pi * cube(r)
    return volume

radius = 5  # par exemple
result = volumeSphere(radius)
print(f"The Volume of the sphere with radius {radius} is {result}")
