class Role:
    def __init__(self, name, responsibily):
        self.name = name 
        self.responsibily = responsibily

    def about(self):
        print("I am a " + self.name + " and I am in charge of " + self.responsibily)

class Frontend(Role):
    pass

class Backend(Role):
    def about(self):
        print("backend scripter")

class Database(Role):
    def about(self):
        print("Database guru")


FE = Frontend("UI/UX designer", "Making sure users like what they see")
BE = Backend("Python developer", "Making sure all business logics works as expected")
DB = Database("SQL guru", "Making sure logic data are stored securely")

for i in (FE, BE, DB):
    print(i.name)
    print(i.responsibily)
    i.about()