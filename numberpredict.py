import random

x =  random.randint(1,10)
chance = int(input("What chance user do you have : "))
#print(f"Correct answer is {x}")
for i in range(0,chance) :
    prediction = int(input("Please enter your prediction (1-10) : "))
    if(prediction>10):
        i = i-1
    if prediction == x :
        print("CORRECT :)")
        quit()
    else:
        print("Please try again :(")
        chance -= 1 
        if prediction < x :
            print("UP")
        else :
            print("DOWN")             

print("UNCORRECT ANSWERS!!!")
print(f"Correct answer is {x}")


