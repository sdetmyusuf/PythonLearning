import os, sys

if os.path.isfile('myFile.txt'):
    f = open("myFile.txt", "w")
    print("Please enter the text")
    s = ''
    while s != '#':
        s = input("Enter text")
        f.write(s)
    

    f.close()