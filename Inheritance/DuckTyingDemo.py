class Human:
    def talk(self):
        print("Human says hello")



class Duck:
    def talk(self):
        print("Human says Quack")


def callTalk(obj):
    obj.talk();


h = Human()
h.talk()
d=Duck()
d.talk()
