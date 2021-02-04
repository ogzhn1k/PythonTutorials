
# for i in range(10) :
#     print(i)

numbers = [x for x in range(10)]
print(numbers)

numbers = [x**2 for x in range(10)]
print(numbers)

numbers = [x*x for x in range(10)]
print(numbers)

numbers = [x*x for x in range(10) if x%3==0]
print(numbers)

letters = 'Oguzhan'
myList = [letter for letter in letters]
print(myList)

years = [1983,1998,2007,1956,1933]
ages = [2021-year for year in years if year>1977]
print(ages)

results = [x if x%2 == 0 else 'TEK' for x in range(1,20)]
print(results)

# result = []
# for x in range(3) :
#     for y in range(3) :
#         result.append((x,y))
# print(result)

numbers = [(x,y) for x in range(3) for y in range(3)]