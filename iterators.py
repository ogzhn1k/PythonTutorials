

numList = [1,2,3,4,5]

iterator = iter(numList)

# print(next(iterator)) # 1
# print(next(iterator)) # 2
# print(next(iterator)) # 3
# eleman bitince hata verir

# for i in numList :
#     print(i)

# iterator = iter(numList)
# while True :
#     try :
#         element = next(iterator)
#         print(element)
        
#     except StopIteration as sI:
#         break
            
class myNumbers :
    def __init__(self,start,stop) :
        self.start = start
        self.stop = stop
    
    def __iter__(self) :
        return self    
    
    def __next__(self) :
        if self.start <= self.stop :
            x = self.start
            self.start += 1
            return x 
        else :
            raise StopIteration

list_ = myNumbers(10,20) 
# for x in list_ :
#     print(x)

list_iter = iter(list_)
while True :
    try :
        num = next(list_iter)
        print(num)
    except StopIteration as si :
        print(si)
        break
