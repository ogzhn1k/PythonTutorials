
def square(num) :
    return num**2

list_num = [1,2,3,4,5,6,7,8,9]

square = lambda num:num**2 
print(square(17))
result = list(map(square,list_num)) # Fonksiyon ismi ve dizi yazilir
result = list(map(lambda num:num**2,list_num))# lambda yerine square yazilabilir
# x, y = map(int, input("Please enter the range : ").split())
# for item in map(square,list_num) :
#     print(item)

print(result)


def isEven(num):
    return num%2==0
# İlk parametre fonksiyon sonraki parametre ise listedir
numbers = [1,4,9,3,12,53,47,64]
check_even = lambda num : num%2 == 0
result = list(filter(isEven,numbers))
result = list(filter(check_even,numbers))
print(result)
