class Student:
    def __init__(self):
        self.__id = 123  # private var are created with _ in the beginning of their nme
        self.__name = "Yusuf"

    def display(self):
        print(self.__id)
        print(self.__name)

    def setAddress(self, add):
        self.add = add

    def setPnumber(self, phone):
        self.phone = phone

    def getAddress(self):
        return self.add

    def getPnumber(self):
        return self.phone


s = Student()
s.setPnumber(12344)
print(s.getPnumber())
# s.display()
# another way to access the private vars
print(s._Student__id)
