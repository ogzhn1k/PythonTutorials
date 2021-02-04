message = "hello there. My name is Oguzhan Birk"

up_mes = message.upper()
lw_mes = message.lower()
tit_mes = message.title()
cap_mes = message.capitalize()
strp_mes = message.strip() # bas ve son bosluk siler
splt_mes = message.split(' ')
join_mes = ' '.join(splt_mes)
num = join_mes.find('Oguzhan')
print(str(num))
isFound = message.startswith("h")
isfound = message.endswith("k")
rep_mes = message.replace("Oguzhan","Onur")
rep_mes = message.replace('ö','o').replace('ü','u').replace(' ','-')
placeholder_mes = message.center(100,'*')

print(up_mes)
print(lw_mes)
print(tit_mes)
print(cap_mes)
print(strp_mes)
print(splt_mes)
print(join_mes)
print(rep_mes)
print(placeholder_mes)
#https://www.w3schools.com/python/python_ref_string.asp