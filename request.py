# PyPI
import requests as req
import json

result = req.get("https://jsonplaceholder.typicode.com/todos") # <Response [200]>
#result = result.text
#print(type(result)) # str
result = json.loads(result.text) # json str  to dict

for i in result:
    if i["userId"] == 1:
       print(i["title"])

