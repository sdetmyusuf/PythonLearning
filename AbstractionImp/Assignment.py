from abc import abstractmethod, ABC
class TouchScreenLaptop(ABC):

  #  def __init__(self, syntax, lib, support):
   #     self.syntax = syntax
    #    self.lib = lib
     #   self.support = support


    def scroll(self):
        pass
    @abstractmethod
    def click(self):
        pass

class HP(TouchScreenLaptop):

    def scroll(self):
        print("Scrolling is smooth in HP laptops")


    def cut(self):
        pass


class DELL(TouchScreenLaptop):
    def scroll(self):
        print("Scrolling is smooth in HP laptops")


    def paste(self):
        pass


class HPNoteboos(HP):

    def click(self):
        print("HP provides smooth operatrions like click")

class DELLNoteboos(DELL):

    def click(self):
        print("DELL provides smooth operatrions like click")



hpNoteboos = HPNoteboos()
hpNoteboos.click()
hpNoteboos.scroll()

dellNoteboos = DELLNoteboos()
dellNoteboos.click()
dellNoteboos.scroll()