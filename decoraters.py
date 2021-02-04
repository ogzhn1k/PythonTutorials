

def my_dec(func) :
    
    def wrapper() :
        print("Before function")
        func()
        print("After function")
    
    return wrapper

@my_dec
def sayhello() :
    print("Hello")

@my_dec    
def sayGreeting() :
    print("Greeting")    
        
sayhello()
sayGreeting() 
    
# sayhello = my_dec(sayhello)
# sayhello()

# sayGreeting = my_dec(sayGreeting)
# sayGreeting()













