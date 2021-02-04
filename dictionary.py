# Dictionary

# cities = ["Kocaeli","Istanbul","Corum","Ankara"]
# plates = [46,34,19,6]

# city = input("Please enter the city : ")
# print(plates[cities.index(city)])

# key : value
plates = {"Kocaeli": 41,
          "Istanbul": 34,
          "Corum": 19,
          "Ankara": 6}

print(plates["Corum"])
plates['Kocaeli'] = 'New Value'          
print(plates)

users = {
    'OguzhanBirk' : {
        'age' : 22,
        'e_mail' : 'oguzhan1998-19@hotmail.com',
        'address' : 'Ankara'
    },
    'EdaBirk' : {
        'age' : 14,
        'e_mail' : "edabirk@gmail.com",
        'address' : "Corum"
    } 

}

print(users['EdaBirk'])


