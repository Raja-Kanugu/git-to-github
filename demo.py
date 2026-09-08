
class bottle:
    company = "aqua"
    def __init__(self):
        self.name = "raj"
        self.age = '20'
    def details(self):
        print("his name is "+self.name,".his age is "+self.age)
        print("company name is "+self.company)
    @staticmethod
    def compname():
        print("comp name is bislery")

b1 = bottle()
b2 = bottle()
b3 = bottle()

bottle.compname()
b1.compname()