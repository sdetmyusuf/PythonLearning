import pickle, StudentsData

f = open("student.dat", "wb")
s = StudentsData.Student(123, "mohd yusuf", 90)
pickle.dump(s, f)
f.close()

