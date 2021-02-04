
# def changeList(n_list,i,city) : # Pass by reference
#     n_list[i] = city


# list_n = ["Corum","Adiyaman","Izmır","Eskisehir","Hatay","Bursa"]
# i = 5
# c = "Ankara"

# changeList(list_n,i,c)
# print(list_n)


# def add(a,b,c=0) :
#     return sum((a,b))

# a = 12
# b = 23
# print(add(a,b))

def add(*params) :
    print(params)# tuple olarak yazdirilir
    return sum((params)) # Sum tuple parametre alir

a = 12
b = 23
#c = 35
print(add(a,b))


def display_user(**args) :
    print(type(args))

    for key,value in args.items():
        print('{} is {}'.format(key,value))

display_user(name='Oguzhan',age= 22, city='Corum') # Key-Value seklinde oldugu icin dictionary oldu
display_user(name='Eda',age= 14, city='Ankara',phone="234772")
display_user(name='Duygu',age= 18, city='London',phone="324892",e_mail="duygubirk@gmail.com")


def my_func(a,b,*args,**kwargs):
    print(a)
    print(b)
    print(args)
    print(kwargs)

my_func(10,20,30,40,50,key1='value1',key2='value2')