class Student:

    def __init__(self, id, name, score ):
        self.id = id
        self.name = name
        self.score = score

    def display(self):
        print("id is ", self.id," name is ", self.name, " score is ", self.score )
        