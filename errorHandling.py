
while True:
    try:
      x = int(input("Enter first number : "))
      y = int(input("Enter second number : "))
      print(x/y)
      
# except ZeroDivisionError as identifier:
#     print("You can not divide the number by zero!!!")
# except ValueError as valerror :
#     print("Please enter the correct form of the value!!!")
    except (ZeroDivisionError, ValueError) as errors:
       print("You have entered incorrect value!!!",errors)
       print(errors)
# except : # general statement
#     print("You have entered incorrect value!!!")
    else:
      print("All statements are right :)")
      break
    
    finally :
      print("End of handling")