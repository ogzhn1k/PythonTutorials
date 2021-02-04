import requests as req
import json

url = "https://api.exchangeratesapi.io/latest?base="
exchangeType = input("Please enter the currency type which is going to be exchanged : ").upper()
intake = input("Please enter the currency type which is going to be taken : ").upper()  
amount = int(input("Please enter the amount of currency : "))
getResult = req.get(url+exchangeType) # <Response [200]> döndürür
#print(type(getResult.text)) # str döndürür
dictResult = json.loads(getResult.text) # dictionary döndürür


k = dictResult["rates"][intake]
print(f"1 {exchangeType} = {k} {intake}")
result = amount * k
print(f"{amount} {exchangeType} = {result} {intake}")        