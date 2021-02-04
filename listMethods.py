numbers = [13,26,89,78,23,67,89,12,77,11,58]

numbers.pop(3)
numbers.append(45)
numbers.insert(4,31)
numbers.remove(77)
max_num = max(numbers)
min_num = min(numbers)
numbers.reverse()
print(numbers)
numbers.sort()
print(numbers)
print(f"{numbers.count(89)}")
index = numbers.index(77)
print(index)
numbers.clear()
#https://www.w3schools.com/python/python_ref_list.asp