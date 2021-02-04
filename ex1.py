import math 

r = float(input("Please enter the radius : "))

area = math.pi * r * r
circum = math.pi * 2 * r

print("Area of the circle : " + str(area))
print("Circumference of the circle : " + str(circum))