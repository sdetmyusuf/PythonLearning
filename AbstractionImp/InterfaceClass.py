from abc import abstractmethod, ABC
class Programming(ABC):

    def __init__(self, syntax, lib, support):
        self.syntax = syntax
        self.lib = lib
        self.support = support


    def getSyntax(self):
        pass
    @abstractmethod
    def showLibs(self):
        pass

    def askSpport(self):
        pass


class Java(Programming):

    def __init__(self,syntax, lib, support, isplateformind):
        super().__init__(syntax, lib, support)
        self.isplateformind = isplateformind

    def getSyntax(self):
        print("Simple Syntax of Java")


    def showLibs(self):
        print("Simple libs of Java")


    def askSpport(self):
        print("All support is available")




java = Java("syntax", "lib", "support", "isplateformind")
java.getSyntax()
java.askSpport()
java.showLibs()