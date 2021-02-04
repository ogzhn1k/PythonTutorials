# Tuple

tpl = (1,"two",3)
print(type(tpl))
print(tpl[2])
print(len(tpl))
print(tpl)
# tpl[2] = "six" error çünkü tuple da tek eleman değiştirilemez, liste üzerine eleman ekleme ve silme yok
names1 = ("Ayse","Eda","Mustafa","Oguzhan","Duygu")
names2 = ("Ali","Veli","Deli") + names1
print(names2)