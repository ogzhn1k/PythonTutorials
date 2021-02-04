
cars = ["Bmw","Mercedes","Opel","Mazda"]
print("Length of the list : {}".format(len(cars)))
print("First element of the list : {}".format(cars[0]))
print("Last element of the list : {}".format(cars[3]))
cars[3] = "Toyota"
print("New List after the replace : {}".format(cars))
key = cars.__contains__("Mercedes")
if key == True:
    print("The list contains {}".format(cars[1]))
#key = "Mercedes" in cars    
print("-2. index of the list : {}".format(cars[-2]))
print(cars[::-1])
#cars.__delitem__(3)
cars[-2:] = ["Wolkswagen","Renault"]
#del cars[-1]
print(cars)

