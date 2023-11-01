import pickle, StudentsData

f = open("student.dat", "rb")
obj = pickle.load(f)
obj.display()
