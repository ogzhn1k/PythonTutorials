import math
#from math import * # modul ismini kullanmaya gerek kalmaz 
#from math import sqrt,factorial
# eger biz de fonksiyon tanimlarsak hazir olani degil de onu kullanir
value = dir(math) # hangi metodlari barindirir
print(value)

value = help(math) # metodlar hakkında bilgilendirmeler
print(value)

value = help(math.fabs) # belirtilen metod hakkinda bilgi verir
print(value)