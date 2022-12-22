class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    # def __init__(anyname, name, age):
    #     anyname.name = name
    #     anyname.age = age

    def myfunc(self):
    # def myfunc(abc):
        print("Hello, my name is " + abc.name)

p1 = Person("Qozeem", 28)
p1.myfunc()