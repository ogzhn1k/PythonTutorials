

def cube():
    for i in range(5):
        yield i ** 3
        
             
generator = cube() # iterable döndürür
# iterator = iter(generator)

for i in cube() :
    print(i)    
    
        
list_ = (i**3 for i in range(5)) # genarator
for i in  list_ :
    print(i)          
        
        