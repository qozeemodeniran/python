class Person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

    def printname(self):
        print(self.firstname, self.lastname)

# p = Person("Qozeem", "Odeniran")
# p.printname()

class Student(Person):
    def __init__(self, fname, lname, year):
        # Person.__init__(self, fname, lname)
        super().__init__(fname, lname)
        self.graduationyear = year

    def welcome(self):
        print("Welcome", self.firstname, self.lastname, "to the class of", self.graduationyear)

s = Student("Banji", "Odeniran", 2024)
# s.printname()

s.welcome()

# print(s.graduationyear)
