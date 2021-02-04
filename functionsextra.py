
# def sayHello() :
#     print("Hello World!!!")

# greeting = sayHello
# # del greeting
# greeting()    

# def outer(num1) :
#     print("Outer Function") 
#     def inner(num1) :
#         print("Inner Function")
#         return num1 + 1 
#     num2 = inner(num1)
#     print(num1, num2)

# outer(22)

def factorial(number) :
    
    if not isinstance(number,int) :
        raise TypeError("Number must be an integer!!!")
    
    if not number >= 1 :
        raise ValueError("Number must be zero or positive")
    
    def inner_fact(number) :
        if number <= 1 :
            return 1
        
        return number * inner_fact(number-1)    
    
    return inner_fact(number)

try:
    print(factorial(-3))
except Exception as ex:
    print(ex)










