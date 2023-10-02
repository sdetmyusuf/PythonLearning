class Patient:
    # def __init__(self):
    #     self.name = None

    def setName(self, name):
        self.name = name

    def getName(self):
        return self.name

    def setid(self, id):
        self.id = id

    def getid(self):
        return self.id

    def setSsn(self, ssn):
        self.ssn = ssn

    def getSsn(self):
        return self.ssn


    def getTestData(self):
        return self.getid()

p = Patient()
p.setid(123)
print(p.getid())
print("=====================================")
print(p.getTestData())
p.setName("Test user")
print(p.getName())
p.setSsn(1232233)
print(p.getSsn())