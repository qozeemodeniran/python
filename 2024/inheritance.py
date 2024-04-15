class Gadgets:
    def __init__(self, category, functionality):
        self.category = category
        self.functionality = functionality

    def printGadget(self):
        print(self.category + " | " + self.functionality)


gadget = Gadgets("Mobile Devices", "Phone Calls")
print("From Base Class...")
gadget.printGadget()

class Apple(Gadgets):
    def __init__(self, category, functionality, maker, year, price):
        super().__init__(category, functionality)
        self.maker = maker
        self.year = year
        self.price = price

    def aboutGadget(self):
        print("The " + self.category + " is an ideal device for " + self.functionality + "\n" + "It was made by " + self.maker + " in the year " + self.year + " and costs " + self.price)


apple = Apple("iPhone 15 Pro Max", "Filming", "Apple", "2023", "$1099")
print("From Child Class...")
apple.printGadget()
apple.aboutGadget()



