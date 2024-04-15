class Frontend:
    def __init__(self, name, responsibily):
        self.name  = name
        self.responsibily = responsibily
    
    def introduce(self):
        print("coding the client side of the projedct")
        # print("I am + a " + self.name + " and I am in charge of " + self.responsibily) 

class Backend:
    def __init__(self, name, responsibily):
        self.name  = name
        self.responsibily = responsibily

    def introduce(self):
        print("coding the server side of the project")

class Database:
    def __init__(self, name, responsibily):
        self.name  = name
        self.responsibily = responsibily

    def introduce(self):
        print("coding the data side of the project")

FE = Frontend("UI/UX designer", "Making sure users like what they see")
BE = Backend("Python developer", "Making sure all business logics works as expected")
DB = Database("SQL guru", "Making sure logic data are stored securely")

for i in (FE, BE, DB):
    i.introduce()
    

