class Person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

    def printname(self):
        print(self.firstname, self.lastname)

# creating an object of class Person and calling printname method with the object
person1 = Person("Qozeem", "Odeniran")
person1.printname()

# creating the child class
class Student(Person):
    def __init__(self, fname, lname, year):
        # Person.__init__(self, fname, lname) child class will still inherit the parent's class __init__()
        super().__init__(fname, lname) # makes child class inherit all methods and properties fo parent class
        self.graduationyear = year

    def welcome(self):
        print("Welcome", self.firstname, self.lastname, "to the class of", self.graduationyear)

student1 = Student("Tomi", "Arokodare", 2024)
student1.printname()
print(student1.graduationyear)
student1.welcome()