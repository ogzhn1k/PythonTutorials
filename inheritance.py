
class Person :

    def __init__(self,fname,lname):
        self.firstname = fname
        self.lastname = lname
        print("Person created")

    def who_am_i(self) :
        print("I am a person")

    def eat(self) :
        print("I am eating pizza")    

class Student(Person) : 

    def __init__(self,fname,lname,number) :
        Person.__init__(self,fname,lname)
        self.studentNumber = number
        print("Student created")        
    def who_am_i(self):
        print("I am a student")

    def sayHello(self) :
        print(f"Hello i am {self.firstname} {self.lastname}")    


class Teacher(Person) :

    def __init__(self,fname,lname,branch) : 
        super().__init__(fname,lname)
        self.branch = branch

    def who_am_i(self) : 
        print(f"I am a {self.branch} teacher")      

p = Person("Oguzhan","Birk")
s = Student("Onuralp","Gulsen",21893952)
t = Teacher("Osman","Gultekin","Math")

print(p.firstname + " " + p.lastname)
print(s.firstname + " " + s.lastname)

p.who_am_i()
s.who_am_i()
s.eat()
print(s.studentNumber)
s.sayHello()
t.who_am_i()