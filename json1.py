import json

person_str = '{"name" : "Ali","languages" : ["Python","C#"]}'
person_dict = {
    "name" : "Oguzhan",
    "languages" : ["Python","Java"]
}
# result =  json.loads(person_str) # json string to dict
# print(type(result))
# print(result['name'])
# print(result['languages'][1])

# with open("person.json") as fr :
#     data = json.load(fr)
#     print(data)


result = json.dumps(person_dict) # dict to json string
print(type(result))

with open("person.json","w") as fw :
    json.dump(person_dict,fw)
    
person_dict = json.loads(person_str)
result = json.dumps(person_dict,indent=4,sort_keys=True)
print(result)
print(person_dict)