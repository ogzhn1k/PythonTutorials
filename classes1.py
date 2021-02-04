
class Person :
    #pass # placeholder

    def __init__(self,name,year):
        self.name = name
        self.year = year
    def intro(self):
        print(f"Hello {self.name}")
    def calculateAge(self):
        return 2021 - self.year


p1 = Person(name="Oguzhan",year=1998)
print(p1.name)
p1.intro()
print(p1.calculateAge())