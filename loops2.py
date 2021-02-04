

for item in range(50,100,10) :
    print(item)

print(list(range(5,100,10))) # [5, 15, 25, 35, 45, 55, 65, 75, 85, 95]

list_1 = [1,2,3,4,5]
list_2 = ['a','b','c','d','e']
list_3 = [100,200,300,400,500]

print(list(zip(list_1,list_2))) # [(1, 'a'), (2, 'b'), (3, 'c'), (4, 'd'), (5, 'e')]

for item in zip(list_1,list_2,list_3):
    print(item)


for a,b,c in zip(list_1,list_2,list_3):
    print(a,b,c) 
# 1 a 100
# 2 b 200
# 3 c 300
# 4 d 400
# 5 e 500