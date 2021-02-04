import re

text = "Python Course : Python Programming Tutorial | 40 Hours"

result = re.findall("Python",text)
print(result) # ["Python","Python"]
print(len(result))

result = re.split(" ",text)
print(result) # ['Python', 'Course', ':', 'Python', 'Programming', 'Tutorial', '|', '40', 'Hours']

result = re.sub(" ","-",text) # bosluk yerine \s konulabilir
print(result) # Python-Course-:-Python-Programming-Tutorial-|-40-Hours

result = re.search("Python",text) # match object
print(result.start()) # 0
print(result.end()) # 6
print(result.group()) # Python
print(result.span()) # (0,6)
print(result.string) # Python Course : Python Programming Tutorial | 40 Hours

result = re.findall("[abc]",text)
print(result)
result = re.findall("[a-e]",text)
print(result)
result = re.findall("[1-5]",text)
print(result)
result = re.findall("[^abc]",text)
print(result)
result = re.findall("[^0-9]",text)
print(result)

result = re.findall("...",text) # ['Pyt', 'hon', ' Co', 'urs', 'e :', ' Py', 'tho', 'n P', 'rog', 'ram', 'min', 'g T', 'uto', 'ria', 'l |', ' 40', ' Ho', 'urs']
print(result)

result = re.findall("Py..on",text) # ['Python', 'Python']
print(result)

result = re.findall("^a",text) # ['Python', 'Python'] # a ile basliyor mu? string ifadenin
print(result)


result = re.findall("t$",text) # t ile bitiyor mu?
print(result)