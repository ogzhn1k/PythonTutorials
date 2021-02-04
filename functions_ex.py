

# def printxtimes(*args) :
#     for i in range(*args[1]) :
#         print(*args[0]) # print(args[0]*args[1])
          

# word = input("Please enter the word : ")
# x = 5

# printxtimes(word,x)

# def convertolist(*args):
#     return list(args)

# a = 23
# b = 7
# c = 98
# d = 11
# e = 45
# f = 123
# g = 2

# list_el = convertolist(a,b,c,d,e,f,g)
# print(list_el)


# def isPrime(num) :
#     if num == 2 :
#         return True
#     for i in range(2,num) :
#         if num%i == 0 :
#             return False

#     return True        


# def findprimesinrange(num1,num2):
#     list_primes = []
#     if (num1 > num2) :
#         begin = num2 + 1
#         for x in range(begin,num1) :
#             if isPrime(x) == True:
#                 list_primes.append(x)

#     if (num1 < num2) :
#         begin = num1 + 1
#         for x in range(begin,num2) :
#              if isPrime(x) == True:
#                 list_primes.append(x)

#     return list_primes


# x, y = [int(x) for x in input("Please enter the range : ").split()] 
# x, y = map(int, input("Please enter the range : ").split())
# print(findprimesinrange(x,y))
