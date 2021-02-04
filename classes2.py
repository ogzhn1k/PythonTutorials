

class Circle : 
    pi = 3.14

    def __init__(self,radius=1) :
        self.radius = radius

    def circum(self) :
        return 2 * self.pi * self.radius

    def area(self) : 
        return self.pi * (self.radius**2)        

    def toString(self) :
        return "Circle"    

c1 = Circle()
c2 = Circle(5)
print(f"Circumference of the {c1.toString()}1 : {c1.circum()}")   
print(f"Circumference of the {c1.toString()}2 : {c2.circum()}")   
print(f"Area of the {c1.toString()}1 : {c1.area()}")   
print(f"Area of the {c1.toString()}2 : {c2.area()}")      