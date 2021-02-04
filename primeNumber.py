

number = int(input("Please enter a number : "))
control = False

for i in range(2,number) :
    if number == 2 :
        control = True
        break
    if number % i == 0 :
        control = True
        break

if control == False :
    print(f"{number} is a prime number")
else:
    print(f"{number} is not a prime number")
