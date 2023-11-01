# read()[reads all data in file], read(position)[reads upto the position], readLine(), readLines()

# f = open("sample.txt", "r")
# print(f.read())
# print(f.read(12))
# print(f.readline()) #reads one line
# print(f.readlines()) #reads all line and returns them as list
# f.seek(7)  # to put the cursor at a particular index
# print(f.readlines())
# f.close()

def writeToFile():
    f = open("sample.txt", "w+")
    f.write("python is awesome")
    print("--------------------")
    f.seek(0)
    print(f.readlines())
    f.close()


def writeMultipleLinesToFile():
    f = open("sample.txt", "w+")
    f.writelines(["I love java\n", "I love python now\n", "come on\n", "lets\n", "learn\n", "python"])
    print("--------------------")
    print("the cursor is at ", f.tell())
    f.seek(0)
    print(f.read())
    f.close()


def appendDataToFile():
    f = open("sample.txt", "a+")
    print("cursor is at after append ", f.tell())
    f.write("Django is the webdevelopment framework\n")
    print("cursor is at after append ", f.tell())
    f.seek(0)
    print(f.read())
    f.close()


def rowCountInfile():
    f = open("sample.txt", "r")
    length = len(f.readlines()) #readlines will return the list and len will return its length
    print(length)
    f.close()


rowCountInfile()
