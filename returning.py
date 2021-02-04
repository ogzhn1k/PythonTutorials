
# def pow(number) :
    
#     def inner(power) :
#         return number ** power
    
#     return inner

# two = pow(2)
# three = pow(3)
# print(two(5))
# print(three(4))

def operation(op_name) :
    def addition(*args) :
        sum = 0
        for i in args : 
            sum += i
        return sum    
    
    def multiplication(*args) :
        mul = 1
        for i in args : 
            mul *= i 
            
        return mul    
    
    if op_name == "addition" :
        return addition
    if op_name == "multiplication" :
        return multiplication
    
    
add = operation("addition")    
print(add(1,2,3,4,5,6,7,8,9))  
mul = operation("multiplication")
print(mul(1,2,3,4,5))  

# fonksiyonlar parametre olarak referanslariyla gonderilebilir







