
x = 15
y = 35

print(f"x = {x} , y = {y}")

x , y = y , x

print(f"x = {x} , y = {y}")

x = 35
y = 4

print(y**2)
print(x//y)

values = 1,2,3,4,5,6,7,8,9,10
print(type(values)) # tuple
print(values)

newVal = 1,2,3
x,y,z = newVal
print(x,y,z)

x,y,*z = values
print(x,y,z)# x=1 y=2 z=[3,4,5,6,7,8,9,10]

a,b,c,d= 5,5,12,23
result = (a==b) #true
print(result)

x = 7
result = (5<x<12) and (x<6)
print(result)

x = y = ["Oguzhan","Eda","Duygu"]
z = ["Mustafa","Ayse"]

print(x is y) # true
print("Oguzhan" in x)# true
