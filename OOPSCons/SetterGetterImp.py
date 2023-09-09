class Programer:

    numObjects = 0

    def __init__(self):
        Programer.numObjects+=1

    @staticmethod
    def staticObjectsCounter():
        print(Programer.numObjects)

    def setName(self, name):
        self.Pname = name

    def setSkills(self, skills):
        self.PSkills = skills

    def setLoc(self, location):
        self.PLoc = location

    def setSal(self, salary):
        self.Psal = salary

    def getName(self):
        return self.Pname

    def getSkills(self):
        return self.PSkills

    def getLoc(self):
        return self.PLoc

    def getSal(self):
        return self.Psal

prog1 = Programer()
prog2 = Programer()
prog1.setName("Yusuf")
print(prog1.getName())
prog1.setSal(200002)
print(prog1.getSal())
prog1.setSkills(["Java", "Selenium", "JS"])
print(prog1.getSkills())
Programer.staticObjectsCounter()
